import random
import string

Num_Char = input("How many characters:  ")
Type_Random = input("All or just letters and numbers:  ")

if Type_Random == "All":
    for i in range(int(Num_Char)):
        print(random.choice(string.printable))
else:
    Num_Char = int(Num_Char) / 2
    for i in range(int(Num_Char)):
        print(random.choice(string.ascii_letters))
        print(random.choice(string.digits))