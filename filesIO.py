myfile = open("test.txt", "a")

#print(myfile.read())
myfile.write("\nThe name of my country is Nigeria")
myfile.close()

myfile = open("test.txt", "r")
print(myfile.read())