# Euro 2020 (2021) Predictions

<!-- Written report for this analysis can be found [here](../reports/boro_01_market_value.md) -->

## 1. Business Understanding

* Determine Busines Objectives
* Situation Assessment
* Determine Data Mining Goal
* Produce Project Plan

```
# 1. Predict results of every match at Euro 2020
# 2. Make predictions before each round of competition
# 3. Ideally, at each round, use the predictions to simulate remainder of competition
# 4. Check against other predictions and actual results
# 5. Write up process (report/blog)
```

## 2. Data Understanding

* Collect Initial Data
* Describe Data
* Explore Data
* Verify Data Quality

    2021-06-28 20:56:01,530 - INFO - Building master filepath for nations_matches
    2021-06-28 20:56:01,534 - INFO - Fetching C:\Users\adeacon\Documents\GitHub\the-ball-is-round\data\processed\ftb_nations_matches.txt
    2021-06-28 20:56:01,535 - INFO - Building master filepath for nations_matches
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Round</th>
      <td>211</td>
      <td>5</td>
      <td>Group stage</td>
      <td>168</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Day</th>
      <td>211</td>
      <td>7</td>
      <td>Sun</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Date</th>
      <td>211</td>
      <td>110</td>
      <td>2016-06-21</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Time</th>
      <td>211</td>
      <td>16</td>
      <td>20:45 (19:45)</td>
      <td>52</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Team_1</th>
      <td>211</td>
      <td>35</td>
      <td>Portugal</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Team_2</th>
      <td>211</td>
      <td>35</td>
      <td>Portugal</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Year</th>
      <td>211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2010.98</td>
      <td>7.05586</td>
      <td>2000</td>
      <td>2004</td>
      <td>2012</td>
      <td>2016</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>Goals_1</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.46857</td>
      <td>1.34672</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Goals_2</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.11429</td>
      <td>1.00491</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Goal_diff</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.354286</td>
      <td>1.75845</td>
      <td>-4</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Venue</th>
      <td>211</td>
      <td>55</td>
      <td>Johan Cruyff ArenA</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Venue_country</th>
      <td>155</td>
      <td>14</td>
      <td>France</td>
      <td>45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Venue_city</th>
      <td>155</td>
      <td>37</td>
      <td>Amsterdam</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Home_1</th>
      <td>211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.132701</td>
      <td>0.340059</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Home_2</th>
      <td>211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0900474</td>
      <td>0.28693</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Goal_total</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.58286</td>
      <td>1.5984</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Result</th>
      <td>175</td>
      <td>3</td>
      <td>Win</td>
      <td>77</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



    
    Goals_1
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_6_1.png)
    


    
    --------------------
    
    Goals_2
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_6_3.png)
    


    
    --------------------
    
    Goal_diff
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_6_5.png)
    


    
    --------------------
    
    Goal_total
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_6_7.png)
    


    
    --------------------
    

    
    Round
    
    Group stage       132
    Quarter-finals     20
    Semi-finals        10
    Round of 16         8
    Final               5
    Name: Round, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_1.png)
    


    
    --------------------
    
    Day
    
    Sun    36
    Sat    30
    Wed    27
    Mon    23
    Tue    22
    Thu    19
    Fri    18
    Name: Day, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_3.png)
    


    
    --------------------
    
    Time
    
    20:45 (19:45)    52
    18:00 (17:00)    38
    21:00 (20:00)    27
    19:45            23
    21:45 (19:45)    11
    15:00 (14:00)     9
    17:00             8
    19:00 (17:00)     4
    22:00 (20:00)     1
    14:30 (13:30)     1
    20:00 (19:00)     1
    Name: Time, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_5.png)
    


    
    --------------------
    
    Year
    
    2016    51
    2012    31
    2008    31
    2004    31
    2000    31
    Name: Year, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_7.png)
    


    
    --------------------
    
    Venue_country
    
    NULL           47
    France         45
    Netherlands    16
    Ukraine        16
    Belgium        15
    Austria        13
    Switzerland    12
    Poland         11
    Name: Venue_country, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_9.png)
    


    
    --------------------
    
    Result
    
    Win     77
    Loss    66
    Draw    32
    Name: Result, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_11.png)
    


    
    --------------------
    

    2021-06-28 20:56:03,213 - INFO - Building master filepath for nations_summaries
    2021-06-28 20:56:03,214 - INFO - Fetching C:\Users\adeacon\Documents\GitHub\the-ball-is-round\data\processed\ftb_nations_summaries.txt
    2021-06-28 20:56:03,215 - INFO - Building master filepath for nations_summaries
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rank Local</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.1964</td>
      <td>6.06398</td>
      <td>1</td>
      <td>5</td>
      <td>10</td>
      <td>14.25</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Rank Global</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>18.6964</td>
      <td>14.7769</td>
      <td>1</td>
      <td>8</td>
      <td>15</td>
      <td>26</td>
      <td>74</td>
    </tr>
    <tr>
      <th>Team</th>
      <td>112</td>
      <td>35</td>
      <td>Czech Republic</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Rating</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1856</td>
      <td>122.945</td>
      <td>1524</td>
      <td>1771.25</td>
      <td>1853</td>
      <td>1948.25</td>
      <td>2127</td>
    </tr>
    <tr>
      <th>Average Rank</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22.5268</td>
      <td>16.0921</td>
      <td>4</td>
      <td>11</td>
      <td>19</td>
      <td>27.25</td>
      <td>83</td>
    </tr>
    <tr>
      <th>Average Rating</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1769.49</td>
      <td>128.753</td>
      <td>1390</td>
      <td>1704.75</td>
      <td>1785.5</td>
      <td>1875.25</td>
      <td>1985</td>
    </tr>
    <tr>
      <th>1 Year Change Rank</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.41071</td>
      <td>5.92073</td>
      <td>-15</td>
      <td>-2</td>
      <td>1</td>
      <td>4</td>
      <td>23</td>
    </tr>
    <tr>
      <th>1 Year Change Rating</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.26786</td>
      <td>42.6667</td>
      <td>-92</td>
      <td>-24.25</td>
      <td>7.5</td>
      <td>35.25</td>
      <td>127</td>
    </tr>
    <tr>
      <th>Matches Total</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>638.009</td>
      <td>214.417</td>
      <td>63</td>
      <td>537.25</td>
      <td>659.5</td>
      <td>787</td>
      <td>1073</td>
    </tr>
    <tr>
      <th>Matches Home</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>285.482</td>
      <td>98.4145</td>
      <td>23</td>
      <td>223</td>
      <td>295</td>
      <td>360</td>
      <td>467</td>
    </tr>
    <tr>
      <th>Matches Away</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>282.17</td>
      <td>99.397</td>
      <td>32</td>
      <td>223.25</td>
      <td>290.5</td>
      <td>344</td>
      <td>494</td>
    </tr>
    <tr>
      <th>Matches Neutral</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>70.3571</td>
      <td>33.2126</td>
      <td>8</td>
      <td>44</td>
      <td>68</td>
      <td>94</td>
      <td>157</td>
    </tr>
    <tr>
      <th>Matches Wins</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>298.768</td>
      <td>128.751</td>
      <td>21</td>
      <td>209</td>
      <td>303.5</td>
      <td>383.25</td>
      <td>628</td>
    </tr>
    <tr>
      <th>Matches Losses</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>194.812</td>
      <td>74.8451</td>
      <td>26</td>
      <td>145</td>
      <td>193.5</td>
      <td>246.5</td>
      <td>410</td>
    </tr>
    <tr>
      <th>Matches Draws</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>144.429</td>
      <td>45.8214</td>
      <td>16</td>
      <td>122.5</td>
      <td>148</td>
      <td>174</td>
      <td>244</td>
    </tr>
    <tr>
      <th>Goals For</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1157.33</td>
      <td>528.22</td>
      <td>83</td>
      <td>821.5</td>
      <td>1175</td>
      <td>1432</td>
      <td>2513</td>
    </tr>
    <tr>
      <th>Goals Against</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>852.866</td>
      <td>323.145</td>
      <td>87</td>
      <td>638.25</td>
      <td>876.5</td>
      <td>1079.5</td>
      <td>1615</td>
    </tr>
    <tr>
      <th>Year</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.36</td>
      <td>7.26941</td>
      <td>2000</td>
      <td>2004</td>
      <td>2012</td>
      <td>2016</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>Country</th>
      <td>112</td>
      <td>32</td>
      <td>United Kingdom</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Data Year</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2010.14</td>
      <td>6.98887</td>
      <td>1999</td>
      <td>2003</td>
      <td>2011</td>
      <td>2015</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>GDP (PPP)</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.19252e+06</td>
      <td>1.19294e+06</td>
      <td>16865.3</td>
      <td>313922</td>
      <td>545971</td>
      <td>2.083e+06</td>
      <td>4.30886e+06</td>
    </tr>
    <tr>
      <th>Population</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35.3018</td>
      <td>35.5946</td>
      <td>0.330243</td>
      <td>8.82449</td>
      <td>16.0182</td>
      <td>60.5572</td>
      <td>145.872</td>
    </tr>
    <tr>
      <th>GDP (PPP) Per Capita</th>
      <td>112</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35377</td>
      <td>13683</td>
      <td>7493.28</td>
      <td>26531.8</td>
      <td>35891.7</td>
      <td>44947.3</td>
      <td>75574.7</td>
    </tr>
  </tbody>
