"""
Developed by: Bisrat Walle
Email: bisratwalle3@gmail.com
"""


import turtle
import random
import copy


def non_zero_push_left(line):
   """
   This function pushes non-zero numbers to the left and
   returns a new list after filling the zeros in place of the pushed numbers
   It takes O(n) time --> linear run-time complexity

   :param line:
   :return line_copy:
   """
   line_copy = []
   zero_counter = 0
   for num in line:
       if num != 0:
           line_copy.append(num)
       else:
           zero_counter += 1
   for index in range(zero_counter):
       line_copy.append(0)
   return line_copy


def zero_remove(line):
   """
   This function just returns a sublist of the passed parameter after removing all zeros
   It takes O(n) time --> linear runtime complexity

   :param line:
   :return non_zero:
   """
   non_zero = []
   for num in line:
       if num != 0:
           non_zero.append(num)
   return non_zero


def merge(line):
   """
   This function returns a new list after shifting and merging to the non-zeros to left
   It also updates the score during merging
   It takes O(n) time --> linear runtime complexity

   :param line:
   :return line_copy:
   """
   global score
   line_copy = non_zero_push_left(line)
   if len(set(zero_remove(line_copy))) == len(zero_remove(line_copy)):  # if it has no zeros
       return line_copy

   # merge adjacent numbers if they are equal
   for temp_index in range(0, 3):
       if line_copy[temp_index] == line_copy[temp_index + 1]:
           score += line_copy[temp_index]  # add the merged number to the score
           line_copy[temp_index] = 2 * line_copy[temp_index + 1]
           line_copy[temp_index + 1] = 0
   return non_zero_push_left(line_copy)


def shift_left(matrix):
   """
   This function takes a 2D list and returns new list after taking merge operation to the left on each rows
   It takes O(n) time --> linear run-time complexity

   :param matrix:
   :return new_matrix:
   """
   new_matrix = []
   for row in matrix:
       new_matrix.append(merge(row))
   return new_matrix


def shift_right(matrix):
   """
   This function takes a 2D list and returns new list after taking merge operation to the right on each rows
   It takes O(n) time --> linear run-time complexity

   :param matrix:
   :return new_matrix:
   """
   new_matrix = []
   for row in matrix:
       row.reverse()
       new_row = copy.deepcopy(merge(row))
       new_row.reverse()
       new_matrix.append(new_row)
   return new_matrix


def transpose(matrix):
   """
   This function return the transponse of a matrix passed to it
   It takes O(n ^ 2) time --> quadratic run-time complexity

   :param matrix:
   :return new_matrix:
   """
   new_matrix = []
   for i in range(4):
       row = []
       for j in range(4):
           row.append(matrix[j][i])
       new_matrix.append(row)
   return new_matrix


def shift_up(matrix):
   """
   This function takes a 2D list and returns new list after taking merge operation upward on each rows
   It takes O(1) time --> constant run-time complexity

   :param matrix:
   :return transpose(shift_left(transpose(matrix))):
   """
   return transpose(shift_left(transpose(matrix)))


def shift_down(matrix):
   """
   This function takes a 2D list and returns new list after taking merge operation upward on each rows
   It takes O(1) time --> constant run-time complexity

   :param matrix:
   :return transpose(shift_right(transpose(matrix))):
   """
   return transpose(shift_right(transpose(matrix)))


def get_random_number():
   """
   This function generates a value randomly, which is either 2 or 4 and returns it
   It takes O(1) time --> constant run-time complexity

   :return random.choice([2, 4]):
   """
   return random.choice([2, 4])


def add_random_number(matrix):
   """
   This function adds two numbers to the 2D list passed to it
   It takes O(n) time --> linear run-time complexity

   :param matrix:
   :return None:
   """
   for i in range(2):
       row_index = random.randint(0, 3)
       col_index = random.randint(0, 3)
       if matrix[row_index][col_index] == 0:
           matrix[row_index][col_index] = get_random_number()


