import pandas as pd
import matplotlib as plt

df = pd.read_csv("https://raw.githubusercontent.com/borgesconsultoriatutoria/ComputacaoCognitiva/main/GlobalLandTemperatures_GlobalLandTemperaturesByMajorCity.csv")
df = df.dropna()


#print(df)
df = df.query('City == "São Paulo"')
df = df[["dt", "AverageTemperature"]]
df['dt'] = pd.to_datetime(df['dt'])
df.set_index('dt', inplace=True)
print(df)
df.plot()
plt.title("Histórico de Temperatura na cidade de São Paulo")
plt.xlabel("Data")
plt.ylabel("Temperatura")
plt.show()