</table>
</div>



    
    Rating
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_1.png)
    


    
    --------------------
    
    Average Rank
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_3.png)
    


    
    --------------------
    
    Average Rating
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_5.png)
    


    
    --------------------
    
    1 Year Change Rank
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_7.png)
    


    
    --------------------
    
    1 Year Change Rating
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_9.png)
    


    
    --------------------
    
    Matches Total
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_11.png)
    


    
    --------------------
    
    Matches Home
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_13.png)
    


    
    --------------------
    
    Matches Away
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_15.png)
    


    
    --------------------
    
    Matches Neutral
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_17.png)
    


    
    --------------------
    
    Matches Wins
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_19.png)
    


    
    --------------------
    
    Matches Losses
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_21.png)
    


    
    --------------------
    
    Matches Draws
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_23.png)
    


    
    --------------------
    
    Goals For
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_25.png)
    


    
    --------------------
    
    Goals Against
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_27.png)
    


    
    --------------------
    
    GDP (PPP)
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_29.png)
    


    
    --------------------
    
    Population
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_31.png)
    


    
    --------------------
    
    GDP (PPP) Per Capita
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_10_33.png)
    


    
    --------------------
    

## 3. Data Preperation

* Select Data
* Clean Data
* Construct Data
* Integrate Data
* Format Data




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Year</th>
      <td>211.0</td>
      <td>2.010976e+03</td>
      <td>7.055859e+00</td>
      <td>2000.000000</td>
      <td>2004.000000</td>
      <td>2012.000000</td>
      <td>2.016000e+03</td>
      <td>2.021000e+03</td>
    </tr>
    <tr>
      <th>Goals_1</th>
      <td>175.0</td>
      <td>1.468571e+00</td>
      <td>1.346723e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000e+00</td>
      <td>6.000000e+00</td>
    </tr>
    <tr>
      <th>Goals_2</th>
      <td>175.0</td>
      <td>1.114286e+00</td>
      <td>1.004914e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000e+00</td>
      <td>4.000000e+00</td>
    </tr>
    <tr>
      <th>Goal_diff</th>
      <td>175.0</td>
      <td>3.542857e-01</td>
      <td>1.758451e+00</td>
      <td>-4.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
      <td>5.000000e+00</td>
    </tr>
    <tr>
      <th>Home_1</th>
      <td>211.0</td>
      <td>1.327014e-01</td>
      <td>3.400585e-01</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Home_2</th>
      <td>211.0</td>
      <td>9.004739e-02</td>
      <td>2.869304e-01</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Goal_total</th>
      <td>175.0</td>
      <td>2.582857e+00</td>
      <td>1.598398e+00</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000e+00</td>
      <td>8.000000e+00</td>
    </tr>
    <tr>
      <th>Rank Local</th>
      <td>211.0</td>
      <td>9.312796e+00</td>
      <td>5.973495e+00</td>
      <td>1.000000</td>
      <td>4.000000</td>
      <td>8.000000</td>
      <td>1.350000e+01</td>
      <td>2.400000e+01</td>
    </tr>
    <tr>
      <th>Rank Global</th>
      <td>211.0</td>
      <td>1.712796e+01</td>
      <td>1.432473e+01</td>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>13.000000</td>
      <td>2.300000e+01</td>
      <td>7.400000e+01</td>
    </tr>
    <tr>
      <th>Rating</th>
      <td>211.0</td>
      <td>1.871540e+03</td>
      <td>1.241549e+02</td>
      <td>1524.000000</td>
      <td>1781.000000</td>
      <td>1875.000000</td>
      <td>1.969500e+03</td>
      <td>2.127000e+03</td>
    </tr>
    <tr>
      <th>Average Rank</th>
      <td>211.0</td>
      <td>2.112796e+01</td>
      <td>1.529138e+01</td>
      <td>4.000000</td>
      <td>9.500000</td>
      <td>18.000000</td>
      <td>2.500000e+01</td>
      <td>8.300000e+01</td>
    </tr>
    <tr>
      <th>Average Rating</th>
      <td>211.0</td>
      <td>1.781190e+03</td>
      <td>1.265029e+02</td>
      <td>1390.000000</td>
      <td>1716.000000</td>
      <td>1792.000000</td>
      <td>1.885500e+03</td>
      <td>1.985000e+03</td>
    </tr>
    <tr>
      <th>1 Year Change Rank</th>
      <td>211.0</td>
      <td>9.952607e-01</td>
      <td>5.237682e+00</td>
      <td>-15.000000</td>
      <td>-2.000000</td>
      <td>0.000000</td>
      <td>3.000000e+00</td>
      <td>2.300000e+01</td>
    </tr>
    <tr>
      <th>1 Year Change Rating</th>
      <td>211.0</td>
      <td>3.530806e+00</td>
      <td>4.317807e+01</td>
      <td>-92.000000</td>
      <td>-26.000000</td>
      <td>1.000000</td>
      <td>3.400000e+01</td>
      <td>1.270000e+02</td>
    </tr>
    <tr>
      <th>Matches Total</th>
      <td>211.0</td>
      <td>6.411043e+02</td>
      <td>2.110706e+02</td>
      <td>63.000000</td>
      <td>544.000000</td>
      <td>658.000000</td>
      <td>7.900000e+02</td>
      <td>1.073000e+03</td>
    </tr>
    <tr>
      <th>Matches Home</th>
      <td>211.0</td>
      <td>2.882464e+02</td>
      <td>9.570100e+01</td>
      <td>23.000000</td>
      <td>231.000000</td>
      <td>297.000000</td>
      <td>3.545000e+02</td>
      <td>4.670000e+02</td>
    </tr>
    <tr>
      <th>Matches Away</th>
      <td>211.0</td>
      <td>2.800758e+02</td>
      <td>9.797071e+01</td>
      <td>32.000000</td>
      <td>216.000000</td>
      <td>282.000000</td>
      <td>3.420000e+02</td>
      <td>4.940000e+02</td>
    </tr>
    <tr>
      <th>Matches Neutral</th>
      <td>211.0</td>
      <td>7.278199e+01</td>
      <td>3.405430e+01</td>
      <td>8.000000</td>
      <td>46.000000</td>
      <td>70.000000</td>
      <td>9.400000e+01</td>
      <td>1.570000e+02</td>
    </tr>
    <tr>
      <th>Matches Wins</th>
      <td>211.0</td>
      <td>3.050569e+02</td>
      <td>1.295522e+02</td>
      <td>21.000000</td>
      <td>210.000000</td>
      <td>304.000000</td>
      <td>3.850000e+02</td>
      <td>6.280000e+02</td>
    </tr>
    <tr>
      <th>Matches Losses</th>
      <td>211.0</td>
      <td>1.913981e+02</td>
      <td>7.329037e+01</td>
      <td>26.000000</td>
      <td>143.000000</td>
      <td>190.000000</td>
      <td>2.415000e+02</td>
      <td>4.100000e+02</td>
    </tr>
    <tr>
      <th>Matches Draws</th>
      <td>211.0</td>
      <td>1.446493e+02</td>
      <td>4.509324e+01</td>
      <td>16.000000</td>
      <td>121.000000</td>
      <td>148.000000</td>
      <td>1.740000e+02</td>
      <td>2.440000e+02</td>
    </tr>
    <tr>
      <th>Goals For</th>
      <td>211.0</td>
      <td>1.177355e+03</td>
      <td>5.298748e+02</td>
      <td>83.000000</td>
      <td>841.500000</td>
      <td>1178.000000</td>
      <td>1.430500e+03</td>
      <td>2.513000e+03</td>
    </tr>
    <tr>
      <th>Goals Against</th>
      <td>211.0</td>
      <td>8.467962e+02</td>
      <td>3.160263e+02</td>
      <td>87.000000</td>
      <td>613.500000</td>
      <td>885.000000</td>
      <td>1.067000e+03</td>
      <td>1.615000e+03</td>
    </tr>
    <tr>
      <th>Data Year</th>
      <td>211.0</td>
      <td>2.009806e+03</td>
      <td>6.818404e+00</td>
      <td>1999.000000</td>
      <td>2003.000000</td>
      <td>2011.000000</td>
      <td>2.015000e+03</td>
      <td>2.019000e+03</td>
    </tr>
    <tr>
      <th>GDP (PPP)</th>
      <td>211.0</td>
      <td>1.264064e+06</td>
      <td>1.194862e+06</td>
      <td>16865.345703</td>
      <td>315494.187500</td>
      <td>617131.812500</td>
      <td>2.144512e+06</td>
      <td>4.308862e+06</td>
    </tr>
    <tr>
      <th>Population</th>
      <td>211.0</td>
      <td>3.670083e+01</td>
      <td>3.442959e+01</td>
      <td>0.330243</td>
      <td>9.575695</td>
      <td>16.738193</td>
      <td>6.057849e+01</td>
      <td>1.458723e+02</td>
    </tr>
    <tr>
      <th>GDP (PPP) Per Capita</th>
      <td>211.0</td>
      <td>3.571921e+04</td>
      <td>1.283603e+04</td>
      <td>7493.284135</td>
      <td>27507.722917</td>
      <td>35954.106469</td>
      <td>4.507160e+04</td>
      <td>7.557470e+04</td>
    </tr>
    <tr>
      <th>Rank Local (2)</th>
      <td>211.0</td>
      <td>1.003318e+01</td>
      <td>6.164711e+00</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>9.000000</td>
      <td>1.400000e+01</td>
      <td>2.400000e+01</td>
    </tr>
    <tr>
      <th>Rank Global (2)</th>
      <td>211.0</td>
      <td>1.822275e+01</td>
      <td>1.447042e+01</td>
      <td>1.000000</td>
      <td>7.500000</td>
      <td>14.000000</td>
      <td>2.400000e+01</td>
      <td>7.400000e+01</td>
    </tr>
    <tr>
      <th>Rating (2)</th>
      <td>211.0</td>
      <td>1.857768e+03</td>
      <td>1.206156e+02</td>
      <td>1524.000000</td>
      <td>1776.500000</td>
      <td>1860.000000</td>
      <td>1.945500e+03</td>
      <td>2.127000e+03</td>
    </tr>
    <tr>
      <th>Average Rank (2)</th>
      <td>211.0</td>
      <td>2.283412e+01</td>
      <td>1.648220e+01</td>
      <td>4.000000</td>
      <td>11.000000</td>
      <td>20.000000</td>
      <td>2.700000e+01</td>
      <td>8.300000e+01</td>
    </tr>
    <tr>
      <th>Average Rating (2)</th>
      <td>211.0</td>
      <td>1.764403e+03</td>
      <td>1.306723e+02</td>
      <td>1390.000000</td>
      <td>1701.500000</td>
      <td>1769.000000</td>
      <td>1.875000e+03</td>
      <td>1.985000e+03</td>
    </tr>
    <tr>
      <th>1 Year Change Rank (2)</th>
      <td>211.0</td>
      <td>1.417062e+00</td>
      <td>5.874602e+00</td>
      <td>-15.000000</td>
      <td>-2.000000</td>
      <td>1.000000</td>
      <td>3.000000e+00</td>
      <td>2.300000e+01</td>
    </tr>
    <tr>
      <th>1 Year Change Rating (2)</th>
      <td>211.0</td>
      <td>7.213270e+00</td>
      <td>4.110401e+01</td>
      <td>-92.000000</td>
      <td>-22.000000</td>
      <td>5.000000</td>
      <td>3.300000e+01</td>
      <td>1.270000e+02</td>
    </tr>
    <tr>
      <th>Matches Total (2)</th>
      <td>211.0</td>
      <td>6.295261e+02</td>
      <td>2.010268e+02</td>
      <td>63.000000</td>
      <td>519.500000</td>
      <td>634.000000</td>
      <td>7.800000e+02</td>
      <td>1.073000e+03</td>
    </tr>
    <tr>
      <th>Matches Home (2)</th>
      <td>211.0</td>
      <td>2.829052e+02</td>
      <td>9.332743e+01</td>
      <td>23.000000</td>
      <td>217.000000</td>
      <td>292.000000</td>
      <td>3.570000e+02</td>
      <td>4.670000e+02</td>
    </tr>
    <tr>
      <th>Matches Away (2)</th>
      <td>211.0</td>
      <td>2.771801e+02</td>
      <td>9.265741e+01</td>
      <td>32.000000</td>
      <td>214.000000</td>
      <td>282.000000</td>
      <td>3.410000e+02</td>
      <td>4.940000e+02</td>
    </tr>
    <tr>
      <th>Matches Neutral (2)</th>
      <td>211.0</td>
      <td>6.944076e+01</td>
      <td>3.254989e+01</td>
      <td>8.000000</td>
      <td>44.000000</td>
      <td>67.000000</td>
      <td>9.400000e+01</td>
      <td>1.570000e+02</td>
    </tr>
    <tr>
      <th>Matches Wins (2)</th>
      <td>211.0</td>
      <td>2.929716e+02</td>
      <td>1.225707e+02</td>
      <td>21.000000</td>
      <td>209.000000</td>
      <td>300.000000</td>
      <td>3.785000e+02</td>
      <td>6.280000e+02</td>
    </tr>
    <tr>
      <th>Matches Losses (2)</th>
      <td>211.0</td>
      <td>1.934218e+02</td>
      <td>6.981402e+01</td>
      <td>26.000000</td>
      <td>145.000000</td>
      <td>188.000000</td>
      <td>2.460000e+02</td>
      <td>4.100000e+02</td>
    </tr>
    <tr>
      <th>Matches Draws (2)</th>
      <td>211.0</td>
      <td>1.431327e+02</td>
      <td>4.340454e+01</td>
      <td>16.000000</td>
      <td>121.000000</td>
      <td>144.000000</td>
      <td>1.725000e+02</td>
      <td>2.440000e+02</td>
    </tr>
    <tr>
      <th>Goals For (2)</th>
      <td>211.0</td>
      <td>1.128199e+03</td>
      <td>5.001572e+02</td>
      <td>83.000000</td>
      <td>791.000000</td>
      <td>1167.000000</td>
      <td>1.373000e+03</td>
      <td>2.513000e+03</td>
    </tr>
    <tr>
      <th>Goals Against (2)</th>
      <td>211.0</td>
      <td>8.432844e+02</td>
      <td>3.028839e+02</td>
      <td>87.000000</td>
      <td>636.500000</td>
      <td>852.000000</td>
      <td>1.061500e+03</td>
      <td>1.615000e+03</td>
    </tr>
    <tr>
      <th>Data Year (2)</th>
      <td>211.0</td>
      <td>2.009806e+03</td>
      <td>6.818404e+00</td>
      <td>1999.000000</td>
      <td>2003.000000</td>
      <td>2011.000000</td>
      <td>2.015000e+03</td>
      <td>2.019000e+03</td>
    </tr>
    <tr>
      <th>GDP (PPP) (2)</th>
      <td>211.0</td>
      <td>1.239602e+06</td>
      <td>1.201554e+06</td>
      <td>16865.345703</td>
      <td>313060.328125</td>
      <td>562544.187500</td>
      <td>2.264640e+06</td>
      <td>4.308862e+06</td>
    </tr>
    <tr>
      <th>Population (2)</th>
      <td>211.0</td>
      <td>3.620574e+01</td>
      <td>3.517885e+01</td>
      <td>0.330243</td>
      <td>9.059020</td>
      <td>16.200951</td>
      <td>6.218211e+01</td>
      <td>1.458723e+02</td>
    </tr>
    <tr>
      <th>GDP (PPP) Per Capita (2)</th>
      <td>211.0</td>
      <td>3.509773e+04</td>
      <td>1.344206e+04</td>
      <td>7493.284135</td>
      <td>26780.469962</td>
      <td>35954.106469</td>
      <td>4.227827e+04</td>
      <td>7.557470e+04</td>
    </tr>
    <tr>
      <th>Elo_rating_diff</th>
      <td>211.0</td>
      <td>1.377251e+01</td>
      <td>1.757021e+02</td>
      <td>-411.000000</td>
      <td>-100.500000</td>
      <td>18.000000</td>
      <td>1.485000e+02</td>
      <td>4.440000e+02</td>
    </tr>
    <tr>
      <th>Home_advantage</th>
      <td>211.0</td>
      <td>4.265403e-02</td>
      <td>4.711491e-01</td>
      <td>-1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Relative_experience</th>
      <td>211.0</td>
      <td>1.232089e+00</td>
      <td>9.553236e-01</td>
      <td>0.103110</td>
      <td>0.779234</td>
      <td>1.019197</td>
      <td>1.345446e+00</td>
      <td>9.095238e+00</td>
    </tr>
    <tr>
      <th>Relative_population</th>
      <td>211.0</td>
      <td>5.071931e+00</td>
      <td>1.984391e+01</td>
      <td>0.028253</td>
      <td>0.265664</td>
      <td>1.024848</td>
      <td>3.953465e+00</td>
      <td>2.016585e+02</td>
    </tr>
    <tr>
      <th>Relative_GDP_per_capita</th>
      <td>211.0</td>
      <td>1.273215e+00</td>
      <td>9.623153e-01</td>
      <td>0.163999</td>
      <td>0.703541</td>
      <td>0.954593</td>
      <td>1.540308e+00</td>
      <td>5.480461e+00</td>
    </tr>
    <tr>
      <th>Relative_ELO_rating</th>
      <td>211.0</td>
      <td>1.011860e+00</td>
      <td>9.604088e-02</td>
      <td>0.798034</td>
      <td>0.946817</td>
      <td>1.008974</td>
      <td>1.083523e+00</td>
      <td>1.291339e+00</td>
    </tr>
  </tbody>
