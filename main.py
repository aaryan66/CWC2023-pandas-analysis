import pandas as pd

#csv -> pd dataframe
cwc = pd.read_csv("CWC2023.csv")

#before cleaning the data we hvae 48 entries including the null values if there are any
print(cwc.info())


#to see if there is any null values

print(cwc.isnull().sum()) 
# there are no null values implying that all the 48 rows contains matches with winners and result and no game had ended on N/R
# further checking was done via points table and the results were consistent with the data in the csv file

