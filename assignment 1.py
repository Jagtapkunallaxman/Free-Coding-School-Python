#!/usr/bin/env python
# coding: utf-8

# In[28]:


lst = ["HI",37,[1,2,3],7.3]

print(lst)


# In[31]:


lst[0]


# In[33]:


lst[-2]


# In[34]:


lst[1:]


# In[35]:


lst[:1]


# In[38]:


# by default functionsin list
print(lst)

lst.count(37)


# In[49]:


lst.append(3)


# In[50]:


lst


# In[51]:


lst.append(4)


# In[52]:


lst


# In[53]:


lst.count(37)


# In[54]:


lst.count(3)


# In[55]:


lst.count(4)


# In[56]:


lst.count(1)


# In[57]:


lst.count(37)


# In[73]:


lst.clear()


# In[72]:


lst.copy()


# In[79]:


lst.extend("HI")


# In[80]:


lst


# In[98]:


print(lst)


# In[99]:


lst = ["HI",47,[1,2,3],7.3]
print(lst)


# In[105]:


lst.index(7.3, 1, 7)


# In[106]:


lst.index(47, 1, 3)


# In[107]:


lst.insert(47,5)


# In[108]:


lst


# In[110]:


lst.pop()


# In[111]:


lst


# In[112]:


lst.pop(0)


# In[113]:


lst


# In[114]:


lst.pop(1)


# In[115]:


lst


# In[116]:


lst = ["HI",37,[1,2,3],7.3]
print(lst)


# In[117]:


help(lst.remove)


# In[119]:


lst.remove(37)


# In[120]:


lst


# In[121]:


lst.remove(7.3)


# In[122]:


lst


# In[123]:


lst = ["HI",77,[1,2,3],7.3]
print(lst)


# In[129]:


lst.reverse()


# In[131]:


lst


# In[140]:


lst = [2, 1, 3, 4]
print(lst)


# In[143]:


lst


# In[152]:


# list sort 
vowels = ['e', 'a', 'u', 'o', 'i']

vowels.sort()
print(vowels)


# In[154]:


#dict

dit = {"my_name":"kunal" , 
       "my_house_name":"Sai" ,
       "my_family_has":4}


# In[155]:


dit.get("my_name")


# In[156]:


dit["my_family_has"]


# In[157]:


# methods in dict


# In[159]:


dit.values()


# In[160]:


dit


# In[161]:


dit.keys()


# In[163]:


dit.pop('my_name')


# In[164]:


dit


# In[165]:


dit.clear()


# In[166]:


dit


# In[167]:


dit = {"my_name":"kunal" , 
       "my_house_name":"Sai" ,
       "my_family_has":4}


# In[168]:


dit.copy()


# In[179]:


# dit.fromkeys
keys = {'a', 'b', 'c', 'd', 'e' }

alphabet = dict.fromkeys(keys)
print(alphabet)


# In[175]:


dit.get()


# In[180]:


#dit.get
person = {'name': 'kunal', 'age': 20,'salary':100000000000}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))


# In[183]:


# dit.items
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print('appple')
print(sales.items())


# In[187]:


sales = { 'sop': 2, 'pen': 3, 'ring': 4 }

items = sales.items()
print('ring items:', items)

# delete an item from dictionary
del[sales['sop']]
print('Updated items:', items)


# In[188]:


person = {'name': 'kunal', 'age': 20, 'salary': 900000000000}

# ('salary', 900000000000) is inserted at the last, so it is removed.
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

# inserting a new element pair
person['profession'] = 'engineer'

# now ('profession', 'engineer') is the latest element
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)


# In[189]:


boy = {'name': 'kunal', 'age': 20}

age = boy.setdefault('age')
print('boy = ',boy)
print('Age = ',age)


# In[195]:



d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)




# In[196]:


# random sales dictionary
sales = { 'monitor': 9000, 'keyboard': 700, 'mouse': 500 }

print(sales.values())


# In[197]:


# set


# In[199]:


# language set remove
language = {'English', 'French', 'German'}

# 'German' element is removed
language.remove('German')

# Updated language set
print('Updated language set: ', language)


# In[200]:


# set add of vowels
vowels = {'a', 'e', 'i', 'u'}

# adding 'o'
vowels.add('o')
print('Vowels are:', vowels)

# adding 'a' again
vowels.add('a')
print('Vowels are:', vowels)