def draw_grid():
   """
   This function creates a 4 * 4 grid at the center of the turtle window
   It takes O(n) time --> linear run-time complexity

   :return None:
   """
   x_pos, y_pos = -100, 100
   grid = turtle.Turtle()
   grid.pensize(3)
   grid.shape("square")
   grid.pencolor('darkblue')
   grid.penup()
   grid.goto(x_pos, y_pos)
   for i in range(5):
       grid.pendown()
       grid.forward(200)
       grid.penup()
       y_pos -= 50
       grid.goto(x_pos, y_pos)

   x_pos, y_pos = -100, 100
   grid.goto(x_pos, y_pos)
   for i in range(5):
       grid.setheading(270)
       grid.pendown()
       grid.forward(200)
       grid.penup()
       x_pos += 50
       grid.goto(x_pos, y_pos)


def descriptions():
   """
   This function prints the string to the turtle window
   :return None:
   """
   name = turtle.Turtle()
   name.hideturtle()
   name.penup()
   name.goto(0, 0)
   name.color("indigo")
   name.setheading(268)
   name.forward(150)
   name.setheading(0)
   name.forward(5)
   name.write("Developed by Bisrat", move=False, align="center", font=("monospace", 15, "normal"))


def display(matrix):
   """
   This function displays the 2D matrix passed to it to the turtle window
   :param matrix:
   :return None:
   """
   turtle.clearscreen()
   global window
   window.bgcolor("lightblue")
   window.tracer(0)
   restart_prompt()
   descriptions()
   draw_grid()
   display_score()
   drawer = turtle.Turtle()
   drawer.hideturtle()
   drawer.penup()
   drawer.pencolor("black")
   index = 0
   pos_x, pos_y = -80 - 4.2 * len(str(matrix[index][0])), 60

   for row in matrix:
       for element in row:
           drawer.goto(pos_x, pos_y)
           drawer.pendown()
           if element == 0:
               drawer.write(" ", align="left", font=('monospace', 15, 'italic'))
           else:
               drawer.write(str(element), align="left", font=('monospace', 15, 'italic'))
           pos_x += 50
           drawer.penup()
       index += 1
       if index < 4:
           pos_x = -80 - 4.2 * len(str(matrix[index][0]))
       pos_y -= 50


def won(matrix):
   """
   This function checks whether a player won a game or not
   It takes O(n) time --> linear run-time complexity

   :param matrix:
   :return boolean:
   """
   for row in matrix:
       if 2048 in row:
           return True
   return False


def lose(matrix):
   """
   This function checks whether a player lose a game or not
   It takes O(1) time --> constant run-time complexity

   :param matrix:
   :return boolean:
   """
   temp_board1 = copy.deepcopy(matrix)
   temp_board2 = copy.deepcopy(matrix)
   if temp_board1 == shift_left(temp_board2):
       if temp_board1 == shift_up(temp_board2):
           if temp_board1 == shift_down(temp_board2):
               temp_board2 = shift_right(temp_board2)
               if temp_board1 == temp_board2:
                   return True
   return False


def left_pressed():  # this function is just for the sake of listening event (since It has no parameter)
   global initial_matrix
   initial_matrix = shift_left(initial_matrix)
   display(initial_matrix)
   event_listener()


def right_pressed():  # this function is just for the sake of listening event (since It has no parameter)
   global initial_matrix
   initial_matrix = shift_right(initial_matrix)
   display(initial_matrix)
   event_listener()


def up_pressed():  # this function is just for the sake of listening event (since It has no parameter)
   global initial_matrix
   initial_matrix = shift_up(initial_matrix)
   display(initial_matrix)
   event_listener()


def down_pressed():   # this function is just for the sake of listening event (since It has no parameter)
   global initial_matrix
   initial_matrix = shift_down(initial_matrix)
   display(initial_matrix)
   event_listener()


