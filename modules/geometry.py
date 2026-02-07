import numpy as np

def calculate_angle(a, b, c):
    a = np.array(a) #điểm đầu
    b = np.array(b) #điểm giữa
    c = np.array(c) #điểm cuối

    #tính góc theo radian
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])

    #đổi radian sang độ
    angle = np.abs(radians*180.0/np.pi)

    #giới hạn góc < 180
    if angle > 180.0:
        angle = 360 - angle

    return angle