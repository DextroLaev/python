from tkinter import *
from tkinter import messagebox
import mysql.connector


#The student management system
def sdbms():
    window.quit()
    window.destroy()
    window.quit()
    def search():
        text.delete(1.0,END)   
        try:
                Class1=''
                section=''
                name=''
                admision=''
                name=entry_Name.get()
                Class1=entry_Class.get()
                section=entry_Section.get()
                roll=entry_Roll_no.get()
                admision=entry_Admission_no.get()
                mydb=mysql.connector.connect(host='localhost',user='root',password='05042002',database='school_information')
                cursor=mydb.cursor()
                if Class1 !='' and section !='':
                    strg="select * from information where Class='%s' and Section='%s' "%(Class1,section)
                else:
                    strg="select * from information where Class1='%s' and roll='%s'"%(Class1,roll)
                    if name !='' and Class1!='' and section!='':
                        strg="select * from information where name='%s' and Class1='%s' and section='%s' " %(name,Class1,section)
                    else:
                        strg="select * from information where class='%s' or name='%s' or admision_no='%s' or roll='%s'"%(Class1,name,admision,roll)
                cursor.execute(strg)
                result=cursor.fetchall()
                mydb.commit()
                text.insert(INSERT, 'Students found with these informations are :-\n\n')
                                                        
                for i in result:
                    
                    text.insert(INSERT, 'Name:-')                                #Searching is not working properly
                    text.insert(INSERT , i[0])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT, 'Roll no:-')
                    text.insert(INSERT, i[1])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT, 'Class:-')
                    text.insert(INSERT, i[2])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT, 'Section:-')
                    text.insert(INSERT, i[3])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT, 'Admision no.:-')
                    text.insert(INSERT, i[4])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT, '-------------')
                    text.insert(INSERT, '\n')
            
        except:
            text.insert(INSERT,'Nothing found with this information')

    #The adding function
    def add():
        text.delete(1.0,END)
        try:
                    
            name=entry_Name.get()
            Class1=entry_Class.get()
            section=entry_Section.get()
            roll=entry_Roll_no.get()
            admision=entry_Admission_no.get()
            mydb=mysql.connector.connect(host='localhost',user='root',password='05042002',database='school_information')
            cursor=mydb.cursor()
            strg="insert into information values('%s','%s','%s','%s','%s')"%(name,Class1,section,roll,admision)
            cursor.execute(strg)
            mydb.commit()    
            text.insert(INSERT, 'Data Entered ')
                
        except:
            text.insert(INSERT, 'Sorry unable to add because of some error in the information given!!!!!\nPlease check the given informations correctly and try again')

    #The delete function
    def delete():
        
           question=messagebox.askyesno('Delete', 'DO YOU WANT TO DELETE IT ?')
           if question==True:
                text.delete(1.0,END)
                try:
                
                    name=entry_Name.get()
                    Class1=entry_Class.get()
                    section=entry_Section.get()
                    roll=entry_Roll_no.get()
                    admision=entry_Admission_no.get()

                    mydb=mysql.connector.connect(host='localhost',user='root',password='05042002',database='school_information')
                    cursor=mydb.cursor()
                    strg="Delete from information where Name='%s' or admision_no='%s'"%(name,admision)
                    cursor.execute(strg)
                    mydb.commit()
                    text.insert(INSERT, 'Data is deleted')
                except:
                    text.insert(INSERT,'All informations are not given properly')
           else:
              
              text.insert(INSERT, 'Thank you :)')

    #The update function
    def update():

        question=messagebox.askyesno('update','DO YOU REALLY WANT TO UPDATE')
        if question==True:
            text.delete(1.0,END)
            try:
                
                name=entry_Name.get()
                Class1=entry_Class.get()
                section=entry_Section.get()
                roll=entry_Roll_no.get()
                admision=entry_Admission_no.get()

                mydb=mysql.connector.connect(host='localhost',user='root',password='05042002',database='school_information')
                cursor=mydb.cursor()
                strg="update information set Name='%s' ,  Roll='%s' ,  Class='%s' ,  Section='%s' where admision_no='%s'" %(name,roll,Class1,section,admision)
                cursor.execute(strg)
                mydb.commit()
                text.insert(INSERT, 'Data Updated\nThank you')
                
            except:
                text.insert(INSERT, 'Informations are not given correctly!!!')          
                 
        else:
            text.insert(INSERT, 'Thanks :)')
            
    #This is for exiting the dbms
    def Exit():
        exit=messagebox.askyesno('Exit', 'DO TOU WANT TO CONTINUE')
        if exit==True:
            root.destroy()

    root=Tk()

    #Creating canvas along with scrollbar and text field
    scroll=Scrollbar(root)

    canvas=Canvas(root, width = 1000, height=500, bg='light green')

    text=Text(root, width=56, height=26,wrap=WORD,padx=10,pady=10,yscrollcommand=scroll.set)
    scroll.config(command=text.yview)
    scroll.pack(side=RIGHT,fill=Y)

    canvas.pack()

    #Creating labels
    Database=Label(root, text='STUDENT DATABASE MANAGEMENT SYSTEM', fg='red',bg='light green')
    Name=Label(root, text='Name',bg='light green')                                                 #These are the labels we need
    Class=Label(root, text='Class',bg='light green')
    Section=Label(root, text='Section',bg='light green')
    Roll_no=Label(root, text='Roll no.',bg='light green')
    Admission_no=Label(root, text='Admission no.',bg='light green')

    #Creating entry section
    entry_Name=Entry(root,width=30)
    entry_Class=Entry(root,width=30)                                 #These are for giving user input
    entry_Section=Entry(root,width=30)
    entry_Roll_no=Entry(root,width=30)
    entry_Admission_no=Entry(root,width=30)

    #Creating Buttons
    Add=Button(root, text='Add',width=14,bg='green',command=add)
    Delete=Button(root, text='Delete',width=14,bg='green', command=delete)                   #These are the buttons
    Search=Button(root, text='Search',width=14,bg='green',command=search)
    Update=Button(root, text='Update',width=14,bg='green', command=update)

    #Creating menu bar
    menu_bar=Menu(root)
    root.config(menu=menu_bar)

    File=Menu(menu_bar)
    menu_bar.add_cascade(label='File', menu=File)
    File.add_command(label='New Entry')
    File.add_command(label='Open Entry')                    #These section is for menu bar at the top
    File.add_separator()
    File.add_cascade(label='Save')

    Save_as=Menu(File)
    File.add_cascade(label='Save as', menu=Save_as)
    Save_as.add_command(label='New entry')
    File.add_separator()

    File.add_command(label='Exit', command=Exit)

    #Placing the gui's
    Database.place(x=130,y=30)
    Name.place(x=80,y=100)
    Class.place(x=80,y=150)
    Section.place(x=80,y=200)
    Roll_no.place(x=80,y=250)
    Admission_no.place(x=80,y=300)

    entry_Name.place(x=230,y=100)
    entry_Class.place(x=230,y=150)
    entry_Section.place(x=230,y=200)
    entry_Roll_no.place(x=230,y=250)
    entry_Admission_no.place(x=230,y=300)

    Add.place(x=120,y=350)
    Search.place(x=250,y=350)
    Update.place(x=120,y=400)
    Delete.place(x=250,y=400)

    line=canvas.create_line(30,20,970,20)
    line=canvas.create_line(30,20,30,469)
    line=canvas.create_line(479,20,479,469)
    line=canvas.create_line(30,469,970,469)
    line=canvas.create_line(970,469,970,20)
    text.place(x=490,y=24.5)

    root.title('STUDENT DATABASE MANAGEMENT SYSTEM')
    root.geometry('1000x500')
    root.mainloop()

