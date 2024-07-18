
regex_pattern = '[0-9abcABC(+)#!$]'
df['STORE_LOCATION'] = df['STORE_LOCATION'].str.replace(regex_pattern, '', regex=True)
df['PRODUCT_ID'] = df['PRODUCT_ID'].str.replace('[a-zA-Z]', '', regex=True)
df['MRP'] = df['MRP'] .str.replace('$', '')
df['CP'] = df['MRP'] .str.replace('$', '')
df['DISCOUNT'] = df['MRP'] .str.replace('$', '')
df['SP'] = df['MRP'] .str.replace('$', '')

df.head( )