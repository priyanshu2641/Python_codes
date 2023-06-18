import os
print(dir(os))             #diiferent directories that we have in OS Module
print(os.getcwd())         #prints current working directory
# a=open("Priyanshu.txt")
# a.close()
# os.chdir("D:/")            #changes the directory
# print(os.getcwd())
print(os.listdir())        #gives the list of all the directories present within the given directories
# print(os.listdir("C://"))
# os.mkdir("Priyanshu")      #makes folder in the current working directory
# os.makedirs("Cricket/Virat Kohli")           #makes subfolder along with folder
# os.rename("Priyanshu.txt","CoderPriyanshu.txt")                #renames file
print(os.environ.get('Path'))
print(os.path.join("D:/","CoderPriyanshu.txt"))             #joins

print(os.path.exists("C://"))                 #tells whether the path exists or not
print(os.path.isfile("C://Program File"))
