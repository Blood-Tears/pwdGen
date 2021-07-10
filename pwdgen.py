import random
import string

directory = input("Welcome! First, type down the path to where the files will be created: ")
app = input("Please enter the name of the platform: ")
username = input("Please enter your username: ")
addrs = input("Enter the Email address: ") 
#----------------------------Password---------------------------
lenght = int(input("How many characters would you like in your password: "))
l = string.ascii_lowercase
u = string.ascii_uppercase
p = string.punctuation
d = string.digits
chars = l+u+p+d
pwd = "".join((random.choice(chars) for i in range(lenght)))

#----------------------------File Handling----------------------
file = open(directory+app+".txt", "a")
file.write("Platform: "+app+"\n"
"Username: "+username+"\n"
"Address: "+addrs+"\n"
"Password: "+pwd+"\n"
)
file.close()

print("===================================================================")
print("Alright! we have saved all of your information in "+app+".txt")
file = open(directory+app+".txt", "r")
print(file.read())
print("===================================================================")
