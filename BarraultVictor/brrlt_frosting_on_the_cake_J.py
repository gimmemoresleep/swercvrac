#!/usr/bin/env python3

def frosting_cake():
	n = int(input());
	a = input();
	b = input();
	a_t = [int(x) for x in a.split()];
	b_t = [int(x) for x in b.split()];
	res = [0,0,0];
	store_a = [0,0,0];
	store_b = [0,0,0];
	for i in [0,1,2] :
		for j in range(i, n, 3) :
			store_b[i] += b_t[j]
			store_a[i] += a_t[j]
	res = [store_b[2]*store_a[2]+store_b[0]*store_a[1]+store_b[1]*store_a[0],
		store_b[2]*store_a[0]+store_b[0]*store_a[2]+store_b[1]*store_a[1],
        store_b[2]*store_a[1]+store_b[0]*store_a[0]+store_b[1]*store_a[2]]
	print(res[0], res[1], res[2]);


if __name__ == '__main__':
    frosting_cake();
