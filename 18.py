'''18. Create a Tkinter form:
 - Name input
 - Submit button
 - Show entered name'''

from tkinter import *   
def submit():
    name = name_entry.get()
    result_label.config(text=f"Entered Name: {name}")
root = Tk()
root.title("Name Entry Form")
name_label = Label(root, text="Enter your name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()
submit_button = Button(root, text="Submit", command=submit)
submit_button.pack()
result_label = Label(root, text="")
result_label.pack()
root.mainloop()
