
# coding: utf-8

# In[9]:


#prime number
num = int(input("enter num: "))
for i in range(2, num):
    if(num % i == 0):
        print("%d is not a prime "%num)
        break
else:
    print("%d is prime number"%num)
    


# In[10]:


# nested loop - (prime number between 10-100)
for i in range(10, 101):
    for i in range(2, num):
        if(num % i == 0):
            break
else:
    print("%d is prime number"%num)



# In[11]:


'''
* * *
* * *
* * *
* * *
'''
row = int(input("enter no of rows: "))
col = int(input("enter no of cols: "))
for r in range(1, row+1):
    for c in range(1, col+1):
        print("*", end=" ")
    print("")


# In[12]:


'''
         *
      *  *  *
   *  *  *  *  * 
*  *  *  *  *  * *
'''
row = int(input("enter no of rows: "))
col = int(input("enter no of cols: "))
for r in range(1, row+1):
    for c in range(1, col+1):
        print("*", end=" ")
    print("")
k = 0
row = 4
for i in range (1, row+1):
    for space in range(1, (row-i) +1):
        print(end=" ")
        while k != (2*i - 1):
            print("*", end="")
            k = k + 1
        K =0        
    print() 


# In[18]:


'''
         *
      *  *  *
   *  *  *  *  * 
*  *  *  *  *  * *
'''
row = int(input("enter no of rows: "))
for r in range(1,row+1):
    for s1 in range(0,row-r):
        print(" ", end=" ")
   
    for s in range (0,2*r-1):
                                          
        print("*", end=" ")
    print("")


# In[19]:


row = int(input("enter no of rows: "))
for r in range(1,row+1):
    for s1 in range(0,r):
        print("*", end=" ")
    print("")

