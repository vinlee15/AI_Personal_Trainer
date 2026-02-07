import mediapipe as mp
from modules.geometry import calculate_angle

mp_pose = mp.solutions.pose

def count_squat(landmarks, counter, stage):
    # lấy vị trí tọa độ
    hip_pos = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, 
               landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    knee_pos = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, 
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    heel_pos = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x, 
                landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]

    # tính góc
    knee_angle = calculate_angle(hip_pos, knee_pos, heel_pos)

    # thay đổi counter và stage
    if knee_angle > 150:
        stage = "UP"
    if knee_angle < 90 and stage == "UP":
        stage = "DOWN"
        counter += 1

    return {
        "stage": stage, 
        "counter": counter, 
        "angle": knee_angle, 
        "knee_pos": knee_pos
    }