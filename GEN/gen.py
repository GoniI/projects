from Tkinter import *
import Tkinter
import Tkinter as tk
import tkMessageBox
import tempfile


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create label,button,entry & text widgets into our frame"""
        self.inst_lbl = Label(self, text="    Enter Code", font=("Courier", 15, "bold"))
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        # entry widgets
        #(input)
        self.inp_ent = Entry(self, font=("Courier", 14, "bold"), )
        self.inp_ent.grid(row=1, column=0, sticky=W)

        self.submit_btn = Button(self, text="Generate", font=("Courier", 14, "bold"), width=19, bd=4, command=self.reveal)
        self.submit_btn.grid(row=2, column=0, sticky=W)

        # text widget ( to display the output)
        self.output_txt = Text(self, font=("Courier", 14, "bold"), width=20, height=2, wrap=WORD)
        self.output_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        contents = self.inp_ent.get()
        list1 = [["U", "T", "E", "A", "Q", "P", "F", "R", "]", "\\"],
                 ["]", "\\", "_", "^", "Y", "X", "[", "Z", "U", "T"],
                 ["]", "\\", "_", "^", "R", "V", "[", "Z", "U", "T"],
                 ["I", "H", "K", "J", "O", "L", "O", "P", "A", "@"],
                 ["Q", "P", "S", "T", "U", "T", "W", "V", "Y", "X"],
                 ["\\", "]", "P", "_", "C", "Y", "Z", "[", "W", "U"],
                 ["\\", "]", "O", "_", "X", "Y", "Z", "[", "T", "U"],
                 ["I", "K", "K", "A", "M", "L", "O", "N", "A", "@"],
                 ["F", "T", "W", "V", "Q", "P", "S", "R", "]", "\\"],
                 ["]", "\\", "_", "^", "Y", "X", "[", "Z", "U", "T"],
                 ["]", "\\", "_", "^", "A", "P", "[", "X", "U", "T"]]
        x = contents
        b = list(x)
        if len(b) > 11:
            tkMessageBox.showinfo("Error", "Enter value less than or equal to 11digits")
        c = []
        if b[0] == "-":
            b.remove("-")
            c.insert(0, "H")
            inti = map(int, b)
            for i in range(len(b)):
                c.append(list1[i + 1][inti[i]])
        else:
            inti = map(int, b)
            for i in range(len(b)):
                c.append(list1[i][inti[i]])
        zhgl = (''.join(c))
        self.output_txt.delete(0.0, END)
        self.output_txt.insert(0.0, zhgl)


root = Tk()
root.geometry("220x160")
app = Application(root)

# right-click


def rClicker(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''
    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-x>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')

        e.widget.focus()

        nclst = [
            (' Cut', lambda e=e: rClick_Cut(e)),
            (' Copy', lambda e=e: rClick_Copy(e)),
            (' Paste', lambda e=e: rClick_Paste(e)),
        ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root + 40, e.y_root + 10, entry="0")

    except TclError:
        print ' - rClick menu, something wrong'
        pass

    return "break"


def rClickbinder(r):

    try:
        for b in ['Text', 'Entry', 'Listbox', 'Label']:
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print ' - rClickbinder, something wrong'
        pass


# center program
def window(main):
    main.title("Keygen")
    main.update_idletasks()
    width = main.winfo_width()
    height = main.winfo_height()
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}+{}+{}'.format(width, height, x, y))


window(root)
ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00' * 1282 + b'\xff' * 64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)


rClickbinder(app)
root.iconbitmap(default=ICON_PATH)
root.mainloop()
