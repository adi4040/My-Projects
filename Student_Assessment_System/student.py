from tkinter import *
from tkinter import ttk, filedialog  # Import filedialog module
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import csv

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Assessment")

        # Text Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_prcombo = StringVar()
        self.var_marks = StringVar()

        # Database connection
        self.conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="python_mp")
        self.cursor = self.conn.cursor()

        # Load Background image
        bg_image = Image.open(r"image_assets/gradient_black.jpeg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photoImgbg = ImageTk.PhotoImage(bg_image)

        # Display Background image
        bg_img = Label(self.root, image=self.photoImgbg)
        bg_img.place(x=0, y=0, width=1530, height=800)

        # Label for Assessment
        title_label = Label(bg_img, text="Practical Assessment", font=("times new roman", 35, "bold"), fg="white", bg="black", compound='center', highlightthickness=0, highlightbackground="black")
        title_label.place(x=0, y=0, width=1530, height=70)

        # Creating a Frame
        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=10, y=100, width=1510, height=650)

        # Dividing the frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Edit & Enter", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=550)

        name_label = Label(left_frame, text="Name:", font=("times new roman", 20, "bold"), fg="black", bg="white", compound='center', highlightthickness=0, highlightbackground="black")
        name_label.place(x=58, y=100, width=100, height=70)

        self.name_entry = ttk.Entry(left_frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"), foreground="gray")
        self.name_entry.place(x=170, y=120, width=200, height=40)

        roll_label = Label(left_frame, text="Roll No:", font=("times new roman", 20, "bold"), fg="black", bg="white", compound='center', highlightthickness=0, highlightbackground="black")
        roll_label.place(x=65, y=30, width=100, height=70)

        self.roll_entry = ttk.Entry(left_frame, textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"), foreground="gray")
        self.roll_entry.place(x=170, y=47, width=200, height=40)

        practical_combo = ttk.Combobox(left_frame, textvariable=self.var_prcombo, font=("times new roman", 12), width=17, state="readonly")
        practical_combo["values"] = ("Select Practicals", "PR1", "PR2", "PR3", "PR4", "PR5", "PR6", "PR7", "PR8", "PR9", "PR10", "PR11", "PR12", "PR13", "PR14", "PR15", "PR16")
        practical_combo.current(0)
        practical_combo.place(x=70, y=200, width=300, height=40)

        self.marks_entry = ttk.Entry(left_frame, textvariable=self.var_marks, width=20, font=("times new roman", 12, "bold"), foreground="gray")
        self.marks_entry.place(x=500, y=200, width=50, height=40)

        marks_label = Label(left_frame, text="Marks:", font=("times new roman", 20, "bold"), fg="black", bg="white", compound='center', highlightthickness=0, highlightbackground="black")
        marks_label.place(x=400, y=190, width=100, height=70)

        assign_btn = Button(left_frame, command=self.add_data, text="Add", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        assign_btn.place(x=120, y=300, width=170, height=40)

        total_btn = Button(left_frame, command=self.calc_total, text="Total", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        total_btn.place(x=350, y=300, width=170, height=40)

        update_btn = Button(left_frame, command=self.update_data, text="Update", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        update_btn.place(x=120, y=350, width=170, height=40)

        import_csv_btn = Button(left_frame, text="Import CSV", command=self.import_csv, cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        import_csv_btn.place(x=350, y=350, width=170, height=40)

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Information", font=("times new roman", 12, "bold"))
        right_frame.place(x=690, y=10, width=790, height=550)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=20, width=770, height=500)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Roll No", "Name", "PR1", "PR2", "PR3", "PR4", "PR5", "PR6", "PR7", "PR8", "PR9", "PR10", "PR11", "PR12", "PR13", "PR14", "PR15", "PR16", "Total", "Avg"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Roll No", text="Roll No")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("PR1", text="PR1")
        self.student_table.heading("PR2", text="PR2")
        self.student_table.heading("PR3", text="PR3")
        self.student_table.heading("PR4", text="PR4")
        self.student_table.heading("PR5", text="PR5")
        self.student_table.heading("PR6", text="PR6")
        self.student_table.heading("PR7", text="PR7")
        self.student_table.heading("PR8", text="PR8")
        self.student_table.heading("PR9", text="PR9")
        self.student_table.heading("PR10", text="PR10")
        self.student_table.heading("PR11", text="PR11")
        self.student_table.heading("PR12", text="PR12")
        self.student_table.heading("PR13", text="PR13")
        self.student_table.heading("PR14", text="PR14")
        self.student_table.heading("PR15", text="PR15")
        self.student_table.heading("PR16", text="PR16")
        self.student_table.heading("Total", text="Total")
        self.student_table.heading("Avg", text="Avg")

        self.student_table["show"] = "headings"

        self.student_table.column("Roll No", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("PR1", width=100)
        self.student_table.column("PR2", width=100)
        self.student_table.column("PR3", width=100)
        self.student_table.column("PR4", width=100)
        self.student_table.column("PR5", width=100)
        self.student_table.column("PR6", width=100)
        self.student_table.column("PR7", width=100)
        self.student_table.column("PR8", width=100)
        self.student_table.column("PR9", width=100)
        self.student_table.column("PR10", width=100)
        self.student_table.column("PR11", width=100)
        self.student_table.column("PR12", width=100)
        self.student_table.column("PR13", width=100)
        self.student_table.column("PR14", width=100)
        self.student_table.column("PR15", width=100)
        self.student_table.column("PR16", width=100)
        self.student_table.column("Total", width=100)
        self.student_table.column("Avg", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)  # binding the focus cursor to student_table
        self.fetch_data()  # to see already available data on the start

    def fetch_data(self):
        try:
            self.cursor.execute("SELECT * FROM studentassess")
            data = self.cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
                self.conn.commit()
        except Exception as es:
            messagebox.showerror("Error", f"Unsuccessful attempt due to: {str(es)}", parent=self.root)

    def add_data(self):
        num = 0
        if self.var_name.get() == "" or self.var_roll.get() == "":
            messagebox.showerror("Error", "Fill all the fields!", parent=self.root)  # show box on same window
        else:
            try:
                self.cursor.execute("insert into studentassess values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.var_roll.get(), self.var_name.get(), num, num, num, num, num, num, num, num, num, num, num, num,
                num, num, num, num, num))
                self.conn.commit()
                self.fetch_data()  # as soon as save button is clicked, this function is called
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_roll.set(data[0]),
        self.var_name.set(data[1])

    def update_data(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        roll = data[0]
        if self.var_prcombo.get() == "Select Practicals":
            messagebox.showerror("Error", "Select Practical No!", parent=self.root)
        else:
            try:
                selected_pr = self.var_prcombo.get()
                assigned_marks = self.var_marks.get()
                query = f"UPDATE studentassess SET {selected_pr}={assigned_marks} WHERE `Roll No`={roll}"
                self.cursor.execute(query)
                self.conn.commit()
                self.fetch_data()  # as soon as save button is clicked, this function is called
                messagebox.showinfo("Success", "PR marks Updated Successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def calc_total(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        roll = data[0]
        try:
            self.cursor.execute("SELECT PR1, PR2, PR3, PR4, PR5, PR6, PR7, PR8, PR9, PR10, PR11, PR12, PR13, PR14, PR15, PR16 FROM studentassess WHERE `Roll No` = %s", (roll,))
            stud_data = self.cursor.fetchone()
            if stud_data:
                values = [0 if val is None else int(val) for val in stud_data]
                total = sum(values)
                avg = total / 16  # Assuming 16 practicals are there
                self.cursor.execute("UPDATE studentassess SET Total = %s, Avg = %s WHERE `Roll No` = %s", (total, avg, roll))
                self.conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Total and Average Calculated!", parent=self.root)
            else:
                messagebox.showwarning("Warning", f"No data found for Roll No: {roll}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def import_csv(self):
        try:
            # Open file dialog to choose CSV file
            file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
            if file_path:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="python_mp")
                cursor = conn.cursor()

                with open(file_path, 'r') as file:
                    # Use tab as the delimiter
                    csv_reader = csv.reader(file, delimiter=';')

                    # Skip header row if present
                    next(csv_reader)

                    # Insert data from CSV into the database table
                    for row in csv_reader:
                        # Extract data from the row
                        if len(row) >= 2:
                            roll_no, name, *marks = row

                            # Convert marks to integers
                            marks = [int(m) for m in marks]

                            # Insert data into the database
                            cursor.execute("INSERT INTO studentassess (`Roll No`, `Name`, `PR1`, `PR2`, `PR3`, `PR4`, `PR5`, `PR6`, `PR7`, `PR8`, `PR9`, `PR10`, `PR11`, `PR12`, `PR13`, `PR14`, `PR15`, `PR16`, `Total`, `Avg`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (roll_no, name, *marks, 0, 0))


                    conn.commit()

                    # Fetch and update the data in the Treeview
                    self.fetch_data()

                # Close file
                file.close()
                messagebox.showinfo("Success", "CSV file imported successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Failed to import CSV file due to: {str(es)}", parent=self.root)
        finally:
            # Close cursor and connection
            if cursor:
                cursor.close()
            if conn:
                conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
