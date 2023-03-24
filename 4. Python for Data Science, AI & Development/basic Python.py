#--------------
# Python basics
#--------------


# check what version of Python we are using
import sys
print(sys.version)

# latest (3.10.2) march 2023

# type of object (equivalent to class() in R)
type(2.14)
type(True)
type(1)
type('string')

# system settings about float type
sys.float_info

# Convert an integer to a string
str(2)

# integer division //
7 // 2

# expressions
43 + 60 + 16 + 41

# variables
x = 43 + 60 + 16 + 41
x

# Use quotation marks for defining string
name = "Michael Jackson"
print(name[13])

# length of a string
len(name)

# slicing
name[8:12]

# striding: get every second element in the range from index 0 to index 4
name[::2]
name[0:5:2]

# Concatenate two strings
statement = name + " is the best"
statement

# print the string for 3 times
3 * name

# new line escape sequence
print(" Michael Jackson \n is the best" )

# convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# replacing a string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b

# Find the substring in the string.
name.find('Jack')

#Split the substring into list
split_string = (name.split())
split_string

# regex
import re

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
    
# 
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)

# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 



# In the string s3, find the four consicutive digit character using \d and search() function:
s3 = "House number- 1105"
re.search('\d', s3)

#In the string str1, replace the sub-string fox with bear using sub() function:
str1= "The quick brown fox jumps over the lazy dog."
# Use re.sub() to replace "fox" with "bear"
new_str1 = re.sub(r"fox", "bear", str1)
new_str1

# In the string str2 find all the occurrences of woo using findall() function:
str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
re.findall('woo', str2)


#----
# end
#----
