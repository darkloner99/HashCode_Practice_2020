import sys
import pulp
import re
sliceMax, pizzaN = map(int, [int(x) for x in re.sub("\n", "", input()).split(" ")])
slices = [int(x) for x in re.sub("\n", "", input()).split(" ")]
p = [i for i in range(len(slices))]
prob = pulp.LpProblem("Pizza_hashcode", pulp.LpMaximize)
pizzas = pulp.LpVariable.dicts("slice", p, lowBound=0, upBound=1, cat=pulp.LpInteger)
prob += pulp.lpSum(pizzas[i]*slices[i] for i in range(len(slices)))
prob += pulp.lpSum(pizzas[i]*slices[i] for i in range(len(slices))) <=sliceMax
prob.solve()
results = {};score=0;
for k, v in pizzas.items():
    if(pulp.value(v)>0):results[k] = k
for k in results.keys():
    score+=slices[k]
print(score, file=sys.stderr) #Print score on stderr
print(str(len(results)))
for k in results.keys():
    print(str(k)+ " ",end="")