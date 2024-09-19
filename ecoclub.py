...
Input format:
The first input containing an integer which denotes the number of the month
Output format:
Print the amoeba size.
Refer the sample output for formatting.
Sample Input:
7
Sample Output:
8
....
n=int(input())
a=0
b=1
for i in range (3,n+1):
	c=a+b
	a=b
	b=c
print (c)
