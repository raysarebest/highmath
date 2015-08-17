from fractions import Fraction
def slope(x1, x2, y1, y2):
    """Generates a slope from 2 point"""
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
    return -(float(new))