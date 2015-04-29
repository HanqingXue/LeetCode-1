"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 


MATRIX IMPLEMENTATION NAIVE
"""
def convert(s, numRows):
	matrix = [list() for _ in range(numRows)]
	length_s = 0
	while length_s != len(s):
		for i in range(numRows):
			if length_s != len(s):
				matrix[i].append(s[length_s])
				length_s += 1
				#print("1st", i, length_s)
			else:
				break
		for i in range(numRows - 2, 0, -1):
			if length_s != len(s):
				matrix[i].append(s[length_s])
				length_s += 1
				#print("2nd", i, length_s)
			else:
				break
	#print(matrix)
	return "".join(["".join(char) for char in matrix])

print(convert("PAYPALISHIRING", 3))


