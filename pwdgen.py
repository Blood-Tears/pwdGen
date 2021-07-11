import random
import string

path = input("Welcome! First, type down the path to the file: ")
app = input("Please enter the name of the platform: ")
username = input("Please enter your username: ")
addrs = input("Enter your Email address: ")
#----------------------------Password---------------------------
length = int(input("How many characters would you like in your password: "))
l = string.ascii_lowercase
u = string.ascii_uppercase
p = string.punctuation
d = string.digits
chars = l+u+p+d
pwd = "".join((random.choice(chars) for i in range(length)))

#----------------------------File Handling----------------------
file = open(path + "/" + app + ".txt", "a")
file.write("Platform: " + app + "\n"
"Username: "+username+"\n"
"Address: "+addrs+"\n"
"Password: "+pwd+"\n"
)
file.close()

print("===================================================================")
print("Alright! We have saved all of your information in " + app + ".txt \n")                                                                       
print("Platform: " + app + "\n"
"Username: "+username+"\n"
"Address: "+addrs+"\n"
"Password: "+pwd)
print("===================================================================")
