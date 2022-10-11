#Write a program which accept name from user and display length of its name
#Input  :Marvellous
#Output : 10

def DisplayLength(str1):
	
	print("Length of string is : ",len(str1))

def main():

	print("Enter Name")
	str1=input()
	
	DisplayLength(str1)

if __name__=="__main__":
	main()
