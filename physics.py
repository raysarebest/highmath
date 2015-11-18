import highmath

################################################################################
# Module Configuration
################################################################################

highmath.trigDeg = True

################################################################################
# Special Classes
################################################################################

class Angle:
    def __init__(self, size=0, degrees=True, *args, **kwargs):
        self.size = float(size)
        self.degrees = degrees
        
    def __str__(self):
        string = "{}".format(self.size)
        if self.degrees == True:
            string += "º"
        else:
            string += "rad"
        return string
    
    def vector_with_magnitude(self, magnitude):
        magnitude = float(magnitude)
        return Vector(self, magnitude)

class Vector:
    direction = Angle()
    magnitude = 0
    
    def __init__(self, magnitude, direction, *args, **kwargs):
        if direction is not Angle:
            print(direction)
            raise TypeError("Direction should be an Angle")
        else:
            self.direction = direction
            self.magnitude = float(magnitude)
    
    def __str__(self):
        return "{}, {}".format(self.magnitude, str(self.direction))
        
    def resolve(self):
        return (Vector(highmath.sin(self.direction.size) * self.magnitude, Angle(90)), Vector(highmath.cos(self.direction.size) * self.magnitude), Angle(0))
        
    def from_polar(x, y, *args, **kwargs):
        return Vector(highmath.sqrt(x.magnitude ** 2 + y.magnitude ** 2), Angle(highmath.atan2(y.direction.size, x.direction.size)))