import tkinter as tk
counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text= str(counter))
        label.after(1000, count)
    count()


root = tk.Tk()
root.title ("Counting Seconds, A MNyota Software")
label = tk.Label(root, fg = "red")
label.pack()
counter_label(label)
button = tk.Button(root, text = "STOP", width = 25, command = root.destroy)
button.pack()
root.mainloop()

