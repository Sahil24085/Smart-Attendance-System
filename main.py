# import cv2
# import face_recognition
# import os
# import numpy as np
# from datetime import datetime


# path = 'student_images'

# images = []
# classNames = []
# mylist = os.listdir(path)
# for cl in mylist:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])  # Extract class name from file name
    
    
# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         encoded_faces = face_recognition.face_encodings(img)
#         if encoded_faces:  
#             encodeList.append(encoded_faces[0])
        
#     return encodeList
# encoded_face_train = findEncodings(images)

# def markAttendance(name):
#     with open('Attendance.csv','r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             now = datetime.now()
#             time = now.strftime('%H:%M:%S')
#             date = now.strftime('%d-%B-%Y')
#             f.writelines(f'\n{name}, {time}, {date}')
            
# cap = cv2.VideoCapture(0)
# while True:
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     faces_in_frame = face_recognition.face_locations(imgS)
#     encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
#     for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#         matches = face_recognition.compare_faces(encoded_face_train, encode_face)
#         faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
#         matchIndex = np.argmin(faceDist)
#         print(matchIndex)
#         if matches[matchIndex]:
#             name = classNames[matchIndex].upper()
#             y1, x2, y2, x1 = faceloc
            
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#             markAttendance(name)
#     cv2.imshow('webcam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
    


# import tkinter as tk
# from tkinter import messagebox
# import pandas as pd

# class AttendanceApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Attendance System")
#         self.root.geometry("300x200")
        
#         self.label = tk.Label(root, text="Attendance System", font=("Helvetica", 16))
#         self.label.pack(pady=20)
        
#         self.show_button = tk.Button(root, text="Show Attendance", command=self.show_attendance)
#         self.show_button.pack(pady=10)
        
#     def show_attendance(self):
#         try:
#             df = pd.read_csv('Attendance.csv')
#             messagebox.showinfo("Attendance", df.to_string(index=False))
#         except FileNotFoundError:
#             messagebox.showerror("Error", "Attendance file not found.")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))   
            
            



# root = tk.Tk()
# app = AttendanceApp(root)

# root.mainloop()
# cap.release()

# cv2.destroyAllWindows()


# ========================================================================== ATTEMPT -1 =================
# import cv2 
# import face_recognition
# import os
# import numpy as np
# from datetime import datetime
# import tkinter as tk
# from tkinter import messagebox
# import pandas as pd

# path = 'student_images'

# images = []
# classNames = []
# mylist = os.listdir(path)
# for cl in mylist:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])  # Extract class name from file name
    
# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         encoded_faces = face_recognition.face_encodings(img)
#         if encoded_faces:  
#             encodeList.append(encoded_faces[0])
#     return encodeList

# encoded_face_train = findEncodings(images)

# def markAttendance(name):
#     with open('Attendance.csv','r+') as f:
#         myDataList = f.readlines()
#         nameList = [line.split(',')[0] for line in myDataList]
#         if name not in nameList:
#             now = datetime.now()
#             time = now.strftime('%H:%M:%S')
#             date = now.strftime('%d-%B-%Y')
#             f.writelines(f'\n{name}, {time}, {date}')

# cap = cv2.VideoCapture(0)
# while True:
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     faces_in_frame = face_recognition.face_locations(imgS)
#     encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

#     for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#         matches = face_recognition.compare_faces(encoded_face_train, encode_face)
#         faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        
#         if len(faceDist) > 0 and np.min(faceDist) < 0.6:
#             matchIndex = np.argmin(faceDist)
#             if matches[matchIndex]:
#                 name = classNames[matchIndex].upper()
#                 color = (0, 255, 0)
#         else:
#             name = "UNAUTHORIZED"
#             color = (0, 0, 255)
        
#         y1, x2, y2, x1 = faceloc
#         y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#         cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
#         cv2.rectangle(img, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
#         cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        
#         if name != "UNAUTHORIZED":
#             markAttendance(name)

#     cv2.imshow('webcam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# # Tkinter UI
# class AttendanceApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Attendance System")
#         self.root.geometry("300x200")
        
#         self.label = tk.Label(root, text="Attendance System", font=("Helvetica", 16))
#         self.label.pack(pady=20)
        
#         self.show_button = tk.Button(root, text="Show Attendance", command=self.show_attendance)
#         self.show_button.pack(pady=10)
        
#     def show_attendance(self):
#         try:
#             df = pd.read_csv('Attendance.csv')
#             messagebox.showinfo("Attendance", df.to_string(index=False))
#         except FileNotFoundError:
#             messagebox.showerror("Error", "Attendance file not found.")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))   

# root = tk.Tk()
# app = AttendanceApp(root)
# root.mainloop()




# ======================= ATTEMPOT-2=====================================



# import cv2
# import face_recognition
# import os
# import numpy as np
# from datetime import datetime
# import tkinter as tk
# from tkinter import messagebox
# import pandas as pd

