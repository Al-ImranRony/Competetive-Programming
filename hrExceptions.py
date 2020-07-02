import sys

# sys.stdin  = open("input.txt", "r")
# sys.stdout  = open("output.txt", "w")

s = input().strip()
try:
    print(int(s))
except ValueError:
    print("Bad String")

# Asking for ser input untill a valid integer 
# while True:
#     try:
#         x = int(input("Enter anumber: "))
#         break
#     except ValueError:
#         print("Sorry ! Not a valid number. Try again...")
