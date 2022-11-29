from __future__ import annotations


class Fraction:

    def __init__(self: Fraction, numerator: float, denominator: float) -> None:
        self.numerator = numerator
        self.denominator = denominator
        
        
    def __str__(self: Fraction) -> str:
        
        return f"{self.numerator}/{self.denominator}"
    
    
    def __add__(self: Fraction, other: Fraction) -> Fraction:
        
        if self.denominator == other.denominator:
            # trivial case
            
            return Fraction(self.numerator + other.numerator, self.denominator)

        # finding gcd of self.denominator and other.denominator
        denominator = gcd(self.denominator, other.denominator)
        
        # Denominator of final
        # fraction obtained finding
        # LCM of self.denominator and other.denominator
        # LCM * GCD = a * b
        denominator = (self.denominator * self.denominator) / denominator
        
        numerator = (self.numerator * (denominator / self.denominator) +
                     other.numerator * (denominator / other.denominator))
        
        result_fraction = Fraction(numerator, denominator)
        
        return result_fraction
    
    
    def __sub__(self: Fraction, other: Fraction) -> Fraction:
        
        if self.denominator == other.denominator:
            # trivial case
            
            return Fraction(self.numerator - other.numerator, self.denominator)

        # finding gcd of self.denominator and other.denominator
        denominator = gcd(self.denominator, other.denominator)
        
        # Denominator of final
        # fraction obtained finding
        # LCM of self.denominator and other.denominator
        # LCM * GCD = a * b
        denominator = (self.denominator * self.denominator) / denominator
        
        numerator = (self.numerator * (denominator / self.denominator) -
                     other.numerator * (denominator / other.denominator))
        
        result_fraction = Fraction(numerator, denominator)
        
        return result_fraction
    
    
    def inverse(self: Fraction) -> Fraction:
        
        return Fraction(self.denominator, self.numerator)
        
        
def gcd(nr1, nr2):
    if nr1 == 0:
        
        return nr2    

    return gcd(nr2 % nr1, nr1)

# function to convert the obtained fraction
# into its simplest form
def lowest(fraction: Fraction):
    common_factor = gcd(fraction.numerator, fraction.denominator)
    
    numerator = int(fraction.numerator / common_factor)
    denominator = int(fraction.denominator / common_factor)
    
    return Fraction(numerator, denominator)

if __name__ == '__main__':
    
    fraction1 = Fraction(2, 3)
    fraction2 = Fraction(4, 3)
    fraction3 = Fraction(2, 15)
    fraction4 = Fraction(4, 3)

    print(fraction1)
    print(fraction2)
    print(fraction3)
    print(fraction4)
    
    print("Add")
    print(f"Original: {fraction1 + fraction2}")
    print(f"Reduced: {lowest(fraction1 + fraction2)}")
    print(f"Original: {fraction3 + fraction4}")
    print(f"Reduced: {lowest(fraction3 + fraction4)}")
    print()
    
    print("Sub")
    print(f"Original: {fraction1 - fraction2}")
    print(f"Original: {fraction3 - fraction4}")
    print()
    
    print(f"Inverse of {fraction1} is {fraction1.inverse()}")
