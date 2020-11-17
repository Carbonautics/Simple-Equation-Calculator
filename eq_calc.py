import re

print('Simple Equation Calculator')
print('Type quit to exit the calculator.\n')

previous = 0
run = True

def process():
    global run
    global previous

    equation = ""
    if previous == 0:
        equation = input('Enter Equation (Ex: 1+3*2-343/2):')
    else:
        equation = input(str(previous) + '\n:' )

    if equation == 'quit':
        print('Goodbye!!')
        run = False
        exit()
#this line checks the input for any alphabets lower & upper case, comma, colon, braces, whitespaces and removes/denies those characters. 
    equation = re.sub('[a-zA-z,:()" "]', '', equation)
# Making eval() safe using regex to filter out characters or keywords

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)

while run:
    process()