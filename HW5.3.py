######worked with gianna

#####Problem1

#import entry as e
#import paypal as p


#####Problem2
#code: part a
Emmas-MacBook-Pro:home emmamearls$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/Users/emmamearls/home'
>>> os.chdir('/Users/emmamearls/home/m3a/frank/chapters')
>>> os.getcwd()
'/Users/emmamearls/home/m3a/frank/chapters'

#partb

Emmas-MacBook-Pro:home emmamearls$ cd user
Emmas-MacBook-Pro:user emmamearls$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/Users/emmamearls/fakeroot/home/user'
>>> os.chdir('/Users/emmamearls/fakeroot/usr/local/src')
>>> os.getcwd()
'/Users/emmamearls/fakeroot/usr/local/src'


#########Problem 3
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)

#########Problem4
def reverse_list(alist):
    if len(alist) == 1:
        return alist #base case
    else:
        return reverse_list(alist[1:]) + [alist[0]]

print(reverse_list([1,2,3,4]))

#########Problem5

def permute_string(lst):

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]


    l = []


    for i in range(len(lst)):
        m = lst[i]


        remLst = lst[:i] + lst[i + 1:]


        for p in permute_string(remLst):
            l.append([m] + p)
    return l


data = list('abc')
for p in permute_string(data):
    print(p)

#########Problem6

def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))

L = [1, 2, 3, 5, 6]
print(maximum(L))

############Problem7

s1 = input('Please enter a string: ')
s2= input('Please enter a string: ')
def compare_string(s1, s2):
    if s1 == s2:
        print(1)
    else:
        print(0)
compare_string(s1.lower(), s2.lower())


############Problem8

import matplotlib.pyplot as plt

X = ['News', 'Judiciary', 'Congress', 'Police', 'Church', 'Military', 'Presidency']
y1 = [20, 23, 9, 56, 41, 73, 36]
y2 = [27, 27, 12, 57, 41, 72, 32]

plt.bar(X, y1)
plt.bar(X, y2)
plt.ylabel('%')
plt.title('Confidence in Institutions')
plt.show()

#########Problem9

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcdefaults()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
y = [311, 316, 304, 294, 274, 267, 266, 265, 262, 261, 263, 277, 282, 271, 269, 261, 297, 304, 321, 339, 347, 337, 342]

plt.plot(y, 'r')

plt.ylabel('Price($)')
plt.xlabel('October')
plt.title('Tesla Stock Price')
plt.show()
