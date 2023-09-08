'''def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
     if(a>b):
        print("First number is greater")
     else:
        print("Second number is greater or equal")

def isLesser(a, b):
     pass
                        
a = 9
b = 8
isGreater(a, b)
calculateGmean(a,b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# printgmean2)'isGr

'''

def seriesConnection (a,b):
   series = a+ b
   print("series connection of R¹ ,R² is",series)

def parallelconnection (a,b):
   parallel = (a*b)/(a+b)
   if (a!=0 and b!=0):
      print("parallel connection of R¹ and R² is",parallel)
   else:
      if(a==0):
         print("current not flows from R¹ because of it short ckt.")
      if(b==0):
         print("current not flows form R²  because of it short ckt")
      print("Whole circuit is short circuited in parallel case")

a = int(input())
b = int(input())
seriesConnection(a,b)
parallelconnection(a,b)



