...
Input Format
Input consists of 4 integers. The first integer corresponds to x1x_1x1​. The second integer corresponds to y1y_1y1​. The third and fourth integers correspond to x2x_2x2​ and y2y_2y2​ respectively.
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]
Sample Input

1
2
3
6

Sample Output

The slope of the line joining Ajay's house and Binoy's house is 2.00
...
Solution

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 != x1:
    slope = (y2 - y1) / (x2 - x1)
    print(f"The slope of the line joining Ajay's house and Binoy's house is {slope:.2f}")
else:
    print("The line is vertical, slope is undefined")
