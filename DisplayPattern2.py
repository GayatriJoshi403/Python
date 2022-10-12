#Write a program which accept one number from user and display below pattern
#Input : 5
#Output : * * * * * 
#         * * * * 
#         * * * 
#         * * 
#         * 

def Display(size):
	
	for i in range(0,size):
		for j in range(size,i,-1):
			print("*",end=" ")
		print()

def main():
	print("Enter number :")
	no=int(input())
	
	Display(no)
	
if __name__=="__main__":
	main()
