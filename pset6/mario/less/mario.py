from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n >= 1 and n <= 8:
        break

for i in range(n):
    for j in range(n):
        if i + j >= n - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()

# ANOTHER OPTIONS

# for i in range(n):
#   for j in range(n):
#       print("#" if i + j >= n - 1 else " ", end="")
#   print()

# for i in range (n):
#    print((n - 1 - i) * " ", end="")
#    print((i + 1) * "#")
