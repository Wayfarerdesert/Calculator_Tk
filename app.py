from tkinter import *  # noqa: F403
import ast

root = Tk()
root.title("Calculator")

display = Entry(root, justify="right")
display.grid(row=0, columnspan=6, sticky=W + E, padx=2 ,pady=6)
root.geometry("300x300")

index = 0

def getNumbers(n):
    global index
    display.insert(index, n)
    index += 1

def getOperator(operator):
    global index
    operator_length = len(operator)
    display.insert(index, operator)
    index += operator_length

def clearDisplay():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clearDisplay()
        display.insert(0, display_new_state)
    else:
        clearDisplay()

def calculate():
    display_state = display.get()
    try:
        math_expression = ast.parse(display_state, mode="eval")
        # result = ast.dump(math_expression)
        result = eval(compile(math_expression, "<string>", "eval"))
        clearDisplay()
        display.insert(0, result)
    except Exception as e:
        clearDisplay()
        display.insert(0, f"Error: {e}")

def changeSign():
    display_state = display.get()
    if display_state and display_state[0] != "-":
        new_display_state = '-' + display_state
        display.delete(0, END)
        display.insert(0, new_display_state)
    elif display_state and display_state[0] == "-":
        new_display_state = display_state[1:]
        display.delete(0, END)
        display.insert(0, new_display_state)

# Operations Buttons
Button(root, text="x²", command=lambda: getOperator("**")).grid(
    row=1, column=1, sticky="nsew")
Button(root, text="√", command=lambda: getOperator("**0.5")).grid(
    row=1, column=2, sticky="nsew")
Button(root, text="←", command=lambda: undo()).grid(
    row=1, column=4, columnspan=2, sticky="nsew")

Button(root, text="%", command=lambda: getOperator("%")).grid(
    row=2, column=0, sticky=W + E)
Button(root, text="÷", command=lambda: getOperator("/")).grid(
    row=2, column=1, sticky=W + E)
Button(root, text="x", command=lambda: getOperator("*")).grid(
    row=2, column=2, sticky=W + E)

Button(root, text="-", command=lambda: getOperator("-")).grid(
    row=2, column=4, sticky=W + E)
Button(root, text="+", command=lambda: getOperator("+")).grid(
    row=3, column=4, sticky=W + E, rowspan=2)
Button(root, text="=", command=lambda: calculate()).grid(
    row=5, column=4, sticky=W + E, rowspan=2)

Button(root, text=",", command=lambda: getOperator(",")).grid(
    row=6, column=2, sticky=W + E)

# Numeric Buttons
Button(root, text="1", command=lambda: getNumbers(1)).grid(
    row=5, column=0, sticky=W + E)
Button(root, text="2", command=lambda: getNumbers(2)).grid(
    row=5, column=1, sticky=W + E)
Button(root, text="3", command=lambda: getNumbers(3)).grid(
    row=5, column=2, sticky=W + E)

Button(root, text="4", command=lambda: getNumbers(4)).grid(
    row=4, column=0, sticky=W + E)
Button(root, text="5", command=lambda: getNumbers(5)).grid(
    row=4, column=1, sticky=W + E)
Button(root, text="6", command=lambda: getNumbers(6)).grid(
    row=4, column=2, sticky=W + E)

Button(root, text="7", command=lambda: getNumbers(7)).grid(
    row=3, column=0, sticky=W + E)
Button(root, text="8", command=lambda: getNumbers(8)).grid(
    row=3, column=1, sticky=W + E)
Button(root, text="9", command=lambda: getNumbers(9)).grid(
    row=3, column=2, sticky=W + E)

Button(root, text="0", command=lambda: getNumbers(0)).grid(
    row=6, column=0, columnspan=2, sticky=W + E)

# Side Buttons
Button(root, text="C", command=lambda:clearDisplay()).grid(
    row=2, column=5, columnspan=2, sticky=W + E)
Button(root, text="AC", command=lambda: clearDisplay()).grid(
    row=3, column=5, columnspan=2, sticky=W + E)
Button(root, text="(", command=lambda: getOperator("(")).grid(
    row=4, column=5, columnspan=2, sticky=W + E)
Button(root, text=")", command=lambda: getOperator(")")).grid(
    row=5, column=5, columnspan=2, sticky=W + E)
Button(root, text="+/-", command=lambda: changeSign()).grid(row=6, column=5, sticky=W + E)

root.mainloop()
