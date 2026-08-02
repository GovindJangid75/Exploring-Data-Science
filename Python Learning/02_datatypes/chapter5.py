# Chapter 5 - Real Numbers (Floats) & Precision

# Precision example
ideal_temp = 95.5
current_temp = 95.4999999999
print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Difference temp: {ideal_temp - current_temp}")

# Reduced precision
current_temp = 95.49
print(f"Difference temp (reduced precision): {ideal_temp - current_temp}")

# Check float info from sys module
import sys
print(sys.float_info)

# Fractions
from fractions import Fraction
print(Fraction(1, 3))
print(Fraction(3, 7))

# Decimals
from decimal import Decimal as D
print(D('0.1') + D('0.2'))
print(0.1 + 0.2)  # Difference with float

# Complex numbers (just mention)
complex_num = 2 + 3j
print(f"Complex number example: {complex_num}")
# Complex number operations
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")
print(f"Conjugate: {complex_num.conjugate()}")