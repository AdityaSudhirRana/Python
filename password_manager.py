import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT,
    account_username TEXT,
    account_password TEXT,
    notes TEXT
)
""")

conn.commit()

cursor.execute("SELECT * FROM users WHERE username='admin'")
if not cursor.fetchone():
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
    conn.commit()

# ---------------- LOGIN ---------------- #

root = tk.Tk()
root.title("Password Manager Login")
root.geometry("400x300")
root.configure(bg="white")


def login():
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username_entry.get(), password_entry.get()))
    if cursor.fetchone():
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Credentials")


def login_screen():
    tk.Label(root, text="Password Manager",
             font=("Arial", 20, "bold"),
             bg="white").pack(pady=40)

    frame = tk.Frame(root, bg="white")
    frame.pack()

    global username_entry, password_entry

    tk.Label(frame, text="Username", bg="white").pack(anchor="w")
    username_entry = tk.Entry(frame, width=25)
    username_entry.pack(pady=5)

    tk.Label(frame, text="Password", bg="white").pack(anchor="w")
    password_entry = tk.Entry(frame, show="*", width=25)
    password_entry.pack(pady=5)

    tk.Button(frame, text="Login",
              bg="#1a73e8", fg="white",
              width=15, command=login).pack(pady=15)


# ---------------- DASHBOARD ---------------- #

def open_dashboard():
    dash = tk.Tk()
    dash.title("Password Vault")
    dash.geometry("950x550")
    dash.configure(bg="#f5f5f5")

    container = tk.Frame(dash, bg="#f5f5f5")
    container.pack(fill="both", expand=True, padx=30, pady=20)

    header = tk.Frame(container, bg="#f5f5f5")
    header.pack(fill="x")

    tk.Label(header, text="Password Vault",
             font=("Arial", 20, "bold"),
             bg="#f5f5f5").pack(side="left")

    btn_frame = tk.Frame(header, bg="#f5f5f5")
    btn_frame.pack(side="right")

    tk.Button(btn_frame, text="Export",
              bg="#fbbc05", fg="black",
              width=12,
              command=export_prompt).pack(side="left", padx=5)

    tk.Button(btn_frame, text="Open",
              bg="#34a853", fg="white",
              width=12,
              command=open_entry_window).pack(side="left", padx=5)

    tk.Button(btn_frame, text="Add",
              bg="#1a73e8", fg="white",
              width=12,
              command=lambda: create_entry_window(dash)).pack(side="left", padx=5)

    card = tk.Frame(container, bg="white", bd=1, relief="solid")
    card.pack(fill="both", expand=True, pady=20)

    global tree

    tree = ttk.Treeview(card,
                        columns=("ID", "Website"),
                        show="headings")

    tree.heading("ID", text="ID")
    tree.heading("Website", text="Website")

    tree.column("ID", width=80, anchor="center")
    tree.column("Website", width=700, anchor="w")

    scrollbar = ttk.Scrollbar(card, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    scrollbar.pack(side="right", fill="y")

    load_data()

    dash.mainloop()


def load_data():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT id, website FROM vault")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


# ---------------- ADD WINDOW ---------------- #

def create_entry_window(parent):
    win = tk.Toplevel(parent)
    win.title("Add Credential")
    win.geometry("500x450")
    win.configure(bg="white")

    container = tk.Frame(win, bg="white")
    container.pack(padx=30, pady=30, anchor="w")

    tk.Label(container, text="Website", bg="white").pack(anchor="w")
    website = tk.Entry(container, width=40)
    website.pack(pady=5)

    tk.Label(container, text="Username", bg="white").pack(anchor="w")
    username = tk.Entry(container, width=40)
    username.pack(pady=5)

    tk.Label(container, text="Password", bg="white").pack(anchor="w")
    password = tk.Entry(container, width=40)
    password.pack(pady=5)

    tk.Label(container, text="Notes", bg="white").pack(anchor="w")
    notes = tk.Text(container, width=40, height=5)
    notes.pack(pady=5)

    def save():
        if website.get() == "" or username.get() == "" or password.get() == "":
            messagebox.showerror("Error", "All fields required")
            return

        cursor.execute("""
            INSERT INTO vault (website, account_username, account_password, notes)
            VALUES (?, ?, ?, ?)
        """, (website.get(), username.get(), password.get(), notes.get("1.0", tk.END)))
        conn.commit()

        load_data()
        win.destroy()

    tk.Button(container, text="Save",
              bg="#1a73e8", fg="white",
              width=15, command=save).pack(pady=15)


# ---------------- OPEN WINDOW ---------------- #

def open_entry_window():
    selected = tree.focus()
    if not selected:
        return

    item = tree.item(selected)["values"]
    cursor.execute("SELECT * FROM vault WHERE id=?", (item[0],))
    data = cursor.fetchone()

    win = tk.Toplevel()
    win.title(data[1])
    win.geometry("800x450")
    win.configure(bg="#f5f5f5")

    card = tk.Frame(win, bg="white", bd=1, relief="solid")
    card.pack(fill="both", expand=True, padx=30, pady=30)

    main = tk.Frame(card, bg="white")
    main.pack(padx=40, pady=30)

    # LEFT COLUMN
    tk.Label(main, text="Username", bg="white").grid(row=0, column=0, sticky="w", pady=(0,5))
    user_entry = tk.Entry(main, width=35)
    user_entry.grid(row=1, column=0, padx=10, pady=(0,15))
    user_entry.insert(0, data[2])
    user_entry.config(state="readonly")

    tk.Label(main, text="Password", bg="white").grid(row=2, column=0, sticky="w", pady=(0,5))
    pass_entry = tk.Entry(main, width=35, show="*")
    pass_entry.grid(row=3, column=0, padx=10, pady=(0,15))
    pass_entry.insert(0, data[3])
    pass_entry.config(state="readonly")

    def toggle_password():
        pass_entry.config(show="" if pass_entry.cget("show") == "*" else "*")

    def copy_password():
        win.clipboard_clear()
        win.clipboard_append(data[3])
        messagebox.showinfo("Copied", "Password copied to clipboard")

    btn_row = tk.Frame(main, bg="white")
    btn_row.grid(row=4, column=0, pady=10)

    tk.Button(btn_row, text="Show/Hide",
              bg="#1a73e8", fg="white",
              width=12, command=toggle_password).pack(side="left", padx=5)

    tk.Button(btn_row, text="Copy",
              bg="#34a853", fg="white",
              width=12, command=copy_password).pack(side="left", padx=5)

    # RIGHT COLUMN
    tk.Label(main, text="Website", bg="white").grid(row=0, column=1, sticky="w", pady=(0,5))
    web_entry = tk.Entry(main, width=35)
    web_entry.grid(row=1, column=1, padx=20, pady=(0,15))
    web_entry.insert(0, data[1])
    web_entry.config(state="readonly")

    tk.Label(main, text="Notes", bg="white").grid(row=2, column=1, sticky="w", pady=(0,5))
    notes_box = tk.Text(main, width=35, height=6)
    notes_box.grid(row=3, column=1, padx=20, pady=(0,15))
    notes_box.insert("1.0", data[4])
    notes_box.config(state="disabled")

    tk.Button(card, text="Delete",
              bg="#ea4335", fg="white",
              width=15,
              command=lambda: delete_entry(data[0], win)).pack(pady=15)


def delete_entry(entry_id, window):
    cursor.execute("DELETE FROM vault WHERE id=?", (entry_id,))
    conn.commit()
    load_data()
    window.destroy()


# ---------------- EXPORT ---------------- #

def export_prompt():
    win = tk.Toplevel()
    win.title("Confirm Export")
    win.geometry("350x200")
    win.configure(bg="white")

    tk.Label(win, text="Re-enter Login Password",
             bg="white").pack(pady=20)

    entry = tk.Entry(win, show="*", width=25)
    entry.pack(pady=5)

    def verify():
        cursor.execute("SELECT password FROM users WHERE username='admin'")
        real_pass = cursor.fetchone()[0]

        if entry.get() == real_pass:
            export_passwords()
            win.destroy()
        else:
            messagebox.showerror("Error", "Incorrect Password")

    tk.Button(win, text="Confirm",
              bg="#1a73e8", fg="white",
              width=15, command=verify).pack(pady=15)


def export_passwords():
    cursor.execute("SELECT website, account_username, account_password, notes FROM vault")
    data = cursor.fetchall()

    with open("password_export.txt", "w", encoding="utf-8") as file:
        file.write("===== PASSWORD EXPORT =====\n\n")
        for entry in data:
            file.write(f"Website: {entry[0]}\n")
            file.write(f"Username: {entry[1]}\n")
            file.write(f"Password: {entry[2]}\n")
            file.write(f"Notes: {entry[3]}\n")
            file.write("-" * 40 + "\n")

    messagebox.showinfo("Success", "Passwords exported to password_export.txt")


# ---------------- START ---------------- #

login_screen()
root.mainloop()
