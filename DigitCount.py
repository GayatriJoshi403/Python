#Write a program which accept one number from user and return number of digits in that number

#Input : 5187934
#Output : 7

def CountDigits(value):
	
	digit=0
	count=0
	
	while(value>0):
		digit=int(value%10)
		count=count+1
		value=int(value/10)
	return count

def main():
	print("Enter number : ")
	no=int(input())
	
	iRet=CountDigits(no)
	
	print("Number of digit is :",iRet)

if __name__=="__main__":
	main()
