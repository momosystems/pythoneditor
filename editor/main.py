import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="Wähle eine Farbe")
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    root.title("Unbenannt - Editor")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("Alle Dateien", "*.*"),
                                                          ("Text Dateien", "*.txt"),
                                                          ("Batch Dateien", "*.bat"),
                                                          ("Momo Systems Dateien", "*.msd")])
    try:
        root.title(os.path.basename(file) + " - Editor")
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())

    except Exception:
        showerror("Error", "Die Datei kann nicht gelesen werden")
        root.title("Unbenannt - Editor")

    finally:
        file.close()


def save_file():
    file = filedialog.asksaveasfilename(initialfile="Unbenannt.txt", defaultextension=".txt", filetypes=[("Alle Dateien", "*.*"),
                                                                                                        ("Text Dateien", "*.txt"),
                                                                                                        ("Batch Dateien", "*.bat"),
                                                                                                        ("Momo Systems Dateien", "*.msd")])
    if file is None:
        return

    else:
        try:
            root.title(os.path.basename(file))
            file = open(file, 'w')

            file.write(text_area.get(1.0, END))

        except Exception:
            showerror("Error", "Die Datei kann nicht gespeichert werden")

        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("Über dieses Program", "Dieses Programm soll allen das arbeiten mit einem Text-Editor erleichtern")

def quit():
    root.destroy()

root = Tk()
root.title("Text Editor")
root.iconbitmap(r"D:\Dev\python programme\editor\document-3503099.ico")
file = None

root_width = 500
root_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (root_width / 2))
y = int((screen_height / 2) - (root_height / 2))

root.geometry("{}x{}+{}+{}".format(root_width, root_height, x, y))

font_name = StringVar(root)
font_name.set("Roboto")

font_size = StringVar(root)
font_size.set("12")

text_area = Text(root, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(root)
frame.grid()

color_btn = Button(frame, text="color", command=change_color)
color_btn.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Datei", menu=file_menu)

file_menu.add_command(label="Neu", command=new_file)
file_menu.add_command(label="Öffnen", command=open_file)
file_menu.add_command(label="Speichern", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Schließen", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Bearbeiten", menu=edit_menu)

edit_menu.add_command(label="Ausschneiden", command=cut)
edit_menu.add_command(label="Kopieren", command=copy)
edit_menu.add_command(label="Einfügen", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Hilfe", menu=help_menu)

help_menu.add_command(label="Über", command=about)

root.mainloop()