a=open("Priyanshu.txt","w")
a.write("My name is Priyanshu Chand.\nI like Cricket a lot. It gives me a sense of joy that no feeling in this world can ever give.\n")
a.close()

a=open("Priyanshu.txt","w")
number=a.write("My name is Priyanshu Chand.\nI like Cricket a lot. It gives me a sense of joy that no feeling in this world can ever give.\n")
print(number)
a.close()


a=open("Priyanshu.txt","a")
a.write("I also like sneakers a lot. I want to have a very big collection of them in future.\nRecently I have developed interest in Astrophysics and Cosmology also. These topics have fantasized me a lot from childhood.")
a.close()

a=open("Priyanshu.txt","r+")              #Handles read and write both
data=a.read()
print(data)
a.write("\nThank You!")
a.close()

# Question
a=int(input("Enter n: "))
b=int(input("Enter 1 or 0: "))
if b==1:
    i=0
    while(i<a):
        print((i+1)*"*")
        i=i+1
else:
    i=0
    while (i < a):
        print((a-(i)) * "*")
        i = i + 1

