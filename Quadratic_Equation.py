#FINDING THE ROOT OF ax^2+bx+c=0
import cmath
a=int(input('ENTER coeffient of x^2  : '))
b=int(input('ENTER coeffient of x      : '))
c=int(input('ENTER coeffient of 1      : '))
'''   To find the value of x following is the formula,
		x=( -b  +ro-  sqrt(b^2 - 4ac))/(2*a)
  
      '''
# (b^2 - 4ac)
z=(b*b)-(4*a*c)

# sqrt(b^2 - 4ac)
z1= cmath.sqrt(z)

#( -b  +ro-  sqrt(b^2 - 4ac))/(2*a)
root1=((-b+z1)/(2*a))
root2=((-b-z1)/(2*a))
#printing the roots
print(root1,root2)


