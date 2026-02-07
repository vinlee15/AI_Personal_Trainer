import cv2
import numpy as np

def draw_info_panel(image, mode, counter, stage):
    """
    Vẽ bảng thông tin đếm số và trạng thái lên ảnh
    """
    h, w, c = image.shape

    # Vẽ khung hình chữ nhật
    cv2.rectangle(image, (0, 0), (250, 120), (245, 117, 16), -1)

    # Hiển thị Chế độ bài tập
    cv2.putText(image, str(mode), (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # Hiển thị counter
    cv2.putText(image, 'REPS', (15, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, str(counter), (10, 110), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

    # Hiển thị stage
    cv2.putText(image, 'STAGE', (100, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    
    # Đổi màu chữ Stage
    stage_text = str(stage) if stage else ""
    text_color = (0, 0, 255) if stage == "WRONG" else (255, 255, 255)
    
    cv2.putText(image, stage_text, (95, 110), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, text_color, 2, cv2.LINE_AA)

def draw_angle(image, angle, position, w, h):
    """
    Vẽ số đo góc ngay tại khớp xương
    """
    # Chuyển đổi tọa độ chuẩn hóa (0.0-1.0) sang Pixel
    pos_pixel = tuple(np.multiply(position, [w, h]).astype(int))
    
    # Vẽ chữ
    cv2.putText(image, str(int(angle)), 
                pos_pixel, 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)