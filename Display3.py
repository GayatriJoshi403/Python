#Write a program which accept number from user and print that number of "*" on screen
#Input : 5
#Output:* * * * * 

def Display(value):
	
	for i in range(0,value):
		print("*",end=" ")	
	print()
	
def main():
	
	print("Enter number")
	no=int(input())
	
	Display(no)

if __name__=="__main__":
	main()

