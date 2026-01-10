# Define a class called Car
class Car:
    
    # Class variable (shared by all objects)
    model = 'Civic'
    
    # Constructor: runs when an object is created
    def __init__(self, color, type):
        self.color = color        # instance variable
        self.type = type          # instance variable
        self.started = False
        self.stopped = False
    
    # Method to start the car
    def start(self):
        print('Car Started')
        self.started = True
        self.stopped = False
    
    # Method to stop the car
    def stop(self):
        print('Car Stopped')
        self.stopped = True
        self.started = False


# -------- Creating Objects (Instances) --------

# Create first object of Car class
my_car1 = Car('blue', 'sedan')

# Create second object of Car class
my_car2 = Car('red', 'BMW')


# -------- Calling Class Methods Using Objects --------

# Start both cars
my_car1.start()
my_car2.start()


# -------- Accessing Object Properties --------

# Print color of each car
print(my_car1.color)
print(my_car2.color)

"""
Output:
Car Started
Car Started
blue
red
"""


# -------- Checking Class vs Object --------

# Print the class itself
print(Car)

# Print the object instance
print(my_car1)

"""
Output:
<class '__console__.Car'>        # This is the class
<__console__.Car object at 0x...>  # This is an object (instance) of the class
"""
# continued...