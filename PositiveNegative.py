#Write a program which accepts number from user and check whether that number is positive or negative or zero.

def ChkNum(value):

	if(value>0):
		print("Positive number")
	if(value<0):
		print("Negative number")
	if(value==0):
		print("Zero")
	

def main():
	
	print("Enter number :")
	no=int(input())
	
	ChkNum(no)
	
if __name__=="__main__":
	main()
