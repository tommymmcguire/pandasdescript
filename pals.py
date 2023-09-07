import pandas as pd

def data_desc(csv_url):
    df = pd.read_csv(csv_url, index_col=0)
    df.drop(['grape'], axis=1, inplace=True)
    return df['rating'].count()
# print(df.describe())

