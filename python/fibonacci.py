# #Loop Method
# # Enter number of terms needed                  
# number=int(input("Enter the terms: "))  # 0,1,1,2,3,5....
# firE=0 #first element of series
# secE=1 #second element of series
# if number<=0:
#     print("The requested series is: ",firE)
# else:
#     print(firE,secE,end=" ")
#     for x in range(2,number):
#         next=firE+secE                           
#         print(next,end=" ")
#         firE=secE
#         secE=next


# Recursion Function
def FibRecursion(number):  
   if number <= 1:  
       return number  
   else:  
       return(FibRecursion(number-1) + FibRecursion(number-2)) 
        
nterms = int(input("Enter the terms? "))  # take input from the user
  
if nterms <= 0:  # check if the number is valid 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(FibRecursion(i))
