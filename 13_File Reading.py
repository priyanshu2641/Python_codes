"""
"r"=Open file for reading-default
"w"=Open file for writing
"a"=Add more content to a file
"x"=Creates file if not exists
"t"=text mode-default
"b"=binary mode
"+"=Read and Write
"""
# File reading
a=open("CoderPriyanshu.txt")                   #opening the file. It will open in read mode if we had not specified anything.
data=a.read()
print(data)
a.close()

a=open("CoderPriyanshu.txt","rb")             #binary mode
data=a.read()
print(data)
a.close()

a=open("CoderPriyanshu.txt","rt")             #text mode
data=a.read()
print(data)
a.close()

# For printing few characters only.
a=open("CoderPriyanshu.txt")
data=a.read(11)
print(data)
data=a.read(16)            #It will print next 16 characters.
print(data)
a.close()

# Reading line by line
a=open("CoderPriyanshu.txt")
for line in a:
    print(line)
a.close()

a=open("CoderPriyanshu.txt")
print(a.readline())
print(a.readline())
print(a.readline())
a.close()


a=open("CoderPriyanshu.txt")                #produces a list
print(a.readlines())
a.close()