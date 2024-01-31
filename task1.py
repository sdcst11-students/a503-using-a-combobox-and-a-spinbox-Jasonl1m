"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""

import tkinter as tk

def display_birthdate():
    birthdate = f"{entry_month.get()} {entry_day.get()}, {entry_year.get()}"
    result_entry.delete(0, tk.END)
    result_entry.insert(0, birthdate)

window = tk.Tk()
window.title("Birthdate Selector")

label_month = tk.Label(window, text="Month:")
label_month.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_month = tk.Entry(window)
entry_month.grid(row=0, column=1, padx=10, pady=10)

label_day = tk.Label(window, text="Day:")
label_day.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_day = tk.Entry(window)
entry_day.grid(row=1, column=1, padx=10, pady=10)

label_year = tk.Label(window, text="Year:")
label_year.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_year = tk.Entry(window)
entry_year.grid(row=2, column=1, padx=10, pady=10)

display_button = tk.Button(window, text="Display Birthdate", command=display_birthdate)
display_button.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(window, text="Selected Birthdate:")
label_result.grid(row=4, column=0, padx=10, pady=10, sticky="w")
result_entry = tk.Entry(window)
result_entry.grid(row=4, column=1, padx=10, pady=10)

window.mainloop()



