import tkinter as tk
from tkinter import ttk
from datetime import datetime
from collections import Counter

key_history = []
key_counter = Counter()


def classify_key(key):
    if len(key) == 1 and key.isalpha():
        return "Letter"
    elif len(key) == 1 and key.isdigit():
        return "Number"
    elif key in ["space", "Return", "BackSpace", "Tab", "Escape"]:
        return "Special Key"
    else:
        return "Symbol / Modifier"


def on_key_press(event):
    key = event.keysym
    category = classify_key(key)
    time = datetime.now().strftime("%H:%M:%S")

    key_history.append((time, key, category))
    key_counter[key] += 1

    tree.insert("", "end", values=(time, key, category))
    tree.yview_moveto(1)

    total_label.config(text=f"Total Keys: {len(key_history)}")
    last_label.config(text=f"Last Key: {key}")

    if key_counter:
        common_label.config(
            text=f"Most Used: {key_counter.most_common(1)[0][0]}"
        )


def clear_history():
    key_history.clear()
    key_counter.clear()

    for item in tree.get_children():
        tree.delete(item)

    total_label.config(text="Total Keys: 0")
    last_label.config(text="Last Key: -")
    common_label.config(text="Most Used: -")


root = tk.Tk()
root.title("Keyboard Event Visualizer")
root.geometry("850x550")
root.configure(bg="#0f172a")

title = tk.Label(
    root,
    text="⌨️ Keyboard Event Visualizer",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Educational tool to visualize keyboard events inside this window only.",
    font=("Arial", 11),
    bg="#0f172a",
    fg="#94a3b8"
)
subtitle.pack()

stats_frame = tk.Frame(root, bg="#0f172a")
stats_frame.pack(pady=20)

total_label = tk.Label(
    stats_frame,
    text="Total Keys: 0",
    font=("Arial", 12, "bold"),
    bg="#1e293b",
    fg="white",
    padx=20,
    pady=10
)
total_label.grid(row=0, column=0, padx=10)

last_label = tk.Label(
    stats_frame,
    text="Last Key: -",
    font=("Arial", 12, "bold"),
    bg="#1e293b",
    fg="white",
    padx=20,
    pady=10
)
last_label.grid(row=0, column=1, padx=10)

common_label = tk.Label(
    stats_frame,
    text="Most Used: -",
    font=("Arial", 12, "bold"),
    bg="#1e293b",
    fg="white",
    padx=20,
    pady=10
)
common_label.grid(row=0, column=2, padx=10)

button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(pady=10)

clear_btn = tk.Button(
    button_frame,
    text="🗑 Clear History",
    command=clear_history,
    bg="#dc2626",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=15,
    pady=8
)
clear_btn.pack()

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="#1e293b",
    foreground="white",
    fieldbackground="#1e293b",
    rowheight=28,
    font=("Arial", 10)
)

style.configure(
    "Treeview.Heading",
    background="#334155",
    foreground="white",
    font=("Arial", 11, "bold")
)

table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=15)

scrollbar = ttk.Scrollbar(table_frame)
scrollbar.pack(side="right", fill="y")

tree = ttk.Treeview(
    table_frame,
    columns=("Time", "Key", "Category"),
    show="headings",
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=tree.yview)

tree.heading("Time", text="Time")
tree.heading("Key", text="Key Pressed")
tree.heading("Category", text="Category")

tree.column("Time", width=150, anchor="center")
tree.column("Key", width=250, anchor="center")
tree.column("Category", width=250, anchor="center")

tree.pack(fill="both", expand=True)

footer = tk.Label(
    root,
    text="Press keys inside this window to visualize events",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Arial", 10)
)
footer.pack(pady=10)

root.bind("<Key>", on_key_press)

root.mainloop()