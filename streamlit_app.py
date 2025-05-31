    # import streamlit as st
    # import pandas as pd
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
    #     classNames.append(os.path.splitext(cl)[0])  

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
    #         nameList = []
    #         for line in myDataList:
    #             entry = line.split(',')
    #             nameList.append(entry[0])
    #         if name not in nameList:
    #             now = datetime.now()
    #             time = now.strftime('%H:%M:%S')
    #             date = now.strftime('%d-%B-%Y')
    #             f.writelines(f'\n{name}, {time}, {date}')


    # st.title("Real-Time Attendance System")
    # st.sidebar.title("Options")


    # if st.sidebar.button("Show Attendance"):
    #     try:
    #         df = pd.read_csv('Attendance.csv')
    #         st.write("### Attendance Records")
    #         st.dataframe(df)
    #     except FileNotFoundError:
    #         st.error("Attendance file not found.")
    #     except Exception as e:
    #         st.error(f"Error: {str(e)}")


    # if st.sidebar.button("Start Webcam"):
    #     st.warning("Press 'q' to stop the webcam.")
    #     cap = cv2.VideoCapture(0)
    #     while True:
    #         success, img = cap.read()
    #         imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    #         faces_in_frame = face_recognition.face_locations(imgS)
    #         encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    #         for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
    #             matches = face_recognition.compare_faces(encoded_face_train, encode_face)
    #             faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
    #             matchIndex = np.argmin(faceDist)
    #             if matches[matchIndex]:
    #                 name = classNames[matchIndex].upper()
    #                 y1, x2, y2, x1 = faceloc
    #                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
    #                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #                 cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
    #                 cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    #                 markAttendance(name)
    #         cv2.imshow('Webcam', img)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    #     cap.release()
    #     cv2.destroyAllWindows()
    #     st.success("Webcam stopped.")
        
        
 # ============ ATTEMPT-1=========================
       
       
# import streamlit as st
# import pandas as pd
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
#     classNames.append(os.path.splitext(cl)[0])  

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

# st.title("Real-Time Attendance System")
# st.sidebar.title("Options")

# if st.sidebar.button("Show Attendance"):
#     try:
#         df = pd.read_csv('Attendance.csv')
#         st.write("### Attendance Records")
#         st.dataframe(df)
#     except FileNotFoundError:
#         st.error("Attendance file not found.")
#     except Exception as e:
#         st.error(f"Error: {str(e)}")

# if st.sidebar.button("Start Webcam"):
#     st.warning("Press 'q' to stop the webcam.")
#     cap = cv2.VideoCapture(0)
#     while True:
#         success, img = cap.read()
#         imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
#         faces_in_frame = face_recognition.face_locations(imgS)
#         encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

#         for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#             matches = face_recognition.compare_faces(encoded_face_train, encode_face)
#             faceDist = face_recognition.face_distance(encoded_face_train, encode_face)

#             if len(faceDist) > 0 and np.min(faceDist) < 0.6:
#                 matchIndex = np.argmin(faceDist)
#                 if matches[matchIndex]:
#                     name = classNames[matchIndex].upper()
#                     color = (0, 255, 0)
#             else:
#                 name = "UNAUTHORIZED"
#                 color = (0, 0, 255)

#             y1, x2, y2, x1 = faceloc
#             y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
#             cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
#             cv2.rectangle(img, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
#             cv2.putText(img, name, (x1+6, y2-5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

#             if name != "UNAUTHORIZED":
#                 markAttendance(name)

#         cv2.imshow('Webcam', img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     st.success("Webcam stopped.")



#===========================================  ATTEMPT-2================================


# import streamlit as st
# import pandas as pd
# import cv2
# import face_recognition
# import os
# import numpy as np
# from datetime import datetime

# path = 'student_images'

# images = []
# classNames = []
# encodeListKnown = []

# mylist = os.listdir(path)
# for cl in mylist:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])

# # Encode all images in student_images
# for img in images:
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     encodes = face_recognition.face_encodings(img_rgb)
#     if encodes:
#         encodeListKnown.append(encodes[0])


# def markAttendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = [line.split(',')[0] for line in myDataList]
#         if name not in nameList:
#             now = datetime.now()
#             time = now.strftime('%H:%M:%S')
#             date = now.strftime('%d-%B-%Y')
#             f.writelines(f'\n{name}, {time}, {date}')


# st.title("Real-Time Attendance System")
# st.sidebar.title("Options")

# if st.sidebar.button("Show Attendance"):
#     try:
#         df = pd.read_csv('Attendance.csv')
#         st.write("### Attendance Records")
#         st.dataframe(df)
#     except FileNotFoundError:
#         st.error("Attendance file not found.")
#     except Exception as e:
#         st.error(f"Error: {str(e)}")


