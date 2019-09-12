import pygame
import random
pygame.init()


# defines varaibles
width, height = 500,500
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
clock = pygame.time.Clock()
tiles = 10
click = 10

moves = []


win = pygame.display.set_mode((width , height))

# makes an array of square tiles for the window
game_board = [[0 for x in range(int(tiles))] for y in range(int(tiles))]


# draws the array of square tiles ontop of the window
def gameboard():
  for x in range(int(width/tiles)):
    for y in range(int(height/tiles)):
       rect = pygame.Rect(x*tiles, y*tiles, tiles, tiles)
       pygame.draw.rect(win, white, rect, -1)

      
      
snake_bods = []

class snake():
  
  # defines variables for the snake
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    self.up = True
    self.down = False
    self.right = False
    self.left = False
    self.move_count = 0
    self.rect = pygame.Rect(self.x*tiles, self.y*tiles, tiles, tiles)
    
  def move(self):
    
    # if self.up is true, -1 will be added to the y cordinate of the snake
    if self.up:
      self.y += -1
      self.rect = pygame.Rect(self.x*tiles, self.y*tiles, tiles, tiles)
      pygame.draw.rect(win, self.color, self.rect)
      # the x and y cordinates are added to an array
      moves.append([self.x, self.y])
      self.move_count +=1 
      
    # if self.down is true, +1 will be added to the y cordinate of the snake
    if self.down:
      self.y += 1
      self.rect = pygame.Rect(self.x*tiles, self.y*tiles, tiles, tiles)
      pygame.draw.rect(win, self.color, self.rect)
      # the x and y cordinates are added to an array
      moves.append([self.x, self.y])
      self.move_count += 1
      
    # if self.left is true, -1 will be added to the x cordinate of the snake
    if self.left:
      self.x += -1
      self.rect = pygame.Rect(self.x*tiles, self.y*tiles, tiles, tiles)
      pygame.draw.rect(win, self.color, self.rect)
      # the x and y cordinates are added to an array
      moves.append([self.x, self.y])
      self.move_count += 1
      
    # if self.right is true, +1 will be added to the y cordinate of the snake
    if self.right:
      self.x += 1
      self.rect = pygame.Rect(self.x*tiles, self.y*tiles, tiles, tiles)
      pygame.draw.rect(win, self.color, self.rect)
      # the x and y cordinates are added to an array
      moves.append([self.x, self.y])
      self.move_count += 1
      
      
  def append_bod(self):
    
    temp_num = len(snake_bods)
    # if the snake is going up, the snake body part needs to be appeneded below the head
    if self.up:
      bod = pygame.Rect(self.x*tiles, (self.y*tiles) +temp_num, tiles, tiles)
      pygame.draw.rect(win, red, bod)
      snake_bods.append(bod)
      
    # if the snake is going down, the snake body part needs to be appeneded ontop of the head
    elif self.down:
      bod = pygame.Rect(self.x*tiles, (self.y*tiles) -temp_num, tiles, tiles)
      pygame.draw.rect(win, red ,bod)
      snake_bods.append(bod)
      
    # if the snake is going to the left, the snake body part needs to be appeneded to the right of the head
    elif self.left:
      bod = pygame.Rect((self.x*tiles) +temp_num, (self.y*tiles), tiles, tiles)
      pygame.draw.rect(win, red, bod)
      snake_bods.append(bod)
      
    # if the snake is going to the right, the snake body part needs to be appeneded to the left of the head 
    elif self.right:
      bod = pygame.Rect((self.x*tiles) -temp_num, (self.y*tiles), tiles, tiles)
      pygame.draw.rect(win, red, bod)
      snake_bods.append(bod)
      
      
      
  def draw(self):
    bod_count = len(snake_bods)-1
    # for each square in the snake's body, the squares will be drawn to the cordinates of the last bod_count 
    # variable indexes in the array moves 
    for bod in range(bod_count):
      temp_x = moves[self.move_count - bod -1][0]
      temp_y = moves[self.move_count - bod- 1][1]
      pygame.draw.rect(win, red, (temp_x * tiles, temp_y * tiles, tiles, tiles))
  
  '''    
  def collide(self):
    start = len(moves)-1
    stop = len(snake_bods)
    
    for i in moves[start -1 : start- stop - 1: -1]:
      if self.x == i[0] and self.y == i[1]:
        print('true')
        run = False
  '''    
      
  
# initialize snake player       
snake = snake((int(width/tiles)/2),(int(height/tiles)/2),red)
  

  
apples = []      
class apple():
  
  def __init__(self, rand_x, rand_y):
    
    self.num = width/tiles -1 # the max x and y position the animal can be drawn
    self.rand_x = random.randint(0,self.num) # random x position between 0 and self.num
    self.rand_y = random.randint(0,self.num) # random y position between 0 and self.num
    
    
  def append_apple(self):
    # if there are no apple objects in the array, a new apple will be appended with a random x and y cord
    if len(apples) == 0:
      self.rand_x = random.randint(0,self.num)
      self.rand_y = random.randint(0,self.num)
      
      # if the snake's x and y cordinates are not equal to the random apple's cords then a new apple will be drawn
      if snake.x != self.rand_x or snake.y != self.rand_y:
        new = pygame.Rect(self.rand_x*tiles, self.rand_y*tiles, tiles, tiles)
        apples.append(new)
        
        
        
  # draws the apple onto the screen
  def draw(self,rand_x,rand_y):
    new = pygame.Rect(self.rand_x*tiles, self.rand_y*tiles, tiles, tiles)
    pygame.draw.rect(win, green, new)





# if the snakes x and y cordinates equal the apple's x and y cordinates, the apple array will be cleared and the append_bod function will be called
def eat():
    if snake.x == new.rand_x and snake.y == new.rand_y:
      apples.clear()
      snake.append_bod()


      
  
# initializes new apple
new = apple(0,0)

# calls all the necessary functions
def redraw_win():
  win.blit(win, (0,0))
  gameboard()
  snake.move()
  snake.draw()
  eat()
  new.append_apple()
  #snake.collide()
  new.draw(new.rand_x, new.rand_y)
  pygame.display.update()
  
run = True
while run:
  clock.tick(click)
  
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
  keys = pygame.key.get_pressed()
  
  # if the 
  if snake.x > width or snake.x < 0:
    run = False
    
  if snake.y > height or snake.y < 0:
    run = False
  
  start = len(moves)-1
  stop = len(snake_bods)
    
  for i in moves[start -1 : start- stop - 1: -1]:
    if snake.x == i[0] and snake.y == i[1]:
      print('true')
      run = False
    
  if keys[pygame.K_LEFT] and snake.right == False:
    snake.up = False
    snake.down = False
    snake.right = False
    snake.left = True
    
  if keys[pygame.K_RIGHT] and snake.left == False:
    snake.up = False
    snake.down = False
    snake.right = True
    snake.left = False
   
    
  
  if keys[pygame.K_UP] and snake.down == False:
    snake.up = True
    snake.down = False
    snake.right = False
    snake.left = False
    
    
    
  if keys[pygame.K_DOWN] and snake.up == False:
    snake.up = False
    snake.down = True
    snake.right = False
    snake.left = False
    
    
    
  redraw_win()
  win.fill(black)

