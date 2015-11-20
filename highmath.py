"""This is your method of passing Pre-Calculus"""
import math
from fractions import Fraction

################################################################################
# Global Constants
################################################################################

nan = float("nan")
NaN = nan

################################################################################
# Configuration Variables
################################################################################

trigDeg = False

################################################################################
# Special Classes
################################################################################

class Point:
    """Represents a cartographical point"""
    def __init__(self, x, y=0, z=0, dimensions=2, *args, **kwargs):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.dimensions = dimensions
            
    def __str__(self):
        """Converts a Point instance to a string"""
        if self.dimensions == 3:
            return "({}, {}, {})".format(self.x, self.y, self.z)
        elif self.dimensions == 2:
            return "({}, {})".format(self.x, self.y)
        elif self.dimensions == 1:
            return "({})".format(self.x)
        else:
            return str()
        
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
        return sqrt(((float(otherPoint.x) - float(self.x)) ** 2) + ((float(otherPoint.y) - float(self.y)) ** 2) + ((float(otherPoint.z) - float(self.z)) ** 2))
        
    # TODO: Add support for 3D versions of the 2D methods
    
    def slope_with_point(self, otherPoint, dimensions=2):
        """Generates a slope from 2 points. Returns NaN if slope is undefined (perfectly vertical)."""
        if dimensions == 2:
            try:
                return ((float(otherPoint.y) - float(self.y)) / (float(otherPoint.x) - float(self.x)))
            except ZeroDivisionError as error:
                return nan
        else:
            print("Not 2")
            return nan
            
    def midpoint_with_point(self, otherPoint):
        return Point((self.x + otherPoint.x) / 2, (self.y + otherPoint.y) / 2, (self.z + otherPoint.z) / 2, math.ceil((self.dimensions + otherPoint.dimensions) / 2))
        
################################################################################
# Global Functions
################################################################################

def slope(x1, x2, y1, y2):
    """Generates a slope from 2 points. Returns NaN if slope is undefined (perfectly vertical)"""
    try:
        return ((float(y2) - float(y1)) / (float(x2) - float(x1)))
    except ZeroDivisionError as error:
        return nan

def perpendicular(sl):
    """Generates a slope perpendicular to a given slope"""
    fract = Fraction(sl)
    new = Fraction(numerator=fract.denominator, denominator=fract.numerator)
    return -(float(new.limit_denominator()))
    
def distance(x1, y1, x2, y2):
    """Generates the distance between 2 points"""
    return sqrt((((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)))

def compound_interest(principal, rate, compounds_per_year, time):
    """Calculates the compound interest earned over a given period of time"""
    principal, rate, compounds_per_year, time = float(principal), float(rate), float(compounds_per_year), float(time)
    return principal * ((1 + ((rate / 100) / compounds_per_year)) ** (compounds_per_year * time))
    
def quad(a, b, c, type="tuple"):
    """Calculates the value of x in a quadratic equation where the coefficients are the passed-in a, b, and c. Can return a tuple of the answers, or a pretty string, depending on the type parameter"""
    a, b, c = float(a), float(b), float(c)
    answer =  (((-b + ((b ** 2) - (4 * a * c)) ** .5) / (2 * a)), ((-b - ((b ** 2) - (4 * a * c)) ** .5) / (2 * a)))
    if type == "str" or type == "string":
        return str((str(Fraction(answer[0]).limit_denominator()), str(Fraction(answer[1]).limit_denominator()))).replace("'", str())
    else:
        return answer

def sqrt(number):
    """Calculates a square root more nicely than using math.sqrt or ** .5 in your source"""
    return root(number, 2)
    
def root(number, index):
    """Calculates the number to the specified root"""
    return float(number) ** (1 / float(index))
    
def imaginary_power(power, num=False):
    """Returns a string of the proper value of i raised to the passed-in power"""
    index = int(power) % 4
    if num:
        return [1j, -1, -1j, 1][index]
    else:
        return ["i", "-1", "-i", "1"][index]
    
def to_fraction(number, format="fract", string=False):
    """Turns an ordinary float to a Fraction, and optionally turns it into a string"""
    fraction = Fraction(number).limit_denominator()
    if format == "str" or format == "string" or string:
        return str(fraction)
    else:
        return fraction
        
def arclen(angle, radius, rad=False):
    """Calculates the size of an arc of a circle"""
    if rad:
        angle = math.degrees(angle)
    return (angle / 360) * (2 * math.pi * radius)

def sector(angle, radius, rad=False):
    """Finds the area of a sector of a circle"""
    if rad:
        angle = math.degrees(angle)
    return (angle / 360) * (math.pi * (radius ** 2))
    
def heron(a, b, c):
    """Calculates the area of a triangle given the length of each side"""
    a, b, c = float(a), float(b), float(c)
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))
    
def segment(angle, radius, rad=False):
    """Calculates the area of a segment of a circle based on the radius and the given angle"""
    if rad:
        angle = math.degrees(angle)
    # The weird math here calculates the area of a triangle given 2 sides and an angle
    return sector(angle, radius, rad) - ((1/2) * radius * radius * sin(angle, True))

################################################################################
# Trigonometric Functions
################################################################################

# Fun fact: The unit of the trigonometric functions is on the parameter, and not the output

def acos(x, deg=None, **kwargs):
    """Computes the arc cosine of the input, in either degrees or radians"""
    x = float(x)
    if deg or (trigDeg and deg is None):
        x = math.radians(x)
    return math.acos(x)
    
def asin(x, deg=None, **kwargs):
    """Computes the arc sine of the input, in either degrees or radians"""
    x = float(x)
    if deg or (trigDeg and deg is None):
        x = math.radians(x)
    return math.acos(x)
    
def atan(x, deg=None, **kwargs):
    """Computes the arc tangent of the input, in either degrees or radians"""
    x = float(x)
    if deg or (trigDeg and deg is None):
        x = math.radians(x)
    return math.atan(x)
    
def atan2(y, x, deg=None, **kwargs):
    """Computes the arc tangent of y/x, in either degrees or radians. Unlike atan(y/x), the signs of both x and y are considered."""
    x, y = float(x), float(y)
    if deg or (trigDeg and deg is None):
        x, y = math.radians(x), math.radians(y)
    return math.atan2(y, x)
    
def cos(x, deg=None, **kwargs):
    """Computes the cosine of x in either degrees or radians"""
    x = float(x)
    if deg or (trigDeg and deg is None):
        x = math.radians(x)
    return math.cos(x)
    
def sin(x, deg=None, **kwargs):
    """Computes the sine of x in either degrees or radians"""
    x = float(x)
    if deg or (trigDeg and deg is None):
        x = math.radians(x)
    return math.sin(x)
    
def tan(x, deg=None, **kwargs):
    """Computes the tangent of x in either degrees or radians"""
    x = float(x)
    if deg or (trigDeg and deg is None):
        x = math.radians(x)
    return math.tan(x)