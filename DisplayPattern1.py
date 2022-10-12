#Write a program which accept one number from user and display below pattern
#Input : 5
#Output : * * * * * 
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *

def DisplayPattern(size):

	for i in range(0,size):
		
		for j in range(0,size):
			
			print("*",end=" ")
		print()
	

def main():
	
	print("Enter number :")
	no=int(input())

	DisplayPattern(no)

if __name__=="__main__":
	main()
