...
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
Print the  'n' terms of the Lucas Sequence, separated by a single space. There are no leading or trailing spaces in the output.
Refer the sample output for formatting.
Sample Input:
5
Sample Output:
0 0 1 1 2
...
n=int(input())
a=0
b=0
c=1
print(a,end=’ ‘)
print(b,end=’ ‘)
print(c,end=’ ‘)
for i in range (4,n+1):
	d=a+b+c
	a=b
	b=c
	c=d
	print(d,end=’ ‘)
