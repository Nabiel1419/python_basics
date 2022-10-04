''' Lists  in python 

important points about lists ::
1.List is used to store multiple values in a single variable
just like arrays we can store multiple values in a single variable
but there is a big difference b/w arrays and lists .Arrays are hemogenous while as lists are 
heterogeous that means every element must have same datatype as declared syntax expresses but in case of
list we have heterogeous data that means  we can have different types of values present in a list
for example 
in arrays we have int arr[]=[1,2,4,5] #we can't store float or string or char value in an array
in list we have myList=["a",4.5,6,'severe',"king",'apple'] 
2.List are indexed 
3.List is mutable that means we can change the element at the specific index
4.List is ordered 
5.Changeable means that we can change the elements of the list we can update ,delete, insert
6.We can create list using list constructor 
7.list can contain numbers,strings, boolean values
8.We can  see the datatype of the list using type() function
9. We can find the length of the list using len()
10. Lists are iteratable
11. Negative  indexing supported in lists



''' 
#This programs demostartes How to declare list  ,index working ,intialize it and explore its various functions

from typing import List


Numbers=[4,55,77,88,888]#list should be square braces
print(type(Numbers))#prints the class 

Strings=["facebook","whatsapp","twitter","instagram"]#list that contains (Hemogenous)

AlphaNumeric=["facebook",55,"whatsapp",90]# list that contains both strings and numbers (Heterogenous)
print(Numbers)
print(Strings)
print(AlphaNumeric)
# range of indexes
print(AlphaNumeric[-4:-1]) # doesn't include last element but includes first element
print(Strings[:])
print(Numbers[:4])
#Negative index
#[-1] means last element
#[0] means first element
#[-2] means second last element
print(Numbers[-2])
print(Numbers[0])
print(Numbers[-1])
#list creation using constructor
fruits=list(("apple","banana","pear"))
print(type(fruits))
print(fruits)
#Lists are indexed
print(fruits[0])
#List is mutable ,means we can update its elements 
fruits[0]="watermelon"
print(fruits)
#change a range of elements
Numbers[0:2]=[9900,77,656]
print(Numbers)

# Find Length of the list using len and and _len_()
print(len(fruits))
length=fruits.__len__()
print(length)
# Take user input  and store in list
social_media=[]
for i in range(3):
    social_media.append(input("Enter Element"))
print(social_media)
#  Exploring various  list functions
'''
append(element)
insert(index,element)
extend(list)
remove(element)
del
pop(index)
pop()
copy()
sort()
''' 
# Use of append(element) function it appends given element at the end of list
fruits.append("grapes")
print(fruits)
#Use of insert(index,elm) function takes first arg index where to place the  element  and second argument as element
fruits.insert(0,'orange')
print(fruits)
# use of extend function takes list as an argument appends list to  a list
fruits.extend(Numbers)
print(fruits)
#use of remove(item_name) function removes specified element
fruits.remove('orange')
#use of pop(index) pop(no argument) pop(index) is used to remove item at specified position pop() when no
fruits.pop(0)
print(fruits)
# argument is passed removes last element form the list 
fruits.pop()
print(fruits)
# use of del list[0] function removes element at specific location it also deletes entire list when index not given
del fruits[3]
print(fruits)
#del list_name
del Numbers
# use of  clear() function this function empities the given list
# list_name.clear() takes no argument
Strings.clear()
print(Strings)

#loop through a list
mobile_Numbers=[9904834743,9838573543,384983534985,3849483943]
for x in mobile_Numbers:
    print(x)
# loop through index using range()and len() function
for i in range(len(mobile_Numbers)):
    print(mobile_Numbers[i])
# using while loop
i=0
while i<len(mobile_Numbers):
    print(mobile_Numbers[i])
    i=i+1
# using list comprhension 
[print(f"using comprhension{x}") for x  in mobile_Numbers]
# sort() function sorts the list sort depends on the elements in list numbers ,strings ,chars
Integers=[]
for i in range(10):
    Integers.append(int(input("enter number")))
print(Integers)
Integers.sort()# in increasing order
print(Integers)
Integers.sort(reverse=True)# in decreasing order
Alphabets=['ac','cb','c','bd']# sorts according to Dictonary order
Alphabets.sort()
print(Alphabets)
Alphabets.sort(reverse=True)
print(Alphabets) 
#reverse the list using reverse() 
Integers.reverse()
print(Integers)
# how to copy one list into another list

List1=['cat','dog','cow','ox','lion']
List1[4]='fish'
Animals=List1
Animals[0]='Tiger'
print(Animals)
print(List1)
# here in this  approach we are only making Animals as a refrence to a List1 changes made in list1 will be made in list2 automatically

# efficent approach
Animals=List1.copy()
List1[0]='frog'
print(Animals)
Animals[0]='parrot'
print(List1)
print(Animals)
# Another way to copy 
mylist=[2,4344,535,55453]
list2=list(mylist)
print(list2)