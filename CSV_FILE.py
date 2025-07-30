import pandas as pd 


dis = {"a":[1,2,3,4,5,6],"b":[7,8,9,12,34,46],"C":[33,55,11,34,78,99] }
d = pd.DataFrame(dis)
print(d)
d.to_csv("test_new3.csv",index=False,header=[1,2,3])