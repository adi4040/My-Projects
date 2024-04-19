import csv
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import re

class AnimatedGIFLabel(Label):
    def __init__(self, master, filename, width, height, delay=100):
        self.image = Image.open(filename)
        self.width = width
        self.height = height
        self.delay = delay
        self.frames = [ImageTk.PhotoImage(self.image.resize((width, height)))]

        Label.__init__(self, master, image=self.frames[0])

        self.idx = 0
        self.after(self.delay, self.update)

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


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")


       

        #***************Text Variables****************
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_dep = StringVar()
        self.var_date = StringVar()
        self.var_timein = StringVar()
        self.var_timeout = StringVar()
        self.fromEntry = StringVar()
        self.toEntry = StringVar()




    # Loading Background image
        bg_image = Image.open(r"image_assets/bgimg2.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photoImgbg = ImageTk.PhotoImage(bg_image)
    
    # Displaying background image
        bg_img = Label(self.root, image=self.photoImgbg)
        bg_img.place(x=0, y=0, width=1530, height=800)

    # Title label with transparent background
        title_label = Label(bg_img, text="Attendance Management", font=("times new roman", 35, "bold"), fg="white",bg="black",compound='center', highlightthickness=0, highlightbackground="black")
        title_label.place(x=20, y=20, width=520, height=90)  

    #Creating a Frame
        main_frame = Frame(bg_img,bd=2,bg="black")
        main_frame.place(x=10,y=150,width=1510,height=600)
    
    #Dividing the frame
        #left
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=600)         
        
        #student id & entry
        student_id_label = Label(left_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=20,sticky=W)
        student_id_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=20,sticky=W)
        
        #roll number
        rollNo_label = Label(left_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        rollNo_label.grid(row=0,column=3,padx=10,pady=20,sticky=W)
        rollNo_entry = ttk.Entry(left_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rollNo_entry.grid(row=0,column=4,padx=10,pady=20,sticky=W)

        #name
        name_label = Label(left_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=70,sticky=W)
        name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=70,sticky=W)
        
        #department
        dep_label = Label(left_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=3,padx=10,pady=70,sticky=W)
        dep_combo = ttk.Combobox(left_frame,textvariable=self.var_dep,font=("times new roman",12),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=4,padx=10,pady=70,sticky=W)


        #date
        date_label = Label(left_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=0,padx=10,pady=40,sticky=W)
        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=20,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=0,sticky=W)

        #timein
        timein_label = Label(left_frame,text="Time(In):",font=("times new roman",12,"bold"),bg="white")
        timein_label.grid(row=3,column=0,padx=10,pady=20,sticky=W)
        timein_entry = ttk.Entry(left_frame,textvariable=self.var_timein,width=20,font=("times new roman",12,"bold"))
        timein_entry.grid(row=3,column=1,padx=10,pady=20,sticky=W)
    
        #timeout
        timeout_label = Label(left_frame,text="Time(out):",font=("times new roman",12,"bold"),bg="white")
        timeout_label.grid(row=3,column=3,padx=10,pady=0,sticky=W)
        timeout_entry = ttk.Entry(left_frame,textvariable=self.var_timeout,width=20,font=("times new roman",12,"bold"))
        timeout_entry.grid(row=3,column=4,padx=10,pady=5,sticky=W)

        #Animated Gif
        gif_path = r"image_assets/face-scan.gif"  # Replace with the path to your animated GIF
        gif_label = AnimatedGIFLabel(left_frame, gif_path, width=130, height=130)  # Adjust width and height as needed
        gif_label.place(x=400, y=200)

        #Add Button
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white",padx=1,pady=0.5)
        btn_frame.place(x=10,y=470,width=583,height=40)  

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold")) 
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold")) 
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold")) 
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold")) 
        reset_btn.grid(row=0,column=3)    

        reset_btn = Button(left_frame,text="Reset Timings",command=self.reset_timings,width=15,font=("times new roman",12,"bold")) 
        reset_btn.place(x=20,y=200,width=140,height=50)
        
        exportCsv_btn = Button(left_frame,text="Export CSV File",command=self.export_csv,width=15,font=("times new roman",12,"bold")) 
        exportCsv_btn.place(x=200,y=200,width=170,height=50)    
        
        appendData_btn = Button(left_frame,text="Append Data",command=self.append_data,width=15,font=("times new roman",12,"bold")) 
        appendData_btn.place(x=10,y=520,width=170,height=40)     
        
        #Right Frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Information",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=790,height=600)
        search_label = Label(right_frame,text="Enter date: ",font=("times new roman",12,"bold"),bg="lightgrey")
        search_label.place(x=5,y=0,width=100,height=30)
        from_label = Label(right_frame,text="From:",font=("times new roman",12,"bold"),bg="white")
        from_label.place(x=120,y=0,width=100,height=30)
        from_entry = ttk.Entry(right_frame,width=20,textvariable=self.fromEntry,font=("times new roman",12,"bold"))
        from_entry.place(x=215,y=0,width=100,height=30)  

        to_label = Label(right_frame,text="To:",font=("times new roman",12,"bold"),bg="white")
        to_label.place(x=320,y=0,width=100,height=30)
        to_entry = ttk.Entry(right_frame,width=20,textvariable=self.toEntry,font=("times new roman",12,"bold"))
        to_entry.place(x=415,y=0,width=100,height=30)  

        sort_btn = Button(right_frame,text="Sort",command=self.sort_by_date,width=15,font=("times new roman",12,"bold")) 
        sort_btn.place(x=525,y=0,width=90,height=30)     
        unsort_btn = Button(right_frame,text="Unsort",command=self.fetch_data,width=15,font=("times new roman",12,"bold")) 
        unsort_btn.place(x=600,y=0,width=90,height=30)     

        #displaying the table
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=30,width=770,height=500)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","Roll No","Dep","Date","Time(In)","Time(out)"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        #match scrollbars with the table
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #headings                                  
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Dep",text="Dep")
        self.student_table.heading("Date",text="Date")
        self.student_table.heading("Time(In)",text="Time(In)")
        self.student_table.heading("Time(out)",text="Time(out)")
        self.student_table["show"] = "headings"
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Date",width=100)
        self.student_table.column("Time(In)",width=100)
        self.student_table.column("Time(out)",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #***************Fetching data*********************
    def fetch_data(self):
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM attendancetb")
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in data:
                        self.student_table.insert("", END, values=row)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Unsuccessful attempt due to: {str(es)}", parent=self.root)


    #****************getting cursor**********************
    def get_cursor(self,event=""):
        
        #focus the cursor on student table:
        cursor_focus = self.student_table.focus() 
        
        #get content of the item on which cursor is focussed:
        content = self.student_table.item(cursor_focus) 
        data = content["values"]

        #set the data from student_table into respective fields:
       
        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_dep.set(data[3])
        self.var_date.set(data[4]),
        self.var_timein.set(data[5]),
        self.var_timeout.set(data[6]),

    #**************Adding Data**********************
    def add_data(self):

        if not self.validating_fields():
            return

        #validating the empty fields
        if self.var_id.get()=="":
            messagebox.showerror("Error","Atleast Enter ID!",parent=self.root) #show box on same window
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into attendancetb values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                self.var_id.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_dep.get(),
                                                                                                self.var_date.get(),
                                                                                                self.var_timein.get(),
                                                                                                self.var_timeout.get(),

                                                                                              ))          
                conn.commit()
                self.fetch_data() #as soon as save button is clicked, this function is called
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    #****************Updating data************************
    def update_data(self):

        if not self.validating_fields():
            return

        if self.var_dep.get()=="Select Department" or self.var_id.get()=="":
            messagebox.showerror("Error","Atleast Enter ID!",parent=self.root) #show box on same window
        else:
            try:
                Update = messagebox.askyesno("Update","Are you sure?",parent=self.root)
                if Update>0: 
                    conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update attendancetb set Name=%s, `Roll No`=%s,Dep=%s,Date=%s,`Status (In)`=%s,`Status (out)`=%s where ID = %s" ,(
                                                                                          
                                                                                            self.var_name.get(),
                                                                                            self.var_roll.get(),                                                                                            
                                                                                            self.var_dep.get(),                                                                                            
                                                                                            self.var_date.get(),
                                                                                            self.var_timein.get(),
                                                                                            self.var_timeout.get(),
                                                                                            self.var_id.get()
                                                                                            
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


    #************Reset Data*******************
    def reset_data(self):
        self.var_dep.set("Select Department")       
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_date.set("")
        self.var_timein.set("")
        self.var_timeout.set("")

    #************Delete Data******************
    def delete_data(self):
        if self.var_id.get()=="": 
            messagebox.showerror("Error","Student ID Required!",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Data","Are you Sure?",parent=self.root)
                if delete>0:
                   conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
                   my_cursor = conn.cursor() 
                   sql = "delete from attendancetb where ID=%s"
                   val = (self.var_id.get(),)
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
    
    #******************Reset In and Out Timing of all students************************
    def reset_timings(self,event=""):
            try:
                Update = messagebox.askyesno("Update","Are you sure?",parent=self.root)
                if Update>0:
                   conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
                   my_cursor = conn.cursor()     
                   my_cursor.execute("UPDATE attendancetb SET `Status (In)` = '';")
                   my_cursor.execute("UPDATE attendancetb SET `Status (out)` = '';")
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete","Timings Reset Successful!",parent=self.root)
                else:
                    if not Update: #if user selects "No" it'll stay on the page
                        return
            except Exception as es:
                messagebox.showerror("Error",f"Unsuccessful attempt due to: {str(es)}",parent=self.root)            

    #*******************Exporting CSV File***********************************
    def export_csv(self, event=""):
        try:
            # Fetching data from the student_table widget
            data = []
            for row in self.student_table.get_children():
                item = self.student_table.item(row)["values"]
                data.append(item)

            # Specify the path for the CSV file
            csv_file_path = "attendance.csv"

            # Open the CSV file in write mode
            with open(csv_file_path, 'w', newline='') as csv_file:
                # Create a CSV writer object
                csv_writer = csv.writer(csv_file, delimiter=';')

                # Write the header row
                header = ["ID", "Name", "Roll No", "Dep", "Date", "Time(In)", "Time(out)"]
                csv_writer.writerow(header)

                # Write the data rows
                csv_writer.writerows(data)

            messagebox.showinfo("Success", "Data exported successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Unsuccessful attempt due to: {str(es)}", parent=self.root)
 


    def validating_fields(self):
        # Validating Student ID
        student_id = self.var_id.get()
        if not student_id.isdigit():
            messagebox.showerror("Error", "ID should only contain numbers", parent=self.root)
            return False
            

        # Validating name
        name = self.var_name.get()
        if not name:
            messagebox.showerror("Error", "Name not entered", parent=self.root)
            return False

        if not re.match(r"^[A-Za-z\-\'\s]+$", name):
            messagebox.showerror("Error", "Invalid name", parent=self.root)
            return False

        return True

    def append_data(self):
        try:
            # Fetching data from the right frame's table
            data = []
            for row in self.student_table.get_children():
                item = self.student_table.item(row)["values"]
                # Skip the first column (ID) and append the rest of the columns
                data.append(item[1:])  

            # Establishing a connection to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
            my_cursor = conn.cursor()

            # Inserting data into the append_data table
            for item in data:
                name, roll, dep, date, timein, timeout = item
                my_cursor.execute("INSERT INTO appended_data (Name, RollNo, Dep, Date, `Time(In)`, `Time(Out)`) VALUES (%s, %s, %s, %s, %s, %s)", (name, roll, dep, date, timein, timeout))

            # Committing the changes and closing the connection
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Data appended to 'append_data' table successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Unsuccessful attempt due to: {str(es)}", parent=self.root)

    
    def sort_by_date(self):
        try:
            # Clear previous data in the student_table
            self.student_table.delete(*self.student_table.get_children())

            # Get the entered from date and to date
            from_date = self.fromEntry.get()
            to_date = self.toEntry.get()

            # Validate the entered dates
            if not from_date or not to_date:
                messagebox.showerror("Error", "Please enter both from and to dates", parent=self.root)
                return

            # Establish connection to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
            my_cursor = conn.cursor()

            # Fetch data from appended_data table where Date falls within the specified range
            my_cursor.execute("SELECT `Name`, `RollNo`, `Dep`, `Date`, `Time(In)`, `Time(Out)` FROM appended_data WHERE `Date` BETWEEN %s AND %s", (from_date, to_date))
            data = my_cursor.fetchall()

            if len(data) != 0:
                # Insert the fetched data into the student_table in the right frame
                for row in data:
                     self.student_table.insert("", END, values=[""] + list(row))
                conn.commit()

            # Close the database connection
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Unsuccessful attempt due to: {str(es)}", parent=self.root)






        


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()