#Census Tracts started as population groups of about 10,000 people, and are probably my best bet
#alternatively I could use FSAs
#I'll have to do the math in Python
#pull the postal codes from our best performing polls in 2017 and 2020
#get the gender percentage, average income, % english speaker, average age, ethnicity/race, education
#maybe come up with a score of some kind? Or a basic ML model for Python
#create categories for good and bad FSAs
#then search through the CTs to find



import pandas
df = pandas.read_csv('FSA_Census_2016_Profile_Data.csv')
print(df.head())
print(df.columns)
# df["prov"] = df.FSA.str[0]
# new_df = df.loc[df['prov']=="V"]
# print(new_df.size)
# new_df.to_csv('BC_PCCF.csv')
