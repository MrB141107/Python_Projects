# Python code for a simulation of vehicles that eat food and avoid poison particles

# Import the necessary libraries
import pygame
import random
import math
import matplotlib.pyplot as plt 
import time
# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 540
screen_height = 540
# screen = pygame.display.set_mode((screen_width, screen_height))

# Set the clock
clock = pygame.time.Clock()

# Set the screen size
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_icon(pygame.image.load(r'C:\Users\MSHOME\Desktop\Newfolder\GeneticAlgorithm\p5\coc_logo.jpg'))
# Set the debug flag
debug = False
generation = 0
class Vehicle:

  def __init__(self, x, y,dna=None):
    global generation
    """
    Initializes a new instance of the Vehicle class.

    Args:
    x (int): The x-coordinate of the vehicle's starting position.
    y (int): The y-coordinate of the vehicle's starting position.
    """
    # Initialize the position, velocity, acceleration, radius, maxspeed, maxforce, health, and DNA of the vehicle
    self.position = pygame.math.Vector2(x, y)
    self.velocity = pygame.math.Vector2(0, -2)
    self.acceleration = pygame.math.Vector2(0, 0)
    self.r = 6
    self.maxspeed = 4
    self.maxforce = 0.2
    self.health = 0
    if dna != None:
      # aHealth.append(1)
      print("T")
      generation = generation + 1
      print(generation)
      show = True
      # while show:
      #   showtext(screen,"Generation: "+str(generation),(screen_width/2-180,screen_height/2),50)
      #   pygame.display.update()
      #   time.sleep(2)
      #   show = False
      
      # randomized DNA closely related to the parent to mtuation
      ro = random.uniform(-0.1, 0.1)
      if -0.1 < ro < -0.075:
        self.dna = [dna[0], dna[1], dna[2] + random.uniform(-5,5), dna[3] + random.uniform(-5, 5)]
      elif -0.075 < ro < -0.05:
        self.dna = [dna[0], dna[1] - random.uniform(-0.1, 0.1), dna[2], dna[3] - random.uniform(-5, 5)]
      elif -0.05 < ro < -0.025:
        self.dna = [dna[0], dna[1] - random.uniform(-0.1, 0.1), dna[2] - random.uniform(-5, 5), dna[3]]
      elif -0.025 < ro < 0:
        self.dna = [dna[0] + random.uniform(-0.1,0.1), dna[1], dna[2] - random.uniform(-5, 5), dna[3] - random.uniform(-5, 5)]
      elif 0 < ro < 0.025:
        self.dna = [dna[0] + random.uniform(-0.1, 0.1), dna[1], dna[2], dna[3] + random.uniform(-5, 5)]
      elif 0.025 < ro < 0.05:
        self.dna = [dna[0] + random.uniform(-0.1, 0.1), dna[1], dna[2] - random.uniform(-5, 5), dna[3]] 
      elif 0.05 < ro < 0.075:
        self.dna = [dna[0] + random.uniform(-0.1, 0.1), dna[1] + random.uniform(-0.1, 0.1), dna[2], dna[3]]
      else:
        self.dna = [dna[0], dna[1] + random.uniform(-0.1, 0.1), dna[2], dna[3]]
    else:
      self.dna = [random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(0, 150), random.uniform(0, 150)]

      # if -0.1 < ro < -0.05:
      #   self.dna = [dna[0], dna[1], dna[2], dna[3] + random.uniform(-5, 5)]
      # elif -0.05 < ro < 0:
      #   self.dna = [dna[0], dna[1] - random.uniform(-0.1, 0.1), dna[2], dna[3]]
      # elif 0 < ro < 0.05:
      #   self.dna = [dna[0] + random.uniform(-0.1, 0.1), dna[1], dna[2], dna[3]]
      # elif 0.05 < ro < 0.1:
      #   self.dna = [dna[0], dna[1], dna[2] + random.uniform(-5, 5), dna[3]]
    # else:
    #   self.dna = [random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(0, 150), random.uniform(0, 150)]
    

  def update(self):
    """
    Updates the vehicle's health, velocity, position, and acceleration.
    """
    # Update the health, velocity, position, and acceleration of the vehicle
    # self.health -= 0.003
    self.velocity += self.acceleration
    # Limit the velocity to the maximum speed
    if self.velocity.length() > self.maxspeed:
      self.velocity.scale_to_length(self.maxspeed)
    self.position += self.velocity
    self.acceleration *= 0

  def applyForce(self, force):
    """
    Applies a force to the acceleration of the vehicle.

    Args:
    force (Vector2): The force to apply to the acceleration of the vehicle.
    """
    # Apply a force to the acceleration of the vehicle
    self.acceleration += force

  def behaviors(self, good, bad):
    """
    Calculates the steering forces for eating good and bad particles.

    Args:
    good (list): A list of good particles.
    bad (list): A list of bad particles.
    """
    # Calculate the steering forces for eating good and bad particles
    steerG = self.eat(good, 0.3, self.dna[2])
    steerB = self.eat(bad, -0.75, self.dna[3])

    # Apply the DNA multipliers to the steering forces
    steerG *= self.dna[0]
    steerB *= self.dna[1]

    # Apply the steering forces to the acceleration of the vehicle
    self.applyForce(steerG)
    self.applyForce(steerB)

  def clone(self):
    """
    Clones the vehicle with a small probability.

    Returns:
    Vehicle: A new instance of the Vehicle class with the same position as the original vehicle.
    """
    # Clone the vehicle with a small probability
    if random.random() < 0.005 and self.health >= 1.6:
      return Vehicle(self.position.x, self.position.y,self.dna)
    elif 0.1 < random.random() <= 0.004 and self.health >= 1.5:
      return Vehicle(self.position.x, self.position.y,self.dna)
    elif 0.01 < random.random() < 0.003 and self.health >= 1.4:
      return Vehicle(self.position.x, self.position.y,self.dna)
    elif 0.005 < random.random() < 0.002 and self.health >= 1.3:
      return Vehicle(self.position.x, self.position.y,self.dna)
    elif random.random() < 0.001 and self.health >= 1.2:
      return Vehicle(self.position.x, self.position.y,self.dna)
    elif random.random() < 0.0001 and self.health >= 1.1:
      return Vehicle(self.position.x, self.position.y,self.dna)
    # elif 0.005 < random.random() < 0.003 and self.health > 1:
    #   return Vehicle(self.position.x, self.position.y,self.dna)
    # elif random.random() < 0.001 and self.health > 0.75:
    #   return Vehicle(self.position.x, self.position.y,self.dna)
    # elif random.random() < 0.0001 and self.health > 0.5:
    #   return Vehicle(self.position.x, self.position.y,self.dna)

  def eat(self, lst, nutrition, perception):
    """
    Finds the closest good or bad particle and eats it if it is within range.

    Args:
    lst (list): A list of particles to search for food.
    nutrition (float): The amount of nutrition to add to the vehicle's health when it eats a particle.
    perception (float): The maximum distance at which the vehicle can detect particles.

    Returns:
    Vector2: The steering force required to reach the closest particle.
    """
    # Find the closest good or bad particle and eat it if it is within range

    # set to a very large number infinity
    record = float("inf")

    # closest to none for now
    closest = None

    # loop through the list of particles backwards to remove them
    for i in range(len(lst)-1, -1, -1):

      # distance to particle
      d = self.position.distance_to(lst[i])

      # if the distance is less than the record and less than the perception
      if d < self.maxspeed:
        lst.pop(i)
        self.health += nutrition
      else:
        # perception for particular particle according to DNA and evolution 
        if d < record and d < perception:
          record = d
          closest = lst[i]


    # if there is a closest particle
    # seek it
    if closest is not None:
      return self.seek(closest)

    return pygame.math.Vector2(0, 0)

  def seek(self, target):
    """
    Seeks a target and returns the steering force required to reach it.

    Args:
    target (Vector2): The target to seek.

    Returns:
    Vector2: The steering force required to reach the target.
    """
    # Seek a target and return the steering force required to reach it
    desired = target - self.position
    desired.normalize()
    desired *= self.maxspeed

    steer = desired - self.velocity
    if steer.length() >= self.maxforce:
      steer.scale_to_length(self.maxforce)

    return steer

  def dead(self):
    """
    Checks if the vehicle is dead.

    Returns:
    bool: True if the vehicle is dead, False otherwise.
    """
    # Check if the vehicle is dead
    return self.health < -1

  def display(self):
    """
    Displays the vehicle on the screen.
    """
    # Calculate the angle of the vehicle's velocity vector
    angle = self.velocity.angle_to(pygame.math.Vector2(0, -1)) + math.pi / 2

    # Draw the vehicle on the screen
    try:
      pygame.draw.circle(screen, (255-255*self.health, 255), 255, 0), (int(self.position.x), int(self.position.y)), self.r
    except:
      pygame.draw.circle(screen, (255, 255, 0), (int(self.position.x), int(self.position.y)), self.r)

    # Draw the vehicle's debug information if the debug flag is set
  # def drawDebug(self, angle):
  #   """
  #   Draws the vehicle's debug information.

  #   Args:
  #   angle (float): The angle of the vehicle's velocity vector.
  #   """
  #   # Set the scale of the debug vectors
  #   scale = 25

  #   # Draw the velocity vector
  #   vel = self.velocity.copy()
  #   vel.normalize()
  #   vel *= scale
  #   drawVector(self.position, vel, (0, 255, 0))

  #   # Draw the acceleration vector
  #   acc = self.acceleration.copy()
  #   acc.normalize()
  #   acc *= scale
  #   drawVector(self.position, acc, (0, 0, 255))

  #   # Draw the desired velocity vector
  #   desired = self.velocity.copy()
  #   desired.normalize()
  #   desired *= scale * 2
  #   drawVector(self.position, desired, (255, 0, 0))

  #   # Draw the heading vector
  #   heading = pygame.math.Vector2(0, -1)
  #   heading.rotate_ip(angle)
  #   heading *= scale
  #   drawVector(self.position, heading, (0, 255, 255))

  #   # Draw the perception radius
  #   pygame.draw.circle(screen, (255, 255, 0), (int(self.position.x), int(self.position.y)), int(self.dna[2]))

  #   # Draw the food and poison perception radius
  #   pygame.draw.circle(screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), int(self.dna[2] * self.dna[0]))
  #   pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), int(self.dna[3] * self.dna[1]))

