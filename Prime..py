#Write a program which accept one number from user and check whether number is prime or not
#Input : 5
#Output : It is prime number

def ChkPrime(value):
	
	Flag=True	
	
	for i in range(2,value):
		if(value%i==0):
			Flag=False
			break
	return Flag
			
def main():
	
	print("Enter number : ")
	no=int(input())
	
	bRet=ChkPrime(no)
	
	if(bRet==True):
		print("Number is prime")
	else:
		print("Number is not prime")

if __name__=="__main__":
	main()
