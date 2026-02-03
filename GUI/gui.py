import tkinter as tk
from tkinter import ttk

def submit_data():
    name_value = name_input.get()
    addition_msg = text_area.get("1.0", tk.END).strip()
    checkbox_value = "Checked" if check_var.get() == 1 else "Not Checked"
    radio_value = radio_var.get()
    dropdown_value = combo_subject.get()

    output_window = tk.Toplevel(root)
    output_window.title("Submitted Data")

    tk.Label(output_window, text=f"Name Input: {name_value}").pack(pady=2)
    tk.Label(output_window, text=f"Addition Message: {addition_msg}").pack(pady=2)
    tk.Label(output_window, text=f"Checkbox: {checkbox_value}").pack(pady=2)
    tk.Label(output_window, text=f"Radio Selected: {radio_value}").pack(pady=2)
    tk.Label(output_window, text=f"Dropdown Selected: {dropdown_value}").pack(pady=2)

root = tk.Tk()
root.title("F105")
root.geometry("400x500")

# Frames
frame_title = tk.Frame(root)
frame_title.pack(pady=10)

frame_name = tk.Frame(root)
frame_name.pack(pady=5)

frame_msg = tk.Frame(root)
frame_msg.pack(pady=5)

frame_check = tk.Frame(root)
frame_check.pack(pady=5)

frame_radio = tk.Frame(root)
frame_radio.pack(pady=5)

frame_combo = tk.Frame(root)
frame_combo.pack(pady=5)

frame_button = tk.Frame(root)
frame_button.pack(pady=10)

# Title label
label_title = tk.Label(frame_title, text="Aditya Rana - F105", font=("Arial", 14, "bold"))
label_title.pack()

# Name label
label_name = tk.Label(frame_name, text="Enter Name:")
label_name.pack()
name_input = tk.Entry(frame_name, width=30) 
name_input.pack()

# Message label
label_msg = tk.Label(frame_msg, text="Addition Message:")
label_msg.pack()
text_area = tk.Text(frame_msg, height=4, width=30)
text_area.pack()

# Radio buttons
radio_var = tk.StringVar(value="Python")
radio1 = tk.Radiobutton(frame_radio, text="Python", variable=radio_var, value="Python")
radio2 = tk.Radiobutton(frame_radio, text="Java", variable=radio_var, value="Java")
radio1.pack()
radio2.pack()

# Checkbox
check_var = tk.IntVar()
checkbox = tk.Checkbutton(frame_check, text="I Agree", variable=check_var)
checkbox.pack()

# Dropdown
combo_subject = ttk.Combobox(frame_combo, values=["OOP", "DSA", "Python"], width=28)
combo_subject.set("Select an item")
combo_subject.pack()

# Submit button
submit_btn = tk.Button(frame_button, text="Submit", command=submit_data)
submit_btn.pack()

root.mainloop()
