#!/usr/bin/env python3

def shattered_cake():
	width = int(input());
	n = int(input());
	sum = 0;
	for i in range(n):
		inp = input();
		sum = sum + int(inp.split()[0])*int(inp.split()[1]);
	print(int(sum/width));

if __name__ == '__main__':
    shattered_cake();
