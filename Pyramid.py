pyramid_width = int(input("Enter Pyramid Width: "))
for i in range(0, pyramid_width):
    for j in range(0, pyramid_width-i):
        print(" ", end="")

    for k in range(0, 2 * i + 1):
        print("*", end="")
    print("")