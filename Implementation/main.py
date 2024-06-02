# a simple example
import Calc

input01 = int(input("Enter the 1st integer: "))
input02 = int(input("Enter the 2nd integer: "))
calc01 = Calc.Calculator(input01, input02)

print(calc01.plus())
print(calc01.minus())
print(calc01.multiply())
print(calc01.divide())
