from tkinter import *
import random
import tkinter.messagebox as msg


win_num=0
tries=0
def play():
    global color,result,tries,win_num
    user_input=radvar.get()
    computer_input=random.choice(['rock','paper','scissor'])
    if user_input==computer_input:
        result='___DRAW___'
        color='yellow'
    elif user_input=='None':
        result='please choose a valid element'
        color='grey'
    elif (user_input=='rock' and computer_input=='scissor') or (user_input=='scissor' and computer_input=='paper') or (user_input=='paper' and computer_input=='rock'):
        result='`````YOU WON`````'
        color='skyblue'
        win_num+=1
    else:
        result='----YOU LOST---!!!'
        color='red'
    result_widget.config(text=result,bg=color)
    tries+=1
    
def luck():
    global win_num,tries
    win_rate=(win_num/tries)*100
    formatted_winrate = round(win_rate, 2)
    msg.showinfo('luck',f'you are {formatted_winrate}% lucky')

def help0():
    msg.showinfo('help','select rock or paper or scissor and click the check')

def about():
    msg.showinfo('info','just a noob project \ncreated by Momin')

root=Tk()
root.title('Game')
root.geometry('666x444')
main_menu=Menu(root)
menu0=Menu(main_menu,tearoff=0)
menu0.add_command(label='check luck',command=luck)
menu0.add_command(label='help',command=help0)
menu0.add_command(label='about',command=about)
main_menu.add_cascade(label='Options',menu=menu0)
root.config(menu=main_menu)
Label(root,text='choose one',borderwidth=8,bg='skyblue',font=('comicsansms',8,'bold')).pack(fill=X)
radvar=StringVar()
radvar.set(None)
rock=Radiobutton(root,text='Rock',variable=radvar,value='rock').pack(anchor='w')
paper=Radiobutton(root,text='Paper',variable=radvar,value='paper').pack(anchor='w')
scissor=Radiobutton(root,text='Scissor',variable=radvar,value='scissor').pack(anchor='w')
Button(root,text='check',command=play,bg='grey').pack()
Label(root,text='').pack()
result_widget=Label(root,text='',borderwidth=8)
result_widget.pack()
root.mainloop()
