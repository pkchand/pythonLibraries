#finding prime numbers
def prime(n):
    """finds and prints prime numbers within a given range"""
    numbers_list=[]
    is_prime=False
    for i in range(2,n):
        if n%i!=0:
            is_prime=True
        else:
            is_prime=False
            print("Not a prime")
            break
    if is_prime:
        print("Prime number")

def fibonacci(n):
    """finds and print fibonacci series for giveen number of people"""
    n1=0
    n2=1
    n3=n2
    count=1
    while count<n:
        print(n3, end=" ")
        count+=1
        n1=n2
        n2=n3
        n3=n2+n1

def factorial(n):
    """find factorial of a number"""
    fact=1
    for i in range(n,1,-1):
        fact*=i

    print(fact)

def sum_of_digit(num):
    """Add all digits of  number and prints it"""
    #num1=str(num)
    # sum=0
    # for i in num1:
    #     sum+=int(i)

    # print(sum)
    
    sum=0
    remainder=1
    while remainder>0:
        if(num<10):
            sum+=num
            remainder=0
        elif num%10!=0:
            remainder=num%10
            sum+=remainder
            num=num//10
            
    print(sum)

def isPalindromeNumber(n):
    """checks if the given number is plandrome and prints the answer"""
    remainder=1
    num=n
    reversed_number=0
    while remainder>0:
        if n>10 and n%10!=0:
            remainder=n%10
            reversed_number=(reversed_number+remainder)*10
            n=n//10
        else:
            reversed_number+=n
            remainder=0
    if num-reversed_number==0:
        print("palindrome number")
    else:
        print("not a palindrome number")

def isAmstrongNumber(n):
    """checks is the number is amstrong number (sum of cube of every digits) or not and then prints it"""
    num=n
    sum=0
    while n>0:
        rem=n%10
        sum+=(rem**3)
        n//=10
    
    if num-sum==0:
        print("Amstrong number")
    else:
        print("Not an Amstrong number")

def convert_to_binary(n):
    """takes a natural number and converts it to binary number"""
    if n>1:
        convert_to_binary(n//2)
    print(n%2, end="")
        
convert_to_binary(100)
#isAmstrongNumber(153)

#isPalindromeNumber(1551)
#prime(61)
#fibonacci(5)
#factorial(100)
#sum_of_digit(122)

