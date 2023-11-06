import tkinter as tk

# Function to update the display when a button is pressed
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

# Function to clear the display
def clear():
    display.delete(0, tk.END)

# Function to perform calculations
def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a display
display = tk.Entry(root, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_num = 1
col_num = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Create a clear button
tk.Button(root, text='C', width=5, height=2, command=clear).grid(row=row_num, column=col_num)

# Run the application
root.mainloop()
