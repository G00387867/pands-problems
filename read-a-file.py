# Adam

with open("myfile.txt", "a") as f:
    print(f.tell())
    f.write("\nHello, from the line!")
    print(f.tell())