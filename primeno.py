"""
this is a program to find whether a number is prime or not
"""

a=int(input("enter a number"))
if a>1:
	for i in range (2,a):
		if a%i==0:
			print(a,"not a prime number ")
			break
	else:
		print ("it is a prime")

else:
	print("it is not a prime")

			
#This program is written by Manav 