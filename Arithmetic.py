import pandas as pd
var = pd.DataFrame({"A":[11,22,13,40,15],"B":[15,61,17,18,19]})
# print(var)

# var["C"] = var["A"]+var["B"]
# var["D"] = var["A"]-var["B"]
# var["F"] = var["A"]*var["B"]
# var["E"] = var["A"]/var["B"]
# var["G"] = var["A"]%var["B"]
# print(var)


var["python"] = var["A"] <= 20
var["java"] = var["B"] >= 16
print(var)