from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.geometry("500x500")
root.config(bg="#F8F0DF")

im=Image.open("nissan.png")
resized=im.resize((340,180)) 
newPic = ImageTk.PhotoImage(resized)


fr=Frame(root,width=355,height=460,bg='#FEFBF3').place(x=90,y=10)

img=ImageTk.PhotoImage(file='hon.png')
myL = Label(root, image=newPic)
myL.place(x=95, y=15)

lb1=Label(fr,text="Nissan GT-R 2021",font=('Roboto','15','bold'),bg="#FEFBF3",fg="#EB6383").place(x=115,y=200)
lb2=Label(fr,text="No Plate :    ba 1 chha 1518",font=('Robotobg','9','bold'),bg="#FEFBF3",fg="#EB6383").place(x=115,y=230)
lb3=Label(fr,text="Model No :    APF No.008",font=('Roboto','9','bold'),bg="#FEFBF3",fg="#EB6383").place(x=115,y=260)
lb4=Label(fr,text="Car Availibility :     yes",font=('Roboto','9','bold'),bg="#FEFBF3",fg="#EB6383").place(x=115,y=290)
lb5=Label(fr,text="Model year :     2009",font=('Roboto','9','bold'),bg="#FEFBF3",fg="#EB6383").place(x=115,y=320)
lb6=Label(fr,text="Last Serviced Date:  2022",font=('Roboto','9','bold'),bg="#FEFBF3",fg="#EB6383").place(x=115,y=350)
lb7=Label(fr,text="Cost:  6000/d",font=('Roboto','9','bold'),bg="#FEFBF3",fg="#EB6383").place(x=115,y=380)

def opencreatebook():
    '''
    Function to destroy the current window and open the book create page for booking the car
    '''
    root.destroy()
    import book_create

def opendash():
    '''
    Function to destroy the current window and render at dash page
    
    '''
    root.destroy()
    import dash

btn1=Button(root,text="Book Now",font=("Roboto","12","bold"),activeforeground="white",activebackground="#FFC7C7",bg="#ff7a7a",width=29,bd=0, fg="white", command= opencreatebook).place(x=115,y=430)

backimage= Image.open("backicon.png")
resized=backimage.resize((50,50), Image.ANTIALIAS)
newPic9 = ImageTk.PhotoImage(resized)

backbutton= Button(root, image= newPic9,bd=0,bg="#F8F0DF",activebackground="#F8F0DF", command=opendash).place(x=0,y=0)
root.mainloop()
