import pygame
import sys

# تهيئة Pygame
pygame.init()

# إعدادات الشاشة
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping Pong")

# إعدادات الألوان
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# إعداد المضارب
paddle_width = 10
paddle_height = 100
paddle_speed = 10

player_paddle = pygame.Rect(50, 250, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(740, 250, paddle_width, paddle_height)

# إعداد الكرة
ball = pygame.Rect(390, 290, 20, 20)
ball_speed_x = 5
ball_speed_y = 5

# إعداد النقاط
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)


def main():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    clock = pygame.time.Clock()

    while True:
        # معالجة الأحداث
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # تحريك المضارب
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_paddle.top > 0:
            player_paddle.y -= paddle_speed
        if keys[pygame.K_s] and player_paddle.bottom < 600:
            player_paddle.y += paddle_speed

        if keys[pygame.K_UP] and opponent_paddle.top > 0:
            opponent_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and opponent_paddle.bottom < 600:
            opponent_paddle.y += paddle_speed

        # تحريك الكرة
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # تصادم الكرة مع الجدران
        if ball.top <= 0 or ball.bottom >= 600:
            ball_speed_y = -ball_speed_y

        # تحديث النقاط وإعادة تعيين الكرة عند تسجيل هدف
        if ball.left <= 0:
            opponent_score += 1
            ball.center = (400, 300)
            ball_speed_x = -ball_speed_x
        if ball.right >= 800:
            player_score += 1
            ball.center = (400, 300)
            ball_speed_x = -ball_speed_x

        # تصادم الكرة مع المضارب
        if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
            ball_speed_x = -ball_speed_x

        # رسم الكائنات
        screen.fill(BLACK)
        # رسم مضرب اللاعب باللون الأحمر
        pygame.draw.rect(screen, RED, player_paddle)
        # رسم مضرب الخصم باللون الأزرق
        pygame.draw.rect(screen, BLUE, opponent_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)

        # عرض النتيجة
        player_text = font.render(str(player_score), True, WHITE)
        screen.blit(player_text, (320, 10))
        opponent_text = font.render(str(opponent_score), True, WHITE)
        screen.blit(opponent_text, (420, 10))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
