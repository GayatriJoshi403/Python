#Write a program which accept one number from user and return addition of its factor
#Input : 12
#Output : (1+2+3+4+6)=16

def DisplayFactor(value):
	
	Ans=0
	i=1
	#for i in range(1,int(value/2)+1):
		#if(value%i==0):
			#Ans=Ans+i
	#return Ans
	
	while(i<=int(value/2)):
		if(value%i==0):
			Ans=Ans+i
		i=i+1
	return Ans	

def main():

	print("Enter number :")
	no=int(input())
	
	iRet=DisplayFactor(no)
	
	print("Addition of factors is :",iRet)

if __name__=="__main__":
	main()
