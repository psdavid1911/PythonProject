import pandas as pd

def pl(x):
    print(x)
    print('\n')


df = pd.DataFrame({
    'Weight': [45, 88, 56, 15, 71],
    'Name': ['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
    'Age': [14, 25, 55, 8, 21]
}).astype(object)

pl(df)
# pl(df.loc[ 1:3 , ['Weight' ,   'Name'  ,'Age']])
#
# pl(df.loc[ :, ])
#
# df.loc[ 1 , ['Weight' ,   'Name'  ,'Age']] = [100, 'David', 33]
# pl(df)


df.set_index('Weight', inplace=True)
pl(df)
#
# df.loc[ 88 , ['Name',  'Age']] = ['David', 33]
# pl(df)


pl(df.loc[[88, ]])

pl(df.loc[[88, ]])

try:
    pl(df.loc[[100, ]])
except:
    pl('inexistente')


df.loc[[88, ]] = ['David', '33']
pl(df)