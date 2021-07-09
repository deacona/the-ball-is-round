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

    2021-07-09 21:04:15,552 - INFO - Building master filepath for nations_matches
    2021-07-09 21:04:15,556 - INFO - Fetching C:\Users\adeacon\Documents\GitHub\the-ball-is-round\data\processed\ftb_nations_matches.txt
    2021-07-09 21:04:15,557 - INFO - Building master filepath for nations_matches
    




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
      <td>226</td>
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
      <td>226</td>
      <td>7</td>
      <td>Sun</td>
      <td>44</td>
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
      <td>226</td>
      <td>119</td>
      <td>2000-06-21</td>
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
      <td>226</td>
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
      <td>226</td>
      <td>35</td>
      <td>Italy</td>
      <td>17</td>
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
      <td>226</td>
      <td>35</td>
      <td>Spain</td>
      <td>15</td>
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
      <td>226</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.64</td>
      <td>7.26084</td>
      <td>2000</td>
      <td>2004</td>
      <td>2012</td>
      <td>2016</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>Goals_1</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.42667</td>
      <td>1.31448</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Goals_2</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.22222</td>
      <td>1.10778</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Goal_diff</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.204444</td>
      <td>1.81092</td>
      <td>-5</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Venue</th>
      <td>226</td>
      <td>60</td>
      <td>Stade de France</td>
      <td>7</td>
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
      <td>134</td>
      <td>11</td>
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
      <td>134</td>
      <td>34</td>
      <td>Vienna</td>
      <td>7</td>
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
      <td>226</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0752212</td>
      <td>0.264333</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Home_2</th>
      <td>226</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0442478</td>
      <td>0.206102</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Goal_total</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.64889</td>
      <td>1.62192</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Result</th>
      <td>225</td>
      <td>3</td>
      <td>Win</td>
      <td>96</td>
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
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_6_1.png)
    


    
    --------------------
    
    Goals_2
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_6_3.png)
    


    
    --------------------
    
    Goal_diff
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_6_5.png)
    


    
    --------------------
    
    Goal_total
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_6_7.png)
    


    
    --------------------
    

    
    Round
    
    Group stage       168
    Quarter-finals     24
    Round of 16        16
    Semi-finals        12
    Final               5
    Name: Round, dtype: int64
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_7_1.png)
    


    
    --------------------
    
    Day
    
    Sun    43
    Sat    40
    Wed    35
    Mon    32
    Tue    29
    Fri    24
    Thu    22
    Name: Day, dtype: int64
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_7_3.png)
    


    
    --------------------
    
    Time
    
    20:45 (19:45)    52
    18:00 (17:00)    48
    21:00 (20:00)    40
    19:45            23
    17:00            12
    21:45 (19:45)    11
    15:00 (14:00)    10
    20:00             7
    19:00 (17:00)     7
    22:00 (20:00)     4
    20:00 (17:00)     3
    14:00             3
    16:00 (14:00)     2
    20:00 (19:00)     1
    17:00 (14:00)     1
    14:30 (13:30)     1
    Name: Time, dtype: int64
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_7_5.png)
    


    
    --------------------
    
    Year
    
    2016    51
    2021    50
    2012    31
    2008    31
    2004    31
    2000    31
    Name: Year, dtype: int64
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_7_7.png)
    


    
    --------------------
    
    Venue_country
    
    NULL           92
    France         45
    Netherlands    16
    Ukraine        16
    Belgium        15
    Austria        13
    Switzerland    12
    Poland         11
    England         2
    Italy           1
    Russia          1
    Germany         1
    Name: Venue_country, dtype: int64
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_7_9.png)
    


    
    --------------------
    
    Result
    
    Win     96
    Loss    88
    Draw    41
    Name: Result, dtype: int64
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_7_11.png)
    


    
    --------------------
    

    2021-07-09 21:04:17,548 - INFO - Building master filepath for nations_summaries
    2021-07-09 21:04:17,549 - INFO - Fetching C:\Users\adeacon\Documents\GitHub\the-ball-is-round\data\processed\ftb_nations_summaries.txt
    2021-07-09 21:04:17,550 - INFO - Building master filepath for nations_summaries
    




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
      <td>Germany</td>
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
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_1.png)
    


    
    --------------------
    
    Average Rank
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_3.png)
    


    
    --------------------
    
    Average Rating
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_5.png)
    


    
    --------------------
    
    1 Year Change Rank
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_7.png)
    


    
    --------------------
    
    1 Year Change Rating
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_9.png)
    


    
    --------------------
    
    Matches Total
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_11.png)
    


    
    --------------------
    
    Matches Home
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_13.png)
    


    
    --------------------
    
    Matches Away
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_15.png)
    


    
    --------------------
    
    Matches Neutral
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_17.png)
    


    
    --------------------
    
    Matches Wins
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_19.png)
    


    
    --------------------
    
    Matches Losses
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_21.png)
    


    
    --------------------
    
    Matches Draws
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_23.png)
    


    
    --------------------
    
    Goals For
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_25.png)
    


    
    --------------------
    
    Goals Against
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_27.png)
    


    
    --------------------
    
    GDP (PPP)
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_29.png)
    


    
    --------------------
    
    Population
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_31.png)
    


    
    --------------------
    
    GDP (PPP) Per Capita
    
    


    
