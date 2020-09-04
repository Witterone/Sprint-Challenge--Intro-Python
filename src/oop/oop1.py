# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    def __init__(self):
        pass
        

# this class inherits from Vehicle
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# This class inherits from FlightVehicle which inherits from Vehicle
class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

# This class inherits from FlightVehicle which inherits from Vehicle
class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
        
# This class inherits from Vehicle
class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass
        
# This class inherits from GroundVehicle which inherits from Vehicle
class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass
        
        
# This class inherits from GroundVehicle which inherits from Vehicle        
class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass
        
    