# if st.sidebar.button("Start Webcam"):
#     st.warning("Press 'q' to stop the webcam.")
#     cap = cv2.VideoCapture(0)
#     marked_names = set()

#     while True:
#         success, img = cap.read()
#         if not success:
#             break

#         imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#         faces_in_frame = face_recognition.face_locations(imgS, model='hog')
#         encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

#         for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#             matches = face_recognition.compare_faces(encodeListKnown, encode_face)
#             faceDist = face_recognition.face_distance(encodeListKnown, encode_face)

#             if len(faceDist) > 0:
#                 matchIndex = np.argmin(faceDist)

#                 if matches[matchIndex]:
#                     name = classNames[matchIndex].upper()

#                     if name not in marked_names:
#                         markAttendance(name)
#                         marked_names.add(name)

#                     y1, x2, y2, x1 = faceloc
#                     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#                     cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#                 else:
#                     y1, x2, y2, x1 = faceloc
#                     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#                     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
#                     cv2.putText(img, "UNAUTHORIZED", (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

#         cv2.imshow('Webcam', img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     st.success("Webcam stopped.")

#===========================================  ATTEMPT-3================================
# import streamlit as st
# import pandas as pd
# import cv2
# import face_recognition
# import os
# import numpy as np
# from datetime import datetime

# path = 'student_images'
# images = []
# classNames = []
# encodeListKnown = []

# mylist = os.listdir(path)
# for cl in mylist:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])

# for img in images:
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     encodes = face_recognition.face_encodings(img_rgb)
#     if encodes:
#         encodeListKnown.append(encodes[0])

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

# st.title("Real-Time Attendance System")
# st.sidebar.title("Options")

# if st.sidebar.button("Show Attendance"):
#     try:
#         df = pd.read_csv('Attendance.csv')
#         st.write("### Attendance Records")
#         st.dataframe(df)
#     except FileNotFoundError:
#         st.error("Attendance file not found.")
#     except Exception as e:
#         st.error(f"Error: {str(e)}")

# if st.sidebar.button("Start Webcam"):
#     st.warning("Press 'q' to stop the webcam.")
#     cap = cv2.VideoCapture(0)
#     marked_names = set()

#     while True:
#         success, img = cap.read()
#         if not success:
#             break

#         imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#         faces_in_frame = face_recognition.face_locations(imgS, model='hog')
#         encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

#         for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#             matches = face_recognition.compare_faces(encodeListKnown, encode_face)
#             faceDist = face_recognition.face_distance(encodeListKnown, encode_face)

#             if len(faceDist) > 0:
#                 matchIndex = np.argmin(faceDist)

#                 if matches[matchIndex]:
#                     name = classNames[matchIndex].upper()

#                     if name not in marked_names:
#                         marked = markAttendance(name)
#                         marked_names.add(name)

#                         y1, x2, y2, x1 = faceloc
#                         y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

#                         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                         cv2.rectangle(img, (x1, y2 - 60), (x2, y2), (0, 255, 0), cv2.FILLED)
#                         cv2.putText(img, name, (x1 + 6, y2 - 35), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)
#                         if marked:
#                             cv2.putText(img, "Successfully marked", (x1 + 6, y2 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)

#                 else:
#                     y1, x2, y2, x1 = faceloc
#                     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#                     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
#                     cv2.putText(img, "UNAUTHORIZED", (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

#         cv2.imshow('Webcam', img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     st.success("Webcam stopped.")


#===========================================  ATTEMPT-4================================


# import streamlit as st
# import pandas as pd
# import cv2
# import face_recognition
# import os
# import numpy as np
# from datetime import datetime
# import time

# path = 'student_images'

# images = []
# classNames = []
# encodeListKnown = []

# mylist = os.listdir(path)
# for cl in mylist:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0].upper())

# for img in images:
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     encodes = face_recognition.face_encodings(img_rgb)
#     if encodes:
#         encodeListKnown.append(encodes[0])

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

# st.title("Real-Time Attendance System")
# st.sidebar.title("Options")

# if st.sidebar.button("Show Attendance"):
#     try:
#         df = pd.read_csv('Attendance.csv')
#         st.write("### Attendance Records")
#         st.dataframe(df)
#     except FileNotFoundError:
#         st.error("Attendance file not found.")
#     except Exception as e:
#         st.error(f"Error: {str(e)}")

# if st.sidebar.button("Start Webcam"):
#     st.warning("Press 'q' to stop the webcam.")
#     cap = cv2.VideoCapture(0)
#     marked_names = set()
#     freeze_time = 5
#     last_mark_time = None
#     freeze_frame = None