#The library management system
def ldbms():    
    #window.quit()
    #window.destroy()
    #window.quit()
    def quit():
        ask=messagebox.askyesno('EXIT', 'DO YOU TO QUIT')
        if ask==True:
            root.destroy()

    def add():
        text.delete(1.0,END)
        try:            
            name = entry_St_name.get()
            Class1 = entry_Class.get()
            book_name = entry_Book_name.get()
            book_id = entry_Book_id.get()
            d_o_p = entry_d_o_p.get()
            mydb = mysql.connector.connect(host="localhost",user="root",password="05042002",database="school_information")
            cursor = mydb.cursor()
            strg="insert into library values('%s','%s','%s','%s','%s')" %(name,Class1,book_name,book_id,d_o_p)
            cursor.execute(strg)
            mydb.commit()
            text.insert(INSERT,"Data Entered..:)")
        except:
            text.insert(INSERT,"sorry we are not able to enter the data plz try again.")

    def delete():
        ask=messagebox.askyesno("Delete","Do you want to delete")
        text.delete(1.0,END)
        if ask==True:
                        
            try:
                name = entry_St_name.get()
                Class1 = entry_Class.get()
                book_id = entry_Book_id.get()        
                mydb= mysql.connector.connect(host="localhost",user="root",password="05042002",database="school_inforamtion")
                cursor= mydb.cursor()
                strg="Delete from library where student_name='%s'and class='%s' and book_id='%s'" %(name,Class1,book_id)
                cursor.execute(strg)
                mydb.commit()
                text.insert(INSERT,"The entry successfully deleted..")
            except:            
                text.insert(INSERT,"Sorry data not deleted due to some error plz check the information you have given and try again later..")
        else:
            text.insert(INSERT,"Thank you")
        
    def update():
        ask=messagebox.askyesno("Update","Do you really want to update")
        text.delete(1.0,END)
        if ask==True:
                        
            try:
                name = entry_St_name.get()
                Class1 = entry_Class.get()
                book_name = entry_Book_name.get()
                book_id = entry_Book_id.get()
                d_o_p = entry_d_o_p.get()
                mydb=mysql.connector.connect(host="localhost",user="root",password="05042002",database="school_information")
                cursor=mydb.cursor()
                strg="update library set class='%s', book_name='%s' , book_id='%s' , d_o_p='%s' where student_name='%s'" %(Class1,book_name,book_id,d_o_p,name)
                cursor.execute(strg)
                mydb.commit()
                text.insert(INSERT,"Data updated successfully..\nThank you")
            except:
                text.insert(INSERT,"Sorry!! unable to update the data.\nplease check the given information and try again..\nYou also need to give all the information of the student.....\n\nTHANK YOU... ")
        else:
           text.insert(INSERT,"Thank you")
           
    def search():
            text.delete(1.0,END)
            try:
                name=''
                Class1=''
                book_name=''
                d_o_p=''
                book_id=''
                name = entry_St_name.get()
                Class1 = entry_Class.get()
                book_name = entry_Book_name.get()
                book_id = entry_Book_id.get()
                d_o_p = entry_d_o_p.get()
                mydb= mysql.connector.connect(host='localhost',user='root',password='05042002',database='school_information')
                cursor= mydb.cursor()
                if name!='' and Class1!='':                
                    strg="select * from library where student_name='%s' and class='%s'" %(name,Class1)
                else:
                    if name!='':
                        strg="select * from library where student_name='%s'" %(name)
                    else:
                        if Class1!='':
                            strg="select * from library where class='%s'" %(Class1)
                        else:
                            if book_name!='':
                                strg="select * from library where book_name='%s'" %(book_name)
                            else:
                                if book_id!='':
                                    strg="select * from library where book_id='%s'" %(book_id)
                                else:
                                    if d_o_p!='':
                                        strg="select * from library where d_o_p='%s'" %(d_o_p)
                cursor.execute(strg)
                result=cursor.fetchall()
                mydb.commit()
                text.insert(INSERT,"Students found are :- ")
                text.insert(INSERT,'\n\n')
                for i in result:
                    text.insert(INSERT,"Name:- ")
                    text.insert(INSERT,i[0])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT,"Class:- ")
                    text.insert(INSERT,i[1])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT,"Book Name:- ")
                    text.insert(INSERT,i[2])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT,"Book Id:- ")
                    text.insert(INSERT,i[3])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT,"Date of publish:- ")
                    text.insert(INSERT,i[4])
                    text.insert(INSERT,'\n')
                    text.insert(INSERT,"---------------------------")
                    text.insert(INSERT,'\n\n')
            except:
                text.insert(INSERT,"Not found")
                
    def fullstatus():
        text.delete(1.0,END)
        try:
            name=''
            Class1=''
            book_name=''
            d_o_p=''
            book_id=''
            name = entry_St_name.get()
            Class1 = entry_Class.get()
            book_name = entry_Book_name.get()
            book_id = entry_Book_id.get()
            d_o_p = entry_d_o_p.get()
            mydb=mysql.connector.connect(host="localhost",user="root",password="05042002",database="school_information")
            cursor=mydb.cursor()
            if name!='':
                strg="select library.name,information.class,information.section,information.roll,information.admision_no,library.book_name,library.book_id,library.d_o_p from information,library where information.name=library.name and library.name='%s'" %(name)            
            else:
                if Class1!='':
                    strg="select library.student_name,information.class,information.section,information.roll,information.admision_no,library.book_name,library.book_id,library.d_o_p from information,library where information.class=library.class and library.class='%s'" %(Class1)
                else:
                    if book_name!='':
                        strg="select student_name,information.class,information.section,information.roll,information.admision_no,book_name,book_id,d_o_p from information,library where information.class=library.class and library.book_name='%s'" %(book_name)
            cursor.execute(strg)
            result=cursor.fetchall()                            
            text.insert(INSERT,"All information about student are:- \n\n")
            for i in result:
                text.insert(INSERT,"Name:- ")
                text.insert(INSERT,i[0])
                text.insert(INSERT,'\n')
                text.insert(INSERT,"Class:- ")
                text.insert(INSERT,i[1])
                text.insert(INSERT,'\n')
                text.insert(INSERT,"Section:- ")
                text.insert(INSERT,i[2])
                text.insert(INSERT,'\n')
                text.insert(INSERT,"Roll no.:- ")
                text.insert(INSERT,i[3])
                text.insert(INSERT,'\n')
                text.insert(INSERT,"Admision no.:- ")
                text.insert(INSERT,i[4])
                text.insert(INSERT,'\n')
                text.insert(INSERT,"Book Name:- ")
                text.insert(INSERT,i[5])
                text.insert(INSERT,'\n')
                text.insert(INSERT,"Book Id:- ")
                text.insert(INSERT,i[6])
                text.insert(INSERT,'\n')
                text.insert(INSERT,"Date of publish:- ")
                text.insert(INSERT,i[7])
                text.insert(INSERT,'\n-------------------------------------')
                text.insert(INSERT,'\n\n')
        except:
            text.insert(INSERT,"Nothing found ......")
    root=Tk()
    
    #creating the canvas and creating textbar along with scrollbar
    canvas=Canvas(root, width=1000, height=700, bg='light green')
    scroll=Scrollbar(root)
    text=Text(root, width=108,height=23,wrap=WORD,pady=10,padx=10,yscrollcommand=scroll.set)
    scroll.config(command=text.yview)
    scroll.pack(side=RIGHT,fill=Y)    
    canvas.pack()
    text.place(x=55,y=280)
    
    #Creating the labels
    library=Label(root, text='**---LIBRARY  MANAGEMENT  SYSTEM---**',font=('altic',12), bg='light green', fg='red')
    Student_name=Label(root, text='Student Name:',font=('altic',11), bg='light green')
    Class=Label(root, text='Class:', bg='light green',font=('altic',11))
    Book_name=Label(root, text='Book Name:', bg='light green',font=('altic',10))
    Book_id=Label(root, text='Book Id:', bg='light green',font=('altic',10))
    d_o_p=Label(root, text='Date of publish(YYYY-MM-DD):', bg='light green',font=('altic',10))

    #craeting the entry box
    entry_St_name=Entry(root,width=26)
    entry_Class=Entry(root,width=26)
    entry_Book_name=Entry(root,width=26)
    entry_Book_id=Entry(root,width=26)
    entry_d_o_p=Entry(root,width=26)

    #creating menubar
    menu_bar=Menu(root)
    root.config(menu=menu_bar)
    file=Menu(menu_bar)
    menu_bar.add_cascade(label="FILE", menu=file)

    open1=Menu(file)
    file.add_cascade(label='Open', menu=open1)
    open1.add_command(label='Student Management system',command=sdbms)
    
    file.add_command(label='Exit',command=quit)
    
    #creating buttons
    Add=Button(root, text='Add',width=18,bg='green',command=add)
    Delete=Button(root, text='Delete',width=18,bg='green',command=delete)                   
    Search=Button(root, text='Search',width=18,bg='green',command=search)
    Update=Button(root, text='Update',width=18,bg='green',command=update)
    Status=Button(root, text='Full Status',width=18,bg='green',command=fullstatus)
                  
    #Placing the guis
    library.place(x=350,y=40)
    Student_name.place(x=55,y=120)
    entry_St_name.place(x=55,y=150)
    Class.place(x=235,y=120)
    entry_Class.place(x=235,y=150)
    Book_name.place(x=415,y=120)
    entry_Book_name.place(x=415,y=150)
    Book_id.place(x=595,y=120)
    entry_Book_id.place(x=595,y=150)
    d_o_p.place(x=775,y=120)
    entry_d_o_p.place(x=775,y=150)

    line=canvas.create_line(55,215,937,215)
    line=canvas.create_line(55,215,55,265)
    line=canvas.create_line(55,265,937,265)
    line=canvas.create_line(937,265,937,215)
    Add.place(x=65,y=225)
    Delete.place(x=245,y=225)
    Search.place(x=425,y=225)
    Update.place(x=605,y=225)
    Status.place(x=785,y=225)
    line=canvas.create_line(20,20,977,20)
    line=canvas.create_line(20,20,20,684)
    line=canvas.create_line(20,684,977,684)
    line=canvas.create_line(977,684,977,20)
   
    root.title('LIBRARY MANAGEMENT SYSTEM')
    root.geometry('1000x700')
    root.mainloop()
    
