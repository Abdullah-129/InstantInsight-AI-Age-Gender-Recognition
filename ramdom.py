import cv2
import math
import random
import os

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
    return frameOpencvDnn, faceBoxes

# Define the file paths for face and gender models
faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"
genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

# Define the model mean values, age, and gender lists
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# Load the face, age, and gender models
faceNet = cv2.dnn.readNet(faceModel, faceProto)
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)

# Capture video from the default camera
video = cv2.VideoCapture(0)
padding = 20

# Define the paths for the male and female folders
male_folder = "Male"
female_folder = "Female"

# Create a named window for the camera feed
cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)

current_age = None
current_gender = None
current_video = None

while cv2.waitKey(1) < 0:
    # Read the video frame
    ret, frame = video.read()
    if not ret or frame is None or frame.size == 0:
        continue

    resultImg, faceBoxes = highlightFace(faceNet, frame)

    if len(faceBoxes) == 0:
        if current_video is not None:
            ret, frame_to_play = current_video.read()
            if not ret:
                current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)

            cv2.imshow("Video", frame_to_play)
            cv2.putText(resultImg, f'Playing ad...', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(resultImg, 'No face detected', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
    else:
        for faceBox in faceBoxes:
            face = frame[max(0, faceBox[1] - padding): min(faceBox[3] + padding, frame.shape[0] - 1),
                         max(0, faceBox[0] - padding): min(faceBox[2] + padding, frame.shape[1] - 1)]

            if face.size == 0:
                print("Empty face image, skipping...")
                continue

            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPreds = genderNet.forward()
            gender = genderList[genderPreds[0].argmax()]
            print(f'Gender: {gender}')

            if gender == 'Male':
                folder_path = male_folder
            else:
                folder_path = female_folder

            ageNet.setInput(blob)
            agePreds = ageNet.forward()
            age = ageList[agePreds[0].argmax()]
            print(f'Age: {age[1:-1]} years')

            if age != current_age or gender != current_gender:
                current_age = age
                current_gender = gender

                age_folder_path = os.path.join(folder_path, age)
                ads = [f"{age_folder_path}/{i}.mp4" for i in range(1, 6)]
                current_video = cv2.VideoCapture(random.choice(ads))
                print(f"Playing ad: {current_video}")

            ret, frame_to_play = current_video.read()
            if not ret:
                current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)

            cv2.imshow("Video", frame_to_play)
            cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Camera", resultImg)

video.release()
cv2.destroyAllWindows()
