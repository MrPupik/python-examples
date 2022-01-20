

##############################################


# 1

def isodd(num):
    return num % 2 == 1

a = int(input("enter num:"))
print(isodd(a))


##############################################


# 2

def avg(n):
    s=0
    for i in range(n):
       s+=int(input("enter num:"))
    return s/n


##############################################


# 3
def numdigits(num):
    s=0
    while (num!=0):
       s+=1
       num//=10
    return s

def numdigits2(num):
    return len(str(abs(num)))

##############################################


# 4
s  = int(input("enter num:"))
print("20 - " , s//20)
print("10 - " , s%20 // 10)
print("5 - " , s%10 // 5)
print("1 - " , s%5)


##############################################


# 5
def mypow(x,y):
    s = 1
    for i in range(y):
        s*=x
    return s

##############################################


# 6
def getdis():
    x = float(input("enter discount:")) 
    return x

def getprice(pr):
    discount=0.1
    if pr > 1000:
        discount = getdis()
    
    return pr-pr*discount


##############################################


# 7

def isnotzero(a):
    return a!=0

def getdet(a,b,c):
    return (b**2 - 4*a*c)

def detpos(a,b,c):
    return getdet(a,b,c) >= 0
    
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

if isnotzero(a) == False:
    print("divide by zero")
elif detpos(a,b,c) == False:
    print("Negative det")
else:
    print("x1=" , (-1*b + getdet(a,b,c) / (2*a)))
    print("x2=" , (-1*b - getdet(a,b,c) / (2*a)))
    


##############################################

# 9
def smalldiv(a,b):
    m = min(a,b)
    for i in range(2,m):
        if (a % i == 0) and (b % i == 0):
            return i
    return 1

def biggest(a,b):
    m=min(a,b)
    for i in range(m,1,-1):
        if (a % i == 0) and (b % i == 0):
            return i
    return 1

def mypow(a,b):
    return pow(a,b)

def sqdiff(a,b):
    return pow(a,0.5) - pow(b,0.5)
        
a = int(input("enter a:"))
b = int(input("enter b:"))

d = {'a':biggest , 'b':smalldiv , 'c':mypow , 'd':sqdiff}

while True:
    print("a-	the biggest devider")
    print("b-	the smallest divider")
    print("c-	the result of pow(a,b)")
    print("d-	the result of sqrt(a)-sqrt(b)")
    print("e-	exit")
    c = input("")
    if c=='e':
        break
    print(d[c](a,b))




##############################################


# 10
def factorial(x):
    m = 1
    for i in range(2,x+1):
        m*=i
    return m

def exp(steps, x):
    s = 0
    m = 1
    for i in range(steps):
        s+= m * ((x ** i) / factorial(i))
        m*=-1
        
    return s

##############################################


# 11

def printmsg(cid):
    print(cid ," - VIP customer")

num = int(input("enter customer id:"))
sm = int(input("enter total orders:"))
good = int(input("pay on time? "))
years = int(input("enter number of years:"))

a = (sm > 8000)
b = (good == 1)
c = (years > 5)

if ((a == True) and (c == True)) or (b == True):
    printmsg(num)



























