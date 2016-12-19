file = open("list.txt", "w")

for n in range(1,11):
    text = input("What would you like to write? ")
    file.write(str(n) + ". " +text + "\n")
    
file.close()