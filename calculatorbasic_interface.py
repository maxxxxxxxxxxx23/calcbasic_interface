import tkinter as tk

def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2

    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Calculator")

num1_label = tk.Label(root, text="First Number")
num1_label.grid(row=0, column=0)

num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1)

num2_label = tk.Label(root, text="Second Number")
num2_label.grid(row=1, column=0)

num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1)

operation_var = tk.StringVar(value="+")
addition_radiobutton = tk.Radiobutton(root, text="+", variable=operation_var, value="+")
addition_radiobutton.grid(row=2, column=0)

subtraction_radiobutton = tk.Radiobutton(root, text="-", variable=operation_var, value="-")
subtraction_radiobutton.grid(row=2, column=1)

multiplication_radiobutton = tk.Radiobutton(root, text="*", variable=operation_var, value="*")
multiplication_radiobutton.grid(row=2, column=2)

division_radiobutton = tk.Radiobutton(root, text="/", variable=operation_var, value="/")
division_radiobutton.grid(row=2, column=3)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=4, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=4)

root.mainloop()
