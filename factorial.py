# Function for returning factorial of 'n' using RECURSION
def fact(n):
  if(n==1):
    return 1
  else:
    return n*fact(n-1)

print("Enter a number of your choice : ")
N = int(input())
result=fact(N)
print("Factorial of ",N," : ",result)
