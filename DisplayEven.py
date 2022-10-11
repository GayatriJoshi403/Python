#Write a program which display first 10 even numbers on screen.

#Output : 2,4,6,8,10,12,14,16,18,20

def DisplayEven():
	
	for i in range(1,10+1):
		print(i*2,end=" ")
	print()
	
def main():

	DisplayEven()	
	
if (__name__=="__main__"):
	main()
