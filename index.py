import pandas as pd

auto = pd.read_csv('auto-mpg-original.csv', sep=';')
# como contabilizar os NA?
# total de linhas - a quantidade de linhas NA em um arquivo csv utilizando pandas?
df_auto = pd.DataFrame(auto)
print(df_auto)

# na_count = auto.isnull().sum()

# print(na_count)
# auto.mpg = auto.mpg.astype(str)
# max_mpg = auto.mpg.max()

# print(f'{max_mpg=}')

iqr_auto = df_auto.horsepower.iqr()
print(iqr_auto)