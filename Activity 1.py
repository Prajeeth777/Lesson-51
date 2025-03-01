with open("StephCurry.txt","a") as f:
      f.write("\n Hellon I am Penguin and I am 15 years old")
f.close()

file=open("StephCurry.txt","r")
data=file.readlines()
for line in data:
    word=line.split()
    print(word)

file.close()
