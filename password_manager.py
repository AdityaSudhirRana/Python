import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import hashlib




def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()






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
    hashed = hash_password("admin123")
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", hashed))
    conn.commit()






root = tk.Tk()
root.title("Password Manager Login")
root.geometry("400x300")
root.configure(bg="white")


def login():
    entered_user = username_entry.get()
    entered_pass = hash_password(password_entry.get())

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (entered_user, entered_pass))

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








def open_dashboard():
    dash = tk.Tk()
    dash.title("Password Vault")
    dash.geometry("900x550")
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
    tree.column("Website", width=650, anchor="w")

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






def open_entry_window():
    selected = tree.focus()
    if not selected:
        return

    item = tree.item(selected)["values"]
    cursor.execute("SELECT * FROM vault WHERE id=?", (item[0],))
    data = cursor.fetchone()

    win = tk.Toplevel()
    win.title(data[1])
    win.geometry("700x400")
    win.configure(bg="#f5f5f5")

    tk.Label(win, text=f"Username: {data[2]}").pack(pady=5)
    tk.Label(win, text=f"Password: {data[3]}").pack(pady=5)
    tk.Label(win, text=f"Website: {data[1]}").pack(pady=5)
    tk.Label(win, text=f"Notes: {data[4]}").pack(pady=5)

    tk.Button(win, text="Delete",
              bg="#ea4335", fg="white",
              command=lambda: delete_entry(data[0], win)).pack(pady=15)


def delete_entry(entry_id, window):
    cursor.execute("DELETE FROM vault WHERE id=?", (entry_id,))
    conn.commit()
    load_data()
    window.destroy()






def export_prompt():
    win = tk.Toplevel()
    win.title("Confirm Export")
    win.geometry("350x200")

    tk.Label(win, text="Re-enter Login Password").pack(pady=15)
    entry = tk.Entry(win, show="*")
    entry.pack()

    def verify():
        cursor.execute("SELECT password FROM users WHERE username='admin'")
        real_hash = cursor.fetchone()[0]

        if hash_password(entry.get()) == real_hash:
            export_passwords()
            win.destroy()
        else:
            messagebox.showerror("Error", "Incorrect Password")

    tk.Button(win, text="Confirm", command=verify).pack(pady=10)


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

    messagebox.showinfo("Success", "Passwords exported successfully")






login_screen()
root.mainloop()
