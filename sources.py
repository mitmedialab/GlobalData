import pandas as pd

# Headers: alpha3,alpha2,label
code_file = 'external/country_codes.csv'
code_df = pd.DataFrame.from_csv(code_file)

# Headers: alpha3,alpha2,label
name_code_file = 'external/name_to_code.csv'
name_code_df = pd.DataFrame.from_csv(name_code_file, index_col=None)

# Sources: http://data.worldbank.org/indicator/SP.POP.TOTL
#          http://ebas1.ebas.gov.tw/phc2010/english/51/301.pdf
# Year: 2010
# Headers: alpha3,population
pop_file = 'external/population-2010.csv'
pop_df = pd.DataFrame.from_csv(pop_file)

# Source: http://www.imf.org/external/pubs/ft/weo/2014/01/weodata/weorept.aspx?sy=2010&ey=2010&sic=1&sort=country&ds=.&br=0&pr1.x=29&pr1.y=9&c=512,668,914,672,612,946,614,137,311,962,213,674,911,676,193,548,122,556,912,678,313,181,419,867,513,682,316,684,913,273,124,868,339,921,638,948,514,943,218,686,963,688,616,518,223,728,516,558,918,138,748,196,618,278,624,692,522,694,622,142,156,449,626,564,628,565,228,283,924,853,233,288,632,293,636,566,634,964,238,182,662,453,960,968,423,922,935,714,128,862,611,135,321,716,243,456,248,722,469,942,253,718,642,724,643,576,939,936,644,961,819,813,172,199,132,733,646,184,648,524,915,361,134,362,652,364,174,732,328,366,258,734,656,144,654,146,336,463,263,528,268,923,532,738,944,578,176,537,534,742,536,866,429,369,433,744,178,186,436,925,136,869,343,746,158,926,439,466,916,112,664,111,826,298,542,927,967,846,443,299,917,582,544,474,941,754,446,698,666&s=PPPPC&grp=0&a=
# Year: 2010
# Headers: alpha3,label,total_gdp
gdp_file = 'external/gdp-2010.csv'
gdp_df = pd.DataFrame.from_csv(gdp_file)

# Source: http://econ.worldbank.org/WBSITE/EXTERNAL/EXTDEC/EXTDECPROSPECTS/0,,contentMDK:22803131~pagePK:64165401~piPK:64165026~theSitePK:476883,00.html
# Year: 2010
# Headers: alpha3,label,total_stock
migrant_file = 'external/migrant-2010.csv'
migrant_df = pd.DataFrame.from_csv(migrant_file)

# Source: https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2153.txt
# Year: various
# Headers: alpha3,label,inet_users
inet_file = 'external/internet_users.csv'
inet_df = pd.DataFrame.from_csv(inet_file)

# Source: http://www.dhl.com/content/dam/Campaigns/gci2014/downloads/dhl_gci_2014_study_low.pdf
# Year: 2011
# Headers: alpha3,label,overall,depth,breadth
dhl_file = 'external/dhl_gci_2011.csv'
dhl_df = pd.DataFrame.from_csv(dhl_file)

# Source: http://tpis7.ita.doc.gov/TPIS_GREPORTS/tpis_ustopcmds1.aspx
# Year: various
# Headers: COUNTRY,FLOW,2010,2012,2013,2014,RANK 2014,SHARE 2014, CHANGE 2010-2014, CHANGE 2013-2014
ita_file = 'external/ita_trade.csv'
ita_df = pd.DataFrame.from_csv(ita_file, index_col=None)
ita_df = pd.merge(
    name_code_df
    , ita_df
    , how='inner'
    , left_on='label'
    , right_on='COUNTRY'
)
ita_import = ita_df[ita_df.FLOW == 'IMPORTS']
ita_export = ita_df[ita_df.FLOW == 'EXPORTS']