![png](intl_02_euro_2020_live_files/intl_02_euro_2020_live_10_33.png)
    


    
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
      <td>226.0</td>
      <td>2.011642e+03</td>
      <td>7.260844e+00</td>
      <td>2000.000000</td>
      <td>2004.000000</td>
      <td>2012.000000</td>
      <td>2.016000e+03</td>
      <td>2.021000e+03</td>
    </tr>
    <tr>
      <th>Goals_1</th>
      <td>225.0</td>
      <td>1.426667e+00</td>
      <td>1.314480e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000e+00</td>
      <td>6.000000e+00</td>
    </tr>
    <tr>
      <th>Goals_2</th>
      <td>225.0</td>
      <td>1.222222e+00</td>
      <td>1.107783e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000e+00</td>
      <td>5.000000e+00</td>
    </tr>
    <tr>
      <th>Goal_diff</th>
      <td>225.0</td>
      <td>2.044444e-01</td>
      <td>1.810924e+00</td>
      <td>-5.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
      <td>5.000000e+00</td>
    </tr>
    <tr>
      <th>Home_1</th>
      <td>226.0</td>
      <td>7.522124e-02</td>
      <td>2.643335e-01</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Home_2</th>
      <td>226.0</td>
      <td>4.424779e-02</td>
      <td>2.061016e-01</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Goal_total</th>
      <td>225.0</td>
      <td>2.648889e+00</td>
      <td>1.621923e+00</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000e+00</td>
      <td>8.000000e+00</td>
    </tr>
    <tr>
      <th>Rank Local</th>
      <td>226.0</td>
      <td>9.207965e+00</td>
      <td>5.913159e+00</td>
      <td>1.000000</td>
      <td>4.000000</td>
      <td>8.000000</td>
      <td>1.300000e+01</td>
      <td>2.400000e+01</td>
    </tr>
    <tr>
      <th>Rank Global</th>
      <td>226.0</td>
      <td>1.671681e+01</td>
      <td>1.404942e+01</td>
      <td>1.000000</td>
      <td>6.250000</td>
      <td>12.500000</td>
      <td>2.200000e+01</td>
      <td>7.400000e+01</td>
    </tr>
    <tr>
      <th>Rating</th>
      <td>226.0</td>
      <td>1.876637e+03</td>
      <td>1.245237e+02</td>
      <td>1524.000000</td>
      <td>1788.000000</td>
      <td>1877.000000</td>
      <td>1.972000e+03</td>
      <td>2.127000e+03</td>
    </tr>
    <tr>
      <th>Average Rank</th>
      <td>226.0</td>
      <td>2.076549e+01</td>
      <td>1.500142e+01</td>
      <td>4.000000</td>
      <td>8.000000</td>
      <td>18.000000</td>
      <td>2.400000e+01</td>
      <td>8.300000e+01</td>
    </tr>
    <tr>
      <th>Average Rating</th>
      <td>226.0</td>
      <td>1.784261e+03</td>
      <td>1.253686e+02</td>
      <td>1390.000000</td>
      <td>1721.000000</td>
      <td>1792.000000</td>
      <td>1.890750e+03</td>
      <td>1.985000e+03</td>
    </tr>
    <tr>
      <th>1 Year Change Rank</th>
      <td>226.0</td>
      <td>1.008850e+00</td>
      <td>5.150181e+00</td>
      <td>-15.000000</td>
      <td>-1.750000</td>
      <td>0.000000</td>
      <td>3.000000e+00</td>
      <td>2.300000e+01</td>
    </tr>
    <tr>
      <th>1 Year Change Rating</th>
      <td>226.0</td>
      <td>3.814159e+00</td>
      <td>4.304810e+01</td>
      <td>-92.000000</td>
      <td>-25.750000</td>
      <td>4.500000</td>
      <td>3.500000e+01</td>
      <td>1.270000e+02</td>
    </tr>
    <tr>
      <th>Matches Total</th>
      <td>226.0</td>
      <td>6.513850e+02</td>
      <td>2.152674e+02</td>
      <td>63.000000</td>
      <td>554.000000</td>
      <td>674.000000</td>
      <td>8.030000e+02</td>
      <td>1.073000e+03</td>
    </tr>
    <tr>
      <th>Matches Home</th>
      <td>226.0</td>
      <td>2.931637e+02</td>
      <td>9.781763e+01</td>
      <td>23.000000</td>
      <td>232.000000</td>
      <td>300.000000</td>
      <td>3.727500e+02</td>
      <td>4.670000e+02</td>
    </tr>
    <tr>
      <th>Matches Away</th>
      <td>226.0</td>
      <td>2.839469e+02</td>
      <td>9.949163e+01</td>
      <td>32.000000</td>
      <td>218.000000</td>
      <td>295.000000</td>
      <td>3.460000e+02</td>
      <td>4.940000e+02</td>
    </tr>
    <tr>
      <th>Matches Neutral</th>
      <td>226.0</td>
      <td>7.427434e+01</td>
      <td>3.503198e+01</td>
      <td>8.000000</td>
      <td>47.000000</td>
      <td>71.000000</td>
      <td>9.725000e+01</td>
      <td>1.570000e+02</td>
    </tr>
    <tr>
      <th>Matches Wins</th>
      <td>226.0</td>
      <td>3.107434e+02</td>
      <td>1.321375e+02</td>
      <td>21.000000</td>
      <td>212.250000</td>
      <td>306.000000</td>
      <td>3.922500e+02</td>
      <td>6.280000e+02</td>
    </tr>
    <tr>
      <th>Matches Losses</th>
      <td>226.0</td>
      <td>1.933717e+02</td>
      <td>7.423048e+01</td>
      <td>26.000000</td>
      <td>145.000000</td>
      <td>190.000000</td>
      <td>2.460000e+02</td>
      <td>4.100000e+02</td>
    </tr>
    <tr>
      <th>Matches Draws</th>
      <td>226.0</td>
      <td>1.472699e+02</td>
      <td>4.650909e+01</td>
      <td>16.000000</td>
      <td>121.500000</td>
      <td>149.000000</td>
      <td>1.770000e+02</td>
      <td>2.440000e+02</td>
    </tr>
    <tr>
      <th>Goals For</th>
      <td>226.0</td>
      <td>1.197403e+03</td>
      <td>5.389982e+02</td>
      <td>83.000000</td>
      <td>844.000000</td>
      <td>1198.000000</td>
      <td>1.452000e+03</td>
      <td>2.513000e+03</td>
    </tr>
    <tr>
      <th>Goals Against</th>
      <td>226.0</td>
      <td>8.567168e+02</td>
      <td>3.189157e+02</td>
      <td>87.000000</td>
      <td>633.000000</td>
      <td>894.000000</td>
      <td>1.075750e+03</td>
      <td>1.615000e+03</td>
    </tr>
    <tr>
      <th>Data Year</th>
      <td>226.0</td>
      <td>2.010416e+03</td>
      <td>6.975163e+00</td>
      <td>1999.000000</td>
      <td>2003.000000</td>
      <td>2011.000000</td>
      <td>2.015000e+03</td>
      <td>2.019000e+03</td>
    </tr>
    <tr>
      <th>GDP (PPP)</th>
      <td>226.0</td>
      <td>1.287812e+06</td>
      <td>1.196577e+06</td>
      <td>16865.345703</td>
      <td>320065.828125</td>
      <td>633721.843750</td>
      <td>2.231273e+06</td>
      <td>4.308862e+06</td>
    </tr>
    <tr>
      <th>Population</th>
      <td>226.0</td>
      <td>3.678355e+01</td>
      <td>3.395233e+01</td>
      <td>0.330243</td>
      <td>9.704747</td>
      <td>17.097130</td>
      <td>6.057849e+01</td>
      <td>1.458723e+02</td>
    </tr>
    <tr>
      <th>GDP (PPP) Per Capita</th>
      <td>226.0</td>
      <td>3.633357e+04</td>
      <td>1.303657e+04</td>
      <td>7493.284135</td>
      <td>27665.659029</td>
      <td>36533.876382</td>
      <td>4.570633e+04</td>
      <td>7.557470e+04</td>
    </tr>
    <tr>
      <th>Rank Local (2)</th>
      <td>226.0</td>
      <td>9.893805e+00</td>
      <td>6.101166e+00</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>9.000000</td>
      <td>1.400000e+01</td>
      <td>2.400000e+01</td>
    </tr>
    <tr>
      <th>Rank Global (2)</th>
      <td>226.0</td>
      <td>1.777876e+01</td>
      <td>1.424717e+01</td>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>14.000000</td>
      <td>2.400000e+01</td>
      <td>7.400000e+01</td>
    </tr>
    <tr>
      <th>Rating (2)</th>
      <td>226.0</td>
      <td>1.863597e+03</td>
      <td>1.209416e+02</td>
      <td>1524.000000</td>
      <td>1777.500000</td>
      <td>1867.000000</td>
      <td>1.960000e+03</td>
      <td>2.127000e+03</td>
    </tr>
    <tr>
      <th>Average Rank (2)</th>
      <td>226.0</td>
      <td>2.228319e+01</td>
      <td>1.621630e+01</td>
      <td>4.000000</td>
      <td>11.000000</td>
      <td>19.000000</td>
      <td>2.700000e+01</td>
      <td>8.300000e+01</td>
    </tr>
    <tr>
      <th>Average Rating (2)</th>
      <td>226.0</td>
      <td>1.770527e+03</td>
      <td>1.304118e+02</td>
      <td>1390.000000</td>
      <td>1704.250000</td>
      <td>1779.000000</td>
      <td>1.879000e+03</td>
      <td>1.985000e+03</td>
    </tr>
    <tr>
      <th>1 Year Change Rank (2)</th>
      <td>226.0</td>
      <td>1.477876e+00</td>
      <td>5.741231e+00</td>
      <td>-15.000000</td>
      <td>-1.000000</td>
      <td>1.000000</td>
      <td>3.000000e+00</td>
      <td>2.300000e+01</td>
    </tr>
    <tr>
      <th>1 Year Change Rating (2)</th>
      <td>226.0</td>
      <td>8.349558e+00</td>
      <td>4.101238e+01</td>
      <td>-92.000000</td>
      <td>-21.000000</td>
      <td>8.000000</td>
      <td>3.450000e+01</td>
      <td>1.270000e+02</td>
    </tr>
    <tr>
      <th>Matches Total (2)</th>
      <td>226.0</td>
      <td>6.406018e+02</td>
      <td>2.042757e+02</td>
      <td>63.000000</td>
      <td>527.750000</td>
      <td>643.000000</td>
      <td>8.010000e+02</td>
      <td>1.073000e+03</td>
    </tr>
    <tr>
      <th>Matches Home (2)</th>
      <td>226.0</td>
      <td>2.878407e+02</td>
      <td>9.441611e+01</td>
      <td>23.000000</td>
      <td>224.000000</td>
      <td>295.000000</td>
      <td>3.645000e+02</td>
      <td>4.670000e+02</td>
    </tr>
    <tr>
      <th>Matches Away (2)</th>
      <td>226.0</td>
      <td>2.814204e+02</td>
      <td>9.403728e+01</td>
      <td>32.000000</td>
      <td>218.000000</td>
      <td>283.000000</td>
      <td>3.430000e+02</td>
      <td>4.940000e+02</td>
    </tr>
    <tr>
      <th>Matches Neutral (2)</th>
      <td>226.0</td>
      <td>7.134071e+01</td>
      <td>3.342446e+01</td>
      <td>8.000000</td>
      <td>46.000000</td>
      <td>68.000000</td>
      <td>9.400000e+01</td>
      <td>1.570000e+02</td>
    </tr>
    <tr>
      <th>Matches Wins (2)</th>
      <td>226.0</td>
      <td>3.006062e+02</td>
      <td>1.260563e+02</td>
      <td>21.000000</td>
      <td>209.250000</td>
      <td>303.500000</td>
      <td>3.855000e+02</td>
      <td>6.280000e+02</td>
    </tr>
    <tr>
      <th>Matches Losses (2)</th>
      <td>226.0</td>
      <td>1.945000e+02</td>
      <td>7.022258e+01</td>
      <td>26.000000</td>
      <td>145.000000</td>
      <td>189.000000</td>
      <td>2.460000e+02</td>
      <td>4.100000e+02</td>
    </tr>
    <tr>
      <th>Matches Draws (2)</th>
      <td>226.0</td>
      <td>1.454956e+02</td>
      <td>4.406049e+01</td>
      <td>16.000000</td>
      <td>123.000000</td>
      <td>148.000000</td>
      <td>1.740000e+02</td>
      <td>2.440000e+02</td>
    </tr>
    <tr>
      <th>Goals For (2)</th>
      <td>226.0</td>
      <td>1.155801e+03</td>
      <td>5.120961e+02</td>
      <td>83.000000</td>
      <td>824.000000</td>
      <td>1195.000000</td>
      <td>1.431000e+03</td>
      <td>2.513000e+03</td>
    </tr>
    <tr>
      <th>Goals Against (2)</th>
      <td>226.0</td>
      <td>8.497124e+02</td>
      <td>3.030021e+02</td>
      <td>87.000000</td>
      <td>644.000000</td>
      <td>854.500000</td>
      <td>1.075750e+03</td>
      <td>1.615000e+03</td>
    </tr>
    <tr>
      <th>Data Year (2)</th>
      <td>226.0</td>
      <td>2.010416e+03</td>
      <td>6.975163e+00</td>
      <td>1999.000000</td>
      <td>2003.000000</td>
      <td>2011.000000</td>
      <td>2.015000e+03</td>
      <td>2.019000e+03</td>
    </tr>
    <tr>
      <th>GDP (PPP) (2)</th>
      <td>226.0</td>
      <td>1.255932e+06</td>
      <td>1.207412e+06</td>
      <td>16865.345703</td>
      <td>314019.625000</td>
      <td>575996.656250</td>
      <td>2.280700e+06</td>
      <td>4.308862e+06</td>
    </tr>
    <tr>
      <th>Population (2)</th>
      <td>226.0</td>
      <td>3.609965e+01</td>
      <td>3.468460e+01</td>
      <td>0.330243</td>
      <td>8.955102</td>
      <td>16.200951</td>
      <td>6.178121e+01</td>
      <td>1.458723e+02</td>
    </tr>
    <tr>
      <th>GDP (PPP) Per Capita (2)</th>
      <td>226.0</td>
      <td>3.583183e+04</td>
      <td>1.367834e+04</td>
      <td>7493.284135</td>
      <td>27503.425456</td>
      <td>37116.156506</td>
      <td>4.423183e+04</td>
      <td>7.557470e+04</td>
    </tr>
    <tr>
      <th>Elo_rating_diff</th>
      <td>226.0</td>
      <td>1.303982e+01</td>
      <td>1.736801e+02</td>
      <td>-411.000000</td>
      <td>-102.500000</td>
      <td>18.000000</td>
      <td>1.477500e+02</td>
      <td>4.440000e+02</td>
    </tr>
    <tr>
      <th>Home_advantage</th>
      <td>226.0</td>
      <td>3.097345e-02</td>
      <td>3.450165e-01</td>
      <td>-1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Relative_experience</th>
      <td>226.0</td>
      <td>1.226452e+00</td>
      <td>9.445298e-01</td>
      <td>0.103110</td>
      <td>0.781259</td>
      <td>1.019656</td>
      <td>1.334768e+00</td>
      <td>9.095238e+00</td>
    </tr>
    <tr>
      <th>Relative_population</th>
      <td>226.0</td>
      <td>4.942925e+00</td>
      <td>1.920556e+01</td>
      <td>0.028253</td>
      <td>0.265281</td>
      <td>1.034090</td>
      <td>4.018824e+00</td>
      <td>2.016585e+02</td>
    </tr>
    <tr>
      <th>Relative_GDP_per_capita</th>
      <td>226.0</td>
      <td>1.267003e+00</td>
      <td>9.602093e-01</td>
      <td>0.163999</td>
      <td>0.710537</td>
      <td>0.944943</td>
      <td>1.525705e+00</td>
      <td>5.480461e+00</td>
    </tr>
    <tr>
      <th>Relative_ELO_rating</th>
      <td>226.0</td>
      <td>1.011328e+00</td>
      <td>9.479120e-02</td>
      <td>0.798034</td>
      <td>0.943532</td>
      <td>1.009114</td>
      <td>1.081703e+00</td>
      <td>1.291339e+00</td>
    </tr>
  </tbody>
