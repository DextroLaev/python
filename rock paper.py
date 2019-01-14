from tkinter import *
from tkinter import messagebox            #Importing the modules
import random


choose=['ROCK','SCISSOR','PAPER']                #Defining some variables
comp_scr=0
player_scr=0

#-------------------------------------------------------------------------------------------------------#
#----------------------------------------Functionality--------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

def exit2():
    ask=messagebox.askyesno('EXIT','DO YOU WANT TO QUIT')                 #The exit function of the application
    if ask==True:
        root.destroy()
        root.quit

#This function is for rock
def rock2():
    global comp_scr
    global player_scr
    choice=random.choice(choose)
    yourtext.delete(1.0,END)
    computertext.delete(1.0,END)
    maintext.delete(1.0,END)
        
    if choice=='ROCK':
        maintext.insert(INSERT,'TIE')
        computertext.insert(INSERT,choice)
        yourtext.insert(INSERT,"ROCK")
    else:
        if choice=='PAPER':
            comp_scr=comp_scr+1           
            maintext.insert(INSERT,"Computer won")            
            comptext.delete(1.0,END)
            comptext.insert(INSERT,comp_scr)
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,"ROCK")
        else:
            player_scr=player_scr+1
            maintext.insert(INSERT,"You won")
            youtext.delete(1.0,END)
            youtext.insert(INSERT,player_scr)
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,"ROCK")

#This function is for paper
def paper2():
    global comp_scr
    global player_scr
    choice=random.choice(choose)
    yourtext.delete(1.0,END)
    computertext.delete(1.0,END)    
    maintext.delete(1.0,END)           
    if choice=='ROCK':                                                          #The whole condition of selecting paper by user
        player_scr=player_scr+1 
        maintext.insert(INSERT,'You won')
        youtext.delete(1.0,END)
        youtext.insert(INSERT,player_scr)
        computertext.insert(INSERT,choice)
        yourtext.insert(INSERT,"PAPER")
    else:
        if choice=='PAPER':
            maintext.insert(INSERT,"TIE")
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,"PAPER")
        else:
            comp_scr=comp_scr+1
            maintext.insert(INSERT,"Computer won")
            comptext.delete(1.0,END)
            comptext.insert(INSERT,comp_scr)
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,"PAPER")

#This function is for scissor
def scissor2():
    global comp_scr
    global player_scr
    choice=random.choice(choose)
    yourtext.delete(1.0,END)
    computertext.delete(1.0,END)    
    maintext.delete(1.0,END)           
    if choice=='ROCK':                                                        #The whole condition for selecting scissor by user
        comp_scr=comp_scr+1 
        maintext.insert(INSERT,"Computer won")
        comptext.delete(1.0,END)
        comptext.insert(INSERT,comp_scr)
        computertext.insert(INSERT,choice)
        yourtext.insert(INSERT,"SCISSOR")
    else:
        if choice=='PAPER':
            player_scr=player_scr+1
            maintext.insert(INSERT,"You won")
            youtext.delete(1.0,END)
            youtext.insert(INSERT,player_scr)
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,"SCISSOR")
        else:
            maintext.insert(INSERT,"TIE")
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,"SCISSOR")


#-------------------------------------------------------------------------------------#
#------------------------------------INTERFACE----------------------------------------#
#-------------------------------------------------------------------------------------#

root=Tk()

#creating the canvas
canvas=Canvas(root, width=500,height=500,bg='black')
canvas.pack()

#creating the labels for game
game=Label(root, text='ROCK PAPER SCISSOR GAME',font=2, fg='skyblue', bg='black')
you=Label(root, text='You:', bg='black',font=2, fg='light green')
computer=Label(root, text='Comp.:', bg='black',fg='red',font=2)
select=Label(root, text='Select one',bg='black',fg='yellow',font=2)

#Creating the buttons
rock=Button(root, text='Rock', bg='orange',fg='black',width=14,command=rock2)
paper=Button(root, text='Paper',bg='orange',fg='black',width=14,command=paper2)
scisor=Button(root, text='Scissor',bg='orange',fg='black',width=14,command=scissor2)
exit1=Button(root, text='EXIT',bg='orange',fg='black',width=14,command=exit2)

#creating text
maintext=Text(root, width=20,height=1,wrap=WORD,pady=10,padx=10)
youtext=Text(root, width=14,height=1)
comptext=Text(root, width=14,height=1)
yourtext=Text(root, width=15,height=1)
computertext=Text(root, width=15,height=1)
youtxt=canvas.create_text(90,340,text='You  choose'+":  ",fill='light green',font=1)
comptxt=canvas.create_text(100,400,text='Comp.  choose'+":  ",fill='red',font=1)


#placing the gui
game.place(x=110,y=30)
you.place(x=30,y=80)
computer.place(x=30,y=280)
rock.place(x=90,y=130)
paper.place(x=90,y=180)
scisor.place(x=90,y=230)
exit1.place(x=165,y=440)

maintext.place(x=240,y=180)
youtext.place(x=90,y=83)
comptext.place(x=90,y=280)
yourtext.place(x=240,y=340)
computertext.place(x=240,y=390)

root.iconbitmap(r'C:\Users\Rajshekhar Rakshit\Desktop')
root.title("ROCK PAPER SCISSOR GAME")
root.geometry('450x480')
root.mainloop()                                                #End of the programme
