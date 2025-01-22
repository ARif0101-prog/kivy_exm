from select import select
import pandas as pd
df = pd.read_excel(io='C:/Users/arief/Dropbox/nav/python_OOP/kivyy/pandas/frm.xlsx', sheet_name=0)
#df= df['IP']
#df = df.index[1]
#select_row = df.loc[df['Jumlah Peralatan Keamanan Penerbangan']==2]
select_row = df.loc[:,~df.columns.isin(['Nomor Kontak Person','Email Kontak Person'])]
print(select_row)