</table>
</div>






<style  type="text/css" >
#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col0,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col1,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col2,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col3,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col5,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col6,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col11,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col7,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col8,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col9,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col10,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col6,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col11{
            background-color:  #b40426;
            color:  #f1f1f1;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col1,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col8{
            background-color:  #adc9fd;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col2{
            background-color:  #dd5f4b;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col3{
            background-color:  #6485ec;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col1,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col7{
            background-color:  #bbd1f8;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col5{
            background-color:  #f39778;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col6{
            background-color:  #cedaeb;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col7,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col2{
            background-color:  #c6d6f1;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col8{
            background-color:  #5e7de7;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col9,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col9{
            background-color:  #7295f4;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col10{
            background-color:  #93b5fe;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col11,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col2,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col1{
            background-color:  #ccd9ed;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col0,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col2,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col6,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col8,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col10,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col11,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col1,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col5,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col7,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col9,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col3{
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col3{
            background-color:  #4a63d3;
            color:  #f1f1f1;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col10{
            background-color:  #a9c6fd;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col5{
            background-color:  #f4c5ad;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col7,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col11,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col6{
            background-color:  #c3d5f4;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col9,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col5{
            background-color:  #5a78e4;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col0{
            background-color:  #eb7d62;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col3{
            background-color:  #688aef;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col7,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col1{
            background-color:  #c7d7f0;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col5{
            background-color:  #86a9fc;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col6{
            background-color:  #e5d8d1;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col7,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col6{
            background-color:  #c0d4f5;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col8,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col10{
            background-color:  #6180e9;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col9{
            background-color:  #5d7ce6;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col10{
            background-color:  #a2c1ff;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col11{
            background-color:  #e3d9d3;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col0,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col0{
            background-color:  #6788ee;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col2,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col2,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col7{
            background-color:  #cdd9ec;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col7,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col7{
            background-color:  #b1cbfc;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col5,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col5{
            background-color:  #5470de;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col6,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col0{
            background-color:  #6f92f3;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col7{
            background-color:  #dc5d4a;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col8{
            background-color:  #4961d2;
            color:  #f1f1f1;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col9,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col6{
            background-color:  #779af7;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col10,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col3{
            background-color:  #82a6fb;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col11{
            background-color:  #6c8ff1;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col0,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col5{
            background-color:  #5572df;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col1{
            background-color:  #afcafc;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col3,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col8{
            background-color:  #445acc;
            color:  #f1f1f1;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col6,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col1{
            background-color:  #84a7fc;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col8{
            background-color:  #4e68d8;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col9{
            background-color:  #4257c9;
            color:  #f1f1f1;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col11{
            background-color:  #81a4fb;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col0,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col1{
            background-color:  #f39577;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col2{
            background-color:  #dfdbd9;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col3,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col5{
            background-color:  #5977e3;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col6,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col11{
            background-color:  #8badfd;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col8{
            background-color:  #506bda;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col9,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col3{
            background-color:  #7597f6;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col10{
            background-color:  #6a8bef;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col0,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col0{
            background-color:  #aec9fc;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col2{
            background-color:  #f5c0a7;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col3{
            background-color:  #3c4ec2;
            color:  #f1f1f1;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col8,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col10{
            background-color:  #a7c5fe;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col9{
            background-color:  #90b2fe;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col3{
            background-color:  #e97a5f;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col5{
            background-color:  #6282ea;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col10{
            background-color:  #7da0f9;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col11{
            background-color:  #7699f6;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col1,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col4{
            background-color:  #bad0f8;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col2,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col10{
            background-color:  #d2dbe8;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col3{
            background-color:  #5673e0;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col4,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col8,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col11{
            background-color:  #c1d4f4;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col6{
            background-color:  #d3dbe7;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col9,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col5{
            background-color:  #7b9ff9;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col11,#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col7{
            background-color:  #d5dbe5;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col0{
            background-color:  #80a3fa;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col4{
            background-color:  #b7cff9;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col8{
            background-color:  #7a9df8;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col10{
            background-color:  #536edd;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col0{
            background-color:  #89acfd;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col1{
            background-color:  #a5c3fe;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col2{
            background-color:  #e4d9d2;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col4{
            background-color:  #bcd2f7;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col1{
            background-color:  #85a8fc;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col2{
            background-color:  #f5c1a9;
            color:  #000000;
        }#T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col9{
            background-color:  #94b6ff;
            color:  #000000;
        }</style><table id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Goals_1</th>        <th class="col_heading level0 col1" >Goals_2</th>        <th class="col_heading level0 col2" >Goal_diff</th>        <th class="col_heading level0 col3" >Home_1</th>        <th class="col_heading level0 col4" >Home_2</th>        <th class="col_heading level0 col5" >Goal_total</th>        <th class="col_heading level0 col6" >Elo_rating_diff</th>        <th class="col_heading level0 col7" >Home_advantage</th>        <th class="col_heading level0 col8" >Relative_experience</th>        <th class="col_heading level0 col9" >Relative_population</th>        <th class="col_heading level0 col10" >Relative_GDP_per_capita</th>        <th class="col_heading level0 col11" >Relative_ELO_rating</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row0" class="row_heading level0 row0" >Goals_1</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col0" class="data row0 col0" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col1" class="data row0 col1" >-0.111391</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col2" class="data row0 col2" >0.794002</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col3" class="data row0 col3" >0.048040</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col4" class="data row0 col4" >-0.014526</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col5" class="data row0 col5" >0.734365</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col6" class="data row0 col6" >0.274183</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col7" class="data row0 col7" >0.045975</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col8" class="data row0 col8" >0.074838</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col9" class="data row0 col9" >0.125363</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col10" class="data row0 col10" >0.156935</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row0_col11" class="data row0 col11" >0.271003</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row1" class="row_heading level0 row1" >Goals_2</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col0" class="data row1 col0" >-0.111391</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col1" class="data row1 col1" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col2" class="data row1 col2" >-0.692577</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col3" class="data row1 col3" >-0.042262</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col4" class="data row1 col4" >-0.102597</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col5" class="data row1 col5" >0.592730</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col6" class="data row1 col6" >-0.309664</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col7" class="data row1 col7" >0.026431</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col8" class="data row1 col8" >-0.047353</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col9" class="data row1 col9" >0.050959</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col10" class="data row1 col10" >-0.150840</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row1_col11" class="data row1 col11" >-0.302684</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row2" class="row_heading level0 row2" >Goal_diff</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col0" class="data row2 col0" >0.794002</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col1" class="data row2 col1" >-0.692577</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col2" class="data row2 col2" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col3" class="data row2 col3" >0.060723</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col4" class="data row2 col4" >0.052217</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col5" class="data row2 col5" >0.170461</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col6" class="data row2 col6" >0.388447</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col7" class="data row2 col7" >0.017203</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col8" class="data row2 col8" >0.083289</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col9" class="data row2 col9" >0.059823</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col10" class="data row2 col10" >0.206186</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row2_col11" class="data row2 col11" >0.381869</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row3" class="row_heading level0 row3" >Home_1</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col0" class="data row3 col0" >0.048040</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col1" class="data row3 col1" >-0.042262</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col2" class="data row3 col2" >0.060723</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col3" class="data row3 col3" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col4" class="data row3 col4" >-0.061366</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col5" class="data row3 col5" >0.010068</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col6" class="data row3 col6" >-0.093970</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col7" class="data row3 col7" >0.802805</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col8" class="data row3 col8" >0.002473</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col9" class="data row3 col9" >0.144338</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col10" class="data row3 col10" >0.102674</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row3_col11" class="data row3 col11" >-0.098387</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row4" class="row_heading level0 row4" >Home_2</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col0" class="data row4 col0" >-0.014526</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col1" class="data row4 col1" >-0.102597</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col2" class="data row4 col2" >0.052217</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col3" class="data row4 col3" >-0.061366</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col4" class="data row4 col4" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col5" class="data row4 col5" >-0.081847</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col6" class="data row4 col6" >-0.014328</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col7" class="data row4 col7" >-0.644382</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col8" class="data row4 col8" >0.020895</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col9" class="data row4 col9" >-0.030583</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col10" class="data row4 col10" >-0.007149</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row4_col11" class="data row4 col11" >-0.020045</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row5" class="row_heading level0 row5" >Goal_total</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col0" class="data row5 col0" >0.734365</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col1" class="data row5 col1" >0.592730</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col2" class="data row5 col2" >0.170461</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col3" class="data row5 col3" >0.010068</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col4" class="data row5 col4" >-0.081847</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col5" class="data row5 col5" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col6" class="data row5 col6" >0.010708</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col7" class="data row5 col7" >0.055313</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col8" class="data row5 col8" >0.028310</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col9" class="data row5 col9" >0.136404</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col10" class="data row5 col10" >0.024162</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row5_col11" class="data row5 col11" >0.012898</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row6" class="row_heading level0 row6" >Elo_rating_diff</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col0" class="data row6 col0" >0.274183</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col1" class="data row6 col1" >-0.309664</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col2" class="data row6 col2" >0.388447</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col3" class="data row6 col3" >-0.093970</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col4" class="data row6 col4" >-0.014328</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col5" class="data row6 col5" >0.010708</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col6" class="data row6 col6" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col7" class="data row6 col7" >-0.063436</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col8" class="data row6 col8" >0.295572</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col9" class="data row6 col9" >0.215862</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col10" class="data row6 col10" >0.227179</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row6_col11" class="data row6 col11" >0.996969</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row7" class="row_heading level0 row7" >Home_advantage</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col0" class="data row7 col0" >0.045975</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col1" class="data row7 col1" >0.026431</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col2" class="data row7 col2" >0.017203</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col3" class="data row7 col3" >0.802805</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col4" class="data row7 col4" >-0.644382</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col5" class="data row7 col5" >0.055313</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col6" class="data row7 col6" >-0.063436</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col7" class="data row7 col7" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col8" class="data row7 col8" >-0.010587</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col9" class="data row7 col9" >0.128854</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col10" class="data row7 col10" >0.082934</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row7_col11" class="data row7 col11" >-0.063405</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row8" class="row_heading level0 row8" >Relative_experience</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col0" class="data row8 col0" >0.074838</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col1" class="data row8 col1" >-0.047353</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col2" class="data row8 col2" >0.083289</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col3" class="data row8 col3" >0.002473</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col4" class="data row8 col4" >0.020895</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col5" class="data row8 col5" >0.028310</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col6" class="data row8 col6" >0.295572</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col7" class="data row8 col7" >-0.010587</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col8" class="data row8 col8" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col9" class="data row8 col9" >0.157891</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col10" class="data row8 col10" >0.377200</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row8_col11" class="data row8 col11" >0.308726</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row9" class="row_heading level0 row9" >Relative_population</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col0" class="data row9 col0" >0.125363</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col1" class="data row9 col1" >0.050959</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col2" class="data row9 col2" >0.059823</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col3" class="data row9 col3" >0.144338</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col4" class="data row9 col4" >-0.030583</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col5" class="data row9 col5" >0.136404</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col6" class="data row9 col6" >0.215862</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col7" class="data row9 col7" >0.128854</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col8" class="data row9 col8" >0.157891</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col9" class="data row9 col9" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col10" class="data row9 col10" >-0.056638</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row9_col11" class="data row9 col11" >0.229049</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row10" class="row_heading level0 row10" >Relative_GDP_per_capita</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col0" class="data row10 col0" >0.156935</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col1" class="data row10 col1" >-0.150840</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col2" class="data row10 col2" >0.206186</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col3" class="data row10 col3" >0.102674</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col4" class="data row10 col4" >-0.007149</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col5" class="data row10 col5" >0.024162</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col6" class="data row10 col6" >0.227179</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col7" class="data row10 col7" >0.082934</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col8" class="data row10 col8" >0.377200</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col9" class="data row10 col9" >-0.056638</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col10" class="data row10 col10" >1.000000</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row10_col11" class="data row10 col11" >0.224446</td>
            </tr>
            <tr>
                        <th id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131level0_row11" class="row_heading level0 row11" >Relative_ELO_rating</th>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col0" class="data row11 col0" >0.271003</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col1" class="data row11 col1" >-0.302684</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col2" class="data row11 col2" >0.381869</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col3" class="data row11 col3" >-0.098387</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col4" class="data row11 col4" >-0.020045</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col5" class="data row11 col5" >0.012898</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col6" class="data row11 col6" >0.996969</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col7" class="data row11 col7" >-0.063405</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col8" class="data row11 col8" >0.308726</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col9" class="data row11 col9" >0.229049</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col10" class="data row11 col10" >0.224446</td>
                        <td id="T_d96a2d8a_e0f0_11eb_b914_74d83eb26131row11_col11" class="data row11 col11" >1.000000</td>
            </tr>
    </tbody></table>



