#!/usr/bin/env python3

def check_the_cheque():
	res = 0
	while(input() != "TOTAL"):
		inp = input()
		res = res + int(inp.split()[0]) * int(inp.split()[1])
	if res <= int(input()) :
		print("PROTEST")
	else :
		print("PAY")

if __name__ == '__main__':
    check_the_cheque();
