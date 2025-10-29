#simple_interest.py
#Program to calculate simple interest
import sys

def calculate_simple_interest(principal, rate, time):
    """"Calculate simple interest given principal, rate, time."""
    return (principal * rate * time) /100

if __name__ == "main":
    print("=== Simple Interest Calculator===")
try:
        if len(sys.argv) == 4:
        # Case 1: Arguments passed (for jenkins or CLI)
            p = float(sys.argv[1])
            r = float(sys.argv[2])
            t = float(sys.argv[3])
        else:
        # Case 2: No arguments passed (for console use)    
            p = float(input("Enter the principal amount: "))
            r = float(input("Enter the rate of the interest (%): "))
            t = float(input("Enter the  time (in years): "))
        print("===Program parameters ===")
        print("Principal Amount :", p)
        print("Rate of Interest :", r)
        print("Time in years :", t)
except ValueError:
        print("Invalid input! Please enter numeric values. ")