## 4. Modelling

* Select Modelling Technique
* Generate Test Design
* Build Model
* Assess Model

## 5. Evaluation

* Evaluate Results
* Review Process
* Determine Next Steps

## 6. Deployment

* Plan Deployment
* Plan Monitoring and Maintenance
* Produce Final Report
* Review Project

    Un-Pickling files...
    




    (EloRegressor(),
     ['Home_advantage',
      'Relative_experience',
      'Relative_population',
      'Relative_GDP_per_capita',
      'Elo_rating_diff'],
     Pipeline(steps=[('standardizer', StandardScaler()), ('estimator', Lasso())]),
     ['Home_advantage',
      'Relative_experience',
      'Relative_population',
      'Relative_GDP_per_capita',
      'Elo_rating_diff'])



    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 211 entries, 0 to 210
    Data columns (total 20 columns):
     #   Column                Non-Null Count  Dtype  
    ---  ------                --------------  -----  
     0   Date                  211 non-null    object 
     1   Year                  211 non-null    object 
     2   Round                 211 non-null    object 
     3   Team_1                211 non-null    object 
     4   Team_2                211 non-null    object 
     5   Usage                 211 non-null    object 
     6   Actual_score_1        175 non-null    float64
     7   Actual_score_2        175 non-null    float64
     8   Actual_goal_diff      175 non-null    float64
     9   Actual_goal_total     175 non-null    float64
     10  Actual_result         175 non-null    object 
     11  Predicted_score_1     211 non-null    float64
     12  Predicted_score_2     211 non-null    float64
     13  Predicted_goal_diff   211 non-null    float64
     14  Predicted_goal_total  211 non-null    float64
     15  Predicted_result      211 non-null    object 
     16  Correct_result        175 non-null    float64
     17  Correct_goal_diff     175 non-null    float64
     18  Correct_score         175 non-null    float64
     19  Points                175 non-null    float64
    dtypes: float64(12), object(8)
    memory usage: 33.1+ KB
    

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
      <td>226</td>
      <td>119</td>
      <td>2000-06-21</td>
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
      <td>226</td>
      <td>6</td>
      <td>2021</td>
      <td>51</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Round</th>
      <td>226</td>
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
      <td>226</td>
      <td>35</td>
      <td>Italy</td>
      <td>17</td>
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
      <td>226</td>
      <td>35</td>
      <td>Spain</td>
      <td>15</td>
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
      <td>226</td>
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
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.42667</td>
      <td>1.31448</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Actual_score_2</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.22222</td>
      <td>1.10778</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Actual_goal_diff</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.204444</td>
      <td>1.81092</td>
      <td>-5</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Actual_goal_total</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.64889</td>
      <td>1.62192</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Actual_result</th>
      <td>225</td>
      <td>3</td>
      <td>Win</td>
      <td>96</td>
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
      <td>226</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.30973</td>
      <td>0.526281</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Predicted_score_2</th>
      <td>226</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.24779</td>
      <td>0.49046</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Predicted_goal_diff</th>
      <td>226</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0619469</td>
      <td>0.887275</td>
      <td>-2</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Predicted_goal_total</th>
      <td>226</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.55752</td>
      <td>0.497783</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Predicted_result</th>
      <td>226</td>
      <td>3</td>
      <td>Draw</td>
      <td>87</td>
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
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.435556</td>
      <td>0.496935</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Correct_goal_diff</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.257778</td>
      <td>0.438386</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Correct_score</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.137778</td>
      <td>0.345435</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Points</th>
      <td>225</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.831111</td>
      <td>1.1011</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
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
      <th>2021</th>
      <td>50</td>
      <td>0.98</td>
      <td>54%</td>
      <td>30%</td>
      <td>14%</td>
      <td>2.58</td>
      <td>2.88</td>
      <td>68%</td>
      <td>82%</td>
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
      <th>Live</th>
      <td>50</td>
      <td>0.98</td>
      <td>54%</td>
      <td>30%</td>
      <td>14%</td>
      <td>2.58</td>
      <td>2.88</td>
      <td>68%</td>
      <td>82%</td>
    </tr>
    <tr>
      <th>Overall</th>
      <td>225</td>
      <td>0.83</td>
      <td>44%</td>
      <td>26%</td>
      <td>14%</td>
      <td>2.56</td>
      <td>2.65</td>
      <td>62%</td>
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
      <th>Actual_score_1</th>
      <td>50.0</td>
      <td>1.280000</td>
      <td>1.195911</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>Actual_score_2</th>
      <td>50.0</td>
      <td>1.600000</td>
      <td>1.355262</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Actual_goal_diff</th>
      <td>50.0</td>
      <td>-0.320000</td>
      <td>1.910658</td>
      <td>-5.0</td>
      <td>-1.75</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>Actual_goal_total</th>
      <td>50.0</td>
      <td>2.880000</td>
      <td>1.698018</td>
      <td>0.0</td>
      <td>2.00</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>Predicted_score_1</th>
      <td>51.0</td>
      <td>1.333333</td>
      <td>0.588784</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Predicted_score_2</th>
      <td>51.0</td>
      <td>1.235294</td>
      <td>0.513351</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Predicted_goal_diff</th>
      <td>51.0</td>
      <td>0.098039</td>
      <td>0.984985</td>
      <td>-2.0</td>
      <td>-1.00</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Predicted_goal_total</th>
      <td>51.0</td>
      <td>2.568627</td>
      <td>0.500196</td>
      <td>2.0</td>
      <td>2.00</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>Correct_result</th>
      <td>50.0</td>
      <td>0.540000</td>
      <td>0.503457</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Correct_goal_diff</th>
      <td>50.0</td>
      <td>0.300000</td>
      <td>0.462910</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Correct_score</th>
      <td>50.0</td>
      <td>0.140000</td>
      <td>0.350510</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Points</th>
      <td>50.0</td>
      <td>0.980000</td>
      <td>1.097121</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>


