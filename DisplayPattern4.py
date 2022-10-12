#Write a program which accept one number from user and display below pattern
#Input : 5
#Output : 1 
#         1 2 
#         1 2 3 
#         1 2 3 4  
#         1 2 3 4 5

def Display(size):
	
	for i in range(1,size+1):
		for j in range(1,i+1):
			print(j,end=" ")
		print()

def main():
	print("Enter number :")
	no=int(input())
	
	Display(no)
	
if __name__=="__main__":
	main()
