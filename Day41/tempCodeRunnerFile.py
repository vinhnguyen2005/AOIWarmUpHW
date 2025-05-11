df['Population'] = df['Population'].str.replace(',', '').astype(int)
df['Land Area (km2)'] = df['Land Area (km2)'].str.replace(',', '').astype(int)

convert_dict = {
    'Population': int,
    'Land Area (km2)': int,
}
df = df.astype(convert_dict)
print(df.info())