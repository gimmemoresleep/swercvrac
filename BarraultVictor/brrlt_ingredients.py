#!/usr/bin/env python3

def find(needle, haystack) :
	for i in range(len(haystack)):
		if haystack[i][0] == needle :
			return (haystack[i][1], haystack[i][2])
	return (0,0)

def add(plat, list) :
	found = False
	i = 0
	if len(list) == 0:
		list.append(plat)
		return (list, 0)
	for i in range(len(list)):
		if plat[0] == list[i][0]:
			if list[i][1] > plat[1]:
				list[i][1] = plat[1]
				list[i][2] = plat[2]
				found = True
			elif list[i][1] == plat[1] and list[i][2] < plat[2]:
				list[i][1] = plat[1]
				list[i][2] = plat[2]
				found = True
	if found == False :
		list.append(plat)
		return (list, len(list)-1)
	return (list, i)

def contains (name, list):
	for i in range(len(list)) :
		if list[i][0] == name :
			return True
	return False

B = int(input())
N = int(input())
prest = 0
prix = 0
prestige = []
res = []
for i in range(N) :
	inn = input().split()
	(ingprest, ingprix) = find(inn[1], prestige);
	(prestige, pos) = add([inn[0], int(inn[3]) + ingprest, int(inn[4]) + ingprix], prestige);
for i in range(len(prestige)):
	if (prix + prestige[i][1]) <= B :
		prest = prest + prestige[i][2]
		prix = prix + prestige[i][1]
		res.append(prestige[i])

for i in range(len(res)):
	for j in range(len(prestige)):
		if (prix - res[i][1] + prestige[j][1] <= B) and (res[i][2] < prestige[j][2]) and not contains(prestige[j][0], res):
			prest = prest - res[i][2] + prestige[j][2]
			prix = prix - res[i][1] + prestige[j][1]
			res[i][0] = prestige[j][0]
			res[i][1] = prestige[j][1]
			res[i][2] = prestige[j][2]


#print(res)
print(prix)
print(prest)
