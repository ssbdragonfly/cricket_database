import cv2
import pytesseract

def extract_over_and_ball(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    config = '--psm 6' 
    text = pytesseract.image_to_string(gray, config=config)
    over, ball = None, None
    for line in text.split('\n'):
        if 'overs' in line.lower():
            parts = line.split()
            for part in parts:
                if '/' in part: 
                    over = part.split('/')[0]
                elif '.' in part:
                    ball = part
    return over, ball

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    over_and_ball_info = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        over, ball = extract_over_and_ball(frame)
        if over and ball:
            over_and_ball_info.append((over, ball))
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + frame_rate)

    cap.release()
    return over_and_ball_info
