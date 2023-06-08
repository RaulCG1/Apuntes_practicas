import pandas as banana

df= banana.read_csv("C:/Users/rulas/OneDrive/Escritorio/Python/curso1/Libro1.csv")
print(df.head(5))
df1= df[["Rating (friends)","Artist"]]
print(df1.head(5))

print(df.iloc[1,2])
#df1.head()
new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index=new_index
print(df_new.loc['a', 'Artist'])
print(df_new.loc['a':'d', 'Artist'])

#print(df_new.head())