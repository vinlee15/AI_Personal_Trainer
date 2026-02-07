import cv2
import mediapipe as mp
import exercises
import utils

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def main():
    cap = cv2.VideoCapture(0)

    counter = 0
    stage = None
    
    if not cap.isOpened():
        print("Không thể mở Camera")
        return
    
    # Chọn chế độ
    mode = input("Chọn chế độ (CURL / SQUAT / PUSH_UP): ").upper().strip()

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Xử lý ảnh
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            h, w, c = image.shape

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                
                res = None

                if mode == "CURL":
                    res = exercises.curl.count_bicep_curl(landmarks, counter, stage)
                    # Vẽ góc khuỷu tay
                    utils.draw_angle(image, res["angle"], res["elbow_pos"], w, h)

                elif mode == "SQUAT":
                    res = exercises.squat.count_squat(landmarks, counter, stage)
                    # Vẽ góc đầu gối
                    utils.draw_angle(image, res["angle"], res["knee_pos"], w, h)
                    
                elif mode == "PUSH_UP":
                    res = exercises.push_up.count_push_up(landmarks, counter, stage, h)
                    # Vẽ góc khuỷu tay và hông
                    utils.draw_angle(image, res["elbow_angle"], res["elbow_pos"], w, h)
                    utils.draw_angle(image, res["hip_angle"], res["hip_pos"], w, h)

                if res:
                    counter = res["counter"]
                    stage = res["stage"]

                # Vẽ xương khớp
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                )

            # Vẽ UI
            utils.draw_info_panel(image, mode, counter, stage)
                
            cv2.imshow('AI Project - Vinh', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()