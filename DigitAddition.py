#Write a program which accept one number from user and return addition of digits in that number

#Input : 5187934
#Output : 37

def CountDigits(value):
	
	digit=0
	Sum=0
	
	while(value>0):
		digit=int(value%10)
		Sum=Sum+digit
		value=int(value/10)
	return Sum

def main():
	print("Enter number : ")
	no=int(input())
	
	iRet=CountDigits(no)
	
	print("Number of digit is :",iRet)

if __name__=="__main__":
	main()
