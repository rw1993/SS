# -*- coding:utf-8 -*-

with open("STS.txt", "r") as f:
    for line in f.readlines():
        line = line[:-1]
        lines = line.split("\t")
        print lines
