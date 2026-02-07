import mediapipe as mp

mp_pose = mp.solutions.pose

def get_ground_level(landmarks, image_height):
    foot_point = [
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
        landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y
    ]

    max_y = max(foot_point)

    ground_pixel = int(max_y * image_height)

    return ground_pixel