#Write a program which contains one function as Add() which accepts two numbers from user and return addition of that two numbers

def Add(value1,value2):
	
	Ans=value1+value2
	return Ans

def main():

	print("Enter first number :")
	no1=int(input())
	
	print("Enter second number :")
	no2=int(input())
	
	iRet=Add(no1,no2)
	
	print("Addition is :",iRet)
	
if __name__=="__main__":
	main()
