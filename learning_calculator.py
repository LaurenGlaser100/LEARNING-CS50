"""
x = float(input("What is x? "))
y = float(input("What is y? "))

z = int(x)+ int(y)
print(z) # not as good, look below after adding int to x and y variables
print(x + y)


#want to round now
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)
print("f{z:,}")     #  :,  adds comma into 1,000 to make it more readable using f string

z = round(x/y, 2)  # comma 2 adds amount of digits to round to (2 is hundreths)
print(f"{z:.2f}")  #adding colon .2f, specifies how many digits to print if dont want to add 2 in above line
"""
#how to square smth using function defining

def main():
    x =int(input("What is x? "))
    print("x squared is", square(x))

def square(n):  #n is thing for number, just what i am using
    return(f"{n * n:,}")  #alternatives for squaring: n ** 2 where two asterisks make second number the exponent also  pow(n, 2) where 2 is exponent, n is number

#return function is like print, but it gives yoou straight up values for what returning

main() #must actually call the main function to run, without this, you are just defining functions

#notes for terminal commands:
"""
ls: list files in current folder
cp: copy file from one place
mv: move file or rename it, putting cd folder, then in "folder/ $" hello.py ..  will move that file out of the folder
rm: remove delete file
mkdir: make a directory
cd: change directories from folders
rmdir: remove directory
clear: clears terminal window to keep tidy!
"""