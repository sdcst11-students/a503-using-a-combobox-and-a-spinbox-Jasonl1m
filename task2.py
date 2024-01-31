#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""
import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = spinbox_operator.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error (division by zero)"
        else:
            result = "Invalid operator"

        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input")

window = tk.Tk()
window.title("Simple Calculator")

label_num1 = tk.Label(window, text="Number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(window, text="Number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operator = tk.Label(window, text="Operator:")
label_operator.grid(row=2, column=0, padx=10, pady=10, sticky="w")
spinbox_operator = tk.Spinbox(window, values=("+", "-", "*", "/"))
spinbox_operator.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(window, text="Result:")
label_result.grid(row=4, column=0, padx=10, pady=10, sticky="w")
result_entry = tk.Entry(window)
result_entry.grid(row=4, column=1, padx=10, pady=10)

window.mainloop()
