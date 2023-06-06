import pygame
import random
pygame.init()

class Spaceship:
    def __init__(self, spaceship_img, position_x = 450, position_y = 530, health = 100):
        self.spaceship_img = spaceship_img
        self.position_x = position_x
        self.position_y = position_y
        self.health = health
        self.speed = 0.45

    def return_object(self):
        return self.spaceship_img, self.position_x, self.position_y, self.health

    def return_health(self):
        return self.health
    
    def move(self,button):
        if button == "left" or button == "right" or button == "released_l" or button == "released_r":
            x_change = self.speed
            return x_change

        if button == "up" or button == "down" or button == "released_u" or button == "released_d":
            y_change = self.speed
            return y_change
    
    def decrease_health(self):
        self.health -= 20
        if self.health < 0:
            self.health = 20
    
    def decrease_health_2(self):
        self.health -= 5
        if self.health < 0:
            self.health = 0
    
    def increase_health(self):
        if self.health <100:
            self.health += 20
    
    def increase_speed(self):
        self.speed += 0.05
    
    def decrease_speed(self):
        if self.speed > 0.45:
            self.speed -= 0.05
    
class Asteroid():
    def __init__(self, asteroid_img, position_x = random.randint(0,936), position_y = -55):
        self.asteroid_img = asteroid_img
        self.position_x = position_x
        self.position_y = position_y
        self.speed = 0.2
        self.score_increase = 60
    
    def return_object(self):
        return self.asteroid_img, self.position_x, self.position_y
    
    def move(self):
        y_change = self.speed
        return y_change

    def reset_positon(self):
        self.position_y = -55
        self.position_x = random.randint(0,936)
    
    def increase_speed(self):
        if Score.class_value > self.score_increase:
            self.score_increase += 60
            self.speed += 0.05
        
class Bullet():
    def __init__(self, bullet_img, position_x=0, position_y=530):
        self.bullet_img = bullet_img
        self.position_x = position_x
        self.position_y = position_y
    
    def return_object(self):
        return self.bullet_img, self.position_x, self.position_y   
    
    def ready(self):
        bullet_state = "ready"
        return bullet_state
    
    def fire(self):
        bullet_state = "fire"
        return bullet_state

    def move(self):
        y_change = 1
        return y_change

    def reset_position(self):
        self.position_y = 530
    
class Score():
    class_value = 0
    def __init__(self, value = 0, position_x = 10, position_y = 10):
        self.value = value
        self.position_x = position_x
        self.position_y = position_y
        Score.class_value = 0
    
    def return_objects(self):
        return self.value, self.position_x, self.position_y

    def return_score(self):
        return self.value
    
    def increase(self):
        self.value += 5
        Score.class_value += 5
    
    def decrease(self):
        if self.value > 0:
            self.value -= 5
            Score.class_value -= 5

class Coin(Asteroid):
    def __init__(self, coin_img, position_x = random.randint(0, 936), position_y = -55):
        super().__init__(coin_img, position_x, position_y)
    
    def return_object(self):
        return super().return_object()
    
    def move(self):
        return super().move()
    
    def reset_positon(self):
        return super().reset_positon()

class Heart(Asteroid):
    def __init__(self, asteroid_img, position_x = random.randint(0, 936), position_y = -55):
        super().__init__(asteroid_img, position_x, position_y)
    
    def return_object(self):
        return super().return_object()
    
    def move(self):
        return super().move()
    
    def reset_positon(self):
        return super().reset_positon()
    
class Speedboost(Asteroid):
    def __init__(self, sppedboost_img, position_x =random.randint(0, 936), position_y = -55):
        super().__init__(sppedboost_img, position_x, position_y)

    def return_object(self):
        return super().return_object()
    
    def move(self):
        return super().move()
    
    def reset_positon(self):
        return super().reset_positon()
    
class Shield(Asteroid):
    def __init__(self, shield_img, position_x=random.randint(0, 936), position_y=-55):
        super().__init__(shield_img, position_x, position_y)

    def return_object(self):
        return super().return_object()

    def move(self):
        return super().move()
    
    def reset_positon(self):
        return super().reset_positon()