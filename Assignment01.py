import math
import sys
from datetime import datetime

# Problem # 1       
print ('''Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!''')

# Problem # 2
print(sys.version)

# Problem # 3
print(datetime.date(datetime.now()))
print(datetime.time(datetime.now()))

# Problem # 4           
a = int(input("Radius of The Circle: "))
a = (pow(a, 2))
Area = math.pi *a
print(Area)
# Problem # 5 
First= input("Your First Name:")
Last= input("Your Last Name:")
E = reversed(First+Last)
print(''. join(E))
# Problem # 6        
g = int(input("Enter 1st #: "))
h = int(input("Enter 2nd #: "))
print(g+h)