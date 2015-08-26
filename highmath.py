from fractions import Fraction

################################################################################
# Special Classes
################################################################################

class Point:
    """Represents a cartographical point"""
    def __init__(self, x, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z
        if z is None and y is None:
            self.dimensions = 1
        elif z is None:
            self.dimensions = 2
        else:
            self.dimensions = 3
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
        
################################################################################
# Global Functions
################################################################################

def slope(x1, x2, y1, y2):
    """Generates a slope from 2 points"""
    try:
        return ((float(y2) - float(y1)) / (float(x2) - float(x1)))
    except ZeroDivisionError as error:
        return error
    except:
        print("Only use numbers in the slope formula")

def perpendicular(sl):
    """Generates a slope perpendicular to a given slope"""
    fract = Fraction(sl)
    new = Fraction(numerator=fract.denominator, denominator=fract.numerator)
    return -(float(new.limit_denominator()))
    
def distance(x1, y1, x2, y2):
    """Generates the distance between 2 points"""
    try:
        return (((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)) ** .5
    except:
        print("Only use numbers in the distance formula")

def compound_interest(principal=0, monthly=0, compounds_per_year=0, time=0, rate=0):
    """Calculates the compound interest earned over a given period of time"""
    return principal * ((1 + (rate / 100)) / compounds_per_year) ** (compounds_per_year * time)
    
def quad(a, b, c):
    """Calculates the value of x in a quadratic equation where the coefficients are the passed-in a, b, and c"""
    a = float(a)
    b = float(b)
    c = float(c)
    return (((-b + ((b**2) - (4 * a * c))**.5) / (2 * a)), ((-b - ((b**2) - (4 * a * c))**.5) / (2 * a)))

################################################################################
# Testing
################################################################################

if __name__ == "__main__":
    x, y = quad(1, 0, -9)
    #Should print "x = 3.0, -3.0"
    print("x = {}, {}".format(x, y))