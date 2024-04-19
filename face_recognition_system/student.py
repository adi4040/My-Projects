from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import re

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")

        #********************Text Variables*************************
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.searchCombo = StringVar()
        self.searchEntry = StringVar()


        

    # Loading Background image
        bg_image = Image.open(r"image_assets/bgimg2.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photoImgbg = ImageTk.PhotoImage(bg_image)
    
    # Displaying background image
        bg_img = Label(self.root, image=self.photoImgbg)
        bg_img.place(x=0, y=0, width=1530, height=800)


    #Students Immage
        stud_img1 = Image.open(r"image_assets/students_img.jpeg")
        stud_img1 = stud_img1.resize((500,160),Image.LANCZOS)
        self.photoImgbg1 = ImageTk.PhotoImage(stud_img1)

        stud_img_lb = Label(self.root,image=self.photoImgbg1)
        stud_img_lb.place(x=0,y=0,width=500,height=160)

    #Details Immage
        detail_img1 = Image.open(r"image_assets/details_img.jpeg")
        detail_img1 = detail_img1.resize((500,160),Image.LANCZOS)
        self.photoImgbg2 = ImageTk.PhotoImage(detail_img1)

        detail_img_lb = Label(self.root,image=self.photoImgbg2)
        detail_img_lb.place(x=500,y=0,width=500,height=160)

    #Data Image
        data_img1 = Image.open(r"image_assets/data_img1.jpeg")
        data_img1 = data_img1.resize((570,160),Image.LANCZOS)
        self.photoImgbg3 = ImageTk.PhotoImage(data_img1)

        data_img_lb = Label(self.root,image=self.photoImgbg3)
        data_img_lb.place(x=1000,y=0,width=570,height=160)

    # Title label with transparent background
        title_label = Label(bg_img, text="Student Management", font=("times new roman", 35, "bold"), fg="white",bg="black",compound='center', highlightthickness=0, highlightbackground="black")
        title_label.place(x=0, y=160, width=500, height=50)

    #Creating a Frame
        main_frame = Frame(bg_img,bd=2,bg="black")
        main_frame.place(x=10,y=210,width=1510,height=560)
    
    #Dividing the frame
        #left
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Enter Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=550)

        #current course information
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=15,width=640,height=160)

        #department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label = Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12),width=17,state="readonly")
        course_combo["values"]=("Select Course","FY","SY","TY")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Class Student Information Frame
        class_student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=180,width=640,height=400)

        #student id & entry
        student_id_label = Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        student_id_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #student name
        student_name_label = Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"),style="TEntry")
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_division_label = Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12),width=19,state="readonly")
        div_combo["values"]=("Select Division","1","2","3")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=1,pady=10,sticky=W)

        #roll number
        rollNo_label = Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        rollNo_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        rollNo_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rollNo_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)   

        #email 
        email_label = Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W) 

        #phone number
        phNo_label = Label(class_student_frame,text="Phone Number:",font=("times new roman",12,"bold"),bg="white")
        phNo_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        phNo_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phNo_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)      

        #radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=3,column=0,padx=10,pady=10)

        
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Don't Take Photo Sample",value="No")
        radiobtn2.grid(row=3,column=1,padx=10,pady=10)

        #Buttons Frame 
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=200,width=583,height=100)  

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold")) 
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold")) 
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold")) 
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold")) 
        reset_btn.grid(row=0,column=3)

        take_photo_btn = Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=15,font=("times new roman",12,"bold")) 
        take_photo_btn.grid(row=1,column=0,pady=5)

        update_photo_btn = Button(btn_frame,text="Update Photo Sample",width=15,font=("times new roman",12,"bold")) 
        update_photo_btn.grid(row=1,column=1,pady=5)




        #Right Frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Information",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=790,height=580)

        info_img1 = Image.open(r"image_assets/information_img.jpg")
        info_img1 = info_img1.resize((780,160),Image.LANCZOS)
        self.photoImgbg4 = ImageTk.PhotoImage(info_img1)
        info_img_lb = Label(right_frame,image=self.photoImgbg4)
        info_img_lb.place(x=5,y=0,width=780,height=160)

        #**************Search System*********************
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=170,width=770,height=80)

        search_label = Label(search_frame,text="Search by:",font=("times new roman",12,"bold"),bg="lightgrey")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        search_combo = ttk.Combobox(search_frame,textvariable=self.searchCombo,font=("times new roman",12),width=17,state="readonly")
        search_combo["values"]=("Select","Roll","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,textvariable=self.searchEntry,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)   

        search_btn = Button(search_frame,text="Search",command = self.search_system, width=15,font=("times new roman",12,"bold")) 
        search_btn.grid(row=0,column=3)

        searchAll_btn = Button(search_frame,text="Search All",command=self.fetch_data,width=15,font=("times new roman",12,"bold")) 
        searchAll_btn.grid(row=0,column=4,padx=10)

        #********************Table Frame**********************
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=265, width=770, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Dep", "Course", "Year", "Id", "Name", "Div", "RollNo", "Email", "PhoneNo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #headings
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Id",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("RollNo",text="Roll No")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("PhoneNo",text="Phone No")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("RollNo",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("PhoneNo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor) #binding the focus cursor to student_table 
        self.fetch_data() #to see already available data on the start

    #*********************Functions for adding data to database****************************
    
    def add_data(self):

        if not self.validating_fields():
            return

        #validating the empty fields
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","Fill all the fields!",parent=self.root) #show box on same window
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student (Dep, Course, Year, Student_id, Name, Division, Roll, Email, Phone, PhotoSample) "
                              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_radio1.get()
                                                                                              ))          
                conn.commit()
                self.fetch_data() #as soon as save button is clicked, this function is called
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

    #**************************Fetching data******************************
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student ORDER BY CAST(Student_id AS UNSIGNED)")
        data = my_cursor.fetchall()

        if len(data)!=0:  #if some data is fetched 
            self.student_table.delete(*self.student_table.get_children()) #delete the already displayed data 
            for i in data: #insert new data 
                self.student_table.insert("",END,values=i)
                conn.commit() #so that data gets added
        conn.close()


    # get cursor function (so that when user clicks on any entry in table, its details will be filled in the fields and user will be able to update it!)
    def get_cursor(self,event=""):
        
        #focus the cursor on student table:
        cursor_focus = self.student_table.focus() 
        
        #get content of the item on which cursor is focussed:
        content = self.student_table.item(cursor_focus) 
        data = content["values"]

        #set the data from student_table into respective fields:
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_std_id.set(data[3]),
        self.var_std_name.set(data[4]),
        self.var_div.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_radio1.set(data[9]),

    
    #**************Update Function*******************
    def update_data(self):

        if not self.validating_fields():
            return

        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","Fill all the fields!",parent=self.root) #show box on same window
        else:
            try:
                Update = messagebox.askyesno("Update","Are you sure?",parent=self.root)
                if Update>0: 
                    conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s, Year=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),                                                                                            
                                                                                            self.var_std_id.get(),                                                                                            
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_std_id.get()    


                    ))
                else:
                    if not Update: #if user selects "No" it'll stay on the page
                        return
                messagebox.showinfo("success","Details Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Unsuccessful attempt due to: {str(es)}",parent=self.root)

    #***********Delete Function**************************
    def delete_data(self):
        if self.var_std_id.get()=="": #data will not be deleted if student id is not selected
            messagebox.showerror("Error","Student ID required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Data","Are you Sure?",parent=self.root)
                if delete>0:
                   conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
                   my_cursor = conn.cursor() 
                   sql = "delete from student where Student_id=%s"
                   val = (self.var_std_id.get(),)
                   my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Unsuccessful attempt due to: {str(es)}",parent=self.root)  

    #*************Reset Data Fields***********************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")


    #************Generate data set and take photo samples********************
    
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "Fill all the fields!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")  
                my_result = my_cursor.fetchall()
                id = 0 
                for x in my_result: #x variable iterates through the result set and increments the id according to the number of results in result set
                   id+=1 
                
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Name=%s,Division=%s,Roll=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),                                                                                                                                                                                                                                                               
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_radio1.get(),
                                                                                                self.var_std_id.get() == id+1   #check whether the incremented ID matches the student_id
                                                                                            ))
                conn.commit()              
                self.fetch_data()
                self.reset_data()
                conn.close()
                

                #**************Load Predefined data on face frontals from opencv***************

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame=cap.read()
                    cropped_face = face_cropped(my_frame)
                    if  cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face,(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(my_frame,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",my_frame)

                        if cv2.waitKey(1) == 13 or int(img_id)==500:
                            break
                    # Display the resulting frame (without cropping)
                    cv2.imshow('frame', my_frame)
                    # Break the loop if 'q' key is pressed
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed !!")

                    
            except Exception as es:
                messagebox.showerror("Error",f"Unsuccessful attempt due to: {str(es)}",parent=self.root) 

    def search_system(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
        my_cursor = conn.cursor()

        comboSelection = self.searchCombo.get()  # Get the selected search criteria from the combobox
        entry = self.searchEntry.get()

        try:
            if comboSelection == "Roll":
                my_cursor.execute("Select * from student where Roll = %s", (entry,))
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                        conn.commit()

            elif comboSelection == "Name":
                my_cursor.execute("Select * from student where Name = %s", (entry,))
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                        conn.commit()
                        print('hey')
            else:
                messagebox.showerror("Error", "No Selection", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Unsuccessful attempt due to: {str(es)}", parent=self.root)

        conn.close()


    def validating_fields(self):
        # Validating Student ID
        student_id = self.var_std_id.get()
        if not student_id.isdigit():
            messagebox.showerror("Error", "ID should only contain numbers", parent=self.root)
            return False
            
        # Validating email address
        email = self.var_email.get()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email address", parent=self.root)
            return False

        # Validating phone number
        phone_number = self.var_phone.get()
        pattern = r"^\+?[0-9]{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,10}$"
        if not re.match(pattern, phone_number) or len(phone_number) != 10:
            messagebox.showerror("Error", "Invalid phone number", parent=self.root)
            return False

        # Validating name
        name = self.var_std_name.get()
        if not name:
            messagebox.showerror("Error", "Name not entered", parent=self.root)
            return False

        if not re.match(r"^[A-Za-z\-\'\s]+$", name):
            messagebox.showerror("Error", "Invalid name", parent=self.root)
            return False

        return True





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
