"""
name = input("What's your name? ")
print("hello, " + name)
print("hello,", name) #when using commas, it automatically implements an extra space
"""
 #anything between three quotes is comment
"""

#\n means new line

#other ways to write it
print("hello, ", end="")  #instead of new line for print, takes return away
print(name)
print("hello, \"friend\"")

print(f"hello, {name}")     #put f at beginning of string to format in special way, code realizes smth special

name = name.capitalize() #capitalizes their name (only first letter)
name = name.title()     #capitalizes every first letter of word
name = name.strip()   #removes white space from string, called a method, updates the value of name

print(f"hello, {name}")

#can combine two things
name = name.strip().title()     #strips white spaces, then capitalizes each word in string

#NEATER
name = input("What's your name ").strip().title() #combines ALL AESTHETICS into one clean line of code
print(f"hello, {name}")
"""

#DAY 2- making own functions w def


"""
#def used to define a function (make your own)
def hello(to="world"):  #open parenthesis shows no arguments in this code, but adding "to" here just sounds nice, colon means stay tuned for indentation,
    print("hello,", to)


#if want to BY DEFAULT, have smth there if programmer doesn't call hello with an argument, put to="world" in parameters/parenthesis of def (will)
hello()  #this will give "hello, world"
name = input("What's your name? ")
hello(name)     #name is another variable called "to" by what we put before
"""

#to order programs in the way you want (most important mnain part of coding at the top), use your defined function in another defined function
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)  #must use to instead of name, bc "name" variable is only defined in the "main" function at top, cannot be used as the same thing in my "hello" function

main()