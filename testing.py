import math
import pygame
from pygame import Vector2

window_x = 900
window_y = 600
screen_size = Vector2(window_x, window_y)
screen_center = screen_size // 2
pygame.display.set_caption('Car Simulation')

key_events = {pygame.K_UP: 'FORWARD', 
			  pygame.K_DOWN: 'BACKWARD',
			  pygame.K_LEFT: 'LEFT',
			  pygame.K_RIGHT: 'RIGHT',
			  pygame.K_SPACE: 'STATIONARY'} 

reference_dict = {}

def rotate_on_pivot(image, angle, pivot, origin):
    
    surf = pygame.transform.rotate(image, angle)
    
    offset = pivot + (origin - pivot).rotate(-angle)
    rect = surf.get_rect(center = offset)
    
    return surf, rect

class Car:
    
    def __init__(self, pivot, starting_angle = 0):
        
        self.pivot = pivot
        self.angle = 0
        self.speed = 0
        self.chain_length = 0
        self.chain_change = 20

        self.offset = Vector2()
        self.offset.from_polar((self.chain_length, -starting_angle))
        
        self.pos = pivot + self.offset
        
        self.image_orig = reference_dict['car']
        self.image = self.image_orig
        self.rect = self.image.get_rect(center = self.pos)

        self.direction = 'FORWARD'
        self.change_to = self.direction
        
    def update(self):

        if (self.direction == 'FORWARD' or self.direction == 'BACKWARD'):
            if self.direction == 'FORWARD':
                self.pos[0] -=  math.sin(math.radians(self.angle)) * self.speed / 100
                self.pos[1] -= math.cos(math.radians(self.angle)) * self.speed /100
            if self.direction == 'BACKWARD':
                self.pos[0] +=  math.sin(math.radians(self.angle)) * self.speed / 100
                self.pos[1] += math.cos(math.radians(self.angle)) * self.speed / 100
        else: 
            self.offset.from_polar((self.chain_length, -self.angle))
            self.pos = self.pivot + self.offset
            self.angle += 1 * (self.speed / 100)
            
        self.image, self.rect = rotate_on_pivot(self.image_orig, self.angle, self.pivot, self.pos)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.running = False
        
        self.screen = pygame.display.set_mode(screen_size)
        
        self.load_image('car')
  
        self.car = Car(screen_center, starting_angle = 0)
  
    def load_image(self, image_name):
        image = pygame.image.load('car.png').convert()
        reference_dict[image_name] = image
  
    def draw(self, surface):
        
        surface.fill('black')

        self.car.draw(surface)
        
        pygame.display.flip()
        
    def run(self):
        
        self.running = True
        
        while self.running:
            
            frame_rate = self.clock.tick() * .001
            self.fps = self.clock.get_fps()
            pygame.display.set_caption(f'FPS: {self.fps}')
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif key_events[event.key] == "STATIONARY":
                        self.car.speed = 0
                        print('stop')
                    elif key_events[event.key] == 'FORWARD' or key_events[event.key] == 'BACKWARD':
                        if (self.car.speed >= 0):
                            self.car.speed += 5
                        else:
                            speed = abs(speed)
                    elif key_events[event.key] == 'LEFT' or key_events[event.key] == 'RIGHT':
                        if (self.car.chain_length == 0):
                            self.car.chain_length = 200
                        else:
                            self.car.chain_length -= self.car.chain_change
                        self.car.direction = key_events[event.key]
                        print('left or right')
            
            self.car.update()
            self.draw(self.screen)
        
        
if __name__ == '__main__':
    Game().run()