def add_value(matrix):
   """
   This function adds a value to the matrix at random index, where no value found
   It takes O(n ^ 2) time --> quadratic run-time complexity

   :param matrix:
   :return None:
   """
   all_non_zero = True
   for row in matrix:
       for element in row:
           if element == 0:
               all_non_zero = False

   if not all_non_zero:
       row_index = random.randint(0, 3)
       col_index = random.randint(0, 3)

       while matrix[row_index][col_index] != 0:
           row_index = random.randint(0, 3)
           col_index = random.randint(0, 3)

       matrix[row_index][col_index] = get_random_number()


def print_message(message):
   """
   This function just prints a message passed to it at the top of turtle window
   It takes O(1) time --> constant run-time complexity

   :param message:
   :return None:
   """
   message_writer = turtle.Turtle()
   message_writer.penup()
   message_writer.goto(-100, 110)
   message_writer.pendown()
   message_writer.pensize(5)
   message_writer.write(message, font=('arial', 15, 'italic'))
   message_writer.hideturtle()
   turtle.done()


def event_listener():
   """
   This function listens keyboard events after checking game won or lose
   :return None:
   """
   global window
   if won(initial_matrix):
       print_message("Congrats, You Won!")

   if lose(initial_matrix):
       print_message("Sorry, You Lose!")

   window.listen()
   window.onclick(restart)
   window.onkeypress(left_pressed, 'Left')
   window.onkeypress(right_pressed, 'Right')
   window.onkeypress(up_pressed, 'Up')
   window.onkeypress(down_pressed, 'Down')
   add_value(initial_matrix)


score_button_x, score_button_y, score_button_length, score_button_width = -150, 150, 120, 20


def display_score():
   """
   This function prints the score to the turtle window
   :return None:
   """
   res = turtle.Turtle()
   res.color('red')
   res.pensize(3)
   res.penup()
   res.goto(score_button_x, score_button_y)
   res.pendown()
   res.forward(score_button_length)
   res.left(90)
   res.forward(score_button_width)
   res.left(90)
   res.forward(score_button_length)
   res.left(90)
   res.forward(score_button_width)
   res.penup()
   res.pencolor('purple')
   res.left(90)
   res.forward(15)
   res.pendown()
   res.write(f"Score: {score}", font=('monospace', 13, 'bold'))
   res.hideturtle()


restart_button_x, restart_button_y, restart_button_length, restart_button_width = 50, 150, 100, 20


def restart_prompt():
   """
   This function prints a prompt to restart the game
   :return None:
   """
   res = turtle.Turtle()
   res.color('red')
   res.pensize(3)
   res.penup()
   res.goto(restart_button_x, restart_button_y)
   res.pendown()
   res.forward(restart_button_length)
   res.left(90)
   res.forward(restart_button_width)
   res.left(90)
   res.forward(restart_button_length)
   res.left(90)
   res.forward(restart_button_width)
   res.penup()
   res.pencolor('purple')
   res.left(90)
   res.forward(15)
   res.pendown()
   res.write("RESTART", font=('monospace', 13, 'bold'))
   res.hideturtle()


def restart(x, y):
   """
   This function is an engine to restart the game
   It automatically restarts the game immediately after being clicked
   :param x:
   :param y:
   :return None:
   """
   global initial_matrix, score
   if restart_button_x <= x <= restart_button_x + restart_button_length:
       if restart_button_y <= y <= restart_button_y + restart_button_width:
           window.clearscreen()
           initial_matrix = [[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]
                             ]
           add_random_number(initial_matrix)
           score = 0
           display(initial_matrix)
           event_listener()


window = turtle.Screen()
window.setup(450, 400)
window.title("2048 Game, Submitted to Kabila Haile")

initial_matrix = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]
                 ]
score = 0

add_random_number(initial_matrix)
try:
   display(initial_matrix)  # driver code
   window.listen()   # driver code
   event_listener()  # driver code
except:
   pass
window.mainloop()
