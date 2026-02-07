import mediapipe as mp
from modules.geometry import calculate_angle

mp_pose = mp.solutions.pose

def count_bicep_curl(landmarks, counter, stage):
    # lấy vị trí tọa độ
    shoulder_pos = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow_pos = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, 
                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist_pos = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, 
                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

    # tính góc
    elbow_angle = calculate_angle(shoulder_pos, elbow_pos, wrist_pos)
    
    # thay đổi counter và stage
    if elbow_angle > 160:
        stage = "down"
    if elbow_angle < 50 and stage == "down":
        stage = "up"
        counter += 1

    return {
        "stage": stage, 
        "counter": counter, 
        "angle": elbow_angle, 
        "elbow_pos": elbow_pos
    }