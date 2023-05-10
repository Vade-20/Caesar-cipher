import string
from tkinter import *
from PIL import ImageTk, Image
import pyperclip

root = Tk()
root.title('Caesar cipher')
root.geometry('750x750')
root.resizable(height=False,width=False)

root.iconbitmap(r'Caesar cipher\laurel.ico')
image = Image.open(r"Caesar cipher\Untitled.jpg")
image = image.resize((750, 750))
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

image_2 = Image.open(r"Caesar cipher\Untitled11.jpg")
image_2 = image_2.resize((100, 75))
background_image_2 = ImageTk.PhotoImage(image_2)

image_3 = Image.open(r"Caesar cipher\Untitled22.jpg")
image_3 = image_3.resize((100, 75))
background_image_3 = ImageTk.PhotoImage(image_3)




alpha_s = {i:j for j,i in enumerate(string.ascii_lowercase)}
alpha_b = {i:j for j,i in enumerate(string.ascii_uppercase)}
digi_s = {int(j):i for j,i in enumerate(string.ascii_lowercase)}
digi_b = {int(j):i for j,i in enumerate(string.ascii_uppercase)}

def decode(text:str,shift:int):
    if shift>25:
        shift = shift%25
    ans = ''
    for i in text:
        if i not in string.ascii_letters:
            ans += i
            continue
        if i.islower():
            num = int(alpha_s[i])
            if num<shift:
                num = 25+num-shift
            else:
                num = num-shift
            ans = ans+digi_s[num]
        elif i.isupper():
            num = int(alpha_b[i])
            if num<shift:
                num = 25+num-shift
            else:
                num = num-shift
            ans = ans+digi_b[num]
    return ans


def encode(text:str,shift:int):
    if shift>25:
        shift = shift%25
    ans =''
    for i in text:
        if i not in string.ascii_letters:
            ans += i
            continue
        if i.islower():
            num = int(alpha_s[i])
            if num+shift>25:
                num = num+shift-25
            else:
                num = num + shift
            ans = ans+digi_s[num]
        elif i.isupper():
            num = int(alpha_b[i])
            if num+shift>25:
                num = num+shift-25
            else:
                num = num + shift
            ans = ans+digi_b[num]     
    return ans


def perform():
    from tkinter import messagebox
    global var,int_var
    command = var.get()
    try:
        shift = int_var.get()
    except:
        messagebox.showerror('Error','Please select a shift')
        return None
    text = t1.get('1.0',END)
    if text=='\n':
        text = pyperclip.paste()
        t1.insert('1.0',text)
    if command not in ['Encode','Decode']:
        messagebox.showerror('Error',"Please select a mode Encode or Decode")
        return None
    elif command=='Encode':
        ans = encode(text,shift)
    else:
        ans = decode(text,shift)
    t2.config(state='normal')
    t2.delete('1.0',END)
    t2.insert('1.0',ans)
    pyperclip.copy(ans)
    t2.config(state='disabled')
        
def reset():
    global var,int_var
    var.set('Select a Mode ')
    int_var.set('Select a shift')
    t2.config(state='normal')
    t2.delete('1.0',END)
    t2.config(state='disabled')
    t1.delete('1.0',END)
    
    

l2 = Label(root,text='Please enter the \ntext here--->',fg='#5e6464',font=('Times New Roman', '20','bold'),bg='#c49936',relief='sunken',height=3)
l2.place(x=0,y=470,)
l3 = Label(root,text='Output--->',fg='#5e6464',font=('Times New Roman', '20','bold'),bg='#c49936',relief='sunken',height=3,width=12)
l3.place(x=0,y=570,)

var = StringVar()
var.set('Select a Mode')
slide = OptionMenu(root, var,*['Encode','Decode'])
slide.config(fg='#5e6464',  font=('Times', '20','bold'),relief='sunken',bg="#c49936",width=24,
                highlightbackground='grey', highlightthickness=2)
slide.place(x=0,y=420)

int_var = IntVar()
int_var.set('Select a shift')
slide_2 = OptionMenu(root, int_var,*[i for i in range(26)])
slide_2.config(fg='#5e6464',  font=('Times', '20','bold'),relief='sunken',bg="#c49936",width=20,
                highlightbackground='grey', highlightthickness=2)
slide_2.place(x=375,y=420)

b1 = Button(root,command=perform,image=background_image_2,width=100)
b1.place(x=225,y=670)
b1 = Button(root,command=reset,image=background_image_3,width=100)
b1.place(x=320,y=670)

t1 = Text(root,fg='#5e6464', bg='#c49936',font=('Times New Roman', '20','bold'), wrap='word',width=35,height=3)
t1.insert(END,'')
t1.place(x=200,y=470)
t2 = Text(root,fg='#5e6464', bg='#c49936',font=('Times New Roman', '20','bold'), wrap='word',width=35,height=3,state=DISABLED)
t2.insert(END,'')
t2.place(x=200,y=570)
mainloop()