</table>
</div>






<style  type="text/css" >
#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col0,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col1,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col2,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col3,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col4,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col5,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col6,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col11,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col7,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col8,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col9,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col10,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col6,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col11{
            background-color:  #b40426;
            color:  #f1f1f1;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col1{
            background-color:  #aac7fd;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col2{
            background-color:  #d85646;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col3,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col3,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col10{
            background-color:  #6788ee;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col4,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col2{
            background-color:  #bfd3f6;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col5,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col0{
            background-color:  #ee8468;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col6{
            background-color:  #b9d0f9;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col7,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col4,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col1{
            background-color:  #cbd8ee;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col8,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col9{
            background-color:  #5d7ce6;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col9{
            background-color:  #7396f5;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col10,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col6,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col11{
            background-color:  #88abfd;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col11,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col4{
            background-color:  #b7cff9;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col0,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col2,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col6,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col10,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col11,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col1,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col3,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col5,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col7,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col8,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col4,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col9{
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col3,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col5{
            background-color:  #5875e1;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col4,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col6{
            background-color:  #afcafc;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col5,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col2,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col2{
            background-color:  #efcfbf;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col7{
            background-color:  #ccd9ed;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col8,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col8{
            background-color:  #5470de;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col9{
            background-color:  #5e7de7;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col0{
            background-color:  #e67259;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col5,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col8{
            background-color:  #adc9fd;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col6,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col1{
            background-color:  #c7d7f0;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col7{
            background-color:  #c4d5f3;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col8{
            background-color:  #5572df;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col10{
            background-color:  #97b8ff;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col11,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col2,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col6{
            background-color:  #c6d6f1;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col0{
            background-color:  #6180e9;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col1,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col8{
            background-color:  #bbd1f8;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col2{
            background-color:  #c5d6f2;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col4{
            background-color:  #abc8fd;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col5,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col6,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col11{
            background-color:  #5977e3;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col6,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col0{
            background-color:  #7ea1fa;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col7{
            background-color:  #dc5d4a;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col9,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col3{
            background-color:  #6a8bef;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col10{
            background-color:  #81a4fb;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col11,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col9,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col3{
            background-color:  #7b9ff9;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col0{
            background-color:  #4f69d9;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col1,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col10{
            background-color:  #a9c6fd;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col9{
            background-color:  #3e51c5;
            color:  #f1f1f1;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col10{
            background-color:  #4c66d6;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col1{
            background-color:  #f6a385;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col2{
            background-color:  #edd2c3;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col3,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col0{
            background-color:  #6282ea;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col4,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col4,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col11,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col11,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col4{
            background-color:  #b3cdfb;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col7{
            background-color:  #cfdaea;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col8,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col8{
            background-color:  #5f7fe8;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col0,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col0{
            background-color:  #a5c3fe;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col1{
            background-color:  #93b5fe;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col5,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col5{
            background-color:  #6b8df0;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col7,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col7{
            background-color:  #d2dbe8;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col9{
            background-color:  #90b2fe;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col3{
            background-color:  #ea7b60;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col5,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col0{
            background-color:  #6687ed;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col6{
            background-color:  #89acfd;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col9,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col3{
            background-color:  #688aef;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col10{
            background-color:  #85a8fc;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col11{
            background-color:  #86a9fc;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col1,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col2{
            background-color:  #c3d5f4;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col3{
            background-color:  #6384eb;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col5{
            background-color:  #6485ec;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col7{
            background-color:  #cedaeb;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col9,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col3{
            background-color:  #7da0f9;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col10,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col11{
            background-color:  #c9d7f0;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col0,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col8{
            background-color:  #80a3fa;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col2{
            background-color:  #cad8ef;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col4{
            background-color:  #bcd2f7;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col5{
            background-color:  #82a6fb;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col7{
            background-color:  #d4dbe6;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col10{
            background-color:  #516ddb;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col1{
            background-color:  #a1c0ff;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col2{
            background-color:  #dddcdc;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col4{
            background-color:  #b6cefa;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col6{
            background-color:  #b5cdfa;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col7{
            background-color:  #d8dce2;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col1,#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col9{
            background-color:  #94b6ff;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col8{
            background-color:  #b2ccfb;
            color:  #000000;
        }#T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col10{
            background-color:  #a7c5fe;
            color:  #000000;
        }</style><table id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Goals_1</th>        <th class="col_heading level0 col1" >Goals_2</th>        <th class="col_heading level0 col2" >Goal_diff</th>        <th class="col_heading level0 col3" >Home_1</th>        <th class="col_heading level0 col4" >Home_2</th>        <th class="col_heading level0 col5" >Goal_total</th>        <th class="col_heading level0 col6" >Elo_rating_diff</th>        <th class="col_heading level0 col7" >Home_advantage</th>        <th class="col_heading level0 col8" >Relative_experience</th>        <th class="col_heading level0 col9" >Relative_population</th>        <th class="col_heading level0 col10" >Relative_GDP_per_capita</th>        <th class="col_heading level0 col11" >Relative_ELO_rating</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row0" class="row_heading level0 row0" >Goals_1</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col0" class="data row0 col0" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col1" class="data row0 col1" >-0.099250</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col2" class="data row0 col2" >0.822576</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col3" class="data row0 col3" >0.036952</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col4" class="data row0 col4" >-0.023449</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col5" class="data row0 col5" >0.780147</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col6" class="data row0 col6" >0.250551</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col7" class="data row0 col7" >0.042118</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col8" class="data row0 col8" >0.053178</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col9" class="data row0 col9" >0.133945</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col10" class="data row0 col10" >0.128932</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row0_col11" class="data row0 col11" >0.249152</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row1" class="row_heading level0 row1" >Goals_2</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col0" class="data row1 col0" >-0.099250</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col1" class="data row1 col1" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col2" class="data row1 col2" >-0.647488</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col3" class="data row1 col3" >-0.016394</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col4" class="data row1 col4" >-0.104014</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col5" class="data row1 col5" >0.545078</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col6" class="data row1 col6" >-0.203757</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col7" class="data row1 col7" >0.048554</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col8" class="data row1 col8" >0.022705</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col9" class="data row1 col9" >0.067961</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col10" class="data row1 col10" >-0.141258</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row1_col11" class="data row1 col11" >-0.200515</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row2" class="row_heading level0 row2" >Goal_diff</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col0" class="data row2 col0" >0.822576</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col1" class="data row2 col1" >-0.647488</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col2" class="data row2 col2" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col3" class="data row2 col3" >0.037669</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col4" class="data row2 col4" >0.041483</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col5" class="data row2 col5" >0.285981</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col6" class="data row2 col6" >0.308329</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col7" class="data row2 col7" >0.004509</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col8" class="data row2 col8" >0.027751</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col9" class="data row2 col9" >0.063745</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col10" class="data row2 col10" >0.179469</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row2_col11" class="data row2 col11" >0.305404</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row3" class="row_heading level0 row3" >Home_1</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col0" class="data row3 col0" >0.036952</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col1" class="data row3 col1" >-0.016394</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col2" class="data row3 col2" >0.037669</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col3" class="data row3 col3" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col4" class="data row3 col4" >-0.123049</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col5" class="data row3 col5" >0.020827</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col6" class="data row3 col6" >0.045697</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col7" class="data row3 col7" >0.796701</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col8" class="data row3 col8" >0.024999</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col9" class="data row3 col9" >0.102430</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col10" class="data row3 col10" >0.107938</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row3_col11" class="data row3 col11" >0.041149</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row4" class="row_heading level0 row4" >Home_2</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col0" class="data row4 col0" >-0.023449</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col1" class="data row4 col1" >-0.104014</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col2" class="data row4 col2" >0.041483</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col3" class="data row4 col3" >-0.123049</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col4" class="data row4 col4" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col5" class="data row4 col5" >-0.085151</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col6" class="data row4 col6" >-0.084696</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col7" class="data row4 col7" >-0.697814</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col8" class="data row4 col8" >-0.066460</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col9" class="data row4 col9" >-0.039238</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col10" class="data row4 col10" >-0.070382</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row4_col11" class="data row4 col11" >-0.083189</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row5" class="row_heading level0 row5" >Goal_total</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col0" class="data row5 col0" >0.780147</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col1" class="data row5 col1" >0.545078</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col2" class="data row5 col2" >0.285981</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col3" class="data row5 col3" >0.020827</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col4" class="data row5 col4" >-0.085151</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col5" class="data row5 col5" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col6" class="data row5 col6" >0.082998</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col7" class="data row5 col7" >0.066012</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col8" class="data row5 col8" >0.059080</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col9" class="data row5 col9" >0.155582</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col10" class="data row5 col10" >0.019822</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row5_col11" class="data row5 col11" >0.083858</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row6" class="row_heading level0 row6" >Elo_rating_diff</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col0" class="data row6 col0" >0.250551</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col1" class="data row6 col1" >-0.203757</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col2" class="data row6 col2" >0.308329</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col3" class="data row6 col3" >0.045697</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col4" class="data row6 col4" >-0.084696</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col5" class="data row6 col5" >0.082998</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col6" class="data row6 col6" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col7" class="data row6 col7" >0.084562</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col8" class="data row6 col8" >0.299810</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col9" class="data row6 col9" >0.218648</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col10" class="data row6 col10" >0.234100</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row6_col11" class="data row6 col11" >0.996934</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row7" class="row_heading level0 row7" >Home_advantage</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col0" class="data row7 col0" >0.042118</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col1" class="data row7 col1" >0.048554</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col2" class="data row7 col2" >0.004509</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col3" class="data row7 col3" >0.796701</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col4" class="data row7 col4" >-0.697814</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col5" class="data row7 col5" >0.066012</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col6" class="data row7 col6" >0.084562</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col7" class="data row7 col7" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col8" class="data row7 col8" >0.058517</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col9" class="data row7 col9" >0.097827</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col10" class="data row7 col10" >0.120768</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row7_col11" class="data row7 col11" >0.080362</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row8" class="row_heading level0 row8" >Relative_experience</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col0" class="data row8 col0" >0.053178</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col1" class="data row8 col1" >0.022705</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col2" class="data row8 col2" >0.027751</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col3" class="data row8 col3" >0.024999</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col4" class="data row8 col4" >-0.066460</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col5" class="data row8 col5" >0.059080</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col6" class="data row8 col6" >0.299810</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col7" class="data row8 col7" >0.058517</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col8" class="data row8 col8" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col9" class="data row8 col9" >0.162459</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col10" class="data row8 col10" >0.345483</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row8_col11" class="data row8 col11" >0.313813</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row9" class="row_heading level0 row9" >Relative_population</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col0" class="data row9 col0" >0.133945</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col1" class="data row9 col1" >0.067961</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col2" class="data row9 col2" >0.063745</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col3" class="data row9 col3" >0.102430</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col4" class="data row9 col4" >-0.039238</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col5" class="data row9 col5" >0.155582</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col6" class="data row9 col6" >0.218648</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col7" class="data row9 col7" >0.097827</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col8" class="data row9 col8" >0.162459</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col9" class="data row9 col9" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col10" class="data row9 col10" >-0.055189</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row9_col11" class="data row9 col11" >0.231719</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row10" class="row_heading level0 row10" >Relative_GDP_per_capita</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col0" class="data row10 col0" >0.128932</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col1" class="data row10 col1" >-0.141258</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col2" class="data row10 col2" >0.179469</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col3" class="data row10 col3" >0.107938</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col4" class="data row10 col4" >-0.070382</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col5" class="data row10 col5" >0.019822</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col6" class="data row10 col6" >0.234100</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col7" class="data row10 col7" >0.120768</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col8" class="data row10 col8" >0.345483</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col9" class="data row10 col9" >-0.055189</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col10" class="data row10 col10" >1.000000</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row10_col11" class="data row10 col11" >0.231399</td>
            </tr>
            <tr>
                        <th id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131level0_row11" class="row_heading level0 row11" >Relative_ELO_rating</th>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col0" class="data row11 col0" >0.249152</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col1" class="data row11 col1" >-0.200515</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col2" class="data row11 col2" >0.305404</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col3" class="data row11 col3" >0.041149</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col4" class="data row11 col4" >-0.083189</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col5" class="data row11 col5" >0.083858</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col6" class="data row11 col6" >0.996934</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col7" class="data row11 col7" >0.080362</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col8" class="data row11 col8" >0.313813</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col9" class="data row11 col9" >0.231719</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col10" class="data row11 col10" >0.231399</td>
                        <td id="T_dfeb2d7e_d84a_11eb_9460_74d83eb26131row11_col11" class="data row11 col11" >1.000000</td>
            </tr>
    </tbody></table>