#The quit function of the main window
def quit():
    ask=messagebox.askyesno('Exit', 'DO YOU WANT TO QUIT')
    if ask==True:
        window.destroy()

#The main window
window=Tk()

#Creating the canvas and a label
canvas=Canvas(window, width=400, height=400 , bg='light green')
canvas.pack()

school=Label(window, text='----SCHOOL MANAGEMENT SYSTEM----',bg='light green',fg='red')

#Creating the buttons
student=Button(window, text='STUDENT MANAGEMENT SYSTEM', width=37, bg='pink',command=sdbms)
library=Button(window, text='SCHOOL LIBRARY SYSTEM',width=37,bg='pink',command=ldbms)
school_inf=Button(window, text='SCHOOL MANAGEMENT SYSTEM', width=37, bg='pink')
marks=Button(window, text='STUDENTS MARKS MANAGEMENT SYSTEM',width=37,bg='pink')

#menubar
menu_bar=Menu(window)
window.config(menu=menu_bar)

file=Menu(menu_bar)
menu_bar.add_cascade(label='FILE', menu=file)
file.add_command(label='Exit',command=quit)

#Placing the guis
school.place(x=90,y=20)
student.place(x=70,y=90)
library.place(x=70,y=160)
school_inf.place(x=70,y=230)
marks.place(x=70,y=300)

line=canvas.create_line(20,10,20,372)
line=canvas.create_line(379,10,379,372)
line=canvas.create_line(20,372,379,372)
line=canvas.create_line(20,10,379,10)

window.title('SCHOOL MANAGEMENT SYSTEM')
window.geometry('400x400')
window.mainloop()