from tkinter import *


root=Tk()
root.geometry('1100x650')
root.title('Retoo')
root.configure(bg="lightgray")

#adding the backgroound image
# image_path = PhotoImage(file= "bg5.png")
# bgImage = Label(root, image=image_path)
# bgImage.place(relheight=1, relwidth=1)

#adding a lable
label1=Label(text='WELCOME TO RETOO',font=('times',30,'bold'),bg='lightgray',foreground='black')
label1.grid(row=0, column=2, pady=30)

#Three dot button:
thre_dot_image = PhotoImage(file="Three_dot2.png")
thre_dot_button = Button(root, image= thre_dot_image)
thre_dot_button.grid(row=0, column=0)

# importing the serach icon
serachIcon = PhotoImage(file="serch2.png")

#adding a search bar
searchbar=Entry(root,width=35,font=('arial',30),bd=5,relief=SUNKEN)
searchbar.grid(row=1, column=2, pady = 50)
# searchlable = Label(root, text="Search: ", font=('arial',30, 'bold'))
# searchlable.grid(row=1, column=0, pady = 50)
searchbutton = Button(root, image=serachIcon)
searchbutton.grid(row=1, column=1)

#configuring the columns and rows
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=2)
root.columnconfigure(3,weight=2)















root.mainloop()