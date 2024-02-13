# a simple example
import Calc

input01 = int(input("Enter the 1st integer: "))
input02 = int(input("Enter the 2nd integer: "))
calc01 = Calc.Calculator(input01, input02)

calc01.plus()
calc01.minus()
calc01.multiply()
calc01.divide()
