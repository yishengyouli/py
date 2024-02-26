import cv2
import time
import os
import pyautogui
import platform
import subprocess

# 常量定义
NO_PERSON_THRESHOLD = 3
SAVE_IMAGE_DELAY = 5
IMG_NAME = "face_photo.jpg"

# 检测操作系统
def detect_os():
    os_name = platform.system()
    if os_name == 'Windows':
        return 'windows'
    elif os_name == 'Darwin':
        return 'mac'
    else:
        return 'other'

# 执行锁屏命令
def lock_screen(os_type):
    if os_type == 'windows':
        os.system('rundll32.exe user32.dll, LockWorkStation')
    elif os_type == 'mac':
        subprocess.run(['pmset', 'displaysleepnow'])

# 执行唤醒屏幕命令
def wake_screen():
    # 模拟鼠标微小移动，阻止屏幕休眠
    pyautogui.move(1, 0)
    pyautogui.move(-1, 0)
    # mac防休眠    
    # subprocess.run(['caffeinate', '-u', '-t', '1'])

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 载入OpenCV的人脸检测模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 无人状态计时器
no_person_timer = 0
# 是否保存图像的标志
save_image = False

# 检测操作系统类型
os_type = detect_os()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        no_person_timer += 1
        if no_person_timer > NO_PERSON_THRESHOLD:
            lock_screen(os_type)
    else:
        no_person_timer = 0
        # 当检测到人脸时唤醒屏幕
        wake_screen()

        # 检测到人脸时保存当前帧
        if not save_image:
            cv2.imwrite(IMG_NAME, frame)
            print(f"Saved image: {IMG_NAME}")
            save_image = True

            # 延迟一定时间再继续保存，避免频繁保存
            cv2.waitKey(SAVE_IMAGE_DELAY * 1000)

    # 检测键盘输入，以退出程序
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC键
        break

cap.release()
cv2.destroyAllWindows()

