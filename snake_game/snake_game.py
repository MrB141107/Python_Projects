"""
Author: Ninja-06
Date: 22-10-2023
Description: This is simple snake game which is build using pygame module.
Run this file from Python projects directory
"""

import random
import pygame
import pygame.font
import time
import constants as c


direction = c.DIRECTIONS
class snakeGame:

    snake_speed_dict = {
            20: 0.1,
            100: 0.09,
            300: 0.08,
            450: 0.07,
            600: 0.06,
            1000: 0.05
        }
    
    def __init__(self):
       
        #initialize all imported modules pygame 
        pygame.init()
        pygame.font.init()

        # setup font to display score
        self.font = pygame.font.SysFont("Segoe UI", 19)
        
        # Set up the drawing window
        self.screen = pygame.display.set_mode([c.GAME_WINDOW_WIDTH, c.GAME_WINDOW_HEIGHT])

        # change window caption
        pygame.display.set_caption(c.GAME_TITLE)

        # change window icon
        pygame_icon = pygame.image.load(c.GAME_ICON_FILENAME)
        pygame.display.set_icon(pygame_icon)

        # initialize score
        self.score = 0

        # initialize snake
        self.snake_init()

        # initialize apple
        self.apple_init()
        
    def snake_init(self):
        """
        initializing snake
        """
        self.snake_x_coordinate = [c.DEFAULT_SNAKE_X_COORDINATE]*c.FIXED_SNAKE_LENGTH
        self.snake_y_coordinate = [c.DEFAULT_SNAKE_Y_COORDINATE]*c.FIXED_SNAKE_LENGTH
        self.snake_direction = direction.get('D')
        self.snake_speed = c.DEFAULT_SNAKE_SPEED
        self.running = True

    def apple_init(self):
        
        """
        initialize apple
        """
        self.apple_x_coordinate = c.DEFAULT_APPLE_X_COORDINATE
        self.apple_y_coordinate = c.DEFAULT_APPLE_Y_COORDINATE
        


    def draw_snake(self):
        """
        this function draws snake on screen
        """
        for i in range(c.FIXED_SNAKE_LENGTH):
            snake_dimensions = pygame.Rect(self.snake_x_coordinate[i], self.snake_y_coordinate[i], c.SNAKE_WIDTH, c.SNAKE_HEIGHT)
            pygame.draw.rect(self.screen, c.SNAKE_COLOR, snake_dimensions)
        pygame.display.flip()
    
    def draw_apple(self):
        """
        this function draws apple on screen
        """
        apple_dimensions = pygame.Rect(self.apple_x_coordinate, self.apple_y_coordinate, c.APPLE_WIDTH, c.APPLE_HEIGHT)
        pygame.draw.rect(self.screen, c.APPLE_COLOR, apple_dimensions)
        pygame.display.flip()

    def change_apple_coordinates(self):
        
        """
        this function changes the apple position on the screen when snake eats apple
        """
        self.apple_y = self.apple_y_coordinate
        self.apple_x = self.apple_x_coordinate
        self.snake_ate_apple = False

        if self.snake_x_coordinate[0] == self.apple_x and self.snake_y_coordinate[0] == self.apple_y:
            self.apple_x, self.apple_y = random.randrange(0, 600 - 20, 20), random.randrange(40, 400 - 20, 20)
            self.snake_ate_apple = True
        return self.apple_x, self.apple_y, self.snake_ate_apple
    
    def display_current_score(self):
        """
        method displays and returns the current score of the player.
        """
        old_score = self.score

        if self.snake_ate_apple:
            new_score = old_score + 1
        else:
            new_score = old_score

        text_to_display = "Score : {}".format(new_score)
        self.font.set_bold(True)
        text = self.font.render(text_to_display, True, c.SCORE_TEXT_COLOR)
        score_dimensions = pygame.Rect(0, 0, 600, 30)
        pygame.draw.rect(self.screen, c.SCORE_AREA_COLOR, score_dimensions)
        self.screen.blit(text, c.SCORE_TEXT_COORDINATES)
        pygame.display.flip()
        return new_score
    
    def display_final_score(self):
        """
        method displays the final once the player lose the game
        """

        self.screen.fill(c.SCREEN_BACKGROUND_COLOR)
        self.font.set_bold(True)
        if self.score == 0 or self.score == -1:
            text_to_display = "Don't Give up, still you can make it up !! Your Score is: 0"
            text = self.font.render(text_to_display, True, (115, 219, 132))
            self.screen.blit(text, (70, 150))
        else:
            text_to_display = "Great !! Your Score is: {}".format(self.score)
            text = self.font.render(text_to_display, True, (115, 219, 132))
            self.screen.blit(text, (200, 150))
    
        pygame.display.flip()

    def game_over(self):
        """
        this function checks of the snake has hit the edge of screen and if yes it displays final score.
        and make the running variable as false so that game loop terminates.
        """
        game_over = False
        if self.snake_x_coordinate[0] == 0 or self.snake_x_coordinate[0] == 570:
            game_over = True
        elif self.snake_y_coordinate[0]  == 30 or self.snake_y_coordinate[0]  == c.GAME_WINDOW_HEIGHT:
            game_over = True
        if game_over:
            self.display_final_score()
            self.running = False 

    def snake_walk(self):

        """
        this function changes the snake position on click of arrow keys. and returns x and y coordinate of snake
        """
        x = self.snake_x_coordinate
        y = self.snake_y_coordinate

        for i in range(c.FIXED_SNAKE_LENGTH - 1, 0, -1):
            x[i] = x[i - 1]
            y[i] = y[i - 1]

        if self.snake_direction == direction.get('U'):
            if y[0] >= c.SURFACE_START_Y_COORDINATE:
                y[0] = y[0] - 10
            else:
                pass
        elif self.snake_direction == direction.get('D'):
            if y[0] <= c.SURFACE_EXTREME_Y_COORDINATE:
                y[0] = y[0] + 10
            else:
                pass
        elif self.snake_direction == direction.get('L'):
            if x[0] != c.SURFACE_START_X_COORDINATE:
                x[0] = x[0] - 10
            else:
                pass
        elif self.snake_direction == direction.get('R'):
            if x[0] <= c.SURFACE_EXTREME_X_COORDINATE:
                x[0] = x[0] + 10
            else:
                pass

        return x, y
    
    def get_snake_direction(self):

        """
        this function makes the snake move in specific direction on press of specific arrow keys.
        """
        if self.event.key == pygame.K_UP:
            self.snake_direction = direction.get('U')

        if self.event.key == pygame.K_DOWN:
            self.snake_direction = direction.get('D')

        if self.event.key == pygame.K_LEFT:
            self.snake_direction = direction.get('L')

        if self.event.key == pygame.K_RIGHT:
            self.snake_direction = direction.get('R')
        
        return self.snake_direction
    
    def get_snake_speed(self):
        
        """
        this function changes the snake speed(sleep time) when user score reaches the threshold value
        """
        if 100 > self.score >= 20:
            self.snake_speed = self.snake_speed_dict.get(20)
        elif 300 > self.score >= 100:
            self.snake_speed = self.snake_speed_dict.get(100)
        elif 450 > self.score >= 300:
            self.snake_speed = self.snake_speed_dict.get(300)
        elif 600 > self.score >= 450:
            self.snake_speed = self.snake_speed_dict.get(450)
        elif 1000 > self.score >= 600:
            self.snake_speed = self.snake_speed_dict(600)
        elif self.score >= 1000:
            self.snake_speed = self.snake_speed_dict.get(1000)

    def run(self):
        """
        this function executed snake game logic until user quits the game or loses the game.
        """
        while self.running:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False

                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        self.running = False

                    self.snake_direction = self.get_snake_direction()
                    

            self.snake_x_coordinate, self.snake_y_coordinate = self.snake_walk()
            
            # this function will set the variable snake_speed to appropriate snake speed. 
            self.get_snake_speed()
            time.sleep(self.snake_speed)

            # Fill the background with color
            self.screen.fill(c.SCREEN_BACKGROUND_COLOR)

            # change apple position once snake eats the apple
            self.apple_x_coordinate, self.apple_y_coordinate, self.snake_ate_apple = self.change_apple_coordinates()

            # draw apple on screen
            self.draw_apple()

            # draw snake on screen 
            self.draw_snake()

            # get current score and display it on the screen
            self.score = self.display_current_score()
            
            # check if the game over conditions are met, if yes, display the final score
            self.game_over()

        self.quit_game() #quit the game once the runnning variable is made False


    def quit_game(self):
        """
        quits the game when user clicks on X button or loses the game
        """
        time.sleep(1)
        pygame.quit()

s = snakeGame()
s.run()
