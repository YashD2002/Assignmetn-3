import math

number = float(input("Enter a number: "))

sqrt_result = math.sqrt(number)

if number > 0:
    log_result = math.log(number)
else:
    log_result = "undefined (logarithm is only defined for positive numbers)"

sine_result = math.sin(number)

print(f"\nResults for the number {number}:")
print(f"Square Root: {sqrt_result}")
print(f"Natural Logarithm: {log_result}")
print(f"Sine (in radians): {sine_result}")
