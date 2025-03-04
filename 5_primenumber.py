#print prime numbers between 1 and 100
#1 2 3 5 7 11

#2 3 4 5 6 7 8 

lowerrange = 1
upperrange = 100
prime=1
for num in range(lowerrange,upperrange+1):
   for i in range(2,(num//2 + 1)):
      if num % i == 0:
        prime = 0
        break
      else:
         prime = 1
   if prime == 1:
      print(num)
       
