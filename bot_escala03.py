import pandas

def pl(x):
    print(x)
    print('\n')

df = pandas.DataFrame(
    {
        'Data' : [],
        'Dia da semana' : [],
        'Escala' :  []
    }
).astype(object)

pl(df.dtypes)
pl(df)


df.set_index('Data', inplace=True)
df.astype(str)
df.loc[ 'Dia 1' , ['Dia da semana','Escala']] = ['quinta', 'turno a']
pl(df)

