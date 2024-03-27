import pygame
import sys
import random
from pygame.locals import QUIT, MOUSEBUTTONDOWN

# 初始化pygame
pygame.init()

# 设置屏幕大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("烟花效果")

# 颜色
BLACK = (0, 0, 0)


# 烟花粒子类
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 5
        self.velocity = [random.randint(-5, 5) for _ in range(2)]
        self.alpha = 255

    def update(self):
        self.velocity[1] += 0.1  # 重力效果
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.alpha -= 4  # 粒子逐渐消失

    def draw(self):
        if self.alpha >= 0:
            surface = pygame.Surface(
                (self.radius * 2, self.radius * 2), pygame.SRCALPHA
            )
            pygame.draw.circle(
                surface,
                self.color + (self.alpha,),
                (self.radius, self.radius),
                self.radius,
            )
            screen.blit(surface, (self.x - self.radius, self.y - self.radius))


particles = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # 在鼠标点击的位置生成新的烟花粒子
            for _ in range(50):  # 生成50个粒子
                particles.append(
                    Particle(
                        event.pos[0],
                        event.pos[1],
                        (
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                        ),
                    )
                )

    screen.fill(BLACK)

    # 更新和绘制所有的粒子
    for particle in particles[:]:
        particle.update()
        particle.draw()
        if particle.alpha <= 0:
            particles.remove(particle)

    pygame.display.flip()
    pygame.time.delay(20)
