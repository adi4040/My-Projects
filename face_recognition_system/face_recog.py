from tkinter import *
from PIL import Image, ImageTk
import cv2
import face_recognition
import xml.etree.ElementTree as ET
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox, QApplication
import sys
import wx


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Detect Faces")

        self.constant = 0

        self.setup_ui()
            
    def setup_ui(self):
        # Set up the user interface
        bg_image = Image.open(r"image_assets/bgimg2.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photoImgbg = ImageTk.PhotoImage(bg_image)

        bg_img = Label(self.root, image=self.photoImgbg)
        bg_img.place(x=0, y=0, width=1530, height=800)

        title_label = Label(bg_img, text="Recognizing faces", font=("times new roman", 35, "bold"),
                            fg="white", bg="black", highlightthickness=0, highlightbackground="black")
        title_label.place(x=0, y=20, width=400, height=70)

        face_img1 = Image.open(r"image_assets/face_recognition1.jpg")
        face_img1 = face_img1.resize((880, 710), Image.LANCZOS)
        self.photoImgbg3 = ImageTk.PhotoImage(face_img1)

        face_img_lb = Label(self.root, image=self.photoImgbg3)
        face_img_lb.place(x=0, y=90, width=880, height=710)

        face_scan_img1 = Image.open(r"image_assets/face_scanning.jpg")
        face_scan_img1 = face_scan_img1.resize((880, 750), Image.LANCZOS)
        self.photoImgbg4 = ImageTk.PhotoImage(face_scan_img1)

        face_scan_img_lb = Label(self.root, image=self.photoImgbg4)
        face_scan_img_lb.place(x=850, y=70, width=660, height=750)

        recognize_Icon1 = Image.open(r"image_assets/recog_icon.png")
        recognize_Icon1 = recognize_Icon1.resize((100, 100), Image.LANCZOS)
        self.photoImgbg2 = ImageTk.PhotoImage(recognize_Icon1)

        recognize_icon_button = Button(self.root, image=self.photoImgbg2, cursor="hand2", bd=0, bg="black",
                                       activebackground="black", command=self.face_recog)
        recognize_icon_button.place(x=750, y=340, width=100, height=100)


    # ********************Marking Attendance**************
    def mark_attendance_in(self,id,name):
        
       #getting data to be displayed
        now = datetime.now() #display date and time
        date = now.strftime("%d/%m/%Y") #date format
        time = now.strftime("%H:%M:%S") #time format 
        
        conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT `Status (In)` FROM attendancetb WHERE ID = %s", (id,))
        time_in = my_cursor.fetchone()
        
        
        my_cursor.execute("SELECT `Status (out)` FROM attendancetb WHERE ID = %s",(id,))
        time_out = my_cursor.fetchone()
        

        if not time_in or not time_in[0]:
            #Database Connectivity
            try:
                    
                    my_cursor.execute("update attendancetb set `Status (In)`=%s where ID=%s",(time,id))
                    my_cursor.execute("update attendancetb set Date = %s where ID = %s",(date,id))    
                    app = wx.App(False)
                    wx.MessageBox("Marked the attendance for {} (IN)!".format(name), "Info", wx.OK | wx.ICON_INFORMATION)
                    self.constant = 1

            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

        elif not time_out or not time_out[0]:
            try:
                    
                    my_cursor.execute("update attendancetb set `Status (out)`=%s where ID=%s",(time,id))
                    app = wx.App(False)
                    wx.MessageBox("Marked the attendance for {} (OUT)!".format(name), "Info", wx.OK | wx.ICON_INFORMATION)
                    self.constant = 1
                    

            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        else :
            #  messagebox.showerror("Error","Can't change the out timing") 
            app = wx.App(False)
            wx.MessageBox("Can't mark OUT attendance for {} again!".format(name), "Info", wx.OK | wx.ICON_INFORMATION)
            self.constant = 1      

     

        conn.commit()
        conn.close()    
            
        

              
            

    #****************Face Recognition*********************

    def face_recog(self):

        # Load known faces encodings and ids from the XML file
        known_encodings, known_ids = self.load_known_faces()

        def recognize(img):
            try:
                face_locations = face_recognition.face_locations(img)
                face_encodings = face_recognition.face_encodings(img, face_locations)

                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(known_encodings, face_encoding,tolerance=0.4)
                    id = ""
                    name = ""
                    roll = ""
                    dep = ""
                    if True in matches:
                        first_match_index = matches.index(True)
                        student_id = known_ids[first_match_index]

                        # Fetch student details using the student ID which is matched
                        details = self.fetch_student_details(student_id)

                        if details:
                           name, roll, dep, id = details  # Assuming details is a tuple (Name, Roll, Dep)
                        
                        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
                        cv2.putText(img, id, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, name, (left, top - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, roll, (left, top - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, dep, (left, top - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        
                        self.mark_attendance_in(id,name)
                        

                    else:
                         cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 3) #Red Rectangle
                         cv2.putText(img, "Unknown Face", (left, top - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                        
                    
                    

                cv2.imshow("Recognition", img)
                cv2.waitKey(1)  # Display each frame for 1 millisecond

            except Exception as e:
                # Print the exception and handle it as needed (e.g., show an error message)
                print(f"Error during face recognition: {e}")
                # You can show an error message to the user if needed
                messagebox.showerror("Error", f"Error during face recognition: {e}")


       

        # Set up video capture
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            recognize(img)

            if self.constant == 1:
                self.constant = 0
                break

            if cv2.waitKey(1) == 13:
                break

        # Release video capture and close OpenCV windows
        video_cap.release()
        cv2.destroyAllWindows()



    def load_known_faces(self, xml_file="classifier.xml"):
        try:
            # Parse XML file for known faces encodings and ids
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Store known faces encodings and ids in class variables
            self.known_encodings = []
            self.known_ids = []

            for encoding_elem in root.find("encodings"):
                encoding_str = encoding_elem.text
                encoding = [float(value) for value in encoding_str.split(",")]
                self.known_encodings.append(encoding)

            for id_elem in root.find("ids"):
                face_id = id_elem.text
                self.known_ids.append(face_id)

            return self.known_encodings, self.known_ids

        except Exception as e:
            print(f"Error loading known faces from {xml_file}: {e}")
            messagebox.showerror("Error", f"Error loading known faces from {xml_file}: {e}")
            return [], []

    def fetch_student_details(self, student_id):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="iamadam4040", database="face_recognizer")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=" + str(student_id))
            id = my_cursor.fetchone()
            id = "+".join(id) if id else "Unknown"

            my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(student_id))
            name = my_cursor.fetchone()
            name = "+".join(name) if name else "Unknown"

            my_cursor.execute("SELECT Roll FROM student WHERE Student_id=" + str(student_id))
            roll = my_cursor.fetchone()
            roll = "+".join(roll) if roll else "Unknown"

            my_cursor.execute("SELECT Dep FROM student WHERE Student_id=" + str(student_id))
            dep = my_cursor.fetchone()
            dep = "+".join(dep) if dep else "Unknown"

            conn.close()

            return name, roll, dep, id

        except Exception as e:
            print(f"Error fetching student details: {e}")
            messagebox.showerror("Error", f"Error fetching student details: {e}")
            return None


if __name__ == "__main__":
    # Create Tkinter window and initialize FaceRecognition object
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
