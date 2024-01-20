#Function to take two strings from the user
def fullname(first_name,last_name):
    return first_name+" "+last_name

#Function that returns every other char in the full_name string
def string_alternative(str):
    return str[::2]

#taking input and assigning to variables
First_name = input("your first name : ")
last_name = input("your last name : ")

#Calling fullname function
Full_name= fullname(First_name,last_name)

#Printing Full Name
print("Full Name: "+Full_name)

#Calling string_alternative and printing the same
print(string_alternative(Full_name))

#2
#defining a empty string
empty_string = ""

#defining a function to count occurances of each word
def wordcount(st):
    count = dict()
    w = st.split()
    for y in w:
        if y in count:
            count[y]+=1
        else:
            count[y]=1
    return count
#reading input.txt file and adding it to empty_string variable
with open(r'input.txt','r') as file:
    data = file.read()
    empty_string +=data

#calling wordcount function
a=str(wordcount(empty_string))
empty_string +="\nWord_Count: \n"
empty_string +=a

#replacing string to get required output
empty_string = empty_string.replace("{","")
empty_string = empty_string.replace("}","")
empty_string = empty_string.replace("'","")
empty_string = empty_string.replace("P","\nP")
empty_string = empty_string.replace(", ","\n")
print(empty_string)

#opening and writing to the file
outputfile = open(r'output.txt','w')
outputfile.write(empty_string)

#closing of txt files
outputfile.close()
file.close()

#3
#Defining a list
list_height = []

#taking input from user for number of customers
no_Of_Customers = int(input("Enter number of customers : "))

#for loop to take input and append to list
for i in range(0, no_Of_Customers):
    height = float(input())
    list_height.append(height)

#converting inches to cms and appending to a list
final_list = [x*2.54 for x in list_height] 

#printing the new list
print(final_list)
