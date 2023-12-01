"""
1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

Click me to see the sample solution

"""
#print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")


"""

2. Write a Python program to find out what version of Python you are using.
Click me to see the sample solution
"""
# import sys
# print(sys.version)


"""
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
Click me to see the sample solution
"""
# import datetime
# now = (datetime.datetime.now())

# print("Current date and time:")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))



"""
4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504

Click me to see the sample solution
"""
# from math import pi
# area = pi * 1.1 ** 2
# print(area)


"""
5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
Click me to see the sample solution
"""
# name = input("enter a name")
# surname = input("enter a surname")
# print(f"{surname} {name}")



"""
6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
Click me to see the sample solution
"""

# user_input = input("Please type your numbers separated by coma.")
# list_1 = user_input.split(",")
# tuple_1 = tuple(list_1)
# print(list_1)
# print(tuple_1)
"""
7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
Click me to see the sample solution
"""
# new_word = input("put your data here: ")
# new = ''
# counter = 1


# for item in new_word:
#     if new_word[len(new_word)-counter] == ".":
#         break
#     new += new_word[len(new_word)-counter]
#     counter += 1
# print(new[::-1])
# # Drugie rozwiązanie szybsze
# list_1 = new_word.split(".")
# print(list_1[-1])
"""
8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
Click me to see the sample solution
"""
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])


"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
Click me to see the sample solution
"""



"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
Click me to see the sample solution

"""