def drawVector(position, vector, color):
  """
  Draws a vector on the screen.

  Args:
  position (Vector2): The starting position of the vector.
  vector (Vector2): The vector to draw.
  color (tuple): The color of the vector.
  """
  # Draw a line representing the vector
  pygame.draw.line(screen, color, (int(position.x), int(position.y)), (int(position.x + vector.x), int(position.y + vector.y)), 1)

def drawVector(position, vector, color):
  # Draw a vector on the screen
  pygame.draw.line(screen, color, (position.x, position.y), (position.x + vector.x, position.y + vector.y), 1)

def addFood():
  # Add a food particle with a small probability
  if random.random() < 0.4:
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    food.append(pygame.math.Vector2(x, y))

def addPoison():
  # Add a poison particle with a small probability
  if random.random() < 0.4:
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    poison.append(pygame.math.Vector2(x, y))

def drawFood():
  # Draw the food particles on the screen
  for f in food:
    pygame.draw.circle(screen, (0, 255, 0), (int(f.x), int(f.y)), 4)

def drawPoison():
  # Draw the poison particles on the screen
  for p in poison:
    pygame.draw.circle(screen, (255, 0, 0), (int(p.x), int(p.y)), 4)

def drawVehicles():
  # Draw the vehicles on the screen
  for v in vehicles:
    # v.boundaries()
    v.behaviors(food, poison)
    v.update()
    v.display()

    newVehicle = v.clone()
    if newVehicle is not None:
      vehicles.append(newVehicle)

    if v.dead():
      x = v.position.x
      y = v.position.y
      food.append(pygame.math.Vector2(x, y))
      vehicles.remove(v)

