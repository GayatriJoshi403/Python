#Write a program which accept one number from user and return its factorial
#Input : 5
#Output : 120

def Factorial(value):
	
	Ans=1
	
	for i in range(1,value+1):
		Ans=Ans*i
	return Ans
	

def main():

	print("Enter number :")
	no=int(input())
	
	iRet=Factorial(no)
	
	print("Factorial is :",iRet)

if __name__=="__main__":
	main()