# In[201]:


# set copy
numbers = {1, 2, 3, 4}
new_numbers = numbers

new_numbers.add('5')

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)


# In[202]:


# set clear of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
print('Vowels (before clear):', vowels)

# clearing vowels
vowels.clear()
print('Vowels (after clear):', vowels)


# In[203]:


# set difference
A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

# Equivalent to A-B
print(A.difference(B))

# Equivalent to B-A
print(B.difference(A))


# In[204]:


# set differnce_update
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)


# In[205]:


# set discard
numbers = {2, 3, 4, 5}

numbers.discard(3)
print('numbers = ', numbers)

numbers.discard(10)
print('numbers = ', numbers)


# In[206]:


#set intersection
A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}

print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A, B))


# In[207]:


# set.intersection_update
A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}

result = C.intersection_update(B, A)

print('result =', result)
print('C =', C)
print('B =', B)
print('A =', A)


# In[208]:


# set.isdisjoint
A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))


# In[209]:


# set.issubset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))

# Returns False
print(A.issubset(C))

# Returns True
print(C.issubset(B))


# In[210]:


# set.pop
A ={'a', 'b', 'c', 'd'}

print('Return Value is', A.pop())
print('A = ', A)


# In[211]:


# set.symmetric_difference
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))


# In[212]:


# set.symmetric_difference_update
A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }

result = A.symmetric_difference_update(B)

print('A =', A)
print('B =', B)
print('result =', result)


# In[213]:


# set.union
A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))
print('A.union() =', A.union())


# In[214]:


# set.update
A = {'a', 'b'}
B = {1, 2, 3}

result = A.update(B)

print('A =', A)
print('result =', result)


# In[215]:


# tuple
# tuple count
vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)


# In[216]:


# tuple index
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# element 'e' is searched
index = vowels.index('e')

# index is printed
print('The index of e:', index)

# element 'i' is searched
index = vowels.index('i')

# only the first index of the element is printed
print('The index of i:', index)


# In[222]:


# string capitalize
string = "kunal is AWesome."

capitalized_string = string.capitalize()

print('Old String: ', string)
print('Capitalized String:', capitalized_string)


# In[221]:


# string center
string = "kunal is awesome"

new_string = string.center(24)

print("Centered String: ", new_string)


# In[220]:


# string.casefold
string = "Kunal IS AWESOME"

# print lowercase string
print("Lowercase string:", string.casefold())


# In[223]:


# string count
string = "kunal is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)


# In[225]:


# string endswith
text = "kunal is ready for exam."

result = text.endswith('for exam')
# returns False
print(result)

result = text.endswith('for exam.')
# returns True
print(result)

result = text.endswith('kunal is ready for exam.')
# returns True
print(result)


# In[226]:


# string expandtabs
str = 'abc\t12345\txyz'

# no argument is passed
# default tabsize is 8
result = str.expandtabs()

print(result)


# In[227]:


# string encode
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)


# In[228]:


# string find

quote = 'Let it be, let it be, let it be'

# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")


# In[230]:


# string format
# default arguments
print("Hello {}, your balance is {}.".format("abhi", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("abhi", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="abhi", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("abhi", blc=230.2346))


# In[237]:


# string index
sentence = 'Python programming is fun.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)

result = sentence.index('Java')
print("Substring 'Java':", result)
      


# In[238]:


sentence = 'Python programming is fun.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)

result = sentence.index('Java')
print("Substring 'Java':", result)


# In[239]:


# string isalnum
name = "Kunal"
print(name.isalnum())

# contains whitespace
name = "Kunal Jagtap "
print(name.isalnum())

name = "KunalJagtap"
print(name.isalnum())

name = "133"
print(name.isalnum())


# In[240]:


# string isalpha
name = "Kunal"
print(name.isalpha())

# contains whitespace
name = "Kunal Jagtap"
print(name.isalpha())

# contains number
name = "KunalJagtap"
print(name.isalpha())


# In[241]:


# string isdecimal
s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())


# In[242]:


# string isdigit 
s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())


# In[243]:


# string isidentifier
str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '77Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())


# In[244]:


# string islower
s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())


# In[245]:


# string isnumeric
s = '1242323'
print(s.isnumeric())

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())

# s = '½'
s = '\u00BD'
print(s.isnumeric())

