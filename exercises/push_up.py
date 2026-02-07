import mediapipe as mp
from modules import calculate_angle, get_ground_level

mp_pose = mp.solutions.pose

def count_push_up(landmarks, counter, stage, image_height):
    # lấy vị trí tọa độ
    shoulder_pos = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow_pos = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, 
                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist_pos = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, 
                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    hip_pos = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, 
               landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    ankle_pos = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, 
                 landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

    # tính góc
    elbow_angle = calculate_angle(shoulder_pos, elbow_pos, wrist_pos)

    hip_angle = calculate_angle(shoulder_pos, hip_pos, ankle_pos)

    # tính khoảng cách từ tay đến mặt đất
    wrist_pos_pixel = int(wrist_pos[1] * image_height)

    dis = abs(wrist_pos_pixel - get_ground_level(landmarks, image_height))

    # thay đổi counter và stage
    if dis < 50:
        if  elbow_angle > 160 and hip_angle > 150:
            stage = 'UP'
        elif  elbow_angle < 90 and hip_angle > 150 and stage == 'UP':
            stage = 'DOWN'
            counter += 1
        elif hip_angle < 150:
            stage = 'WRONG'
    if dis > 300:
        stage = 'READY'

    return {
        "stage": stage, 
        "counter": counter, 
        "elbow_angle": elbow_angle, 
        "hip_angle": hip_angle, 
        "elbow_pos": elbow_pos, 
        "hip_pos": hip_pos
    }


