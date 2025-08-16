import pandas as pd;
data={'student':["Amit","John","David","steve"],
      'rank':[1,4,5,2],
      'marks':[95,34,56,78]
      }
df=pd.DataFrame(data)
print("student records \n\n",df)

#assign index to each value
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD'])
print("student records \n\n",df)


#Access the only one value
print("\n Value=",df.loc['RowA','student'])


#Access with integer value
print("\n Value=",df.iloc[[0,3]])

#access col name
print("\n displaying the columns")
for col in df:
    print(col)

