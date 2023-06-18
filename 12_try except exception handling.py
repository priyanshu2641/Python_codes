print("Enter the first No.=")
a=input()
print("Enter the second No.=")
b=input()
try:
    print("Sum=",int(a)+int(b))
except Exception as line:
    print(line)

print("We want to print this line even if the error occurs.")