s = '1242323'
s='python12'
print(s.isnumeric())


# In[246]:


# string isprintable
s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\nNew Line is printable'
print(s)
print(s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())


# In[247]:


# string isspace
s = '   \t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ''
print(s.isspace())


# In[248]:


# string istitle
s = 'Python Is Good.'
print(s.istitle())

s = 'Python is good'
print(s.istitle())

s = 'This Is @ Symbol.'
print(s.istitle())

s = '99 Is A Number'
print(s.istitle())

s = 'PYTHON'
print(s.istitle())


# In[249]:


# string isupper
# example string
string = "THIS IS GOOD!"
print(string.isupper());

# numbers in place of alphabets
string = "THIS IS ALSO G00D!"
print(string.isupper());

# lowercase string
string = "THIS IS not GOOD!"
print(string.isupper());


# In[250]:


# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))


# In[252]:


# string just
string = 'Kunal'
width = 5

# print left justified string
print(string.ljust(width))


# In[254]:


# example string rjust
string = 'Kunal'
width = 5

# print right justified string
print(string.rjust(width))


# In[255]:


# example string lower
string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())

# string with numbers
# all alphabets whould be lowercase
string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())


# In[256]:


# example string upper
string = "this should be uppercase!"
print(string.upper())

# string with numbers
# all alphabets whould be lowercase
string = "Th!s Sh0uLd B3 uPp3rCas3!"
print(string.upper())


# In[257]:


# example string swapcase
string = "THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())

string = "this should all be uppercase."
print(string.swapcase())

string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())


# In[258]:


# string istrip
random_string = '   this is good '

# Leading whitepsace are removed
print(random_string.lstrip())

# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('sti'))

print(random_string.lstrip('s ti'))

website = 'https://www.programiz.com/'
print(website.lstrip('htps:/.'))


# In[259]:


# string rstrip
random_string = ' this is good'

# Leading whitepsace are removed
print(random_string.rstrip())

# Argument doesn't contain 'd'
# No characters are removed.
print(random_string.rstrip('si oo'))

print(random_string.rstrip('sid oo'))

website = 'www.programiz.com/'
print(website.rstrip('m/.'))


# In[261]:


# string strip
string = '  kunal love dadmom   '

# Leading and trailing whitespaces are removed
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' mom'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))


# In[262]:


# string partition
string = "Python is fun"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('not '))

string = "Python is fun, isn't it"

# splits at first occurence of 'is'
print(string.partition('is'))


# In[264]:


# string maketrans
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))


# In[265]:


# string rpartition
string = "Python is fun"

# 'is' separator is found
print(string.rpartition('is '))

# 'not' separator is not found
print(string.rpartition('not '))

string = "Python is fun, isn't it"

# splits at last occurence of 'is'
print(string.rpartition('is'))


# In[266]:


# string translate
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))


# In[267]:


# string replace
song = 'cold, cold heart'
print (song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

'''only two occurences of 'let' is replaced'''
print(song.replace('let', "don't let", 2))


# In[268]:


# string r find
quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if  (result != -1):
  print("Highest index where 'be,' occurs:", result)
else:
  print("Doesn't contain substring")


# In[269]:


# string rindex
quote = 'Let it be, let it be, let it be'

result = quote.rindex('let it')
print("Substring 'let it':", result)
  
result = quote.rindex('small')
print("Substring 'small ':", result)


# In[270]:


# string split
text= 'Love the neighbor'

# splits at space
print(text.split())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))

# Splitting at ':'
print(grocery.split(':'))


# In[272]:


# sting rsplit
text= 'Love thy neighbor'

# splits at space
print(text.rsplit())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.rsplit(', '))

# Splitting at ':'
print(grocery.rsplit(':'))


# In[273]:


# string splitlines
grocery = 'Milk\nChicken\r\nBread\rButter'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())


# In[274]:


# string startswith
text = "Python is easy to learn."

result = text.startswith('is easy')
# returns False
print(result)

result = text.startswith('Python is ')
# returns True
print(result)

result = text.startswith('Python is easy to learn.')
# returns True
print(result)


# In[275]:


# string title
text = 'My favorite number is 25.'
print(text.title())

text = '234 k3l2 *43 fun'
print(text.title())


# In[276]:


# string zfill
text = "program is fun"
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))


# In[277]:


#string format _map
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))


# In[ ]:




