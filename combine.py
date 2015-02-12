
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
    df.to_csv('output/unilateral.csv')
    df['alpha3'] = df.index
    
    bilateral_df = pd.DataFrame(sources.cepii_df.index)
    bilateral_df['alpha3'] = sources.cepii_df['iso_o']
    bilateral_df['alpha3_other'] = sources.cepii_df['iso_d']
    bilateral_df['dist_capital'] = sources.cepii_df['distcap']
    print len(bilateral_df)
    us_df = bilateral_df[bilateral_df.alpha3 == 'usa']
    print len(us_df)
    us_df = pd.merge(
        us_df, sources.troop_df, how='inner', left_on='alpha3_other', right_on='alpha3')
    print len(us_df)
    us_df = pd.merge(
        us_df
        , sources.ita_import_df
        , how='inner'
        , left_on='alpha3_other'
        , right_on='alpha3'
    )
    print len(us_df)
    us_df = pd.merge(
        us_df
        , sources.ita_export_df
        , how='inner'
        , left_on="alpha3_other"
        , right_on="alpha3"
    )
    print len(us_df)
    us_df = pd.merge(
        us_df
        , df
        , how='inner'
        , left_on='alpha3_other'
        , right_on='alpha3')
    us_df.set_index('alpha3_other')
    print len(us_df)
    us_df.to_csv('output/usa_bilateral.csv')
if __name__ == '__main__':
    main()
