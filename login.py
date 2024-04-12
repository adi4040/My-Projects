from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student

import cv2 
import os


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login Page")

    # Loading Background image
        bg_image = Image.open(r"image_assets/gradient_black.jpeg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photoImgbg = ImageTk.PhotoImage(bg_image)
    
    # Displaying background image
        bg_img = Label(self.root, image=self.photoImgbg)
        bg_img.place(x=0, y=0, width=1530, height=800)

    
    #Lable for Login 
        title_label = Label(bg_img, text="Teacher Login", font=("times new roman", 35, "bold"), fg="white",bg="black",compound='center', highlightthickness=0, highlightbackground="black")
        title_label.place(x=0, y=0, width=1530, height=70)
   
    #Login template
        login_image = Image.open(r"image_assets/login_template.jpg")
        login_image = login_image.resize((500,500),Image.LANCZOS)
        self.loginImgbg = ImageTk.PhotoImage(login_image)
        login_img = Label(self.root,image=self.loginImgbg)
        login_img.place(x=500,y=200,width=500,height=500)

    # Lable for Login Button
        loginBtn_label = Label(login_img, text="Login", font=("times new roman", 35, "bold"), fg="white", bg="black", compound='center', highlightthickness=0, highlightbackground="black", cursor="hand2")
        loginBtn_label.place(x=185, y=400, width=120, height=60)
        loginBtn_label.bind("<Button-1>", self.login)  # Bind the login method to the button click


    #TextField for Username   
        self.username_entry = ttk.Entry(login_img,width=20,font=("times new roman",12,"bold"),foreground="gray")
        self.username_entry.place(x=90,y=105,width=300,height=50)
        

    #TextField for Password 
        self.password_entry = ttk.Entry(login_img,width=20,font=("times new roman",12,"bold"),foreground="gray")
        self.password_entry.place(x=90,y=275,width=300,height=50)


    def login(self, event):
        # Replace the following with your actual logic to check credentials
        stored_username = "Kkwpoly"
        stored_password = "Admin"

        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username == stored_username and entered_password == stored_password:
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)
        else:
            messagebox.showerror("Login Error", "Invalid username or password")  # Display an error message


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
