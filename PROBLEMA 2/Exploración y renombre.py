import pandas as pd

file_path = '/workspaces/PC-5/PROBLEMA 2/winemag.csv'  # Cambia esto según la ubicación de tu archivo
df = pd.read_csv(file_path)

print("Primeras filas del DataFrame:")
print(df.head())

print("\nInformación del DataFrame:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

df.rename(columns={
    'country': 'Country',
    'description': 'Description',
    'points': 'Points',
    'price': 'Price',
    'variety': 'Variety', 
    'winery': 'Winery' 
}, inplace=True)


continent_mapping = {
    'Italy': 'Europe',
    'France': 'Europe',
    'Spain': 'Europe',
    'USA': 'North America',
    'Argentina': 'South America',
    'Chile': 'South America',
}
df['Continent'] = df['Country'].map(continent_mapping)

df['Is_Expensive'] = df['Price'].apply(lambda x: 'Yes' if x > 50 else 'No')

df['Description_Length'] = df['Description'].str.len()

print("\nDataFrame después de renombrar y crear nuevas columnas:")
print(df.head())




