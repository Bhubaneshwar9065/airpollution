# import pandas as pd
# a = pd.Series(23)
# print(a)

# import pandas as pd

# a = pd.Series("Bhuban babu ")
# print(a)

# Serice in pandas 

# import pandas as pd
# a = [2,3,4,5,6,]
# var = pd.Series(a,index=['a','b','e','q','u'],dtype="float")

# print(var)
# print(type(var))
# print(var['e'])

# import pandas as pd
# dis = {"Name": ["python","Java","Javascript","C","C++"],"Pro":[12,34,56,34,67],"Rank":[1,2,3,4,5]}
# var = pd.Series(dis)
# print(var)


import pandas as pd
s = pd.Series(12,index=[1,2,3,4,5,6,7])
t = pd.Series(15,index=[2,3,4,5])
print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)