aHealth = []
def averageHealth(aHealth):
  # Calculate the average health of the vehicles
  total = 0
  for v in vehicles:
    total += v.health
    average_Health = total / len(vehicles)
    # print(v.health)
    aHealth.append(average_Health)
  return average_Health

def appearText():
  # Display the text on the screen
  text = "Average Health: " + str(100*averageHealth(aHealth))
  pygame.display.set_caption(text)

def drawRangeCircles(vehicle):
  # Draw the hollow range circles around the vehicle
  pygame.draw.circle(screen, (0, 255, 0), (int(vehicle.position.x), int(vehicle.position.y)), int(vehicle.dna[2]), 1)
  pygame.draw.circle(screen, (255, 0, 0), (int(vehicle.position.x), int(vehicle.position.y)), int(vehicle.dna[3]), 1)
  
def DrawAttractionLines(vehicle):
  pygame.draw.line(screen, (0, 255, 0), (int(vehicle.position.x), int(vehicle.position.y)), (int(vehicle.position.x + 40*vehicle.dna[0]), int(vehicle.position.y + 40*vehicle.dna[0])), 2)
  pygame.draw.line(screen, (255, 0, 0), (int(vehicle.position.x), int(vehicle.position.y)), (int(vehicle.position.x - 40*vehicle.dna[1]), int(vehicle.position.y - 40*vehicle.dna[1])), 2)
