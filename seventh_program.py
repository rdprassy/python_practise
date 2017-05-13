def collatz(number):
    if(number%2==0):
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1


print('enter an integer')
try:
      x=int(input())
      while(collatz(x)!=1):
          x=collatz(x)

          
except ValueError:
      print('please enter integer values only')
        
