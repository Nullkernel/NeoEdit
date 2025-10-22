# Importing Required libraries & Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import base64
from fpdf import FPDF
import re

# Defining NeoEdit Class
class NeoEdit:
    # Defining Constructor
    def __init__(self,root):
        # Assigning root
        self.root = root
        # Title of the window
        self.root.title("NeoEdit")
        # Window Geometry
        self.root.geometry("1200x700+200+150")
        # Initializing filename
        self.filename = None
        # Declaring Title variable
        self.title = StringVar()
        # Declaring Status variable
        self.status = StringVar()
        # Creating Titlebar
        self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        self.titlebar.pack(side=TOP,fill=BOTH)
        self.settitle()
        # Creating Statusbar
        self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        self.statusbar.pack(side=BOTTOM,fill=BOTH)
        self.status.set("Welcome To NeoEdit")
        # Creating Menubar
        self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="skyblue")
        self.root.config(menu=self.menubar)
        # Creating File Menu
        self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
        self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
        self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
        self.filemenu.add_command(label="Save As",accelerator="Ctrl+Shift+S",command=self.saveasfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Export as PDF",command=self.export_pdf)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",accelerator="Ctrl+Q",command=self.exit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        # Creating Edit Menu
        self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Undo",accelerator="Ctrl+Z",command=self.undo)
        self.editmenu.add_command(label="Redo",accelerator="Ctrl+Y",command=self.redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Find/Replace",accelerator="Ctrl+F",command=self.find_replace)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        # Creating Tools Menu
        self.toolsmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        self.toolsmenu.add_command(label="Encrypt",command=self.encrypt)
        self.toolsmenu.add_command(label="Decrypt",command=self.decrypt)
        self.menubar.add_cascade(label="Tools", menu=self.toolsmenu)
        # Creating Help Menu
        self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        self.helpmenu.add_command(label="About",command=self.infoabout)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        # Creating Scrollbar
        scrol_y = Scrollbar(self.root,orient=VERTICAL)
        self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",15,"bold"),state="normal",relief=GROOVE,undo=True)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        self.shortcuts()
    # Title setting method
    def settitle(self):
        if self.filename:
            self.title.set(self.filename)
        else:
            self.title.set("Untitled - NeoEdit")
    # File Ops
    def newfile(self,*args):
        self.txtarea.delete("1.0",END)
        self.filename = None
        self.settitle()
        self.status.set("New File Created")
    def openfile(self,*args):
        try:
            self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            if self.filename:
                with open(self.filename,"r") as infile:
                    self.txtarea.delete("1.0",END)
                    self.txtarea.insert(END,infile.read())
                self.settitle()
                self.status.set("Opened Successfully")
        except Exception as e:
            messagebox.showerror("Exception",e)
    def savefile(self,*args):
        try:
            if self.filename:
                data = self.txtarea.get("1.0",END)
                with open(self.filename,"w") as outfile:
                    outfile.write(data)
                self.settitle()
                self.status.set("Saved Successfully")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("Exception",e)
    def saveasfile(self,*args):
        try:
            untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            data = self.txtarea.get("1.0",END)
            with open(untitledfile,"w") as outfile:
                outfile.write(data)
            self.filename = untitledfile
            self.settitle()
            self.status.set("Saved Successfully")
        except Exception as e:
            messagebox.showerror("Exception",e)
    def export_pdf(self):
        try:
            text = self.txtarea.get("1.0",END)
            pdf_filename = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile="Document.pdf", filetypes=[("PDF Files", "*.pdf")])
            if pdf_filename:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                for line in text.split('\n'):
                    pdf.cell(0, 10, line, ln=True)
                pdf.output(pdf_filename)
                self.status.set("Exported to PDF Successfully")
        except Exception as e:
            messagebox.showerror("Exception",e)
    def exit(self,*args):
        op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
        if op>0:
            self.root.destroy()
    # Edit Ops
    def cut(self,*args):
        self.txtarea.event_generate("<<Cut>>")
    def copy(self,*args):
        self.txtarea.event_generate("<<Copy>>")
    def paste(self,*args):
        self.txtarea.event_generate("<<Paste>>")
    def undo(self,*args):
        try:
            self.txtarea.edit_undo()
            self.status.set("Undo Successful")
        except:
            self.status.set("Nothing to Undo")
    def redo(self,*args):
        try:
            self.txtarea.edit_redo()
            self.status.set("Redo Successful")
        except:
            self.status.set("Nothing to Redo")
    def find_replace(self):
        def do_find_replace():
            find_txt = find_entry.get()
            replace_txt = replace_entry.get()
            full_text = self.txtarea.get("1.0",END)
            new_text = full_text.replace(find_txt, replace_txt)
            self.txtarea.delete("1.0",END)
            self.txtarea.insert("1.0", new_text)
            findwin.destroy()
            self.status.set("Find and Replace Done")
        findwin = Toplevel(self.root)
        findwin.title("Find/Replace")
        findwin.geometry("300x150")
        Label(findwin,text="Find:").pack(pady=5)
        find_entry = Entry(findwin)
        find_entry.pack(pady=5)
        Label(findwin,text="Replace:").pack(pady=5)
        replace_entry = Entry(findwin)
        replace_entry.pack(pady=5)
        Button(findwin,text="Replace",command=do_find_replace).pack(pady=20)
    def encrypt(self):
        try:
            text = self.txtarea.get("1.0", END)
            encoded = base64.b64encode(text.encode()).decode()
            self.txtarea.delete("1.0", END)
            self.txtarea.insert(END, encoded)
            self.status.set("Text Encrypted (Base64)")
        except Exception as e:
            messagebox.showerror("Exception",e)
    def decrypt(self):
        try:
            text = self.txtarea.get("1.0", END)
            decoded = base64.b64decode(text.encode()).decode()
            self.txtarea.delete("1.0", END)
            self.txtarea.insert(END, decoded)
            self.status.set("Text Decrypted (Base64)")
        except Exception as e:
            messagebox.showerror("Exception",e)
    def infoabout(self):
        messagebox.showinfo("About NeoEdit","NeoEdit is an enhanced text editor for all your editing needs!")
    def shortcuts(self):
        self.txtarea.bind("<Control-n>",self.newfile)
        self.txtarea.bind("<Control-o>",self.openfile)
        self.txtarea.bind("<Control-s>",self.savefile)
        self.txtarea.bind("<Control-Shift-S>",self.saveasfile)
        self.txtarea.bind("<Control-q>",self.exit)
        self.txtarea.bind("<Control-x>",self.cut)
        self.txtarea.bind("<Control-c>",self.copy)
        self.txtarea.bind("<Control-v>",self.paste)
        self.txtarea.bind("<Control-z>",self.undo)
        self.txtarea.bind("<Control-y>",self.redo)
        self.txtarea.bind("<Control-f>",self.find_replace)
    
if __name__ == "__main__":
    root = Tk()
    NeoEdit(root)
    root.mainloop()