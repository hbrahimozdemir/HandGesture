import mediapipe as mp
import cv2
import pyautogui
import time
cam = cv2.VideoCapture(0)
screen_x, screen_y = pyautogui.size()
pyautogui.FAILSAFE = False

mp_hand = mp.solutions.hands
detector = mp_hand.Hands()
drawing_styles = mp.solutions.drawing_styles
drawer = mp.solutions.drawing_utils

if not cam.isOpened():
    print("!! Can not Open Camera !!")

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    frame_y, frame_x, _ = frame.shape
    result = detector.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    hands = result.multi_hand_landmarks
    start=time.time()
    if hands:
        for hand_landmark in hands:

            drawer.draw_landmarks(frame, hand_landmark, mp_hand.HAND_CONNECTIONS,
                                  drawing_styles.get_default_hand_landmarks_style())

            landmark = hand_landmark.landmark
            for point, landmark in enumerate(landmark):
                x = int(landmark.x * frame_x)
                y = int(landmark.y * frame_y)

                if point == 20:
                    thmb12_x = (screen_x / frame_x * x)
                    thmb12_y = (screen_y / frame_y * y)
                    pyautogui.moveTo(thmb12_x, thmb12_y)

                if point == 4:
                    thmb_x = screen_x / frame_x * x
                    thmb_y = screen_y / frame_y * y

                if point == 8:
                    thm_x = screen_x / frame_x * x
                    thm_y = screen_y / frame_y * y
                    if abs(thmb_x - thm_x) < 3:
                        pyautogui.doubleClick()
                        dtime=time.time()
                        print('Dtime=',dtime-start)
                        pyautogui.sleep(0.5)

                if point == 12:
                    th_x = screen_x / frame_x * x
                    th_y = screen_y / frame_y * y
                    if abs(thmb_x - th_x) < 3:
                        pyautogui.leftClick()
                        ltime = time.time()
                        print('Ltime=', ltime - start)
                        pyautogui.sleep(0.5)


                if point == 16:
                    tp_x = screen_x / frame_x * x
                    tp_y = screen_y / frame_y * y
                    if abs(thmb_x - tp_x) < 3.6:
                        pyautogui.rightClick()
                        rtime = time.time()
                        print('Rtime=', rtime - start)
                        pyautogui.sleep(0.5)


    cv2.imshow('H.G.M.C', frame)
    cv2.waitKey(1)