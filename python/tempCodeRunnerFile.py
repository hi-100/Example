for i in range(1, n):
    # Left numbers
    for j in range(1, i+1):
        print(j, end="")
    # Spaces
    for j in range(2*(n-i)):
        print(" ", end="")
    # Right numbers
    for j in range(1, i+1):
        print(j, end="")
    print()