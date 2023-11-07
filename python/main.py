#####################
# Welcome to Cursor #
#####################

'''
Step 1: Try generating with Cmd+K or Ctrl+K on a new line. Ask for CLI-based game of TicTacToe.

Step 2: Hit Cmd+L or Ctrl+L and ask the chat what the code does. 
   - Then, try running the code

Step 3: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
   - Instruct it to change the game in some way (e.g. add colors, add a start screen, make it 4x4 instead of 3x3)

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
'''
num = 10
if num > 5:
    print("Number is greater than 5")
elif num == 5:
    print("Number is equal to 5")
else:
    print("Number is less than 5")
for i in range(10):
    print("This is a bigger loop. Iteration: ", i)
    for j in range(i):
        print("Nested loop. Parent iteration: ", i, " Child iteration: ", j)



