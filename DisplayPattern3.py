#Write a program which accept one number from user and display below pattern
#Input : 5
#Output : 1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5 
#         1 2 3 4 5

def Display(size):
	
	for i in range(0,size):
		for j in range(1,size+1):
			print(j,end=" ")
		print()

def main():
	print("Enter number :")
	no=int(input())
	
	Display(no)
	
if __name__=="__main__":
	main()
