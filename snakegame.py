import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake_segment_img = pygame.image.load('snake.png')
food_img = pygame.image.load('mydonut.png')
snake_segment_img = pygame.transform.scale(snake_segment_img, (20, 20))
food_img = pygame.transform.scale(food_img, (20, 20))

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.score = 0
        self.food = self.create_food()

    def create_food(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.body:
                return (x, y)

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        if head == self.food:
            self.score += 1
            self.body.insert(0, head)
            self.food = self.create_food()
        else:
            if head in self.body[1:] or not (0 <= head[0] < GRID_WIDTH and 0 <= head[1] < GRID_HEIGHT):
                return False
            self.body.insert(0, head)
            self.body.pop()
        return True

    def change_direction(self, direction):
        if direction[0] * -1 != self.direction[0] or direction[1] * -1 != self.direction[1]:
            self.direction = direction

    def draw(self):
        for segment in self.body:
            screen.blit(snake_segment_img, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE))
        screen.blit(food_img, (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE))

# Main function
def main():
    snake = Snake()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        screen.fill((0, 0, 0))
        if not snake.move():
            break
        snake.draw()
        pygame.display.flip()
        clock.tick(10)  # Controls the speed of the game

    pygame.quit()

if __name__ == "__main__":
    main()
