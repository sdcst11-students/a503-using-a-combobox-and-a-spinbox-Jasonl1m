#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""
import tkinter as tk
from tkinter import ttk

def calculate_final_value():
    try:
        principal = float(entry_principal.get())
        interest_rate = float(entry_interest_rate.get()) / 100 
        time = float(entry_time.get())
        compounding_frequency = int(combobox_compounding_frequency.get())

        final_value = principal * (1 + interest_rate / compounding_frequency)**(compounding_frequency * time)

        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"{final_value:.2f}")
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input")

window = tk.Tk()
window.title("Compound Interest Calculator")

label_principal = tk.Label(window, text="Principal:")
label_principal.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_principal = tk.Entry(window)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

label_interest_rate = tk.Label(window, text="Interest Rate (%):")
label_interest_rate.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_interest_rate = tk.Entry(window)
entry_interest_rate.grid(row=1, column=1, padx=10, pady=10)

label_time = tk.Label(window, text="Time (years):")
label_time.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_time = tk.Entry(window)
entry_time.grid(row=2, column=1, padx=10, pady=10)

label_compounding_frequency = tk.Label(window, text="Compounding Frequency:")
label_compounding_frequency.grid(row=3, column=0, padx=10, pady=10, sticky="w")
compounding_frequency_options = ["1", "2", "4", "12", "365"]
combobox_compounding_frequency = ttk.Combobox(window, values=compounding_frequency_options)
combobox_compounding_frequency.set("12")
combobox_compounding_frequency.grid(row=3, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate Final Value", command=calculate_final_value)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

label_result = tk.Label(window, text="Final Value:")
label_result.grid(row=5, column=0, padx=10, pady=10, sticky="w")
result_entry = tk.Entry(window)
result_entry.grid(row=5, column=1, padx=10, pady=10)

window.mainloop()

