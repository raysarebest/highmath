from fractions import Fraction

################################################################################
# Special Classes
################################################################################

class Point:
    """Represents a cartographical point"""
    def __init__(self, x=0, y=0, z=0, dimensions=2):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.dimensions = dimensions
            
    def __str__(self):
        """Converts a Point instance to a string"""
        format_string = str()
        if self.dimensions == 3:
            format_string = "({x}, {y}, {z})"
        elif self.dimensions == 2:
            format_string =  "({x}, {y})"
        elif self.dimensions == 1:
            format_string = "({x})"
        return format_string.format(self)
        
    def as_tuple(self):
        """Generates a tuple representation of a point instance"""
        if self.dimensions == 1:
            return (self.x)
        elif self.dimensions == 2:
            return (self.x, self.y)
        elif self.dimensions == 3:
            return (self.x, self.y, self.z)
        else:
            #This should never happen, but just in case...
            return tuple()
            
    def distance_from_point(self, otherPoint):
        """Finds the distance between 2 cartographical points"""
        return (((float(otherPoint.x) - float(self.x)) ** 2) + ((float(otherPoint.y) - float(self.y)) ** 2) + ((float(otherPoint.z) - float(self.z)) ** 2)) ** .5
        
    # TODO: Add support for 3D versions of the 2D methods
        
################################################################################
# Global Functions
################################################################################

def slope(x1, x2, y1, y2):
    """Generates a slope from 2 points. Returns None if slope is undefined (perfectly vertical)"""
    try:
        return ((float(y2) - float(y1)) / (float(x2) - float(x1)))
    except ZeroDivisionError as error:
        return None

def perpendicular(sl):
    """Generates a slope perpendicular to a given slope"""
    fract = Fraction(sl)
    new = Fraction(numerator=fract.denominator, denominator=fract.numerator)
    return -(float(new.limit_denominator()))
    
def distance(x1, y1, x2, y2):
    """Generates the distance between 2 points"""
    return (((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)) ** .5

def compound_interest(principal, monthly, compounds_per_year, time, rate):
    """Calculates the compound interest earned over a given period of time"""
    return float(principal) * ((1 + (float(rate) / 100)) / float(compounds_per_year)) ** (float(compounds_per_year) * float(time))
    
def quad(a, b, c, type="tuple"):
    """Calculates the value of x in a quadratic equation where the coefficients are the passed-in a, b, and c. Can return a tuple of the answers, or a pretty string, depending on the type parameter"""
    a = float(a)
    b = float(b)
    c = float(c)
    answer =  (((-b + ((b ** 2) - (4 * a * c)) ** .5) / (2 * a)), ((-b - ((b ** 2) - (4 * a * c)) ** .5) / (2 * a)))
    if type == "str" or type == "string":
        return str((str(Fraction(answer[0]).limit_denominator()), str(Fraction(answer[1]).limit_denominator()))).replace("'", str())
    else:
        return answer