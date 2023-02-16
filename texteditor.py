from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Text Ipad")
root.geometry("1200x660")

#Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#Create Text Box
my_text = Text(my_frame,width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#Create Scroll Bar for Text
text_scroll.configure(command=my_text.yview)

#Create Menu Bar
my_menu= Menu(root)
root.configure(menu=my_menu)

#Add File Menu
file_menu = Menu(my_menu)
file_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit")

#Add Edit Menu
edit_menu = Menu(my_menu)
edit_menu.add_cascade(label="File",menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

root.mainloop()
