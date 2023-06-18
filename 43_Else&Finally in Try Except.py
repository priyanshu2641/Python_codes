file1=open("Priyanshu.txt")

try:
    file2=open("Pokemon.txt")

except Exception as line:
    print(line)
    print("File does not exists.")

# If else will run then Except Statement will not run and If Except statement runs then the Else statement will not run.
else:
    print("This will only run if Except statement does not run.")

# Finally is used to clean up the code. For eg., In the above code, we want to close file1
finally:
    print("It will run anyway")
    file1.close()

print("Priyanshu.txt is now closed")
