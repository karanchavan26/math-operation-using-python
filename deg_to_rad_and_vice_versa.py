''' TO CONVERT DEGREE TO RADIAN AND VICE VERSA       '''

z=int(input('	1 : TO CONVERT DEG TO RAD \n	2 : TO CONVERT RAD TO DEG\n '))
print(z)

if(z==1):
		
	a=int(input('ENTER DEGREE : '))
	r=a*0.01745329252
	print('Radian of entered no. is : ',r)
	
elif(z==2):
	
	b=int(input(' ENTER RADIAN : '))
	d=b*57.2957795131
	print('Degree of entered no. is : ',d)

	
else:
	
	print('PLEASE ENTER VALID INPUT')

