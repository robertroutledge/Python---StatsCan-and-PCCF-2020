#this file opens the full PCCF file and scrapes it for FSAs that start with V - should catch all of BC
import pandas
df = pandas.read_csv('pccf_subset_test.tsv', sep='\t',encoding='cp1252')
df["prov"] = df.FSA.str[0]
new_df = df.loc[df['prov']=="V"]
print(new_df.size)
new_df.to_csv('BC_PCCF.csv')

