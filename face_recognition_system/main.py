from tkinter import *
from tkinter import ttk, filedialog  # Import filedialog module
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import csv
import os
from student import Student
from train import Train
from attendance import Attendance
from face_recog import FaceRecognition


class AnimatedGIFLabel(Label):
    def __init__(self, master, filename, width, height, delay=70):
        self.image = Image.open(filename)
        self.width = width
        self.height = height
        self.delay = delay
        self.frames = [ImageTk.PhotoImage(self.image.resize((width, height)))]

        Label.__init__(self, master, image=self.frames[0])

        self.idx = 0
        self.after(self.delay, self.update)

        # Bind events for cursor change
        self.bind("<Enter>", self.change_cursor_to_hand)
        self.bind("<Leave>", self.restore_cursor)

    def update(self):
        self.idx += 1
        try:
            self.image.seek(self.idx)
            self.frames.append(ImageTk.PhotoImage(self.image.resize((self.width, self.height))))
            self.configure(image=self.frames[-1])
        except EOFError:
            self.idx = 0
            self.image.seek(self.idx)
            self.frames = [ImageTk.PhotoImage(self.image.resize((self.width, self.height)))]

        self.after(self.delay, self.update)

    def change_cursor_to_hand(self, event):
        self.configure(cursor="hand2")

    def restore_cursor(self, event):
        self.configure(cursor="")




class Face_Recognition_System:
    def __init__(self, root,login_window_destroy_callback=None):
        self.root = root
        self.login_window_destroy_callback = login_window_destroy_callback
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance System")


    
        # Loading Background image
        bg_image = Image.open(r"image_assets/bgimg2.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photoImgbg = ImageTk.PhotoImage(bg_image)
    
        # Displaying background image
        bg_img = Label(self.root, image=self.photoImgbg)
        bg_img.place(x=0, y=0, width=1530, height=800)

        # Title label with transparent background
        title_label = Label(bg_img, text="Student Attendance System", font=("times new roman", 35, "bold"), fg="white",bg="black",compound='center', highlightthickness=0, highlightbackground="black")
        title_label.place(x=0, y=0, width=1530, height=50)
        
        
        #buttons

        #student button
        stud_btn1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        stud_btn1.place(x=200,y=300,width=220,height=40)

        studBtn_path = r"image_assets/students.gif"  # Replace with the path to your animated GIF
        studBtn_label = AnimatedGIFLabel(bg_img, studBtn_path, width=215, height=195)  # Adjust width and height as needed
        studBtn_label.place(x=200, y=100)
        studBtn_label.bind("<Button-1>", self.student_details)

        #Detect Face button
        detect_btn1 = Button(bg_img, text="Detect Faces",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="black",fg="white")
        detect_btn1.place(x=500,y=300,width=220,height=40)

        detectBtn_path = r"image_assets/face-scanner.gif"  # Replace with the path to your animated GIF
        detectBtn_label = AnimatedGIFLabel(bg_img, detectBtn_path, width=215, height=195)  # Adjust width and height as needed
        detectBtn_label.place(x=500, y=100)
        detectBtn_label.bind("<Button-1>", self.face_recog)


        #Attendance button
        attend_btn1 = Button(bg_img, text="Attendance",cursor="hand2",command=self.attendance_stud,font=("times new roman",15,"bold"),bg="black",fg="white")
        attend_btn1.place(x=800,y=300,width=220,height=40)

        attendBtn_path = r"image_assets/attendance.gif"  # Replace with the path to your animated GIF
        attendBtn_label = AnimatedGIFLabel(bg_img, attendBtn_path, width=215, height=195)  # Adjust width and height as needed
        attendBtn_label.place(x=800, y=100)
        attendBtn_label.bind("<Button-1>", self.attendance_stud)


        #Train Button
        train_btn1 = Button(bg_img, text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        train_btn1.place(x=300,y=700,width=220,height=40)

        trainBtn_path = r"image_assets/ai.gif"  # Replace with the path to your animated GIF
        trainBtn_label = AnimatedGIFLabel(bg_img, trainBtn_path, width=215, height=195)  # Adjust width and height as needed
        trainBtn_label.place(x=300, y=500)
        trainBtn_label.bind("<Button-1>", self.train_data)

        #Photos Button
        photos_btn1 = Button(bg_img, text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
        photos_btn1.place(x=700,y=700,width=220,height=40)

        photosBtn_path = r"image_assets/image.gif"  # Replace with the path to your animated GIF
        photosBtn_label = AnimatedGIFLabel(bg_img, photosBtn_path, width=215, height=195)  # Adjust width and height as needed
        photosBtn_label.place(x=700, y=500)
        photosBtn_label.bind("<Button-1>", self.open_img)

        #Exit Button
        exit_btn1 = Button(bg_img, text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="black",fg="white")
        exit_btn1.place(x=1200,y=400,width=220,height=40)

        exitBtn_path = r"image_assets/exit.gif"  # Replace with the path to your animated GIF
        exitBtn_label = AnimatedGIFLabel(bg_img, exitBtn_path, width=215, height=195)  # Adjust width and height as needed
        exitBtn_label.place(x=1200, y=200)
        exitBtn_label.bind("<Button-1>", self.exit)

    #To open the images sample when the "Photos" button on Home Page is clicked
    def open_img(self,event):
        os.startfile("Data")


    def exit(self,event):
        response = messagebox.askyesno("Face Recognition", "Are you sure?")
        if response:
            self.root.destroy()


    #*******************Event Functions*****************************
    def student_details(self,event):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self,event):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)  

    def face_recog(self,event):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def attendance_stud(self,event):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)              



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


