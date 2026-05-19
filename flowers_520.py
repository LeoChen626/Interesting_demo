# 开发大神：Leo Chen
# 开发时间：2026/5/20 0:33
# 文件路径：D:\test002\flower520_demo\flowers_520.py
import pygame
import random
import sys
import math

# 初始化Pygame
pygame.init()

# 获取屏幕信息
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# 设置全屏显示
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Happy 520!")
clock = pygame.time.Clock()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)
RED = (255, 0, 0)
LIGHT_PINK = (255, 182, 193)
HOT_PINK = (255, 105, 180)


class Flower:
    """花的类，用于绘制和管理每一朵花"""

    def __init__(self, x, y):
        """初始化花的位置和属性"""
        self.x = x
        self.y = y
        self.size = 0
        self.max_size = random.randint(30, 60)
        self.grow_speed = random.uniform(0.5, 1.5)
        self.petals = random.randint(5, 8)
        self.color = random.choice([PINK, LIGHT_PINK, HOT_PINK, (255, 228, 225)])
        self.center_color = (255, 215, 0)
        self.growing = True

    def grow(self):
        """花生长的动画"""
        if self.growing and self.size < self.max_size:
            self.size += self.grow_speed
        else:
            self.growing = False

    def draw(self, surface):
        """在指定表面上绘制花"""
        if self.size <= 0:
            return

        # 绘制花瓣
        petal_radius = self.size // 2
        for i in range(self.petals):
            angle = (2 * math.pi * i) / self.petals
            petal_x = self.x + math.cos(angle) * petal_radius
            petal_y = self.y + math.sin(angle) * petal_radius
            pygame.draw.circle(surface, self.color, (int(petal_x), int(petal_y)), int(petal_radius * 0.8))

        # 绘制花心
        pygame.draw.circle(surface, self.center_color, (int(self.x), int(self.y)), int(self.size * 0.3))


def main():
    """主函数，控制整个程序流程"""

    # 存储所有花的列表
    flowers = []

    # 状态标志
    flowers_full = False
    text_show = False
    text_alpha = 0

    # 创建字体对象
    font_large = pygame.font.Font(None, 72)
    font_medium = pygame.font.Font(None, 48)

    # 主循环
    running = True
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 填充背景
        screen.fill(BLACK)

        if not flowers_full:
            # 随机生成新花
            if random.random() < 0.3 and len(flowers) < 200:
                x = random.randint(0, screen_width)
                y = random.randint(0, screen_height)
                flowers.append(Flower(x, y))

            # 更新和绘制所有花
            all_grown = True
            for flower in flowers:
                flower.grow()
                flower.draw(screen)
                if flower.growing:
                    all_grown = False

            # 检查是否所有花都开满了
            if all_grown and len(flowers) >= 150:
                flowers_full = True
        else:
            # 花已经开满，开始显示文字
            text_show = True
            if text_alpha < 255:
                text_alpha += 3

            # 继续绘制花
            for flower in flowers:
                flower.draw(screen)

            # 显示文字
            if text_show:
                text_surface = font_large.render("Happy 520, single dog!", True, WHITE)
                text_surface.set_alpha(text_alpha)
                text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
                screen.blit(text_surface, text_rect)

        # 更新显示
        pygame.display.flip()
        clock.tick(60)

    # 退出程序
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
