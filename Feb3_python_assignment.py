#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the  range of 1 to 25. 
'''def keyword is used to create function
'''
l=[]
def odd_num():
    for i in range(1,26):
        if i%2!=0:
            l.append(i)
    return l
odd_num()
    


# In[2]:


#Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs  to demonstrate their use. 
'''*args is used to pass variable arguments to a function.
It is not a keyword, you can take any name in place of it'''
#Example of *args
def test(*args):
    return args
test([1,2,3,4],'Monika',(3,4,5),78)


# In[5]:


#**kwargs
'''It is used to as a dictionary to pass as a argument to a function.
It is used to map each keyword to a value'''
#Example:
def test1(**kwargs):
    return kwargs
test1(name='Monika',values=[1,2,3,4,5])


# In[17]:


'''Q3.  What is an iterator in python? Name the method used to initialise the iterator object and the method  used for iteration.
Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,  16, 18, 20]. '''
'''An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects
like list, tuples, sets, etc.
Using an iterator-

iter() function is used to create an iterator containing an iterable object.
next() function is used to call the next element in the iterable object.'''
l=iter([2,4,6,8,10,12,14,16,18,20])
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))


# In[18]:


#Q4.  What is a generator function in python? Why yield keyword is used? Give an example of a generator  function. 
'''It is a way of creating iterators.
Why we have to use generator function?
Because suppose if the data is 10M then normal function occupies a lot of memory result in system performance slow.
By using generator function, it yield/throw the output simultaneously hence occupying less memory
A Generator in Python is a function that returns an iterator using the Yield keyword.'''
def test_fib(n):
    a,b=0,1
    for i in range(n):
        yield a#use to throw a value
        a,b=b,a+b
for i in test_fib(10):
    print(i)


# In[30]:


#Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the  first 20 prime numbers.
def prime():
    yield 2
    l=[2]
    flag=0
    for i in range(3,1000):
        
        for j in l:
            if i%j==0:
                flag=1
                break
            else:
                flag=0
        if flag==0:
            l.append(i)
            yield i
prime_number=prime()  

for i in range(20):
    print(next(prime_number))


# In[38]:


#Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop. 
def test_fib():
    a,b=0,1
    
    while True:
        yield a
        a,b=b,a+b
        
        
   

    
    


# In[37]:


fib=test_fib()
for i in range(10):
    print(next(fib))
    


# In[1]:


#Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’. 
#Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']  
s="pwskills"
[i for i in s]


# In[2]:


#Q8. Write a python program to check whether a given number is Palindrome or not using a while loop. 
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


# In[3]:


#Q9. Write a code to print odd numbers from 1 to 100 using list comprehension. 
#Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter  out odd numbers. 
[i for i in range(1,100) if i%2 !=0]


# In[ ]:




