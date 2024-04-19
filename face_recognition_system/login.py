from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from main import Face_Recognition_System
import subprocess


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login Page")


        # Loading Background image
        bg_image = Image.open(r"image_assets/login_final.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photoImgbg = ImageTk.PhotoImage(bg_image)
    
        # Displaying background image
        bg_img = Label(self.root, image=self.photoImgbg)
        bg_img.place(x=0, y=0, width=1530, height=800)

        #Lable for Login 
        title_label = Label(bg_img, text="Teacher Login", font=("times new roman", 35, "bold"), fg="white",bg="black",compound='center', highlightthickness=0, highlightbackground="black")
        title_label.place(x=0, y=0, width=1530, height=70)

         #Login template
        login_image = Image.open(r"image_assets/login_temp_final2.jpg")
        login_image = login_image.resize((500,500),Image.LANCZOS)
        self.loginImgbg = ImageTk.PhotoImage(login_image)
        login_img = Label(self.root,image=self.loginImgbg)
        login_img.place(x=950,y=150,width=500,height=500)

        #EntryField for Username   
        self.username_entry = ttk.Entry(login_img,width=20,font=("times new roman",12,"bold"),foreground="gray")
        self.username_entry.place(x=70,y=105,width=300,height=50)

        #EntryField for Password 
        self.password_entry = ttk.Entry(login_img,width=20,font=("times new roman",12,"bold"),foreground="gray")
        self.password_entry.place(x=70,y=275,width=300,height=50)

        # Lable for Login Button
        loginBtn_label = Label(login_img, text="Login", font=("times new roman", 35, "bold"), fg="white", bg="black", compound='center', highlightthickness=0, highlightbackground="black", cursor="hand2")
        loginBtn_label.place(x=185, y=400, width=120, height=60)
        loginBtn_label.bind("<Button-1>", self.login)  # Bind the login method to the button click


    def login(self, event):

        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error","Fill all the fields!")

        elif self.username_entry.get() == "Admin" or self.password_entry.get() == "@dmin":

            self.root.destroy()  # Close the login window
            subprocess.run(["python", "main.py"])    
            # messagebox.showinfo("Success","Welcome!")
        else:
             messagebox.showerror("Error","Invalid Credentials!")
        



if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()