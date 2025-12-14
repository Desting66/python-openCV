import cv2
import numpy as np

# 窗口大小和小球半径
width, height = 200, 200
r = 20
x = r + 20
y = r + 100
x_speed = y_speed = 4

# 创建窗口
cv2.namedWindow('img')

# 主循环
while True:
    # 检查是否按下退出键（Esc键）
    key = cv2.waitKey(1)
    if key == 27:  # Esc 键
        break

    # 更新小球位置，并在碰到边缘时反向
    if x > width - r or x < r:
        x_speed *= -1
    if y > height - r or y < r:
        y_speed *= -1

    x += x_speed
    y += y_speed

    # 创建一个白色背景的图像，并画上小球
    img = np.zeros((width, height), np.uint8)

    # 蓝色小球，颜色为 (255, 0, 0)
    cv2.circle(img, (x, y), r, (255, 0, 0), -1)  # 蓝色圆形

    # 显示图像
    cv2.imshow('img', img)

# 循环结束后关闭所有窗口
cv2.destroyAllWindows()
