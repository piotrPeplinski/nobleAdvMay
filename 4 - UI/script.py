import tkinter as tk
import pandas as pd
import sqlite3

root = tk.Tk()
root.title('Employees registry')

frame = tk.Frame(root)
frame.pack()

# entries
name_label = tk.Label(frame, text='Name')
name_entry = tk.Entry(frame)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

salary_label = tk.Label(frame, text='Salary')
salary_entry = tk.Entry(frame)

salary_label.grid(row=1, column=0)
salary_entry.grid(row=1, column=1)

# function


def register_employee():
    name = name_entry.get()
    salary = salary_entry.get()

    df = pd.DataFrame({
        'Name':[name],
        'Salary':[float(salary)]
    })

    connection = sqlite3.connect('ui-company.sqlite')
    #cursor = connection.cursor()
    df.to_sql('employees',connection, if_exists='append', index=False)
    connection.close()

    name_entry.delete(0,tk.END)
    salary_entry.delete(0, tk.END)


# button
register_btn = tk.Button(frame, text='Register employee',command=register_employee)
register_btn.grid(row=2, column=1)


root.mainloop()
