#!/usr/bin/python
import sys
infile = sys.argv[1]

input = open(infile, "r")

lignes = ["A", "B", "C", "D", "E", "F", "G", "H"]

header = input.readline().strip().split("\t")
cnt = -1

res = ""
for i in input:
	cnt += 1
	i = i.strip().split("\t")
	for j in range(len(i))[1:]:
		res += "{0}_{1}\t{2}\n".format(lignes[cnt], j, i[j].replace("/", "_"))
input.close()

print(res)

