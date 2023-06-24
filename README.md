# NBA Advanced stats filters

Generated data through links (BBReference) or manually (RAPTOR and LEBRON) from the respective websites (538 and BBIndex). I then use simple filtering mechanisms from pandas to create dataframes containing the players that might be interesting to look at.

The filtering is under the format

```python
nbaStats = nbaStats[(nbaStats['OFFRTG'].astype(float) >= 114.3)].reset_index().drop(['index'],axis=1)
```

