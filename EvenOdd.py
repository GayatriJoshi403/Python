#Write a program which contains one function as ChkNum() which accept one parameter as number.If number is then it shuould display "Even number"otherwise display "odd number" on console 

#Input : 11
#Output : Odd number

def ChkNum(value):
	if(value%2==0):
		return True
	else:
		return False

def main():
	print("Enter number :")
	no=int(input())
	
	bRet=ChkNum(no)
	
	if(bRet==True):
		print("Even number")
	else:
		print("Odd number")
		
if __name__=="__main__":
	main()
