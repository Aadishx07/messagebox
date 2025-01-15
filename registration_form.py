import tkinter as tk
from tkinter import messagebox
import re


def validate_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email)


def validate_phone(phone):
    return re.match(r"^\d{10}$", phone)


def submit():
    first_name = first_name_var.get()
    middle_name = middle_name_var.get()
    last_name = last_name_var.get()
    email = email_var.get()
    phone = phone_var.get()
    gender = gender_var.get()
    selected_course = course_var.get()

    if not all([first_name, last_name, email, phone, gender, selected_course]):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    if not validate_email(email):
        messagebox.showwarning("Input Error", "Invalid email format!")
        return

    if not validate_phone(phone):
        messagebox.showwarning("Input Error", "Phone number must be 10 digits!")
        return

    with open("registration_data.txt", "a") as file:
        file.write(
            f"First Name: {first_name}\nMiddle Name: {middle_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}\nGender: {gender}\nSelected Course: {selected_course}\n{'-' * 40}\n"
        )

    messagebox.showinfo(
        "Registration Info",
        f"First Name: {first_name}\nMiddle Name: {middle_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}\nGender: {gender}\nSelected Course: {selected_course}",
    )
    clear()


def clear():
    first_name_var.set("")
    middle_name_var.set("")
    last_name_var.set("")
    email_var.set("")
    phone_var.set("")
    gender_var.set("")
    course_var.set("")


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Registration Form")
first_name_var = tk.StringVar()
middle_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
gender_var = tk.StringVar()
course_var = tk.StringVar()
tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=first_name_var).grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, text="Middle Name").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=middle_name_var).grid(row=1, column=1, padx=10, pady=10)
tk.Label(root, text="Last Name").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=last_name_var).grid(row=2, column=1, padx=10, pady=10)
tk.Label(root, text="Email").grid(row=3, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=email_var).grid(row=3, column=1, padx=10, pady=10)
tk.Label(root, text="Phone").grid(row=4, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=phone_var).grid(row=4, column=1, padx=10, pady=10)
tk.Label(root, text="Gender").grid(row=5, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(
    row=5, column=1
)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(
    row=5, column=2
)
tk.Label(root, text="Select Course:").grid(row=6, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="BVoc SD", variable=course_var, value="BVoc SD").grid(
    row=6, column=1, sticky="w"
)
tk.Radiobutton(root, text="BSC IT", variable=course_var, value="BSC IT").grid(
    row=7, column=1, sticky="w"
)
tk.Radiobutton(root, text="BSC Biotech", variable=course_var, value="BSC Biotech").grid(
    row=8, column=1, sticky="w"
)
tk.Radiobutton(root, text="BSC", variable=course_var, value="BSC").grid(
    row=9, column=1, sticky="w"
)
tk.Radiobutton(root, text="BDS", variable=course_var, value="BDS").grid(
    row=10, column=1, sticky="w"
)
tk.Radiobutton(root, text="BMM", variable=course_var, value="BMM").grid(
    row=11, column=1, sticky="w"
)
tk.Button(root, text="Submit", command=submit).grid(row=12, column=0, pady=20)
tk.Button(root, text="Clear", command=clear).grid(row=12, column=1, pady=20)
tk.Button(root, text="Exit", command=exit_app).grid(row=12, column=2, pady=20)

root.mainloop()

