...
Input Format:
First line of the input is an integer that specifies Dhoni's income in rupees from Salary.
Second line is an integer that specifies Dhoni's income in rupees from Bonuses and Awards.
Third line is an integer that specifies Dhoni's income in rupees from endorsements.
Output Format:
Output should display 3 floats in a line, separated by a space. The first float corresponds to the percentage of income from Salary, the second float corresponds to the percentage of income from Bonuses and Awards and the third float corresponds to the percentage of income from endorsements.
All float values should be displayed correct to 2 decimal places.
Sample Input and Output 1:
100
20
80
50.00 10.00 40.00
Sample Input and Output2:
50000
10000
35000
52.63 10.53 36.84
...
s=int(input ())
b=int(input ())
e=int(input ())
ti=s+b+e
ps=(s/ti)*100
pb=(b/ti)*100
pe=(e/ti)*100
print("%.2f"%ps,"%.2f"%pb,"%.2f"%pe)

