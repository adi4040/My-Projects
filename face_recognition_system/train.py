from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import face_recognition
import os
import numpy as np
import json
import xml.etree.ElementTree as ET

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")

        # Loading Background image
        bg_image = Image.open(r"image_assets/train_dataset_new.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photoImgbg = ImageTk.PhotoImage(bg_image)

        # Displaying background image
        bg_img = Label(self.root, image=self.photoImgbg)
        bg_img.place(x=0, y=0, width=1530, height=800)

        # Title label with transparent background
        title_label = Label(bg_img, text="Train dataset", font=("times new roman", 35, "bold"), fg="white", bg="black", bd=0, relief="flat", highlightthickness=0)
        title_label.place(x=1100, y=30, width=400, height=50)

        # Processing icon in the center
        processing_Icon1 = Image.open(r"image_assets/face-recognition.png")
        processing_Icon1 = processing_Icon1.resize((140, 140), Image.LANCZOS)
        self.photoImgbg2 = ImageTk.PhotoImage(processing_Icon1)

        processing_img_button = Button(bg_img, image=self.photoImgbg2, command=self.train_classifier, cursor="hand2")
        processing_img_button.place(x=870, y=165, width=140, height=140)

    def train_classifier(self):
        data_dir = "Data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        known_encodings = []
        known_ids = []

        # Load existing encodings and IDs from the XML file
        existing_encodings, existing_ids = self.load_existing_data()

        for image_path in path:
            face_id = os.path.split(image_path)[1].split('.')[1]  # Extract ID from the file name

            # Check if data for this ID already exists in the XML file
            if face_id in existing_ids:
                continue  # Skip this image if data already exists for this ID

            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)

            if len(face_encoding) > 0:
                known_encodings.append(face_encoding[0])
                known_ids.append(face_id)

                # Displaying the training image in a Tkinter window
                img = Image.open(image_path)
                img_tk = ImageTk.PhotoImage(img)
                img_label = Label(self.root, image=img_tk)
                img_label.image = img_tk
                img_label.place(x=250, y=150, width=img.width, height=img.height)

                self.root.update()  # Update the Tkinter window to display the image
                self.root.after(10)  # Delay for 10 milliseconds 

        # Append new encodings and IDs to the existing ones and save them in the XML file
        self.save_new_data(known_encodings, known_ids)
        messagebox.showinfo("Result", "Data trained successfully!")

    def load_existing_data(self):
        try:
            tree = ET.parse("classifier.xml")
            root = tree.getroot()

            existing_encodings = [np.array(enc.text.split(","), dtype=np.float64) for enc in root.find("encodings")]
            existing_ids = [id_elem.text for id_elem in root.find("ids")]

            return existing_encodings, existing_ids
        except FileNotFoundError:
            return [], []

    def save_new_data(self, new_encodings, new_ids):
        try:
            tree = ET.parse("classifier.xml")
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("root")

        encodings_elem = root.find("encodings")
        if encodings_elem is None:
            encodings_elem = ET.SubElement(root, "encodings")
        ids_elem = root.find("ids")
        if ids_elem is None:
            ids_elem = ET.SubElement(root, "ids")

        for encoding in new_encodings:
            encoding_elem = ET.SubElement(encodings_elem, "encoding")
            encoding_elem.text = ",".join(map(str, encoding.tolist()))

        for face_id in new_ids:
            id_elem = ET.SubElement(ids_elem, "id")
            id_elem.text = str(face_id)

        tree = ET.ElementTree(root)
        tree.write("classifier.xml")

        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
