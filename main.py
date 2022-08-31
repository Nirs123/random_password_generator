import random
import tkinter as tk
import pyperclip

win = tk.Tk()
win.title("Random Password Generator")
win.geometry("350x600")
win.minsize(350,600)
win.maxsize(350,600)

min_letters = "abcdefghijklmnopqrstuvwxyz"
maj_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "&!#$%"

s_min_letters = tk.IntVar()
s_maj_letters = tk.IntVar()
s_numbers = tk.IntVar()
s_special = tk.IntVar()
password_lengh = tk.StringVar()

res = False
memory_res = None

class Error_Box:
    def __init__(self,msg):
        self.msg = msg
        self.tmp_box = tk.Toplevel(win)
        self.tmp_box.title("ERROR")
        text = tk.Label(self.tmp_box, text=msg,font=('Segoe UI Black',"22"))
        button = tk.Button(self.tmp_box, text="OK",font=('Segoe UI Black',"22"),command=self.tmp_box.destroy)
        text.grid(row=0,column=0)
        button.grid(row=1,column=0)

def generate():
    chars = ""
    if s_maj_letters.get() == 0 and s_min_letters.get() == 0 and s_numbers.get() == 0 and s_special.get() == 0:
        Error_Box("No characters selected")
    else:
        if s_min_letters.get() == 1:
            chars += min_letters
        if s_maj_letters.get() == 1:
            chars += maj_letters
        if s_numbers.get() == 1:
            chars += numbers
        if s_special.get() == 1:
            chars += special
        random_password(chars)

def c_password(e):
    pyperclip.copy(e)

def random_password(chars):
    global res,memory_res
    result = ""
    if password_lengh.get() == "":
        Error_Box("No password lengh")
    elif password_lengh.get().isdigit() == False:
        Error_Box("Password cannot be text or float")
    elif int(password_lengh.get()) > 28:
        Error_Box("Password lengh too big")
    else:
        if res:
            memory_res.grid_forget()
        res = True
        for i in range(int(password_lengh.get())):
            result += chars[random.randint(0,len(chars)-1)]
        t_res_title = tk.Label(win,text="Result:",font=('Segoe UI Black',"16"))
        t_res = tk.Label(win,text=result,font=('Segoe UI Black',"14"))
        copy_button = tk.Button(win,text="Copy Password",font=('Segoe UI Black',"14"),command= lambda e = result:c_password(e))
        t_res_title.grid(row=9,column=0,pady=10)
        t_res.grid(row=10,column=0)
        copy_button.grid(row=11,column=0,pady=8)
        memory_res = t_res

title = tk.Label(win,text="Welcome to Random\nPassword Generator",font=('Segoe UI Black',"22"))
subtitle = tk.Label(win,text="Select your options:",font=('Segoe UI Black',"16"))
o_min_letters = tk.Checkbutton(win,text="Min Letters",font=('Segoe UI Black',"14"),variable=s_min_letters)
o_maj_letters = tk.Checkbutton(win,text="Maj Letters",font=('Segoe UI Black',"14"),variable=s_maj_letters)
o_numbers = tk.Checkbutton(win,text="Numbers",font=('Segoe UI Black',"14"),variable=s_numbers)
o_special = tk.Checkbutton(win,text="Special",font=('Segoe UI Black',"14"),variable=s_special)
subtitle_2 = tk.Label(win,text="Enter the password lengh:",font=('Segoe UI Black',"16"))
p_lengh = tk.Entry(win,font=('Segoe UI Black',"14"),textvariable=password_lengh)
b_g = tk.Button(win,text="Generate",font=('Segoe UI Black',"16"),command=generate)

title.grid(row=0,column=0,padx=20,pady=10)
subtitle.grid(row=1,column=0)
o_min_letters.grid(row=2,column=0)
o_maj_letters.grid(row=3,column=0)
o_numbers.grid(row=4,column=0)
o_special.grid(row=5,column=0)
subtitle_2.grid(row=6,column=0,pady=10)
p_lengh.grid(row=7,column=0)
b_g.grid(row=8,column=0,pady=10)

win.mainloop()