 #insert
import pandas as pd 
var = pd.DataFrame({"A":[1,2,3,4,5,6],"B":[9,8,6,5,4,10]})
# print(var)

var.insert(1,"java",var["A"])
var.insert(2,"python",var["B"])

var ["python_12"] = var["A"][:4]
print(var)

#Delection

import pandas as pd
var = pd.DataFrame({"A":[1,2,3,4,5,6],"B":[11,12,13,14,16,17],"C":[22,33,44,55,66,77,]})
# print(var)

Delet = var.pop("B")
Delet = var.pop("C")
print(var)