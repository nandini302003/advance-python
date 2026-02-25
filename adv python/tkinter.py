import tkinter as tk
from tkinter import ttk

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("STUDENT GRADE BOOK")
root.geometry("1100x700")
root.configure(bg="black")

# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="STUDENT GRADE BOOK",
    font=("Segoe UI", 32, "bold"),
    fg="cyan",
    bg="black"
)
title.pack(pady=20)

# ---------------- STUDENT DATA ----------------

students = [

{"name":"Priya Singh","marks":{"Python":98,"Math":95,"AI":97,"DSA":96}},
{"name":"Nandini Panda","marks":{"Python":88,"Math":92,"AI":85,"DSA":90}},
{"name":"Sneha Das","marks":{"Python":84,"Math":82,"AI":86,"DSA":80}},
{"name":"Rahul Sharma","marks":{"Python":75,"Math":72,"AI":78,"DSA":74}},
{"name":"Arjun Mehta","marks":{"Python":70,"Math":68,"AI":72,"DSA":71}},
{"name":"Amit Kumar","marks":{"Python":65,"Math":60,"AI":68,"DSA":66}},
{"name":"Riya Patel","marks":{"Python":62,"Math":64,"AI":60,"DSA":63}},
{"name":"Karan Verma","marks":{"Python":55,"Math":52,"AI":58,"DSA":54}},
{"name":"Neha Kapoor","marks":{"Python":51,"Math":50,"AI":53,"DSA":52}},
{"name":"Vikram Roy","marks":{"Python":40,"Math":45,"AI":42,"DSA":38}},
{"name":"Simran Kaur","marks":{"Python":35,"Math":30,"AI":40,"DSA":32}},
{"name":"Anjali Gupta","marks":{"Python":90,"Math":88,"AI":92,"DSA":91}},
{"name":"Devansh Joshi","marks":{"Python":80,"Math":78,"AI":82,"DSA":79}},
{"name":"Pooja Reddy","marks":{"Python":72,"Math":70,"AI":74,"DSA":73}},
{"name":"Sahil Malhotra","marks":{"Python":60,"Math":62,"AI":58,"DSA":61}},
{"name":"Tanya Nair","marks":{"Python":48,"Math":50,"AI":45,"DSA":47}}

]

# ---------------- FUNCTIONS ----------------

def get_percentage(student):
    total = sum(student["marks"].values())
    return round(total/4, 2)

def get_grade(percent):

    if percent >= 90: return "A+"
    if percent >= 80: return "A"
    if percent >= 70: return "B"
    if percent >= 60: return "C"
    if percent >= 50: return "D"
    return "F"

# ---------------- TOPPER FRAME ----------------

topper_frame = tk.Frame(root, bg="black")
topper_frame.pack(pady=10)

# ---------------- TABLE ----------------

table_frame = tk.Frame(root, bg="black")
table_frame.pack(pady=10)

columns = ("Rank","Name","Python","Math","AI","DSA","Percentage","Grade")

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=120)

tree.pack()

# Style table
style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background="black",
                foreground="cyan",
                fieldbackground="black")

style.configure("Treeview.Heading",
                background="black",
                foreground="cyan")

# ---------------- SCAN FUNCTION ----------------

def scan():

    # clear previous
    for widget in topper_frame.winfo_children():
        widget.destroy()

    for row in tree.get_children():
        tree.delete(row)

    # calculate percent and grade
    for s in students:
        s["percent"] = get_percentage(s)
        s["grade"] = get_grade(s["percent"])

    # sort students
    sorted_students = sorted(students,
                             key=lambda x: x["percent"],
                             reverse=True)

    # top 3 toppers
    badges = ["🥇", "🥈", "🥉"]

    for i in range(3):

        s = sorted_students[i]

        card = tk.Frame(
            topper_frame,
            bg="black",
            highlightbackground="cyan",
            highlightthickness=2
        )
        card.pack(side="left", padx=15)

        tk.Label(
            card,
            text=s["name"],
            font=("Segoe UI",14,"bold"),
            fg="cyan",
            bg="black"
        ).pack(pady=5)

        tk.Label(
            card,
            text=f"Percentage: {s['percent']}%",
            fg="cyan",
            bg="black"
        ).pack()

        tk.Label(
            card,
            text=f"Grade: {s['grade']}",
            fg="cyan",
            bg="black"
        ).pack()

        tk.Label(
            card,
            text=f"{badges[i]} TOPPER",
            font=("Segoe UI",12,"bold"),
            fg="gold",
            bg="black"
        ).pack(pady=5)

    # fill table
    for i, s in enumerate(sorted_students):

        tree.insert("", "end", values=(
            i+1,
            s["name"],
            s["marks"]["Python"],
            s["marks"]["Math"],
            s["marks"]["AI"],
            s["marks"]["DSA"],
            str(s["percent"])+"%",
            s["grade"]
        ))

# ---------------- BUTTON ----------------

scan_button = tk.Button(
    root,
    text="START SCAN",
    font=("Segoe UI",14),
    fg="cyan",
    bg="black",
    activebackground="cyan",
    activeforeground="black",
    highlightbackground="cyan",
    highlightthickness=2,
    command=scan
)

scan_button.pack(pady=20)

# ---------------- RUN ----------------

root.mainloop()