#     while True:
#         if last_mark_time and (time.time() - last_mark_time < freeze_time):
#             if freeze_frame is not None:
#                 cv2.imshow('Webcam', freeze_frame)
#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     break
#             continue

#         success, img = cap.read()
#         if not success:
#             break

#         imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#         faces_in_frame = face_recognition.face_locations(imgS, model='hog')
#         encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

#         for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
#             matches = face_recognition.compare_faces(encodeListKnown, encode_face)
#             faceDist = face_recognition.face_distance(encodeListKnown, encode_face)

#             if len(faceDist) > 0:
#                 matchIndex = np.argmin(faceDist)

#                 if matches[matchIndex]:
#                     name = classNames[matchIndex]

#                     if name not in marked_names:
#                         marked = markAttendance(name)
#                         marked_names.add(name)

#                         y1, x2, y2, x1 = faceloc
#                         y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

#                         # Blue rectangle and text
#                         cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
#                         cv2.rectangle(img, (x1, y2 - 60), (x2, y2), (255, 0, 0), cv2.FILLED)
#                         cv2.putText(img, name, (x1 + 6, y2 - 35), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)

#                         if marked:
#                             cv2.putText(img, "Successfully marked", (x1 + 6, y2 - 10),
#                                         cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)

#                             freeze_frame = img.copy()
#                             last_mark_time = time.time()

#                 else:
#                     y1, x2, y2, x1 = faceloc
#                     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#                     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
#                     cv2.putText(img, "UNAUTHORIZED", (x1 + 6, y2 - 5),
#                                 cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

#         cv2.imshow('Webcam', img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     st.success("Webcam stopped.")



#===========================================  ATTEMPT-4================================
#streamlit_app.py
import streamlit as st
import pandas as pd
import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import time

# Path to directory with known student images
path = 'student_images'

images = []
classNames = []
encodeListKnown = []

# Load each image from the directory and get the name (filename without extension)
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0].upper())

# Encode all known faces
for img in images:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB as face_recognition expects RGB format
    encodes = face_recognition.face_encodings(img_rgb)
    if encodes:
        encodeListKnown.append(encodes[0])  # Store the encoding of the first face

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
            return True  # New attendance marked
    return False  # Already marked

# Streamlit UI
st.title("Real-Time Attendance System")
st.sidebar.title("Options")

# Show attendance table if button is clicked
if st.sidebar.button("Show Attendance"):
    try:
        df = pd.read_csv('Attendance.csv')
        st.write("### Attendance Records")
        st.dataframe(df)  # Display attendance as a table
    except FileNotFoundError:
        st.error("Attendance file not found.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Start webcam if button is clicked
if st.sidebar.button("Start Webcam"):
    st.warning("Press 'q' in the webcam window to stop.")
    cap = cv2.VideoCapture(0)
    marked_names = set()
    freeze_time = 5  # Seconds to freeze after marking attendance
    last_mark_time = None
    freeze_frame = None

    # Real-time face recognition loop
    while True:
        # Hold on the freeze frame if recently marked
        if last_mark_time and (time.time() - last_mark_time < freeze_time):
            if freeze_frame is not None:
                cv2.imshow('Webcam', freeze_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            continue

        success, img = cap.read()
        if not success:
            break

        # Resize and convert frame for faster processing
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        # Detect face locations and encodings
        faces_in_frame = face_recognition.face_locations(imgS, model='hog')  # Use 'hog' for speed
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

        # Loop through all detected faces
        for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
            matches = face_recognition.compare_faces(encodeListKnown, encode_face)
            faceDist = face_recognition.face_distance(encodeListKnown, encode_face)

            if len(faceDist) > 0:
                matchIndex = np.argmin(faceDist)
                if matches[matchIndex]:
                    name = classNames[matchIndex]
                    marked = False

                    # Mark attendance if not already done
                    if name not in marked_names:
                        marked = markAttendance(name)
                        marked_names.add(name)

                    # Scale face location back to original size and draw box
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y1 - 35), (x2, y1), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y1 - 6),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)

                    # Show status on screen
                    msg = "Successfully marked" if marked else "Marked"
                    cv2.rectangle(img, (x1, y2), (x2, y2 + 25), (255, 0, 0), cv2.FILLED)
                    cv2.putText(img, msg, (x1 + 6, y2 + 20),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

                    freeze_frame = img.copy()
                    last_mark_time = time.time()
                else:
                    # Unknown face - mark in red
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, "UNAUTHORIZED", (x1 + 6, y2 - 5),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        # Show webcam feed with annotations
        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release webcam and close OpenCV window
    cap.release()
    cv2.destroyAllWindows()
    st.success("Webcam stopped.")
