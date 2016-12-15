file = open("list.txt", "w")

lines = 0

while lines < 10:
    text = input("What would you like to write? ")
    file.write(text + "\n")
    lines += 1
    
file.close()