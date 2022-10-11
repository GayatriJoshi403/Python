#Write a program which contains one function that accept one number from user and return true if number is divisible by 5 otherwise return false

def Division(value):
	
	if(value%5==0):
		return True
	else:
		return False

def main():

	print("Enter number : ")
	no=int(input())
	
	bRet=Division(no)

	if(bRet==True):
		print("True")	
	else:
		print("False")
	
if __name__=="__main__":
	main()

