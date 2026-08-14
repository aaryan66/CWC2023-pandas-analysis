import pandas as pd

#csv -> pd dataframe
cwc = pd.read_csv("CWC2023.csv")

#before cleaning the data we hvae 48 entries including the null values if there are any
print(cwc.info())

