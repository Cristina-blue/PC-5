import pandas as pd

file_path = '/workspaces/PC-5/PROBLEMA 2/winemag.csv'  
df = pd.read_csv(file_path)

print("Nombres de las columnas originales:")
print(df.columns)


df.rename(columns={
    'country': 'Country',
    'description': 'Description',
    'points': 'Points',
    'price': 'Price',
    'variety': 'Variety',
    'winery': 'Winery',

}, inplace=True)


print("\nNombres de las columnas después del renombrado:")
print(df.columns)

# Reporte 1: Por continente mostrar los vinos mejor puntuados
top_wines_by_continent = df.groupby('Country')['Points'].max().reset_index()
top_wines_by_continent['Continent'] = top_wines_by_continent['Country'].map({
    'Italy': 'Europe',
    'France': 'Europe',
    'Spain': 'Europe',
    'USA': 'North America',
    'Argentina': 'South America',
    'Chile': 'South America',
})
top_wines_by_continent = top_wines_by_continent.groupby('Continent').agg({'Points': 'max'}).reset_index()
print("\nReporte 1: Vinos mejor puntuados por continente:")
print(top_wines_by_continent)

# Reporte 2: Promedio de precio de vino y cantidad de reviews obtenidos según país
if 'Description' in df.columns:
    df['Reviews'] = df['Description'].apply(lambda x: x.count('.') + 1)
else:
    df['Reviews'] = 0  

average_price_reviews = df.groupby('Country').agg({'Price': 'mean', 'Reviews': 'sum'}).reset_index()
average_price_reviews = average_price_reviews.sort_values(by='Price', ascending=False)
print("\nReporte 2: Promedio de precio de vino y cantidad de reviews por país:")
print(average_price_reviews)

# Reporte 3: Cantidad de vinos por variedad
wines_by_variety = df['Variety'].value_counts().reset_index()
wines_by_variety.columns = ['Variety', 'Count']
print("\nReporte 3: Cantidad de vinos por variedad:")
print(wines_by_variety)

# Reporte 4: Distribución de precios de vinos en función de la puntuación
price_distribution = df[['Points', 'Price']]
price_distribution = price_distribution.sort_values(by='Points', ascending=False)
print("\nReporte 4: Distribución de precios de vinos según puntuación:")
print(price_distribution)