# path = 'student_images'

# images = []
# classNames = []
# mylist = os.listdir(path)
# for cl in mylist:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     name = os.path.splitext(cl)[0].split('_')[0]  # Extract name before underscore
#     classNames.append(name.upper())

# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         encoded_faces = face_recognition.face_encodings(img)
#         if encoded_faces:
#             encodeList.append(encoded_faces[0])
#     return encodeList

# encoded_face_train = findEncodings(images)

# def markAttendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = [line.split(',')[0] for line in myDataList]
#         if name not in nameList:
#             now = datetime.now()
#             time = now.strftime('%H:%M:%S')
#             date = now.strftime('%d-%B-%Y')
#             f.writelines(f'\n{name}, {time}, {date}')

# cap = cv2.VideoCapture(0)
# while True:
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     faces_in_frame = face_recognition.face_locations(imgS, model='cnn')
#     encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

#     detected_names = set()

#     for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#         matches = face_recognition.compare_faces(encoded_face_train, encode_face, tolerance=0.5)
#         faceDist = face_recognition.face_distance(encoded_face_train, encode_face)

#         if faceDist.size > 0:
#             matchIndex = np.argmin(faceDist)
#             if matches[matchIndex]:
#                 name = classNames[matchIndex]
#                 if name not in detected_names:
#                     detected_names.add(name)
#                     y1, x2, y2, x1 = faceloc
#                     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#                     cv2.putText(img, name, (x1 + 6, y2 - 5),
#                                 cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#                     markAttendance(name)
#             else:
#                 # Unauthorized face detected
#                 y1, x2, y2, x1 = faceloc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#                 cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
#                 cv2.putText(img, "UNAUTHORIZED", (x1 + 6, y2 - 5),
#                             cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

#     cv2.imshow('webcam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# # GUI for viewing attendance
# class AttendanceApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Attendance System")
#         self.root.geometry("300x200")

#         self.label = tk.Label(root, text="Attendance System", font=("Helvetica", 16))
#         self.label.pack(pady=20)

#         self.show_button = tk.Button(root, text="Show Attendance", command=self.show_attendance)
#         self.show_button.pack(pady=10)

#     def show_attendance(self):
#         try:
#             df = pd.read_csv('Attendance.csv')
#             messagebox.showinfo("Attendance", df.to_string(index=False))
#         except FileNotFoundError:
#             messagebox.showerror("Error", "Attendance file not found.")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))


# root = tk.Tk()
# app = AttendanceApp(root)
# root.mainloop()



# //================= attempt-3======================
# import cv2
# import face_recognition
# import os
# import numpy as np
# from datetime import datetime
# import tkinter as tk
# from tkinter import messagebox
# import pandas as pd

# path = 'student_images'
# images = []
# classNames = []
# mylist = os.listdir(path)

# for cl in mylist:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     name = os.path.splitext(cl)[0].split('_')[0]
#     classNames.append(name.upper())

# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         encoded_faces = face_recognition.face_encodings(img)
#         if encoded_faces:
#             encodeList.append(encoded_faces[0])
#     return encodeList

# encoded_face_train = findEncodings(images)

# def markAttendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = [line.split(',')[0] for line in myDataList]
#         if name not in nameList:
#             now = datetime.now()
#             time = now.strftime('%H:%M:%S')
#             date = now.strftime('%d-%B-%Y')
#             f.writelines(f'\n{name}, {time}, {date}')
#             return True
#     return False

# cap = cv2.VideoCapture(0)
# while True:
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     faces_in_frame = face_recognition.face_locations(imgS, model='cnn')
#     encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

#     detected_names = set()

#     for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#         matches = face_recognition.compare_faces(encoded_face_train, encode_face, tolerance=0.5)
#         faceDist = face_recognition.face_distance(encoded_face_train, encode_face)

#         if faceDist.size > 0:
#             matchIndex = np.argmin(faceDist)
#             if matches[matchIndex]:
#                 name = classNames[matchIndex]
#                 if name not in detected_names:
#                     detected_names.add(name)
#                     marked = markAttendance(name)

#                     y1, x2, y2, x1 = faceloc
#                     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.rectangle(img, (x1, y2 - 60), (x2, y2), (0, 255, 0), cv2.FILLED)
#                     cv2.putText(img, name, (x1 + 6, y2 - 35), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)
#                     if marked:
#                         cv2.putText(img, "Successfully marked", (x1 + 6, y2 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)
#             else:
#                 y1, x2, y2, x1 = faceloc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#                 cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
#                 cv2.putText(img, "UNAUTHORIZED", (x1 + 6, y2 - 5),
#                             cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

#     cv2.imshow('webcam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



# //================= attempt-4======================

# import cv2
# import face_recognition
# import os
# import numpy as np
# from datetime import datetime
# import time

# path = 'student_images'
# images = []
# classNames = []
# mylist = os.listdir(path)

