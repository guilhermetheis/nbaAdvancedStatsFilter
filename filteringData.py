# -*- coding: utf-8 -*-
"""
@author: Guilherme
"""


import pandas as pd

init_df = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2023_advanced.html#advanced_stats')[0]

# removing stuff out
df = init_df[init_df.iloc[:, 0] != init_df.columns[0]]
df = df.iloc[:, ~df.columns.str.contains('^Unnamed')]
df = df.drop_duplicates(subset='Player', keep='first').reset_index()
df = df.drop(['index'], axis=1)

df_PG = df[df['Pos'].str.contains('PG')].reset_index().drop(['index'], axis=1)
df_SG = df[df['Pos'].str.contains('SG')].reset_index().drop(['index'], axis=1)
df_SF = df[df['Pos'].str.contains('SF')].reset_index().drop(['index'], axis=1)
df_PF = df[df['Pos'].str.contains('PF')].reset_index().drop(['index'], axis=1)
df_C = df[df['Pos'].str.contains('C')].reset_index().drop(['index'], axis=1)

# Remove negative VORP players

df_PG = df_PG[(df_PG['VORP'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
df_SG = df_SG[(df_SG['VORP'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
df_SF = df_SF[(df_SF['VORP'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
df_PF = df_PF[(df_PF['VORP'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
df_C = df_C[(df_C['VORP'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)

# For PGs

df_PG = df_PG[(df_PG['AST%'].astype(float) >= 20)].reset_index().drop(['index'],axis=1)
df_PG = df_PG[(df_PG['TOV%'].astype(float) <= 15)].reset_index().drop(['index'],axis=1)
df_PG = df_PG[(df_PG['USG%'].astype(float) <= 20)].reset_index().drop(['index'],axis=1)

# For Wings?

df_SG = df_SG[(df_SG['TOV%'].astype(float) <= 14)].reset_index().drop(['index'],axis=1)
df_SG = df_SG[(df_SG['USG%'].astype(float) <= 20)].reset_index().drop(['index'],axis=1)
df_SG = df_SG[(df_SG['DBPM'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
df_SG = df_SG[(df_SG['G'].astype(float) >= 50)].reset_index().drop(['index'],axis=1)
df_SG = df_SG[(df_SG['3PAr'].astype(float) >= 0.4)].reset_index().drop(['index'],axis=1)


df_SF = df_SF[(df_SF['TOV%'].astype(float) <= 12)].reset_index().drop(['index'],axis=1)
df_SF = df_SF[(df_SF['USG%'].astype(float) <= 20)].reset_index().drop(['index'],axis=1)
df_SF = df_SF[(df_SF['DBPM'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
df_SF = df_SF[(df_SF['G'].astype(float) >= 50)].reset_index().drop(['index'],axis=1)
df_SF = df_SF[(df_SF['3PAr'].astype(float) >= 0.4)].reset_index().drop(['index'],axis=1)

# For bigs?


df_PF = df_PF[(df_PF['TOV%'].astype(float) <= 10)].reset_index().drop(['index'],axis=1)
df_PF = df_PF[(df_PF['USG%'].astype(float) <= 20)].reset_index().drop(['index'],axis=1)
df_PF = df_PF[(df_PF['DBPM'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
df_PF = df_PF[(df_PF['G'].astype(float) >= 50)].reset_index().drop(['index'],axis=1)


df_C = df_C[(df_C['TOV%'].astype(float) <= 12)].reset_index().drop(['index'],axis=1)
df_C = df_C[(df_C['USG%'].astype(float) <= 20)].reset_index().drop(['index'],axis=1)
df_C = df_C[(df_C['DBPM'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
df_C = df_C[(df_C['G'].astype(float) >= 50)].reset_index().drop(['index'],axis=1)

# to markdown

df_C.to_csv('Centers.csv', stralign='left',numalign='center', index=False, floatfmt='.3f')
df_SG.to_csv('Shooting Guards.csv', stralign='left',numalign='center', index=False, floatfmt='.3f')
df_PG.to_csv('Point Guards.csv', stralign='left',numalign='center', index=False, floatfmt='.3f')
df_SF.to_csv('Small Forwards.csv', stralign='left',numalign='center', index=False, floatfmt='.3f')
df_PF.to_csv('Power Forwards.csv', stralign='left',numalign='center', index=False, floatfmt='.3f')

##### NBA Stats Advanced

nbaStats = pd.read_csv('data.csv')

nbaStats = nbaStats.iloc[:, ~nbaStats.columns.str.contains('^Unnamed')]

nbaStats = nbaStats[(nbaStats['GP'].astype(float) >= 40)].reset_index().drop(['index'],axis=1)
nbaStats = nbaStats[(nbaStats['NETRTG'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
nbaStats = nbaStats[(nbaStats['AST/TO'].astype(float) >= 2)].reset_index().drop(['index'],axis=1)
nbaStats = nbaStats[(nbaStats['USG%'].astype(float) <= 20)].reset_index().drop(['index'],axis=1)

# OFFRTG = 114.3 DRTG 110.3 --> 5th place cut-off (teams)


nbaStats = nbaStats[(nbaStats['OFFRTG'].astype(float) >= 114.3)].reset_index().drop(['index'],axis=1)
nbaStats = nbaStats[(nbaStats['DEFRTG'].astype(float) <= 110.3)].reset_index().drop(['index'],axis=1)

nbaStats.to_markdown('NBA Advanced stats.csv')

#RAPTOR
raptor = pd.read_csv('latest_RAPTOR_by_player.csv')
raptor = raptor[(raptor['mp'].astype(float) >= 500)].reset_index().drop(['index'],axis=1)
raptor = raptor[(raptor['raptor_defense'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
raptor = raptor[(raptor['raptor_offense'].astype(float) >= -0.5)].reset_index().drop(['index'],axis=1)
raptor = raptor[(raptor['war_reg_season'].astype(float) >= 1)].reset_index().drop(['index'],axis=1)
raptor = raptor[(raptor['raptor_onoff_total'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)

# LEBRON 

LEBRON  = pd.read_csv('LEBRON.csv', thousands=',')
LEBRON = LEBRON[(LEBRON['Minutes'].astype(float) >= 500)].reset_index().drop(['index'],axis=1)
LEBRON = LEBRON[(LEBRON['LEBRON'].astype(float) >= -0.5)].reset_index().drop(['index'],axis=1)
LEBRON = LEBRON[(LEBRON['O-LEBRON'].astype(float) >= -0.5)].reset_index().drop(['index'],axis=1)
LEBRON = LEBRON[(LEBRON['D-LEBRON'].astype(float) >= 0.5)].reset_index().drop(['index'],axis=1)
LEBRON = LEBRON[(LEBRON['WAR'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
LEBRON = LEBRON[(LEBRON['BOX-LEBRON'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)
LEBRON = LEBRON[(LEBRON['BOX-D-LEBRON'].astype(float) >= 0)].reset_index().drop(['index'],axis=1)