## 4. Modelling

* Select Modelling Technique
* Generate Test Design
* Build Model
* Assess Model

    GD Train data has shape: (140, 5)
    GD Test data has shape: (35, 5)
    ------
    GT Train data has shape: (140, 5)
    GT Test data has shape: (35, 5)
    

    _show_params...
    yType: Diff
    goalWeight: 4.0
    goalBoost: 1.0
    _show_params...
    yType: Total
    goalWeight: 5.849999999999993
    goalBoost: 1.0
    Wall time: 674 ms
    




    (10, 10)



## 5. Evaluation

* Evaluate Results
* Review Process
* Determine Next Steps

    Goal difference model
    
    Evaluating Dummy (mean)...
    
    {'MedAE': 1.3642857142857143, 'RMSE': 1.618026638866503, 'R^2': -0.0009558364544317577, 'Name': 'Dummy (mean)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_1.png)
    


    
    --------------------
    
    Evaluating Dummy (median)...
    
    {'MedAE': 1.0, 'RMSE': 1.647508942095828, 'R^2': -0.03776529338327084, 'Name': 'Dummy (median)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_3.png)
    


    
    --------------------
    
    Evaluating Linear Reg...
    
    {'MedAE': 1.2226734480871315, 'RMSE': 1.8513117016200222, 'R^2': -0.31039634684149386, 'Name': 'Linear Reg'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_5.png)
    


    
    --------------------
    
    Evaluating Lasso...
    
    {'MedAE': 1.3642857142857143, 'RMSE': 1.618026638866503, 'R^2': -0.0009558364544317577, 'Name': 'Lasso'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_7.png)
    


    
    --------------------
    
    Evaluating Ridge...
    
    {'MedAE': 1.2224670817367969, 'RMSE': 1.8491849362118993, 'R^2': -0.3073873399448914, 'Name': 'Ridge'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_9.png)
    


    
    --------------------
    
    Evaluating Random Forest...
    
    {'MedAE': 1.25, 'RMSE': 1.9431549113551934, 'R^2': -0.4436384165626299, 'Name': 'Random Forest'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_11.png)
    


    
    --------------------
    
    Evaluating Gradient Boost...
    
    {'MedAE': 1.7065667791289507, 'RMSE': 2.184113249239861, 'R^2': -0.823870034252107, 'Name': 'Gradient Boost'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_13.png)
    


    
    --------------------
    
    Evaluating SVM (linear)...
    
    {'MedAE': 1.219921328607752, 'RMSE': 1.7880707668612643, 'R^2': -0.22239900357278097, 'Name': 'SVM (linear)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_15.png)
    


    
    --------------------
    
    Evaluating SVM (rbf)...
    
    {'MedAE': 1.3485037112630542, 'RMSE': 1.7167976462381442, 'R^2': -0.1268907127677339, 'Name': 'SVM (rbf)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_17.png)
    


    
    --------------------
    
    Evaluating Elo...
    
    _show_params...
    yType: Diff
    goalWeight: 4.0
    goalBoost: 1.0
    {'MedAE': 1.0, 'RMSE': 1.7647338933351153, 'R^2': -0.19069912609238426, 'Name': 'Elo'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_19.png)
    


    
    --------------------
    
    10 models evaluated
    ==============
    ==============
    Goal total model
    
    Evaluating Dummy (mean)...
    
    {'MedAE': 0.6357142857142857, 'RMSE': 1.5548639943147202, 'R^2': -0.02975052155771918, 'Name': 'Dummy (mean)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_21.png)
    


    
    --------------------
    
    Evaluating Dummy (median)...
    
    {'MedAE': 1.0, 'RMSE': 1.5766148184367308, 'R^2': -0.0587621696801115, 'Name': 'Dummy (median)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_23.png)
    


    
    --------------------
    
    Evaluating Linear Reg...
    
    {'MedAE': 1.327977424318707, 'RMSE': 1.658860777479953, 'R^2': -0.17210652706891838, 'Name': 'Linear Reg'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_25.png)
    


    
    --------------------
    
    Evaluating Lasso...
    
    {'MedAE': 0.6357142857142857, 'RMSE': 1.5548639943147202, 'R^2': -0.02975052155771918, 'Name': 'Lasso'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_27.png)
    


    
    --------------------
    
    Evaluating Ridge...
    
    {'MedAE': 1.3289184425196892, 'RMSE': 1.6575176992118903, 'R^2': -0.17020932924924614, 'Name': 'Ridge'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_29.png)
    


    
    --------------------
    
    Evaluating Random Forest...
    
    {'MedAE': 1.3399999999999999, 'RMSE': 1.8155065295201112, 'R^2': -0.40392154014062776, 'Name': 'Random Forest'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_31.png)
    


    
    --------------------
    
    Evaluating Gradient Boost...
    
    {'MedAE': 1.370957879734548, 'RMSE': 2.003913994416676, 'R^2': -0.7104302290849349, 'Name': 'Gradient Boost'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_33.png)
    


    
    --------------------
    
    Evaluating SVM (linear)...
    
    {'MedAE': 0.9996347989888283, 'RMSE': 1.680971084027552, 'R^2': -0.20355985293377454, 'Name': 'SVM (linear)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_35.png)
    


    
    --------------------
    
    Evaluating SVM (rbf)...
    
    {'MedAE': 1.0090683235008102, 'RMSE': 1.6173065659936927, 'R^2': -0.11411983563898875, 'Name': 'SVM (rbf)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_37.png)
    


    
    --------------------
    
    Evaluating Elo...
    
    _show_params...
    yType: Total
    goalWeight: 5.849999999999993
    goalBoost: 1.0
    {'MedAE': 1.0, 'RMSE': 2.311462122306386, 'R^2': -1.2757301808066766, 'Name': 'Elo'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_28_39.png)
    


    
    --------------------
    
    10 models evaluated
    




<style  type="text/css" >
#T_e2392666_d84a_11eb_bef3_74d83eb26131row0_col1,#T_e2392666_d84a_11eb_bef3_74d83eb26131row3_col1{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row0_col2,#T_e2392666_d84a_11eb_bef3_74d83eb26131row1_col3,#T_e2392666_d84a_11eb_bef3_74d83eb26131row3_col2,#T_e2392666_d84a_11eb_bef3_74d83eb26131row9_col3{
            background-color:  #fff5f0;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row0_col3,#T_e2392666_d84a_11eb_bef3_74d83eb26131row3_col3{
            background-color:  #fa6547;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row1_col1{
            background-color:  #005221;
            color:  #f1f1f1;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row1_col2{
            background-color:  #ffece4;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row2_col1{
            background-color:  #42ab5d;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row2_col2{
            background-color:  #fc8666;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row2_col3,#T_e2392666_d84a_11eb_bef3_74d83eb26131row4_col3{
            background-color:  #fca689;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row4_col1{
            background-color:  #40aa5d;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row4_col2{
            background-color:  #fc8767;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row5_col1{
            background-color:  #81ca81;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row5_col2{
            background-color:  #f44d38;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row5_col3{
            background-color:  #fc997a;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row6_col1{
            background-color:  #f7fcf5;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row6_col2,#T_e2392666_d84a_11eb_bef3_74d83eb26131row6_col3{
            background-color:  #67000d;
            color:  #f1f1f1;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row7_col1{
            background-color:  #278f48;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row7_col2{
            background-color:  #fcab8f;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row7_col3{
            background-color:  #fca78b;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row8_col1{
            background-color:  #087432;
            color:  #f1f1f1;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row8_col2{
            background-color:  #fdd2bf;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row8_col3{
            background-color:  #fb6c4c;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row9_col1{
            background-color:  #1e8741;
            color:  #000000;
        }#T_e2392666_d84a_11eb_bef3_74d83eb26131row9_col2{
            background-color:  #fcb89e;
            color:  #000000;
        }</style><table id="T_e2392666_d84a_11eb_bef3_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Name</th>        <th class="col_heading level0 col1" >R^2</th>        <th class="col_heading level0 col2" >RMSE</th>        <th class="col_heading level0 col3" >MedAE</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row0_col0" class="data row0 col0" >Dummy (mean)</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row0_col1" class="data row0 col1" >-0.000956</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row0_col2" class="data row0 col2" >1.618027</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row0_col3" class="data row0 col3" >1.364286</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row1_col0" class="data row1 col0" >Dummy (median)</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row1_col1" class="data row1 col1" >-0.037765</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row1_col2" class="data row1 col2" >1.647509</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row1_col3" class="data row1 col3" >1.000000</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row2_col0" class="data row2 col0" >Linear Reg</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row2_col1" class="data row2 col1" >-0.310396</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row2_col2" class="data row2 col2" >1.851312</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row2_col3" class="data row2 col3" >1.222673</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row3_col0" class="data row3 col0" >Lasso</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row3_col1" class="data row3 col1" >-0.000956</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row3_col2" class="data row3 col2" >1.618027</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row3_col3" class="data row3 col3" >1.364286</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row4_col0" class="data row4 col0" >Ridge</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row4_col1" class="data row4 col1" >-0.307387</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row4_col2" class="data row4 col2" >1.849185</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row4_col3" class="data row4 col3" >1.222467</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row5_col0" class="data row5 col0" >Random Forest</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row5_col1" class="data row5 col1" >-0.443638</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row5_col2" class="data row5 col2" >1.943155</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row5_col3" class="data row5 col3" >1.250000</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row6_col0" class="data row6 col0" >Gradient Boost</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row6_col1" class="data row6 col1" >-0.823870</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row6_col2" class="data row6 col2" >2.184113</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row6_col3" class="data row6 col3" >1.706567</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row7" class="row_heading level0 row7" >7</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row7_col0" class="data row7 col0" >SVM (linear)</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row7_col1" class="data row7 col1" >-0.222399</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row7_col2" class="data row7 col2" >1.788071</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row7_col3" class="data row7 col3" >1.219921</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row8" class="row_heading level0 row8" >8</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row8_col0" class="data row8 col0" >SVM (rbf)</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row8_col1" class="data row8 col1" >-0.126891</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row8_col2" class="data row8 col2" >1.716798</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row8_col3" class="data row8 col3" >1.348504</td>
            </tr>
            <tr>
                        <th id="T_e2392666_d84a_11eb_bef3_74d83eb26131level0_row9" class="row_heading level0 row9" >9</th>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row9_col0" class="data row9 col0" >Elo</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row9_col1" class="data row9 col1" >-0.190699</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row9_col2" class="data row9 col2" >1.764734</td>
                        <td id="T_e2392666_d84a_11eb_bef3_74d83eb26131row9_col3" class="data row9 col3" >1.000000</td>
            </tr>
    </tbody></table>






<style  type="text/css" >
#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row0_col1,#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row3_col1{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row0_col2,#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row0_col3,#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row3_col2,#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row3_col3{
            background-color:  #fff5f0;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row1_col1{
            background-color:  #004a1e;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row1_col2{
            background-color:  #fff0e9;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row1_col3,#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row7_col3,#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row9_col3{
            background-color:  #fb6c4c;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row2_col1{
            background-color:  #00692a;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row2_col2{
            background-color:  #fedccd;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row2_col3,#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row4_col3{
            background-color:  #820711;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row4_col1{
            background-color:  #00682a;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row4_col2{
            background-color:  #fedecf;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row5_col1{
            background-color:  #2f974e;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row5_col2{
            background-color:  #fc9c7d;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row5_col3{
            background-color:  #7a0510;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row6_col1{
            background-color:  #84cc83;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row6_col2{
            background-color:  #f24734;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row6_col3,#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row9_col2{
            background-color:  #67000d;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row7_col1{
            background-color:  #03702e;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row7_col2{
            background-color:  #fdd4c2;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row8_col1{
            background-color:  #005a24;
            color:  #f1f1f1;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row8_col2{
            background-color:  #fee7dc;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row8_col3{
            background-color:  #fa6849;
            color:  #000000;
        }#T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row9_col1{
            background-color:  #f7fcf5;
            color:  #000000;
        }</style><table id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Name</th>        <th class="col_heading level0 col1" >R^2</th>        <th class="col_heading level0 col2" >RMSE</th>        <th class="col_heading level0 col3" >MedAE</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row0_col0" class="data row0 col0" >Dummy (mean)</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row0_col1" class="data row0 col1" >-0.029751</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row0_col2" class="data row0 col2" >1.554864</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row0_col3" class="data row0 col3" >0.635714</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row1_col0" class="data row1 col0" >Dummy (median)</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row1_col1" class="data row1 col1" >-0.058762</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row1_col2" class="data row1 col2" >1.576615</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row1_col3" class="data row1 col3" >1.000000</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row2_col0" class="data row2 col0" >Linear Reg</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row2_col1" class="data row2 col1" >-0.172107</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row2_col2" class="data row2 col2" >1.658861</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row2_col3" class="data row2 col3" >1.327977</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row3_col0" class="data row3 col0" >Lasso</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row3_col1" class="data row3 col1" >-0.029751</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row3_col2" class="data row3 col2" >1.554864</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row3_col3" class="data row3 col3" >0.635714</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row4_col0" class="data row4 col0" >Ridge</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row4_col1" class="data row4 col1" >-0.170209</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row4_col2" class="data row4 col2" >1.657518</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row4_col3" class="data row4 col3" >1.328918</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row5_col0" class="data row5 col0" >Random Forest</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row5_col1" class="data row5 col1" >-0.403922</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row5_col2" class="data row5 col2" >1.815507</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row5_col3" class="data row5 col3" >1.340000</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row6_col0" class="data row6 col0" >Gradient Boost</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row6_col1" class="data row6 col1" >-0.710430</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row6_col2" class="data row6 col2" >2.003914</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row6_col3" class="data row6 col3" >1.370958</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row7" class="row_heading level0 row7" >7</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row7_col0" class="data row7 col0" >SVM (linear)</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row7_col1" class="data row7 col1" >-0.203560</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row7_col2" class="data row7 col2" >1.680971</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row7_col3" class="data row7 col3" >0.999635</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row8" class="row_heading level0 row8" >8</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row8_col0" class="data row8 col0" >SVM (rbf)</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row8_col1" class="data row8 col1" >-0.114120</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row8_col2" class="data row8 col2" >1.617307</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row8_col3" class="data row8 col3" >1.009068</td>
            </tr>
            <tr>
                        <th id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131level0_row9" class="row_heading level0 row9" >9</th>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row9_col0" class="data row9 col0" >Elo</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row9_col1" class="data row9 col1" >-1.275730</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row9_col2" class="data row9 col2" >2.311462</td>
                        <td id="T_e23ccfa4_d84a_11eb_af9e_74d83eb26131row9_col3" class="data row9 col3" >1.000000</td>
            </tr>
    </tbody></table>






    (EloRegressor(),
     Pipeline(steps=[('standardizer', StandardScaler()), ('estimator', Lasso())]))



    Pickling ../models/intl_02_gd_model.pkl
    Pickling ../models/intl_02_gt_model.pkl
    Pickling ../models/intl_02_gd_features.pkl
    Pickling ../models/intl_02_gt_features.pkl
    Pickled dict_keys(['../models/intl_02_gd_model.pkl', '../models/intl_02_gt_model.pkl', '../models/intl_02_gd_features.pkl', '../models/intl_02_gt_features.pkl'])
    

## 6. Deployment

* Plan Deployment
* Plan Monitoring and Maintenance
* Produce Final Report
* Review Project

    _show_params...
    yType: Diff
    goalWeight: 4.0
    goalBoost: 1.0
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Date</th>
      <td>211</td>
      <td>110</td>
      <td>2016-06-21</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Year</th>
      <td>211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2010.98</td>
      <td>7.05586</td>
      <td>2000</td>
      <td>2004</td>
      <td>2012</td>
      <td>2016</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>Round</th>
      <td>211</td>
      <td>5</td>
      <td>Group stage</td>
      <td>168</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Team_1</th>
      <td>211</td>
      <td>35</td>
      <td>Portugal</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Team_2</th>
      <td>211</td>
      <td>35</td>
      <td>Portugal</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Usage</th>
      <td>211</td>
      <td>3</td>
      <td>Training</td>
      <td>140</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Actual_score_1</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.46857</td>
      <td>1.34672</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Actual_score_2</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.11429</td>
      <td>1.00491</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Actual_goal_diff</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.354286</td>
      <td>1.75845</td>
      <td>-4</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Actual_goal_total</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.58286</td>
      <td>1.5984</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Actual_result</th>
      <td>175</td>
      <td>3</td>
      <td>Win</td>
      <td>77</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Predicted_score_1</th>
      <td>211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.30806</td>
      <td>0.529943</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Predicted_score_2</th>
      <td>211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.24171</td>
      <td>0.491223</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Predicted_goal_diff</th>
      <td>211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0663507</td>
      <td>0.891951</td>
      <td>-2</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Predicted_goal_total</th>
      <td>211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.54976</td>
      <td>0.498701</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Predicted_result</th>
      <td>211</td>
      <td>3</td>
      <td>Draw</td>
      <td>82</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Correct_result</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.405714</td>
      <td>0.492439</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Correct_goal_diff</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.245714</td>
      <td>0.431745</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Correct_score</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.137143</td>
      <td>0.344985</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Points</th>
      <td>175</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.788571</td>
      <td>1.10166</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Matches played</th>
      <th>Points per game</th>
      <th>% correct result</th>
      <th>% correct goal diff</th>
      <th>% correct score</th>
      <th>Goals per game (predicted)</th>
      <th>Goals per game (actual)</th>
      <th>% games won (predicted)</th>
      <th>% games won (actual)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>31</td>
      <td>0.71</td>
      <td>35%</td>
      <td>19%</td>
      <td>16%</td>
      <td>2.48</td>
      <td>2.84</td>
      <td>52%</td>
      <td>87%</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>31</td>
      <td>0.74</td>
      <td>42%</td>
      <td>23%</td>
      <td>10%</td>
      <td>2.61</td>
      <td>2.74</td>
      <td>74%</td>
      <td>74%</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>31</td>
      <td>0.74</td>
      <td>35%</td>
      <td>26%</td>
      <td>13%</td>
      <td>2.45</td>
      <td>2.61</td>
      <td>45%</td>
      <td>87%</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>31</td>
      <td>0.84</td>
      <td>42%</td>
      <td>26%</td>
      <td>16%</td>
      <td>2.45</td>
      <td>2.58</td>
      <td>45%</td>
      <td>84%</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>51</td>
      <td>0.86</td>
      <td>45%</td>
      <td>27%</td>
      <td>14%</td>
      <td>2.69</td>
      <td>2.31</td>
      <td>75%</td>
      <td>78%</td>
    </tr>
    <tr>
      <th>Training</th>
      <td>140</td>
      <td>0.81</td>
      <td>42%</td>
      <td>24%</td>
      <td>14%</td>
      <td>2.55</td>
      <td>2.64</td>
      <td>61%</td>
      <td>81%</td>
    </tr>
    <tr>
      <th>Testing</th>
      <td>35</td>
      <td>0.71</td>
      <td>34%</td>
      <td>26%</td>
      <td>11%</td>
      <td>2.57</td>
      <td>2.37</td>
      <td>56%</td>
      <td>86%</td>
    </tr>
    <tr>
      <th>Overall</th>
      <td>175</td>
      <td>0.79</td>
      <td>41%</td>
      <td>25%</td>
      <td>14%</td>
      <td>2.55</td>
      <td>2.58</td>
      <td>60%</td>
      <td>82%</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Year</th>
      <td>36.0</td>
      <td>2021.000000</td>
      <td>0.000000</td>
      <td>2021.0</td>
      <td>2021.00</td>
      <td>2021.0</td>
      <td>2021.00</td>
      <td>2021.0</td>
    </tr>
    <tr>
      <th>Predicted_score_1</th>
      <td>36.0</td>
      <td>1.333333</td>
      <td>0.632456</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>2.00</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Predicted_score_2</th>
      <td>36.0</td>
      <td>1.194444</td>
      <td>0.524783</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>1.25</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Predicted_goal_diff</th>
      <td>36.0</td>
      <td>0.138889</td>
      <td>1.046157</td>
      <td>-2.0</td>
      <td>-0.25</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Predicted_goal_total</th>
      <td>36.0</td>
      <td>2.527778</td>
      <td>0.506309</td>
      <td>2.0</td>
      <td>2.00</td>
      <td>3.0</td>
      <td>3.00</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



    
    
    #### Group  A
                 Points  Goal_diff_all  Goals_for  Rank  Points_mini  \
    Italy             9            3.0        6.0    98          NaN   
    Switzerland       2           -1.0        3.0    91          2.0   
    Turkey            2           -1.0        3.0    86          2.0   
    Wales             2           -1.0        3.0    81          2.0   
    
                 Goal_diff_mini  Goals_for_mini  Rank_mini  
    Italy                   NaN             NaN        NaN  
    Switzerland             0.0             2.0       91.0  
    Turkey                  0.0             2.0       86.0  
    Wales                   0.0             2.0       81.0  
    
    
    #### Group  B
             Points  Goal_diff_all  Goals_for  Rank  Points_mini  Goal_diff_mini  \
    Belgium       7            3.0        5.0    99          1.0             0.0   
    Denmark       7            3.0        5.0    85          1.0             0.0   
    Russia        3           -1.0        4.0    88          NaN             NaN   
    Finland       0           -5.0        1.0    80          NaN             NaN   
    
             Goals_for_mini  Rank_mini  
    Belgium             1.0       99.0  
    Denmark             1.0       85.0  
    Russia              NaN        NaN  
    Finland             NaN        NaN  
    
    
    #### Group  C
                     Points  Goal_diff_all  Goals_for  Rank  Points_mini  \
    Netherlands           9            4.0        6.0    89          NaN   
    Ukraine               4            0.0        4.0    94          1.0   
    Austria               4            0.0        4.0    84          1.0   
    North Macedonia       0           -4.0        2.0    70          NaN   
    
                     Goal_diff_mini  Goals_for_mini  Rank_mini  
    Netherlands                 NaN             NaN        NaN  
    Ukraine                     0.0             1.0       94.0  
    Austria                     0.0             1.0       84.0  
    North Macedonia             NaN             NaN        NaN  
    
    
    #### Group  D
                    Points  Goal_diff_all  Goals_for  Rank  Points_mini  \
    England              9            4.0        6.0    97          NaN   
    Croatia              2           -1.0        3.0    90          2.0   
    Czech Republic       2           -1.0        3.0    82          2.0   
    Scotland             2           -2.0        2.0    71          2.0   
    
                    Goal_diff_mini  Goals_for_mini  Rank_mini  
    England                    NaN             NaN        NaN  
    Croatia                    0.0             2.0       90.0  
    Czech Republic             0.0             2.0       82.0  
    Scotland                   0.0             2.0       71.0  
    
    
    #### Group  E
              Points  Goal_diff_all  Goals_for  Rank  Points_mini  Goal_diff_mini  \
    Spain          9            4.0        6.0    95          NaN             NaN   
    Poland         4            0.0        4.0    92          1.0             0.0   
    Sweden         4            0.0        4.0    83          1.0             0.0   
    Slovakia       0           -4.0        2.0    78          NaN             NaN   
    
              Goals_for_mini  Rank_mini  
    Spain                NaN        NaN  
    Poland               1.0       92.0  
    Sweden               1.0       83.0  
    Slovakia             NaN        NaN  
    
    
    #### Group  F
              Points  Goal_diff_all  Goals_for  Rank  Points_mini  Goal_diff_mini  \
    Germany        5            1.0        4.0    96          2.0             0.0   
    France         5            1.0        4.0    93          2.0             0.0   
    Portugal       5            1.0        4.0    87          2.0             0.0   
    Hungary        0           -3.0        3.0    69          NaN             NaN   
    
              Goals_for_mini  Rank_mini  
    Germany              2.0       96.0  
    France               2.0       93.0  
    Portugal             2.0       87.0  
    Hungary              NaN        NaN  
    
    
    #### Third-placed teams
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Points</th>
      <th>Goal_diff_all</th>
      <th>Goals_for</th>
      <th>Rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Portugal</th>
      <td>5.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td>4.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>84.0</td>
    </tr>
    <tr>
      <th>Sweden</th>
      <td>4.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>83.0</td>
    </tr>
    <tr>
      <th>Russia</th>
      <td>3.0</td>
      <td>-1.0</td>
      <td>4.0</td>
      <td>88.0</td>
    </tr>
    <tr>
      <th>Turkey</th>
      <td>2.0</td>
      <td>-1.0</td>
      <td>3.0</td>
      <td>86.0</td>
    </tr>
    <tr>
      <th>Czech Republic</th>
      <td>2.0</td>
      <td>-1.0</td>
      <td>3.0</td>
      <td>82.0</td>
    </tr>
  </tbody>
</table>
</div>


