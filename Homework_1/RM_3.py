task_test_1 = ([1, 3, 3, 3, 5, 5, 5], 2)
a, k = task_test_1
dd = {x: 0 for x in set(a)}
for x in a:
    dd[x] += 1

da = {x + 1: [] for x in range(max(dd.values()))}
for x in dd:
    da[dd[x]].append(x)

tmp_res = []
for x in range(max(dd.values()),0,-1):
    tmp_res += da[x]

res = []
for x in range(0,k):
    res.append(tmp_res[x])

print(res)