def showtext(screen,text,location,fontsize):
    font = pygame.font.SysFont("Copperplate gothic", fontsize, True, False)
    textObject = font.render(text, 0, pygame.Color('White'))
    location1 = pygame.Rect(location, location)
    # textLocation = p.Rect(0, 0, screen_width, screen_height).move(screen_width / 2 - textObject.get_width() / 2, screen_height / 2 - textObject.get_height() / 2)
    # white = p.Color("black")
    # screen.blit(white,p.rect(textLocation,textLocation,200,200))
    screen.blit(textObject, location1)



# Initialize the variables
vehicles = []
food = []
poison = []
debug = False

# Create the vehicles
for i in range(50):
  x = random.randint(0, screen_width)
  y = random.randint(0, screen_height)
  vehicles.append(Vehicle(x, y))

# Create the food particles
for i in range(100):
  x = random.randint(0, screen_width)
  y = random.randint(0, screen_height)
  food.append(pygame.math.Vector2(x, y))

# Create the poison particles
for i in range(100):
  x = random.randint(0, screen_width)
  y = random.randint(0, screen_height)
  poison.append(pygame.math.Vector2(x, y))

# Start the game loop
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_d:
        debug = not debug
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
      vehicles.append(Vehicle(x, y))

  # Clear the screen
  screen.fill((51, 51, 51))

  # Add food and poison particles
  addFood()
  addPoison()

  # Draw the food and poison particles
  drawFood()
  drawPoison()
  appearText()
  if debug:
    for v in vehicles:
      drawRangeCircles(v)
      DrawAttractionLines(v)

  # Draw the vehicles
  drawVehicles()
  # for v in vehicles:
  #   drawRangeCircles(v)
  #   DrawAttractionLines(v)
  # Update the display
  pygame.display.flip()

  # Set the frame rate
  clock.tick(30)
  # importing the required module 
import matplotlib.pyplot as plt
# Define the x-axis values
x = range(len(aHealth))

# Plot the graph
plt.plot(x, aHealth)

# Add labels and title
plt.xlabel('Generation')
plt.ylabel('Average Health')
plt.title('Average Health per Generation')

# Show the graph
plt.show()
# Quit Pygame
pygame.quit()
# def nextGeneration():
  # """
  # Creates the next generation of vehicles.
  # """
  # global vehicles

  # # Create a new list of vehicles for the next generation
  # newVehicles = []

  # # Calculate the total health of all vehicles in the current generation
  # totalHealth = 0
  # for v in vehicles:
  #   totalHealth += v.health

  # # For each vehicle in the current generation
  # for i in range(len(vehicles)):
  #   # Calculate the fitness of the vehicle as its health divided by the total health of all vehicles
  #   fitness = vehicles[i].health / totalHealth

  #   # Select two parent vehicles based on their fitness
  #   parentA = pickParent(vehicles, fitness)
  #   parentB = pickParent(vehicles, fitness)

  #   # Create a new vehicle by crossing over the DNA of the two parent vehicles
  #   child = parentA.crossover(parentB)

   

  #   # Add the new vehicle to the list of vehicles for the next generation
  #   newVehicles.append(child)

  # # Replace the current generation with the list of vehicles for the next generation
  # vehicles = newVehicles

# def pickParent(vehicles, fitness):
#   """
#   Picks a parent vehicle based on its fitness.

#   Args:
#   vehicles (list): The list of vehicles to choose from.
#   fitness (float): The fitness of the vehicles.

#   Returns:
#   Vehicle: The parent vehicle.
#   """
#   # Pick a random number between 0 and 1
#   r = random.uniform(0, 1)

#   # Loop through the vehicles and calculate the cumulative fitness
#   cumulativeFitness = 0
#   for v in vehicles:
#     cumulativeFitness += v.health / fitness

#     # If the cumulative fitness is greater than the random number, return the vehicle
#     if cumulativeFitness > r:
#       return v

#   # If no vehicle was selected, return the last vehicle in the list
#   return vehicles[-1]
