# import pandas as pd
# # obj= pd.Series([4,7,-5,3],index=['d','b','a','c'])
# # print(obj)
# # print(obj.values)


# # obj=pd.Series([4,7,-5,3],index=['d','b','a','c'])
# # print('b' in obj)
# # print('e' in obj)


# sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
# obj=pd.Series(sdata)
# print(obj)
# states=['California','Ohio','Oregon','Texas']
# obj2 =pd.Series(sdata,index=states)
# print(obj2)
# print(obj+obj2)




import pandas as pd

data ={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
'year':[2000,2001,2002,2001,2002,2003],
'pop':[1.5, 1.7,3.6,2.4,2.9,3.2]}
frame=pd.DataFrame(data,
columns=['year','state','pop','debt'],
index=['one','two','three','four','five','six'])
print(frame)


frame['eastern']=(frame.state=='Ohio')
print(frame)

del frame['eastern']
print(frame)