# for cl in mylist:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     name = os.path.splitext(cl)[0].split('_')[0]
#     classNames.append(name.upper())

# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         encoded_faces = face_recognition.face_encodings(img)
#         if encoded_faces:
#             encodeList.append(encoded_faces[0])
#     return encodeList

# encoded_face_train = findEncodings(images)

# def markAttendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = [line.split(',')[0] for line in myDataList]
#         if name not in nameList:
#             now = datetime.now()
#             timeStr = now.strftime('%H:%M:%S')
#             dateStr = now.strftime('%d-%B-%Y')
#             f.writelines(f'\n{name}, {timeStr}, {dateStr}')
#             return True
#     return False

# cap = cv2.VideoCapture(0)
# freeze_time = 5  # seconds
# last_mark_time = None
# freeze_frame = None

# while True:
#     if last_mark_time and (time.time() - last_mark_time < freeze_time):
#         if freeze_frame is not None:
#             cv2.imshow('webcam', freeze_frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         continue

#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     faces_in_frame = face_recognition.face_locations(imgS, model='cnn')
#     encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

#     detected_names = set()

#     for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#         matches = face_recognition.compare_faces(encoded_face_train, encode_face, tolerance=0.5)
#         faceDist = face_recognition.face_distance(encoded_face_train, encode_face)

#         if faceDist.size > 0:
#             matchIndex = np.argmin(faceDist)
#             if matches[matchIndex]:
#                 name = classNames[matchIndex]
#                 if name not in detected_names:
#                     detected_names.add(name)
#                     marked = markAttendance(name)

#                     y1, x2, y2, x1 = faceloc
#                     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Blue border
#                     cv2.rectangle(img, (x1, y2 - 60), (x2, y2), (255, 0, 0), cv2.FILLED)
#                     cv2.putText(img, name, (x1 + 6, y2 - 35), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)

#                     if marked:
#                         cv2.putText(img, "Successfully marked", (x1 + 6, y2 - 10),
#                                     cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)  # Blue text
#                         freeze_frame = img.copy()
#                         last_mark_time = time.time()

#             else:
#                 y1, x2, y2, x1 = faceloc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#                 cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
#                 cv2.putText(img, "UNAUTHORIZED", (x1 + 6, y2 - 5),
#                             cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

#     cv2.imshow('webcam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




# //================= attempt-4======================
#main.py
import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import time

# Path to the folder containing student face images
path = 'student_images'
images = []
classNames = []

# Load each image from the folder and extract the name
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    name = os.path.splitext(cl)[0].split('_')[0]  # Extract name from filename
    classNames.append(name.upper())

# Function to encode all known student face images
def findEncodings(images):
    encodeList = []
    for img in images:
        encoded_faces = face_recognition.face_encodings(img)
        if encoded_faces:
            encodeList.append(encoded_faces[0])  # Store only the first face encoding
    return encodeList

# Encode all known faces at the start
encoded_face_train = findEncodings(images)

# Function to mark attendance in a CSV file
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            timeStr = now.strftime('%H:%M:%S')
            dateStr = now.strftime('%d-%B-%Y')
            f.writelines(f'\n{name}, {timeStr}, {dateStr}')
            return True  # Attendance marked
    return False  # Already marked

# Initialize webcam
cap = cv2.VideoCapture(0)

# Time to freeze frame after marking attendance
freeze_time = 5  # seconds
last_mark_time = None
freeze_frame = None
marked_names = set()

# Continuous loop for real-time face recognition
while True:
    # Freeze frame if attendance just marked
    if last_mark_time and (time.time() - last_mark_time < freeze_time):
        if freeze_frame is not None:
            cv2.imshow('webcam', freeze_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        continue

    success, img = cap.read()

    # Resize frame for faster processing and convert to RGB
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    faces_in_frame = face_recognition.face_locations(imgS, model='hog')  # use 'hog' for faster CPU-based detection
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

    # Loop through each detected face
    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face, tolerance=0.5)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)

        if faceDist.size > 0:
            matchIndex = np.argmin(faceDist)
            if matches[matchIndex]:
                name = classNames[matchIndex]
                marked = False

                # Mark attendance if not already done
                if name not in marked_names:
                    marked = markAttendance(name)
                    marked_names.add(name)

                # Draw green box and name on face
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Scale back to original size
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y1 - 35), (x2, y1), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y1 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)

                # Show status (Marked/Already Marked)
                msg = "Successfully marked" if marked else "Marked"
                cv2.rectangle(img, (x1, y2), (x2, y2 + 25), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, msg, (x1 + 6, y2 + 20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

                freeze_frame = img.copy()
                last_mark_time = time.time()
            else:
                # Face detected but not recognized
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, "UNAUTHORIZED", (x1 + 6, y2 - 5),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    # Show the webcam feed with annotations
    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close window on quit
cap.release()
cv2.destroyAllWindows()


