
import csv
import numpy as np
import pandas as pd
import sources

def index_lower(df):
    df.index = map(str.lower, df.index)
    return df

def columns_lower(df):
    df.columns = map(str.lower, df.columns)
    return df

def main():
    df = pd.DataFrame(sources.code_df)
    df['population'] = index_lower(sources.pop_df)['population']
    df['total_gdp'] = index_lower(sources.gdp_df)['total_gdp']
    df['total_migrant_stock'] = index_lower(sources.migrant_df)['total_stock']
    df['migrant_per'] = df['total_migrant_stock'] / df['population']
    df['inet_users'] = index_lower(sources.inet_df)['inet_users']
    df['inet_pen'] = df['inet_users'] / df['population']
    df['dhl_gci_overall'] = index_lower(sources.dhl_df)['overall']
    df.to_csv('output/common.csv')
    
if __name__ == '__main__':
    main()
