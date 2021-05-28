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

### EURO 2020 fixtures/results
* https://en.wikipedia.org/wiki/UEFA_Euro_2020
* https://www.whoscored.com/Regions/247/Tournaments/124/Seasons/7329/Stages/16297/Show/International-European-Championship-2020
* https://www.uefa.com/uefaeuro-2020/fixtures-results/#/md/33673
* https://fbref.com/en/comps/676/schedule/UEFA-Euro-Scores-and-Fixtures

### Historic results
* https://www.staff.city.ac.uk/r.j.gerrard/football/aifrform.html (1871-2001)
* https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017/data (1872-)
* https://fbref.com/en/comps/676/history/European-Championship-Seasons (2000-)
* https://en.wikipedia.org/wiki/UEFA_Euro_2020_qualifying (qualifying)
* https://fbref.com/en/comps/678/Euro-Qualifying-Stats (qualifying)

### ELO ratings
* https://en.m.wikipedia.org/wiki/World_Football_Elo_Ratings
* https://www.eloratings.net/2021_European_Championship
* http://eloratings.net/2016_European_Championship_start
* https://www.eloratings.net/about

### Historic trends
* https://blog.annabet.com/soccer-goal-probabilities-poisson-vs-actual-distribution/
* https://en.wikipedia.org/wiki/Poisson_distribution

### GDP
* https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)
* https://en.wikipedia.org/wiki/List_of_countries_by_past_and_projected_GDP_(nominal)
* https://www.rug.nl/ggdc/productivity/pwt/

### Prediction competitions
* https://www.squawka.com/en/euro-2020-predictions-odds-outright-group-winner-final/
* https://www.telegraph.co.uk/football/euro-2020-wallchart-predictor/
* https://gaming.uefa.com/en/uefaeuro2020tournamentpredictor/main
* https://www.uefa.com/uefaeuro-2020/news/0269-1232cabf40a1-47e385aa9131-1000--euro-2020-tournament-predictor-rules/

    2021-05-28 17:52:54,880 - INFO - Building master filepath for nations_matches
    2021-05-28 17:52:54,885 - INFO - Fetching C:\Users\adeacon\Documents\GitHub\the-ball-is-round\data\processed\ftb_nations_matches.txt
    2021-05-28 17:52:54,885 - INFO - Building master filepath for nations_matches
    




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
      <td>France</td>
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
      <td>0.118483</td>
      <td>0.323948</td>
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
      <td>0.0805687</td>
      <td>0.272819</td>
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
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_1.png)
    


    
    --------------------
    
    Goals_2
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_3.png)
    


    
    --------------------
    
    Goal_diff
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_5.png)
    


    
    --------------------
    
    Goal_total
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_7_7.png)
    


    
    --------------------
    

    
    Round
    
    Group stage       132
    Quarter-finals     20
    Semi-finals        10
    Round of 16         8
    Final               5
    Name: Round, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_8_1.png)
    


    
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
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_8_3.png)
    


    
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
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_8_5.png)
    


    
    --------------------
    
    Year
    
    2016    51
    2012    31
    2008    31
    2004    31
    2000    31
    Name: Year, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_8_7.png)
    


    
    --------------------
    
    Venue_country
    
    NULL           47
    France         45
    Ukraine        16
    Netherlands    16
    Belgium        15
    Austria        13
    Switzerland    12
    Poland         11
    Name: Venue_country, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_8_9.png)
    


    
    --------------------
    
    Result
    
    Win     77
    Loss    66
    Draw    32
    Name: Result, dtype: int64
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_8_11.png)
    


    
    --------------------
    

    2021-05-28 17:52:56,602 - INFO - Building master filepath for nations_summaries
    2021-05-28 17:52:56,603 - INFO - Fetching C:\Users\adeacon\Documents\GitHub\the-ball-is-round\data\processed\ftb_nations_summaries.txt
    2021-05-28 17:52:56,604 - INFO - Building master filepath for nations_summaries
    




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
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_1.png)
    


    
    --------------------
    
    Average Rank
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_3.png)
    


    
    --------------------
    
    Average Rating
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_5.png)
    


    
    --------------------
    
    1 Year Change Rank
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_7.png)
    


    
    --------------------
    
    1 Year Change Rating
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_9.png)
    


    
    --------------------
    
    Matches Total
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_11.png)
    


    
    --------------------
    
    Matches Home
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_13.png)
    


    
    --------------------
    
    Matches Away
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_15.png)
    


    
    --------------------
    
    Matches Neutral
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_17.png)
    


    
    --------------------
    
    Matches Wins
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_19.png)
    


    
    --------------------
    
    Matches Losses
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_21.png)
    


    
    --------------------
    
    Matches Draws
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_23.png)
    


    
    --------------------
    
    Goals For
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_25.png)
    


    
    --------------------
    
    Goals Against
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_27.png)
    


    
    --------------------
    
    GDP (PPP)
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_29.png)
    


    
    --------------------
    
    Population
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_31.png)
    


    
    --------------------
    
    GDP (PPP) Per Capita
    
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_11_33.png)
    


    
    --------------------
    

## 3. Data Preperation

* Select Data
* Clean Data
* Construct Data
* Integrate Data
* Format Data

    
    
    England                10
    Wales                   4
    Republic of Ireland     2
    Scotland                1
    Northern Ireland        1
    Name: Team_1, dtype: int64
    
    
    England             5
    Wales               2
    Ireland             2
    Northern Ireland    1
    Scotland            1
    Name: Team, dtype: int64
    
    
     England               8
    Republic of Ireland    5
     Wales                 5
     Northern Ireland      3
     Scotland              2
    Name: Team_2, dtype: int64
    
    
    England             5
    Wales               2
    Ireland             2
    Northern Ireland    1
    Scotland            1
    Name: Team, dtype: int64
    




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
      <td>173.0</td>
      <td>2.010358e+03</td>
      <td>7.078374e+00</td>
      <td>2000.000000</td>
      <td>2004.000000</td>
      <td>2012.000000</td>
      <td>2.016000e+03</td>
      <td>2.021000e+03</td>
    </tr>
    <tr>
      <th>Goals_1</th>
      <td>145.0</td>
      <td>1.420690e+00</td>
      <td>1.352308e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000e+00</td>
      <td>6.000000e+00</td>
    </tr>
    <tr>
      <th>Goals_2</th>
      <td>145.0</td>
      <td>1.110345e+00</td>
      <td>9.726627e-01</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000e+00</td>
      <td>4.000000e+00</td>
    </tr>
    <tr>
      <th>Goal_diff</th>
      <td>145.0</td>
      <td>3.103448e-01</td>
      <td>1.757987e+00</td>
      <td>-4.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
      <td>5.000000e+00</td>
    </tr>
    <tr>
      <th>Home_1</th>
      <td>173.0</td>
      <td>1.329480e-01</td>
      <td>3.405040e-01</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Home_2</th>
      <td>173.0</td>
      <td>9.248555e-02</td>
      <td>2.905511e-01</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Goal_total</th>
      <td>145.0</td>
      <td>2.531034e+00</td>
      <td>1.568152e+00</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000e+00</td>
      <td>7.000000e+00</td>
    </tr>
    <tr>
      <th>Rank Local</th>
      <td>173.0</td>
      <td>9.202312e+00</td>
      <td>5.880555e+00</td>
      <td>1.000000</td>
      <td>4.000000</td>
      <td>9.000000</td>
      <td>1.400000e+01</td>
      <td>2.400000e+01</td>
    </tr>
    <tr>
      <th>Rank Global</th>
      <td>173.0</td>
      <td>1.705202e+01</td>
      <td>1.446980e+01</td>
      <td>1.000000</td>
      <td>6.000000</td>
      <td>13.000000</td>
      <td>2.300000e+01</td>
      <td>7.400000e+01</td>
    </tr>
    <tr>
      <th>Rating</th>
      <td>173.0</td>
      <td>1.872948e+03</td>
      <td>1.255476e+02</td>
      <td>1524.000000</td>
      <td>1783.000000</td>
      <td>1873.000000</td>
      <td>1.972000e+03</td>
      <td>2.127000e+03</td>
    </tr>
    <tr>
      <th>Average Rank</th>
      <td>173.0</td>
      <td>2.221387e+01</td>
      <td>1.590361e+01</td>
      <td>7.000000</td>
      <td>11.000000</td>
      <td>18.000000</td>
      <td>2.700000e+01</td>
      <td>8.300000e+01</td>
    </tr>
    <tr>
      <th>Average Rating</th>
      <td>173.0</td>
      <td>1.773289e+03</td>
      <td>1.242423e+02</td>
      <td>1390.000000</td>
      <td>1721.000000</td>
      <td>1792.000000</td>
      <td>1.876000e+03</td>
      <td>1.939000e+03</td>
    </tr>
    <tr>
      <th>1 Year Change Rank</th>
      <td>173.0</td>
      <td>8.034682e-01</td>
      <td>5.363159e+00</td>
      <td>-15.000000</td>
      <td>-2.000000</td>
      <td>0.000000</td>
      <td>3.000000e+00</td>
      <td>2.300000e+01</td>
    </tr>
    <tr>
      <th>1 Year Change Rating</th>
      <td>173.0</td>
      <td>7.052023e-01</td>
      <td>4.455047e+01</td>
      <td>-92.000000</td>
      <td>-29.000000</td>
      <td>-3.000000</td>
      <td>3.200000e+01</td>
      <td>1.270000e+02</td>
    </tr>
    <tr>
      <th>Matches Total</th>
      <td>173.0</td>
      <td>6.270809e+02</td>
      <td>2.029637e+02</td>
      <td>63.000000</td>
      <td>523.000000</td>
      <td>640.000000</td>
      <td>7.660000e+02</td>
      <td>1.060000e+03</td>
    </tr>
    <tr>
      <th>Matches Home</th>
      <td>173.0</td>
      <td>2.818960e+02</td>
      <td>9.318767e+01</td>
      <td>23.000000</td>
      <td>220.000000</td>
      <td>293.000000</td>
      <td>3.500000e+02</td>
      <td>4.600000e+02</td>
    </tr>
    <tr>
      <th>Matches Away</th>
      <td>173.0</td>
      <td>2.721908e+02</td>
      <td>9.185057e+01</td>
      <td>32.000000</td>
      <td>214.000000</td>
      <td>281.000000</td>
      <td>3.360000e+02</td>
      <td>4.780000e+02</td>
    </tr>
    <tr>
      <th>Matches Neutral</th>
      <td>173.0</td>
      <td>7.299422e+01</td>
      <td>3.333594e+01</td>
      <td>8.000000</td>
      <td>47.000000</td>
      <td>70.000000</td>
      <td>9.400000e+01</td>
      <td>1.570000e+02</td>
    </tr>
    <tr>
      <th>Matches Wins</th>
      <td>173.0</td>
      <td>2.960578e+02</td>
      <td>1.189059e+02</td>
      <td>21.000000</td>
      <td>211.000000</td>
      <td>303.000000</td>
      <td>3.800000e+02</td>
      <td>5.640000e+02</td>
    </tr>
    <tr>
      <th>Matches Losses</th>
      <td>173.0</td>
      <td>1.904740e+02</td>
      <td>7.421375e+01</td>
      <td>26.000000</td>
      <td>141.000000</td>
      <td>190.000000</td>
      <td>2.350000e+02</td>
      <td>4.100000e+02</td>
    </tr>
    <tr>
      <th>Matches Draws</th>
      <td>173.0</td>
      <td>1.405491e+02</td>
      <td>4.208911e+01</td>
      <td>16.000000</td>
      <td>118.000000</td>
      <td>145.000000</td>
      <td>1.670000e+02</td>
      <td>2.290000e+02</td>
    </tr>
    <tr>
      <th>Goals For</th>
      <td>173.0</td>
      <td>1.143329e+03</td>
      <td>4.829089e+02</td>
      <td>83.000000</td>
      <td>848.000000</td>
      <td>1167.000000</td>
      <td>1.413000e+03</td>
      <td>2.180000e+03</td>
    </tr>
    <tr>
      <th>Goals Against</th>
      <td>173.0</td>
      <td>8.424682e+02</td>
      <td>3.242345e+02</td>
      <td>87.000000</td>
      <td>608.000000</td>
      <td>863.000000</td>
      <td>1.087000e+03</td>
      <td>1.615000e+03</td>
    </tr>
    <tr>
      <th>Data Year</th>
      <td>173.0</td>
      <td>2.009197e+03</td>
      <td>6.839233e+00</td>
      <td>1999.000000</td>
      <td>2003.000000</td>
      <td>2011.000000</td>
      <td>2.015000e+03</td>
      <td>2.019000e+03</td>
    </tr>
    <tr>
      <th>GDP (PPP)</th>
      <td>173.0</td>
      <td>1.129100e+06</td>
      <td>1.158626e+06</td>
      <td>16865.345703</td>
      <td>314019.625000</td>
      <td>560735.312500</td>
      <td>1.932679e+06</td>
      <td>4.308862e+06</td>
    </tr>
    <tr>
      <th>Population</th>
      <td>173.0</td>
      <td>3.403896e+01</td>
      <td>3.473912e+01</td>
      <td>0.330243</td>
      <td>8.951436</td>
      <td>15.835523</td>
      <td>5.756459e+01</td>
      <td>1.458723e+02</td>
    </tr>
    <tr>
      <th>GDP (PPP) Per Capita</th>
      <td>173.0</td>
      <td>3.512835e+04</td>
      <td>1.315152e+04</td>
      <td>7493.284135</td>
      <td>26699.610804</td>
      <td>35545.200434</td>
      <td>4.532020e+04</td>
      <td>7.183164e+04</td>
    </tr>
    <tr>
      <th>Rank Local (2)</th>
      <td>173.0</td>
      <td>9.335260e+00</td>
      <td>5.838204e+00</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>9.000000</td>
      <td>1.300000e+01</td>
      <td>2.400000e+01</td>
    </tr>
    <tr>
      <th>Rank Global (2)</th>
      <td>173.0</td>
      <td>1.686705e+01</td>
      <td>1.387903e+01</td>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>13.000000</td>
      <td>2.200000e+01</td>
      <td>7.400000e+01</td>
    </tr>
    <tr>
      <th>Rating (2)</th>
      <td>173.0</td>
      <td>1.868936e+03</td>
      <td>1.187314e+02</td>
      <td>1524.000000</td>
      <td>1788.000000</td>
      <td>1867.000000</td>
      <td>1.960000e+03</td>
      <td>2.127000e+03</td>
    </tr>
    <tr>
      <th>Average Rank (2)</th>
      <td>173.0</td>
      <td>2.345665e+01</td>
      <td>1.670902e+01</td>
      <td>7.000000</td>
      <td>11.000000</td>
      <td>19.000000</td>
      <td>2.800000e+01</td>
      <td>8.300000e+01</td>
    </tr>
    <tr>
      <th>Average Rating (2)</th>
      <td>173.0</td>
      <td>1.762341e+03</td>
      <td>1.258470e+02</td>
      <td>1390.000000</td>
      <td>1710.000000</td>
      <td>1775.000000</td>
      <td>1.868000e+03</td>
      <td>1.939000e+03</td>
    </tr>
    <tr>
      <th>1 Year Change Rank (2)</th>
      <td>173.0</td>
      <td>1.294798e+00</td>
      <td>5.539481e+00</td>
      <td>-15.000000</td>
      <td>-1.000000</td>
      <td>1.000000</td>
      <td>3.000000e+00</td>
      <td>2.300000e+01</td>
    </tr>
    <tr>
      <th>1 Year Change Rating (2)</th>
      <td>173.0</td>
      <td>7.335260e+00</td>
      <td>4.076454e+01</td>
      <td>-79.000000</td>
      <td>-25.000000</td>
      <td>8.000000</td>
      <td>3.300000e+01</td>
      <td>1.270000e+02</td>
    </tr>
    <tr>
      <th>Matches Total (2)</th>
      <td>173.0</td>
      <td>6.182428e+02</td>
      <td>1.960553e+02</td>
      <td>63.000000</td>
      <td>516.000000</td>
      <td>627.000000</td>
      <td>7.660000e+02</td>
      <td>1.060000e+03</td>
    </tr>
    <tr>
      <th>Matches Home (2)</th>
      <td>173.0</td>
      <td>2.775838e+02</td>
      <td>9.220730e+01</td>
      <td>23.000000</td>
      <td>213.000000</td>
      <td>283.000000</td>
      <td>3.510000e+02</td>
      <td>4.600000e+02</td>
    </tr>
    <tr>
      <th>Matches Away (2)</th>
      <td>173.0</td>
      <td>2.688844e+02</td>
      <td>8.807079e+01</td>
      <td>32.000000</td>
      <td>214.000000</td>
      <td>277.000000</td>
      <td>3.360000e+02</td>
      <td>4.780000e+02</td>
    </tr>
    <tr>
      <th>Matches Neutral (2)</th>
      <td>173.0</td>
      <td>7.177457e+01</td>
      <td>3.173988e+01</td>
      <td>8.000000</td>
      <td>49.000000</td>
      <td>68.000000</td>
      <td>9.400000e+01</td>
      <td>1.570000e+02</td>
    </tr>
    <tr>
      <th>Matches Wins (2)</th>
      <td>173.0</td>
      <td>2.891561e+02</td>
      <td>1.125026e+02</td>
      <td>21.000000</td>
      <td>210.000000</td>
      <td>303.000000</td>
      <td>3.700000e+02</td>
      <td>5.640000e+02</td>
    </tr>
    <tr>
      <th>Matches Losses (2)</th>
      <td>173.0</td>
      <td>1.888613e+02</td>
      <td>6.803174e+01</td>
      <td>26.000000</td>
      <td>136.000000</td>
      <td>187.000000</td>
      <td>2.350000e+02</td>
      <td>4.100000e+02</td>
    </tr>
    <tr>
      <th>Matches Draws (2)</th>
      <td>173.0</td>
      <td>1.402254e+02</td>
      <td>4.229686e+01</td>
      <td>16.000000</td>
      <td>118.000000</td>
      <td>143.000000</td>
      <td>1.670000e+02</td>
      <td>2.290000e+02</td>
    </tr>
    <tr>
      <th>Goals For (2)</th>
      <td>173.0</td>
      <td>1.108064e+03</td>
      <td>4.547242e+02</td>
      <td>83.000000</td>
      <td>824.000000</td>
      <td>1167.000000</td>
      <td>1.366000e+03</td>
      <td>2.180000e+03</td>
    </tr>
    <tr>
      <th>Goals Against (2)</th>
      <td>173.0</td>
      <td>8.295838e+02</td>
      <td>3.082880e+02</td>
      <td>87.000000</td>
      <td>608.000000</td>
      <td>824.000000</td>
      <td>1.077000e+03</td>
      <td>1.615000e+03</td>
    </tr>
    <tr>
      <th>Data Year (2)</th>
      <td>173.0</td>
      <td>2.009197e+03</td>
      <td>6.839233e+00</td>
      <td>1999.000000</td>
      <td>2003.000000</td>
      <td>2011.000000</td>
      <td>2.015000e+03</td>
      <td>2.019000e+03</td>
    </tr>
    <tr>
      <th>GDP (PPP) (2)</th>
      <td>173.0</td>
      <td>1.119556e+06</td>
      <td>1.141579e+06</td>
      <td>16865.345703</td>
      <td>279525.093750</td>
      <td>531206.875000</td>
      <td>1.986634e+06</td>
      <td>4.308862e+06</td>
    </tr>
    <tr>
      <th>Population (2)</th>
      <td>173.0</td>
      <td>3.442009e+01</td>
      <td>3.535238e+01</td>
      <td>0.330243</td>
      <td>9.162939</td>
      <td>11.539328</td>
      <td>5.958908e+01</td>
      <td>1.458723e+02</td>
    </tr>
    <tr>
      <th>GDP (PPP) Per Capita (2)</th>
      <td>173.0</td>
      <td>3.325806e+04</td>
      <td>1.247084e+04</td>
      <td>7493.284135</td>
      <td>25177.362877</td>
      <td>33549.863626</td>
      <td>4.104300e+04</td>
      <td>7.183164e+04</td>
    </tr>
    <tr>
      <th>Elo_rating_diff</th>
      <td>173.0</td>
      <td>4.011561e+00</td>
      <td>1.750416e+02</td>
      <td>-398.000000</td>
      <td>-111.000000</td>
      <td>6.000000</td>
      <td>1.370000e+02</td>
      <td>4.440000e+02</td>
    </tr>
    <tr>
      <th>Home_advantage</th>
      <td>173.0</td>
      <td>4.046243e-02</td>
      <td>4.744444e-01</td>
      <td>-1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>Relative_experience</th>
      <td>173.0</td>
      <td>1.225697e+00</td>
      <td>9.651152e-01</td>
      <td>0.103110</td>
      <td>0.785036</td>
      <td>1.011986</td>
      <td>1.336898e+00</td>
      <td>9.095238e+00</td>
    </tr>
    <tr>
      <th>Relative_population</th>
      <td>173.0</td>
      <td>4.281837e+00</td>
      <td>1.597253e+01</td>
      <td>0.028253</td>
      <td>0.263376</td>
      <td>1.024848</td>
      <td>3.793660e+00</td>
      <td>2.016585e+02</td>
    </tr>
    <tr>
      <th>Relative_GDP_per_capita</th>
      <td>173.0</td>
      <td>1.317500e+00</td>
      <td>9.903390e-01</td>
      <td>0.163999</td>
      <td>0.729705</td>
      <td>1.007875</td>
      <td>1.623428e+00</td>
      <td>5.480461e+00</td>
    </tr>
    <tr>
      <th>Relative_ELO_rating</th>
      <td>173.0</td>
      <td>1.006392e+00</td>
      <td>9.537485e-02</td>
      <td>0.807635</td>
      <td>0.940793</td>
      <td>1.003058</td>
      <td>1.075358e+00</td>
      <td>1.291339e+00</td>
    </tr>
  </tbody>
</table>
</div>






<style  type="text/css" >
#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col52{
            background-color:  #b40426;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col6{
            background-color:  #80a3fa;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col39{
            background-color:  #b2ccfb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col8{
            background-color:  #bfd3f6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col43{
            background-color:  #88abfd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col48{
            background-color:  #dadce0;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col6{
            background-color:  #5e7de7;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col40{
            background-color:  #f1cdba;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col52{
            background-color:  #e8d6cc;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col21{
            background-color:  #d1dae9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col48{
            background-color:  #e0dbd8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col10{
            background-color:  #dddcdc;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col40{
            background-color:  #93b5fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col40{
            background-color:  #8badfd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col16{
            background-color:  #ead4c8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col14{
            background-color:  #e6d7cf;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col11{
            background-color:  #dbdcde;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col47{
            background-color:  #efcfbf;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col50{
            background-color:  #c0d4f5;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col49{
            background-color:  #f1ccb8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col32{
            background-color:  #a9c6fd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col29{
            background-color:  #b3cdfb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col22{
            background-color:  #799cf8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col7{
            background-color:  #ccd9ed;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col29{
            background-color:  #f5c0a7;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col28{
            background-color:  #f3c7b1;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col10{
            background-color:  #bbd1f8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col24{
            background-color:  #d5dbe5;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col46{
            background-color:  #94b6ff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col34{
            background-color:  #84a7fc;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col51{
            background-color:  #efcebd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col24{
            background-color:  #ebd3c6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col36{
            background-color:  #e9d5cb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col8{
            background-color:  #e3d9d3;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col52{
            background-color:  #f2cbb7;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col14{
            background-color:  #dedcdb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col24{
            background-color:  #bcd2f7;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col48{
            background-color:  #d2dbe8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col2{
            background-color:  #c7d7f0;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col3{
            background-color:  #c4d5f3;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col34{
            background-color:  #9dbdff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col46{
            background-color:  #d4dbe6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col8{
            background-color:  #6485ec;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col42{
            background-color:  #a5c3fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col3{
            background-color:  #d65244;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col22{
            background-color:  #6a8bef;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col25{
            background-color:  #c3d5f4;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col28{
            background-color:  #e97a5f;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col26{
            background-color:  #a6c4fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col1{
            background-color:  #b5cdfa;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col27{
            background-color:  #f2cab5;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col45{
            background-color:  #506bda;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col12{
            background-color:  #516ddb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col10{
            background-color:  #c9d7f0;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col2{
            background-color:  #cad8ef;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col47{
            background-color:  #e5d8d1;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col4{
            background-color:  #7597f6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col16{
            background-color:  #a3c2fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col34{
            background-color:  #a1c0ff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col14{
            background-color:  #dfdbd9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col1{
            background-color:  #cdd9ec;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col3{
            background-color:  #e7d7ce;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col48{
            background-color:  #cfdaea;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col16{
            background-color:  #7b9ff9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col13{
            background-color:  #5875e1;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col1{
            background-color:  #c1d4f4;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col26{
            background-color:  #b7cff9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col50{
            background-color:  #bed2f6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col16{
            background-color:  #cedaeb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col5{
            background-color:  #b1cbfc;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col10{
            background-color:  #90b2fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col11{
            background-color:  #edd2c3;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col22{
            background-color:  #cbd8ee;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col10{
            background-color:  #d3dbe7;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col24{
            background-color:  #edd1c2;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col4{
            background-color:  #5d7ce6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col45{
            background-color:  #6788ee;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col46{
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col21{
            background-color:  #eed0c0;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col36{
            background-color:  #96b7ff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col29{
            background-color:  #9bbcff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col40{
            background-color:  #9fbfff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col43{
            background-color:  #81a4fb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col43{
            background-color:  #6f92f3;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col33{
            background-color:  #5572df;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col52{
            background-color:  #b9d0f9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col12{
            background-color:  #7396f5;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col33{
            background-color:  #6b8df0;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col25{
            background-color:  #bad0f8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col39{
            background-color:  #afcafc;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col31{
            background-color:  #aac7fd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col24{
            background-color:  #9abbff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col35{
            background-color:  #9ebeff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col17{
            background-color:  #de614d;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col5{
            background-color:  #abc8fd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col31{
            background-color:  #f5c1a9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col37{
            background-color:  #4f69d9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col45{
            background-color:  #4e68d8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col33{
            background-color:  #6384eb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col9{
            background-color:  #ecd3c5;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col0{
            background-color:  #85a8fc;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col33{
            background-color:  #5673e0;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col36{
            background-color:  #c6d6f1;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col35{
            background-color:  #8fb1fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col22{
            background-color:  #779af7;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col2{
            background-color:  #c5d6f2;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col36{
            background-color:  #adc9fd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col25{
            background-color:  #6c8ff1;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col37{
            background-color:  #89acfd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col9{
            background-color:  #d7dce3;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col14{
            background-color:  #b6cefa;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col3{
            background-color:  #d8dce2;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col49{
            background-color:  #d9dce1;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col33{
            background-color:  #6180e9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col22{
            background-color:  #dc5d4a;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col15{
            background-color:  #e4d9d2;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col14{
            background-color:  #aec9fc;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col25{
            background-color:  #8caffe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col42{
            background-color:  #a2c1ff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col45{
            background-color:  #6687ed;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col46{
            background-color:  #7a9df8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col44{
            background-color:  #6282ea;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col9{
            background-color:  #e2dad5;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col32{
            background-color:  #5b7ae5;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col28{
            background-color:  #e67259;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col11{
            background-color:  #f7aa8c;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col3{
            background-color:  #f0cdbb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col5,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col17{
            background-color:  #d6dce4;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col26{
            background-color:  #7295f4;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col6{
            background-color:  #7699f6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col44{
            background-color:  #688aef;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col4{
            background-color:  #465ecf;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col38{
            background-color:  #c73635;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col45{
            background-color:  #3c4ec2;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col31{
            background-color:  #ec7f63;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col20{
            background-color:  #a7c5fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col45{
            background-color:  #7da0f9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col0{
            background-color:  #6e90f2;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col38{
            background-color:  #3f53c6;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col26{
            background-color:  #4358cb;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col13{
            background-color:  #3e51c5;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col45{
            background-color:  #4257c9;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col1{
            background-color:  #82a6fb;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col13{
            background-color:  #5977e3;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col19{
            background-color:  #7093f3;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col32{
            background-color:  #4055c8;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col42{
            background-color:  #ef886b;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col12{
            background-color:  #4b64d5;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col29{
            background-color:  #f7af91;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col17{
            background-color:  #f7b99e;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col2,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col5{
            background-color:  #dcdddd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col20{
            background-color:  #e1dad6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col22{
            background-color:  #5a78e4;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col48,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col14{
            background-color:  #98b9ff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col32,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col34{
            background-color:  #e46e56;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col49{
            background-color:  #4a63d3;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col3,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col1{
            background-color:  #92b4fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col31{
            background-color:  #ec8165;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col42{
            background-color:  #f39577;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col38{
            background-color:  #f29072;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col27{
            background-color:  #f4c6af;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col9{
            background-color:  #f7a688;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col37{
            background-color:  #8db0fe;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col16{
            background-color:  #f7b89c;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col25{
            background-color:  #3d50c3;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col13,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col43{
            background-color:  #5470de;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col18{
            background-color:  #f6bfa6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col49{
            background-color:  #97b8ff;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col1,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col6,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col29{
            background-color:  #5f7fe8;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col7,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col8,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col15{
            background-color:  #ead5c9;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col49{
            background-color:  #445acc;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col44{
            background-color:  #f7b497;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col42{
            background-color:  #7ea1fa;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col34{
            background-color:  #bb1b2c;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col39{
            background-color:  #be242e;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col28{
            background-color:  #c53334;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col46{
            background-color:  #f18d6f;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col14{
            background-color:  #c0282f;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col34{
            background-color:  #f6bea4;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col52{
            background-color:  #f6bda2;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col29{
            background-color:  #f7b79b;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col45{
            background-color:  #d1493f;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col44{
            background-color:  #f08a6c;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col37{
            background-color:  #d0473d;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col38{
            background-color:  #ee8468;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col35{
            background-color:  #cb3e38;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col35{
            background-color:  #c83836;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col25{
            background-color:  #d75445;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col37{
            background-color:  #f2c9b4;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col44{
            background-color:  #cf453c;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col17{
            background-color:  #f39778;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col18{
            background-color:  #d85646;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col19,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col21{
            background-color:  #e8765c;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col36{
            background-color:  #cd423b;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col36{
            background-color:  #d55042;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col39{
            background-color:  #f7bca1;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col39{
            background-color:  #f59c7d;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col24{
            background-color:  #ed8366;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col4,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col27{
            background-color:  #ea7b60;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col29{
            background-color:  #f7ac8e;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col41{
            background-color:  #e16751;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col30{
            background-color:  #df634e;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col29,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col40{
            background-color:  #f7b599;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col40{
            background-color:  #f7a889;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col24{
            background-color:  #d44e41;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col42,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col40{
            background-color:  #cc403a;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col38{
            background-color:  #ba162b;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col11{
            background-color:  #f7a98b;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col15,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col17,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col33{
            background-color:  #e9785d;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col40{
            background-color:  #e57058;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col20,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col38{
            background-color:  #f5a081;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col34{
            background-color:  #c32e31;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col47,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col9,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col26,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col28{
            background-color:  #f3c8b2;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col10,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col25,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col16,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col12,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col23,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col43,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col0,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col41{
            background-color:  #86a9fc;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col36{
            background-color:  #ca3b37;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col24,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col30{
            background-color:  #f5c4ac;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col31{
            background-color:  #f29274;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col14,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col19{
            background-color:  #c12b30;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col16{
            background-color:  #d24b40;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col18{
            background-color:  #b8122a;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col36,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col30{
            background-color:  #f39475;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col49,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col35{
            background-color:  #f5c2aa;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col35,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col35{
            background-color:  #f4c5ad;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col11,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col30{
            background-color:  #f7b093;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col18,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col37,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col41,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col30{
            background-color:  #f49a7b;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col21,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col46{
            background-color:  #f59f80;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col51,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col31,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col37{
            background-color:  #f6a586;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col4{
            background-color:  #485fd1;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col44,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col22{
            background-color:  #4961d2;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col45,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col33,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col33{
            background-color:  #455cce;
            color:  #f1f1f1;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col47{
            background-color:  #ee8669;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col52,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col27,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col27{
            background-color:  #eb7d62;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col28,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col9{
            background-color:  #e0654f;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col52{
            background-color:  #f6a283;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col41{
            background-color:  #f6a385;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col30,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col17{
            background-color:  #f7ba9f;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col42{
            background-color:  #e7745b;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col31{
            background-color:  #f7b194;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col37{
            background-color:  #f08b6e;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col39,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col34,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col37{
            background-color:  #e36c55;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col40,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col37{
            background-color:  #d95847;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col41{
            background-color:  #e36b54;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col22,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col50{
            background-color:  #4c66d6;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col46{
            background-color:  #f59d7e;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col36{
            background-color:  #dd5f4b;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col38,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col30{
            background-color:  #f7b396;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col50,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col0{
            background-color:  #536edd;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col46,#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col34{
            background-color:  #f18f71;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col36{
            background-color:  #f7ad90;
            color:  #000000;
        }#T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col9{
            background-color:  #e26952;
            color:  #000000;
        }</style><table id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Year</th>        <th class="col_heading level0 col1" >Goals_1</th>        <th class="col_heading level0 col2" >Goals_2</th>        <th class="col_heading level0 col3" >Goal_diff</th>        <th class="col_heading level0 col4" >Home_1</th>        <th class="col_heading level0 col5" >Home_2</th>        <th class="col_heading level0 col6" >Goal_total</th>        <th class="col_heading level0 col7" >Rank Local</th>        <th class="col_heading level0 col8" >Rank Global</th>        <th class="col_heading level0 col9" >Rating</th>        <th class="col_heading level0 col10" >Average Rank</th>        <th class="col_heading level0 col11" >Average Rating</th>        <th class="col_heading level0 col12" >1 Year Change Rank</th>        <th class="col_heading level0 col13" >1 Year Change Rating</th>        <th class="col_heading level0 col14" >Matches Total</th>        <th class="col_heading level0 col15" >Matches Home</th>        <th class="col_heading level0 col16" >Matches Away</th>        <th class="col_heading level0 col17" >Matches Neutral</th>        <th class="col_heading level0 col18" >Matches Wins</th>        <th class="col_heading level0 col19" >Matches Losses</th>        <th class="col_heading level0 col20" >Matches Draws</th>        <th class="col_heading level0 col21" >Goals For</th>        <th class="col_heading level0 col22" >Goals Against</th>        <th class="col_heading level0 col23" >Data Year</th>        <th class="col_heading level0 col24" >GDP (PPP)</th>        <th class="col_heading level0 col25" >Population</th>        <th class="col_heading level0 col26" >GDP (PPP) Per Capita</th>        <th class="col_heading level0 col27" >Rank Local (2)</th>        <th class="col_heading level0 col28" >Rank Global (2)</th>        <th class="col_heading level0 col29" >Rating (2)</th>        <th class="col_heading level0 col30" >Average Rank (2)</th>        <th class="col_heading level0 col31" >Average Rating (2)</th>        <th class="col_heading level0 col32" >1 Year Change Rank (2)</th>        <th class="col_heading level0 col33" >1 Year Change Rating (2)</th>        <th class="col_heading level0 col34" >Matches Total (2)</th>        <th class="col_heading level0 col35" >Matches Home (2)</th>        <th class="col_heading level0 col36" >Matches Away (2)</th>        <th class="col_heading level0 col37" >Matches Neutral (2)</th>        <th class="col_heading level0 col38" >Matches Wins (2)</th>        <th class="col_heading level0 col39" >Matches Losses (2)</th>        <th class="col_heading level0 col40" >Matches Draws (2)</th>        <th class="col_heading level0 col41" >Goals For (2)</th>        <th class="col_heading level0 col42" >Goals Against (2)</th>        <th class="col_heading level0 col43" >Data Year (2)</th>        <th class="col_heading level0 col44" >GDP (PPP) (2)</th>        <th class="col_heading level0 col45" >Population (2)</th>        <th class="col_heading level0 col46" >GDP (PPP) Per Capita (2)</th>        <th class="col_heading level0 col47" >Elo_rating_diff</th>        <th class="col_heading level0 col48" >Home_advantage</th>        <th class="col_heading level0 col49" >Relative_experience</th>        <th class="col_heading level0 col50" >Relative_population</th>        <th class="col_heading level0 col51" >Relative_GDP_per_capita</th>        <th class="col_heading level0 col52" >Relative_ELO_rating</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row0" class="row_heading level0 row0" >Year</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col0" class="data row0 col0" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col1" class="data row0 col1" >-0.027040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col2" class="data row0 col2" >-0.055270</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col3" class="data row0 col3" >0.009779</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col4" class="data row0 col4" >0.139323</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col5" class="data row0 col5" >0.130791</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col6" class="data row0 col6" >-0.057600</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col7" class="data row0 col7" >0.208459</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col8" class="data row0 col8" >0.119249</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col9" class="data row0 col9" >-0.059841</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col10" class="data row0 col10" >0.052615</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col11" class="data row0 col11" >0.025420</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col12" class="data row0 col12" >0.081657</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col13" class="data row0 col13" >0.057362</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col14" class="data row0 col14" >0.354077</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col15" class="data row0 col15" >0.328604</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col16" class="data row0 col16" >0.332956</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col17" class="data row0 col17" >0.319800</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col18" class="data row0 col18" >0.305614</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col19" class="data row0 col19" >0.257118</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col20" class="data row0 col20" >0.390689</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col21" class="data row0 col21" >0.262763</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col22" class="data row0 col22" >0.240312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col23" class="data row0 col23" >0.999181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col24" class="data row0 col24" >0.092892</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col25" class="data row0 col25" >-0.010312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col26" class="data row0 col26" >0.304851</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col27" class="data row0 col27" >0.305324</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col28" class="data row0 col28" >0.259107</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col29" class="data row0 col29" >-0.185116</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col30" class="data row0 col30" >0.114521</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col31" class="data row0 col31" >-0.032236</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col32" class="data row0 col32" >0.064162</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col33" class="data row0 col33" >0.107218</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col34" class="data row0 col34" >0.306104</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col35" class="data row0 col35" >0.302135</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col36" class="data row0 col36" >0.268532</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col37" class="data row0 col37" >0.267942</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col38" class="data row0 col38" >0.243925</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col39" class="data row0 col39" >0.269882</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col40" class="data row0 col40" >0.335971</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col41" class="data row0 col41" >0.192936</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col42" class="data row0 col42" >0.219553</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col43" class="data row0 col43" >0.999181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col44" class="data row0 col44" >0.157812</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col45" class="data row0 col45" >0.069006</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col46" class="data row0 col46" >0.344897</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col47" class="data row0 col47" >0.082644</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col48" class="data row0 col48" >0.019894</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col49" class="data row0 col49" >0.006154</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col50" class="data row0 col50" >0.084347</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col51" class="data row0 col51" >-0.088840</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row0_col52" class="data row0 col52" >0.091312</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row1" class="row_heading level0 row1" >Goals_1</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col0" class="data row1 col0" >-0.027040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col1" class="data row1 col1" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col2" class="data row1 col2" >-0.120010</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col3" class="data row1 col3" >0.835636</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col4" class="data row1 col4" >0.045197</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col5" class="data row1 col5" >-0.008193</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col6" class="data row1 col6" >0.787920</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col7" class="data row1 col7" >-0.305658</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col8" class="data row1 col8" >-0.296821</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col9" class="data row1 col9" >0.296767</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col10" class="data row1 col10" >-0.238502</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col11" class="data row1 col11" >0.225890</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col12" class="data row1 col12" >-0.167248</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col13" class="data row1 col13" >-0.151949</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col14" class="data row1 col14" >0.165593</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col15" class="data row1 col15" >0.176155</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col16" class="data row1 col16" >0.096714</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col17" class="data row1 col17" >0.242782</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col18" class="data row1 col18" >0.227829</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col19" class="data row1 col19" >-0.013347</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col20" class="data row1 col20" >0.160638</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col21" class="data row1 col21" >0.215455</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col22" class="data row1 col22" >0.074271</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col23" class="data row1 col23" >-0.027040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col24" class="data row1 col24" >0.224033</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col25" class="data row1 col25" >0.139519</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col26" class="data row1 col26" >0.140413</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col27" class="data row1 col27" >0.055158</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col28" class="data row1 col28" >0.101520</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col29" class="data row1 col29" >-0.073758</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col30" class="data row1 col30" >0.102114</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col31" class="data row1 col31" >-0.074107</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col32" class="data row1 col32" >-0.024751</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col33" class="data row1 col33" >-0.039889</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col34" class="data row1 col34" >-0.006771</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col35" class="data row1 col35" >-0.046243</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col36" class="data row1 col36" >-0.005457</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col37" class="data row1 col37" >0.107358</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col38" class="data row1 col38" >0.007259</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col39" class="data row1 col39" >-0.038496</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col40" class="data row1 col40" >0.010474</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col41" class="data row1 col41" >-0.005749</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col42" class="data row1 col42" >-0.040640</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col43" class="data row1 col43" >-0.027040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col44" class="data row1 col44" >-0.018947</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col45" class="data row1 col45" >-0.009853</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col46" class="data row1 col46" >-0.071821</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col47" class="data row1 col47" >0.270399</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col48" class="data row1 col48" >0.039548</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col49" class="data row1 col49" >0.087769</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col50" class="data row1 col50" >0.224610</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col51" class="data row1 col51" >0.171901</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row1_col52" class="data row1 col52" >0.272704</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row2" class="row_heading level0 row2" >Goals_2</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col0" class="data row2 col0" >-0.055270</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col1" class="data row2 col1" >-0.120010</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col2" class="data row2 col2" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col3" class="data row2 col3" >-0.645599</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col4" class="data row2 col4" >-0.015307</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col5" class="data row2 col5" >-0.089835</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col6" class="data row2 col6" >0.516769</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col7" class="data row2 col7" >0.184248</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col8" class="data row2 col8" >0.096002</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col9" class="data row2 col9" >-0.117715</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col10" class="data row2 col10" >0.052934</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col11" class="data row2 col11" >-0.066167</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col12" class="data row2 col12" >0.079141</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col13" class="data row2 col13" >0.094137</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col14" class="data row2 col14" >0.012887</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col15" class="data row2 col15" >-0.027698</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col16" class="data row2 col16" >0.097024</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col17" class="data row2 col17" >-0.104521</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col18" class="data row2 col18" >-0.035578</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col19" class="data row2 col19" >0.124857</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col20" class="data row2 col20" >-0.046584</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col21" class="data row2 col21" >0.016586</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col22" class="data row2 col22" >0.112082</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col23" class="data row2 col23" >-0.055270</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col24" class="data row2 col24" >-0.116405</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col25" class="data row2 col25" >-0.043534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col26" class="data row2 col26" >-0.132443</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col27" class="data row2 col27" >-0.202140</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col28" class="data row2 col28" >-0.143813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col29" class="data row2 col29" >0.173110</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col30" class="data row2 col30" >-0.069452</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col31" class="data row2 col31" >0.085403</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col32" class="data row2 col32" >-0.051804</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col33" class="data row2 col33" >0.025883</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col34" class="data row2 col34" >-0.052202</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col35" class="data row2 col35" >-0.025269</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col36" class="data row2 col36" >-0.077926</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col37" class="data row2 col37" >-0.030840</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col38" class="data row2 col38" >-0.015329</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col39" class="data row2 col39" >-0.090208</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col40" class="data row2 col40" >-0.056300</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col41" class="data row2 col41" >-0.014466</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col42" class="data row2 col42" >-0.067570</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col43" class="data row2 col43" >-0.055270</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col44" class="data row2 col44" >0.020977</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col45" class="data row2 col45" >-0.015539</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col46" class="data row2 col46" >0.087310</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col47" class="data row2 col47" >-0.203178</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col48" class="data row2 col48" >0.040090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col49" class="data row2 col49" >0.062642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col50" class="data row2 col50" >0.049408</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col51" class="data row2 col51" >-0.200309</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row2_col52" class="data row2 col52" >-0.198575</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row3" class="row_heading level0 row3" >Goal_diff</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col0" class="data row3 col0" >0.009779</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col1" class="data row3 col1" >0.835636</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col2" class="data row3 col2" >-0.645599</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col3" class="data row3 col3" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col4" class="data row3 col4" >0.043236</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col5" class="data row3 col5" >0.043402</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col6" class="data row3 col6" >0.320178</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col7" class="data row3 col7" >-0.337064</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col8" class="data row3 col8" >-0.281441</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col9" class="data row3 col9" >0.293414</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col10" class="data row3 col10" >-0.212752</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col11" class="data row3 col11" >0.210372</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col12" class="data row3 col12" >-0.172441</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col13" class="data row3 col13" >-0.168969</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col14" class="data row3 col14" >0.120250</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col15" class="data row3 col15" >0.150830</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col16" class="data row3 col16" >0.020715</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col17" class="data row3 col17" >0.244587</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col18" class="data row3 col18" >0.194939</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col19" class="data row3 col19" >-0.079348</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col20" class="data row3 col20" >0.149343</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col21" class="data row3 col21" >0.156559</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col22" class="data row3 col22" >-0.004881</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col23" class="data row3 col23" >0.009779</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col24" class="data row3 col24" >0.236739</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col25" class="data row3 col25" >0.131410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col26" class="data row3 col26" >0.181289</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col27" class="data row3 col27" >0.154270</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col28" class="data row3 col28" >0.157662</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col29" class="data row3 col29" >-0.152516</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col30" class="data row3 col30" >0.116977</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col31" class="data row3 col31" >-0.104258</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col32" class="data row3 col32" >0.009623</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col33" class="data row3 col33" >-0.045004</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col34" class="data row3 col34" >0.023674</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col35" class="data row3 col35" >-0.021591</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col36" class="data row3 col36" >0.038918</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col37" class="data row3 col37" >0.099647</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col38" class="data row3 col38" >0.014066</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col39" class="data row3 col39" >0.020298</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col40" class="data row3 col40" >0.039207</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col41" class="data row3 col41" >0.003581</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col42" class="data row3 col42" >0.006124</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col43" class="data row3 col43" >0.009779</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col44" class="data row3 col44" >-0.026181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col45" class="data row3 col45" >0.001018</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col46" class="data row3 col46" >-0.103554</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col47" class="data row3 col47" >0.320416</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col48" class="data row3 col48" >0.008241</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col49" class="data row3 col49" >0.032856</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col50" class="data row3 col50" >0.145442</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col51" class="data row3 col51" >0.243060</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row3_col52" class="data row3 col52" >0.319642</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row4" class="row_heading level0 row4" >Home_1</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col0" class="data row4 col0" >0.139323</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col1" class="data row4 col1" >0.045197</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col2" class="data row4 col2" >-0.015307</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col3" class="data row4 col3" >0.043236</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col4" class="data row4 col4" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col5" class="data row4 col5" >-0.125005</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col6" class="data row4 col6" >0.029482</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col7" class="data row4 col7" >0.038753</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col8" class="data row4 col8" >0.103609</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col9" class="data row4 col9" >-0.050974</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col10" class="data row4 col10" >-0.052521</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col11" class="data row4 col11" >0.047187</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col12" class="data row4 col12" >-0.112956</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col13" class="data row4 col13" >0.017546</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col14" class="data row4 col14" >0.126201</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col15" class="data row4 col15" >0.163511</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col16" class="data row4 col16" >0.096965</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col17" class="data row4 col17" >0.044117</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col18" class="data row4 col18" >0.072756</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col19" class="data row4 col19" >0.159463</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col20" class="data row4 col20" >0.121853</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col21" class="data row4 col21" >0.098592</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col22" class="data row4 col22" >0.159523</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col23" class="data row4 col23" >0.133515</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col24" class="data row4 col24" >-0.002807</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col25" class="data row4 col25" >-0.053640</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col26" class="data row4 col26" >0.227658</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col27" class="data row4 col27" >0.117830</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col28" class="data row4 col28" >0.048050</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col29" class="data row4 col29" >-0.073276</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col30" class="data row4 col30" >0.074083</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col31" class="data row4 col31" >-0.086812</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col32" class="data row4 col32" >0.028418</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col33" class="data row4 col33" >0.022321</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col34" class="data row4 col34" >0.115083</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col35" class="data row4 col35" >0.078806</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col36" class="data row4 col36" >0.179654</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col37" class="data row4 col37" >-0.016577</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col38" class="data row4 col38" >0.042861</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col39" class="data row4 col39" >0.203090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col40" class="data row4 col40" >0.092773</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col41" class="data row4 col41" >0.078123</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col42" class="data row4 col42" >0.175602</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col43" class="data row4 col43" >0.133515</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col44" class="data row4 col44" >-0.098410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col45" class="data row4 col45" >-0.079523</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col46" class="data row4 col46" >0.060064</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col47" class="data row4 col47" >0.013143</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col48" class="data row4 col48" >0.794244</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col49" class="data row4 col49" >-0.000479</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col50" class="data row4 col50" >0.160143</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col51" class="data row4 col51" >0.129389</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row4_col52" class="data row4 col52" >0.008687</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row5" class="row_heading level0 row5" >Home_2</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col0" class="data row5 col0" >0.130791</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col1" class="data row5 col1" >-0.008193</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col2" class="data row5 col2" >-0.089835</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col3" class="data row5 col3" >0.043402</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col4" class="data row5 col4" >-0.125005</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col5" class="data row5 col5" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col6" class="data row5 col6" >-0.062786</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col7" class="data row5 col7" >0.114887</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col8" class="data row5 col8" >0.088737</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col9" class="data row5 col9" >-0.038119</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col10" class="data row5 col10" >0.130323</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col11" class="data row5 col11" >-0.128785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col12" class="data row5 col12" >-0.025578</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col13" class="data row5 col13" >0.045687</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col14" class="data row5 col14" >-0.030690</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col15" class="data row5 col15" >-0.013170</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col16" class="data row5 col16" >-0.036611</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col17" class="data row5 col17" >-0.049165</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col18" class="data row5 col18" >-0.084803</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col19" class="data row5 col19" >0.069676</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col20" class="data row5 col20" >-0.031276</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col21" class="data row5 col21" >-0.097014</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col22" class="data row5 col22" >0.022002</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col23" class="data row5 col23" >0.119534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col24" class="data row5 col24" >0.018187</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col25" class="data row5 col25" >0.033152</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col26" class="data row5 col26" >0.004791</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col27" class="data row5 col27" >-0.032095</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col28" class="data row5 col28" >-0.066137</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col29" class="data row5 col29" >0.104324</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col30" class="data row5 col30" >-0.126111</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col31" class="data row5 col31" >0.113456</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col32" class="data row5 col32" >-0.118182</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col33" class="data row5 col33" >-0.010978</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col34" class="data row5 col34" >0.207813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col35" class="data row5 col35" >0.206087</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col36" class="data row5 col36" >0.151284</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col37" class="data row5 col37" >0.265167</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col38" class="data row5 col38" >0.232201</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col39" class="data row5 col39" >0.089774</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col40" class="data row5 col40" >0.201248</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col41" class="data row5 col41" >0.228297</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col42" class="data row5 col42" >0.147512</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col43" class="data row5 col43" >0.119534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col44" class="data row5 col44" >0.245284</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col45" class="data row5 col45" >0.157189</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col46" class="data row5 col46" >0.199662</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col47" class="data row5 col47" >-0.098104</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col48" class="data row5 col48" >-0.702118</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col49" class="data row5 col49" >-0.132134</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col50" class="data row5 col50" >-0.025911</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col51" class="data row5 col51" >-0.127645</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row5_col52" class="data row5 col52" >-0.098073</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row6" class="row_heading level0 row6" >Goal_total</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col0" class="data row6 col0" >-0.057600</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col1" class="data row6 col1" >0.787920</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col2" class="data row6 col2" >0.516769</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col3" class="data row6 col3" >0.320178</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col4" class="data row6 col4" >0.029482</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col5" class="data row6 col5" >-0.062786</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col6" class="data row6 col6" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col7" class="data row6 col7" >-0.149305</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col8" class="data row6 col8" >-0.196419</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col9" class="data row6 col9" >0.182905</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col10" class="data row6 col10" >-0.172841</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col11" class="data row6 col11" >0.153757</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col12" class="data row6 col12" >-0.095140</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col13" class="data row6 col13" >-0.072645</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col14" class="data row6 col14" >0.150793</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col15" class="data row6 col15" >0.134729</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col16" class="data row6 col16" >0.143583</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col17" class="data row6 col17" >0.144534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col18" class="data row6 col18" >0.174403</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col19" class="data row6 col19" >0.065934</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col20" class="data row6 col20" >0.109634</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col21" class="data row6 col21" >0.196087</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col22" class="data row6 col22" >0.133568</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col23" class="data row6 col23" >-0.057600</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col24" class="data row6 col24" >0.120995</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col25" class="data row6 col25" >0.093313</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col26" class="data row6 col26" >0.038937</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col27" class="data row6 col27" >-0.077813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col28" class="data row6 col28" >-0.001655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col29" class="data row6 col29" >0.043768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col30" class="data row6 col30" >0.044981</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col31" class="data row6 col31" >-0.010934</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col32" class="data row6 col32" >-0.053476</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col33" class="data row6 col33" >-0.018344</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col34" class="data row6 col34" >-0.038219</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col35" class="data row6 col35" >-0.055551</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col36" class="data row6 col36" >-0.053040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col37" class="data row6 col37" >0.073452</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col38" class="data row6 col38" >-0.003248</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col39" class="data row6 col39" >-0.089150</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col40" class="data row6 col40" >-0.025888</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col41" class="data row6 col41" >-0.013930</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col42" class="data row6 col42" >-0.076957</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col43" class="data row6 col43" >-0.057600</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col44" class="data row6 col44" >-0.003328</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col45" class="data row6 col45" >-0.018135</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col46" class="data row6 col46" >-0.007781</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col47" class="data row6 col47" >0.107157</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col48" class="data row6 col48" >0.058971</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col49" class="data row6 col49" >0.114542</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col50" class="data row6 col50" >0.224340</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col51" class="data row6 col51" >0.023997</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row6_col52" class="data row6 col52" >0.112000</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row7" class="row_heading level0 row7" >Rank Local</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col0" class="data row7 col0" >0.208459</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col1" class="data row7 col1" >-0.305658</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col2" class="data row7 col2" >0.184248</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col3" class="data row7 col3" >-0.337064</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col4" class="data row7 col4" >0.038753</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col5" class="data row7 col5" >0.114887</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col6" class="data row7 col6" >-0.149305</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col7" class="data row7 col7" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col8" class="data row7 col8" >0.895092</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col9" class="data row7 col9" >-0.932067</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col10" class="data row7 col10" >0.626423</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col11" class="data row7 col11" >-0.578218</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col12" class="data row7 col12" >0.153169</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col13" class="data row7 col13" >0.138886</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col14" class="data row7 col14" >-0.158488</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col15" class="data row7 col15" >-0.234039</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col16" class="data row7 col16" >0.041219</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col17" class="data row7 col17" >-0.424280</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col18" class="data row7 col18" >-0.352563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col19" class="data row7 col19" >0.214076</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col20" class="data row7 col20" >-0.145714</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col21" class="data row7 col21" >-0.278837</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col22" class="data row7 col22" >0.051028</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col23" class="data row7 col23" >0.205147</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col24" class="data row7 col24" >-0.419915</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col25" class="data row7 col25" >-0.229838</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col26" class="data row7 col26" >-0.203206</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col27" class="data row7 col27" >0.037470</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col28" class="data row7 col28" >0.004748</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col29" class="data row7 col29" >0.006097</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col30" class="data row7 col30" >-0.033548</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col31" class="data row7 col31" >0.053100</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col32" class="data row7 col32" >0.046169</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col33" class="data row7 col33" >0.060882</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col34" class="data row7 col34" >0.010401</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col35" class="data row7 col35" >0.028806</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col36" class="data row7 col36" >0.027291</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col37" class="data row7 col37" >-0.095164</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col38" class="data row7 col38" >-0.017483</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col39" class="data row7 col39" >0.066848</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col40" class="data row7 col40" >-0.012807</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col41" class="data row7 col41" >0.012138</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col42" class="data row7 col42" >0.043040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col43" class="data row7 col43" >0.205147</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col44" class="data row7 col44" >-0.112362</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col45" class="data row7 col45" >-0.127366</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col46" class="data row7 col46" >0.114020</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col47" class="data row7 col47" >-0.672655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col48" class="data row7 col48" >-0.042544</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col49" class="data row7 col49" >-0.048738</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col50" class="data row7 col50" >-0.084076</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col51" class="data row7 col51" >-0.163334</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row7_col52" class="data row7 col52" >-0.662025</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row8" class="row_heading level0 row8" >Rank Global</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col0" class="data row8 col0" >0.119249</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col1" class="data row8 col1" >-0.296821</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col2" class="data row8 col2" >0.096002</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col3" class="data row8 col3" >-0.281441</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col4" class="data row8 col4" >0.103609</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col5" class="data row8 col5" >0.088737</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col6" class="data row8 col6" >-0.196419</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col7" class="data row8 col7" >0.895092</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col8" class="data row8 col8" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col9" class="data row8 col9" >-0.940073</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col10" class="data row8 col10" >0.654002</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col11" class="data row8 col11" >-0.580753</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col12" class="data row8 col12" >0.195370</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col13" class="data row8 col13" >0.175777</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col14" class="data row8 col14" >-0.234114</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col15" class="data row8 col15" >-0.278563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col16" class="data row8 col16" >-0.065865</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col17" class="data row8 col17" >-0.465210</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col18" class="data row8 col18" >-0.397074</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col19" class="data row8 col19" >0.129254</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col20" class="data row8 col20" >-0.235089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col21" class="data row8 col21" >-0.320707</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col22" class="data row8 col22" >-0.012519</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col23" class="data row8 col23" >0.118922</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col24" class="data row8 col24" >-0.383505</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col25" class="data row8 col25" >-0.223325</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col26" class="data row8 col26" >-0.205782</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col27" class="data row8 col27" >0.002408</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col28" class="data row8 col28" >-0.029842</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col29" class="data row8 col29" >0.025640</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col30" class="data row8 col30" >-0.063775</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col31" class="data row8 col31" >0.077593</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col32" class="data row8 col32" >0.021785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col33" class="data row8 col33" >0.019338</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col34" class="data row8 col34" >0.011679</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col35" class="data row8 col35" >0.027125</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col36" class="data row8 col36" >0.018057</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col37" class="data row8 col37" >-0.056763</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col38" class="data row8 col38" >0.001984</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col39" class="data row8 col39" >0.037375</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col40" class="data row8 col40" >-0.011257</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col41" class="data row8 col41" >0.025741</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col42" class="data row8 col42" >0.034479</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col43" class="data row8 col43" >0.118922</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col44" class="data row8 col44" >-0.044279</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col45" class="data row8 col45" >-0.070009</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col46" class="data row8 col46" >0.110052</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col47" class="data row8 col47" >-0.691653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col48" class="data row8 col48" >0.020017</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col49" class="data row8 col49" >-0.066596</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col50" class="data row8 col50" >-0.067435</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col51" class="data row8 col51" >-0.169190</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row8_col52" class="data row8 col52" >-0.681077</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row9" class="row_heading level0 row9" >Rating</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col0" class="data row9 col0" >-0.059841</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col1" class="data row9 col1" >0.296767</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col2" class="data row9 col2" >-0.117715</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col3" class="data row9 col3" >0.293414</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col4" class="data row9 col4" >-0.050974</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col5" class="data row9 col5" >-0.038119</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col6" class="data row9 col6" >0.182905</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col7" class="data row9 col7" >-0.932067</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col8" class="data row9 col8" >-0.940073</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col9" class="data row9 col9" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col10" class="data row9 col10" >-0.630384</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col11" class="data row9 col11" >0.593890</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col12" class="data row9 col12" >-0.183734</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col13" class="data row9 col13" >-0.131246</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col14" class="data row9 col14" >0.264492</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col15" class="data row9 col15" >0.324167</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col16" class="data row9 col16" >0.073659</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col17" class="data row9 col17" >0.501207</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col18" class="data row9 col18" >0.444523</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col19" class="data row9 col19" >-0.129265</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col20" class="data row9 col20" >0.247548</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col21" class="data row9 col21" >0.366552</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col22" class="data row9 col22" >0.034834</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col23" class="data row9 col23" >-0.061889</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col24" class="data row9 col24" >0.453588</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col25" class="data row9 col25" >0.253114</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col26" class="data row9 col26" >0.245205</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col27" class="data row9 col27" >0.016649</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col28" class="data row9 col28" >0.029785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col29" class="data row9 col29" >-0.026171</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col30" class="data row9 col30" >0.058254</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col31" class="data row9 col31" >-0.071991</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col32" class="data row9 col32" >-0.033684</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col33" class="data row9 col33" >-0.032625</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col34" class="data row9 col34" >0.032784</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col35" class="data row9 col35" >0.021691</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col36" class="data row9 col36" >0.010229</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col37" class="data row9 col37" >0.111108</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col38" class="data row9 col38" >0.038588</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col39" class="data row9 col39" >-0.006169</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col40" class="data row9 col40" >0.059246</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col41" class="data row9 col41" >0.005288</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col42" class="data row9 col42" >0.002037</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col43" class="data row9 col43" >-0.061889</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col44" class="data row9 col44" >0.112632</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col45" class="data row9 col45" >0.114451</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col46" class="data row9 col46" >-0.043993</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col47" class="data row9 col47" >0.734996</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col48" class="data row9 col48" >-0.013239</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col49" class="data row9 col49" >0.061703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col50" class="data row9 col50" >0.071847</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col51" class="data row9 col51" >0.158316</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row9_col52" class="data row9 col52" >0.723067</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row10" class="row_heading level0 row10" >Average Rank</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col0" class="data row10 col0" >0.052615</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col1" class="data row10 col1" >-0.238502</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col2" class="data row10 col2" >0.052934</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col3" class="data row10 col3" >-0.212752</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col4" class="data row10 col4" >-0.052521</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col5" class="data row10 col5" >0.130323</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col6" class="data row10 col6" >-0.172841</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col7" class="data row10 col7" >0.626423</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col8" class="data row10 col8" >0.654002</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col9" class="data row10 col9" >-0.630384</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col10" class="data row10 col10" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col11" class="data row10 col11" >-0.953029</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col12" class="data row10 col12" >0.300963</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col13" class="data row10 col13" >0.258598</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col14" class="data row10 col14" >-0.454551</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col15" class="data row10 col15" >-0.447504</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col16" class="data row10 col16" >-0.323160</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col17" class="data row10 col17" >-0.626145</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col18" class="data row10 col18" >-0.653132</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col19" class="data row10 col19" >0.087305</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col20" class="data row10 col20" >-0.500735</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col21" class="data row10 col21" >-0.593433</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col22" class="data row10 col22" >-0.133458</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col23" class="data row10 col23" >0.049964</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col24" class="data row10 col24" >-0.411368</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col25" class="data row10 col25" >-0.251766</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col26" class="data row10 col26" >-0.239768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col27" class="data row10 col27" >0.033726</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col28" class="data row10 col28" >0.003027</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col29" class="data row10 col29" >-0.000073</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col30" class="data row10 col30" >-0.086594</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col31" class="data row10 col31" >0.101664</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col32" class="data row10 col32" >0.007133</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col33" class="data row10 col33" >0.013072</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col34" class="data row10 col34" >0.092535</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col35" class="data row10 col35" >0.090088</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col36" class="data row10 col36" >0.111694</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col37" class="data row10 col37" >-0.000054</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col38" class="data row10 col38" >0.081719</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col39" class="data row10 col39" >0.079245</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col40" class="data row10 col40" >0.084103</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col41" class="data row10 col41" >0.106544</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col42" class="data row10 col42" >0.092964</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col43" class="data row10 col43" >0.049964</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col44" class="data row10 col44" >0.027181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col45" class="data row10 col45" >0.009901</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col46" class="data row10 col46" >0.150828</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col47" class="data row10 col47" >-0.452090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col48" class="data row10 col48" >-0.117504</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col49" class="data row10 col49" >-0.212514</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col50" class="data row10 col50" >-0.052703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col51" class="data row10 col51" >-0.199415</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row10_col52" class="data row10 col52" >-0.446640</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row11" class="row_heading level0 row11" >Average Rating</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col0" class="data row11 col0" >0.025420</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col1" class="data row11 col1" >0.225890</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col2" class="data row11 col2" >-0.066167</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col3" class="data row11 col3" >0.210372</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col4" class="data row11 col4" >0.047187</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col5" class="data row11 col5" >-0.128785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col6" class="data row11 col6" >0.153757</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col7" class="data row11 col7" >-0.578218</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col8" class="data row11 col8" >-0.580753</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col9" class="data row11 col9" >0.593890</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col10" class="data row11 col10" >-0.953029</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col11" class="data row11 col11" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col12" class="data row11 col12" >-0.255863</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col13" class="data row11 col13" >-0.247371</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col14" class="data row11 col14" >0.370581</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col15" class="data row11 col15" >0.357545</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col16" class="data row11 col16" >0.233883</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col17" class="data row11 col17" >0.612355</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col18" class="data row11 col18" >0.619111</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col19" class="data row11 col19" >-0.220181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col20" class="data row11 col20" >0.426214</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col21" class="data row11 col21" >0.548189</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col22" class="data row11 col22" >0.007131</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col23" class="data row11 col23" >0.027931</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col24" class="data row11 col24" >0.395999</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col25" class="data row11 col25" >0.214778</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col26" class="data row11 col26" >0.197321</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col27" class="data row11 col27" >-0.024020</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col28" class="data row11 col28" >0.008650</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col29" class="data row11 col29" >-0.006319</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col30" class="data row11 col30" >0.067027</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col31" class="data row11 col31" >-0.083622</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col32" class="data row11 col32" >0.010165</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col33" class="data row11 col33" >-0.004835</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col34" class="data row11 col34" >-0.021473</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col35" class="data row11 col35" >-0.016264</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col36" class="data row11 col36" >-0.043278</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col37" class="data row11 col37" >0.034693</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col38" class="data row11 col38" >-0.025052</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col39" class="data row11 col39" >-0.013380</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col40" class="data row11 col40" >-0.011379</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col41" class="data row11 col41" >-0.045051</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col42" class="data row11 col42" >-0.022737</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col43" class="data row11 col43" >0.027931</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col44" class="data row11 col44" >-0.028103</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col45" class="data row11 col45" >-0.013413</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col46" class="data row11 col46" >-0.092119</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col47" class="data row11 col47" >0.430250</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col48" class="data row11 col48" >0.112734</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col49" class="data row11 col49" >0.146912</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col50" class="data row11 col50" >0.012540</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col51" class="data row11 col51" >0.155931</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row11_col52" class="data row11 col52" >0.425818</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row12" class="row_heading level0 row12" >1 Year Change Rank</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col0" class="data row12 col0" >0.081657</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col1" class="data row12 col1" >-0.167248</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col2" class="data row12 col2" >0.079141</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col3" class="data row12 col3" >-0.172441</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col4" class="data row12 col4" >-0.112956</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col5" class="data row12 col5" >-0.025578</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col6" class="data row12 col6" >-0.095140</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col7" class="data row12 col7" >0.153169</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col8" class="data row12 col8" >0.195370</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col9" class="data row12 col9" >-0.183734</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col10" class="data row12 col10" >0.300963</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col11" class="data row12 col11" >-0.255863</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col12" class="data row12 col12" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col13" class="data row12 col13" >0.776446</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col14" class="data row12 col14" >0.006777</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col15" class="data row12 col15" >-0.011639</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col16" class="data row12 col16" >0.089184</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col17" class="data row12 col17" >-0.171935</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col18" class="data row12 col18" >-0.081205</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col19" class="data row12 col19" >0.164537</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col20" class="data row12 col20" >-0.028031</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col21" class="data row12 col21" >-0.048268</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col22" class="data row12 col22" >0.106311</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col23" class="data row12 col23" >0.080312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col24" class="data row12 col24" >-0.176918</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col25" class="data row12 col25" >-0.101992</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col26" class="data row12 col26" >-0.150388</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col27" class="data row12 col27" >-0.013852</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col28" class="data row12 col28" >-0.025816</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col29" class="data row12 col29" >0.045467</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col30" class="data row12 col30" >-0.087162</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col31" class="data row12 col31" >0.049743</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col32" class="data row12 col32" >-0.085319</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col33" class="data row12 col33" >-0.028497</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col34" class="data row12 col34" >0.083268</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col35" class="data row12 col35" >0.076981</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col36" class="data row12 col36" >0.065275</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col37" class="data row12 col37" >0.109579</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col38" class="data row12 col38" >0.089838</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col39" class="data row12 col39" >0.038024</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col40" class="data row12 col40" >0.085851</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col41" class="data row12 col41" >0.074531</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col42" class="data row12 col42" >0.062837</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col43" class="data row12 col43" >0.080312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col44" class="data row12 col44" >0.085363</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col45" class="data row12 col45" >0.071281</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col46" class="data row12 col46" >0.044468</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col47" class="data row12 col47" >-0.162623</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col48" class="data row12 col48" >-0.065403</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col49" class="data row12 col49" >-0.081937</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col50" class="data row12 col50" >-0.034572</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col51" class="data row12 col51" >-0.185442</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row12_col52" class="data row12 col52" >-0.158286</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row13" class="row_heading level0 row13" >1 Year Change Rating</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col0" class="data row13 col0" >0.057362</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col1" class="data row13 col1" >-0.151949</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col2" class="data row13 col2" >0.094137</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col3" class="data row13 col3" >-0.168969</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col4" class="data row13 col4" >0.017546</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col5" class="data row13 col5" >0.045687</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col6" class="data row13 col6" >-0.072645</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col7" class="data row13 col7" >0.138886</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col8" class="data row13 col8" >0.175777</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col9" class="data row13 col9" >-0.131246</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col10" class="data row13 col10" >0.258598</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col11" class="data row13 col11" >-0.247371</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col12" class="data row13 col12" >0.776446</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col13" class="data row13 col13" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col14" class="data row13 col14" >-0.046730</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col15" class="data row13 col15" >-0.051801</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col16" class="data row13 col16" >0.028682</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col17" class="data row13 col17" >-0.218735</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col18" class="data row13 col18" >-0.151556</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col19" class="data row13 col19" >0.139989</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col20" class="data row13 col20" >-0.044020</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col21" class="data row13 col21" >-0.142423</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col22" class="data row13 col22" >0.055000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col23" class="data row13 col23" >0.053047</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col24" class="data row13 col24" >-0.220599</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col25" class="data row13 col25" >-0.091278</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col26" class="data row13 col26" >-0.198418</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col27" class="data row13 col27" >-0.001272</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col28" class="data row13 col28" >-0.016679</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col29" class="data row13 col29" >0.052749</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col30" class="data row13 col30" >-0.012541</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col31" class="data row13 col31" >-0.024448</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col32" class="data row13 col32" >-0.062053</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col33" class="data row13 col33" >-0.012594</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col34" class="data row13 col34" >0.062919</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col35" class="data row13 col35" >0.059136</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col36" class="data row13 col36" >0.057575</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col37" class="data row13 col37" >0.057092</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col38" class="data row13 col38" >0.047475</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col39" class="data row13 col39" >0.072290</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col40" class="data row13 col40" >0.049093</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col41" class="data row13 col41" >0.037171</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col42" class="data row13 col42" >0.069732</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col43" class="data row13 col43" >0.053047</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col44" class="data row13 col44" >0.071153</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col45" class="data row13 col45" >0.060996</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col46" class="data row13 col46" >0.096833</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col47" class="data row13 col47" >-0.129915</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col48" class="data row13 col48" >-0.015386</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col49" class="data row13 col49" >-0.094119</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col50" class="data row13 col50" >0.054745</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col51" class="data row13 col51" >-0.230776</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row13_col52" class="data row13 col52" >-0.123604</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row14" class="row_heading level0 row14" >Matches Total</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col0" class="data row14 col0" >0.354077</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col1" class="data row14 col1" >0.165593</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col2" class="data row14 col2" >0.012887</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col3" class="data row14 col3" >0.120250</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col4" class="data row14 col4" >0.126201</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col5" class="data row14 col5" >-0.030690</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col6" class="data row14 col6" >0.150793</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col7" class="data row14 col7" >-0.158488</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col8" class="data row14 col8" >-0.234114</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col9" class="data row14 col9" >0.264492</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col10" class="data row14 col10" >-0.454551</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col11" class="data row14 col11" >0.370581</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col12" class="data row14 col12" >0.006777</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col13" class="data row14 col13" >-0.046730</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col14" class="data row14 col14" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col15" class="data row14 col15" >0.968553</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col16" class="data row14 col16" >0.959655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col17" class="data row14 col17" >0.736791</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col18" class="data row14 col18" >0.917907</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col19" class="data row14 col19" >0.723876</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col20" class="data row14 col20" >0.952683</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col21" class="data row14 col21" >0.946703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col22" class="data row14 col22" >0.863563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col23" class="data row14 col23" >0.354727</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col24" class="data row14 col24" >0.395014</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col25" class="data row14 col25" >0.164892</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col26" class="data row14 col26" >0.648047</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col27" class="data row14 col27" >0.155725</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col28" class="data row14 col28" >0.150819</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col29" class="data row14 col29" >-0.140144</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col30" class="data row14 col30" >0.129272</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col31" class="data row14 col31" >-0.117400</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col32" class="data row14 col32" >-0.025592</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col33" class="data row14 col33" >0.001094</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col34" class="data row14 col34" >-0.000855</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col35" class="data row14 col35" >-0.008503</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col36" class="data row14 col36" >-0.000592</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col37" class="data row14 col37" >0.021061</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col38" class="data row14 col38" >-0.042525</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col39" class="data row14 col39" >0.045894</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col40" class="data row14 col40" >0.035327</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col41" class="data row14 col41" >-0.064585</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col42" class="data row14 col42" >0.004520</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col43" class="data row14 col43" >0.354727</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col44" class="data row14 col44" >-0.028563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col45" class="data row14 col45" >-0.033637</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col46" class="data row14 col46" >-0.042417</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col47" class="data row14 col47" >0.284766</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col48" class="data row14 col48" >0.109368</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col49" class="data row14 col49" >0.397826</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col50" class="data row14 col50" >0.079791</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col51" class="data row14 col51" >0.324838</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row14_col52" class="data row14 col52" >0.283473</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row15" class="row_heading level0 row15" >Matches Home</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col0" class="data row15 col0" >0.328604</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col1" class="data row15 col1" >0.176155</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col2" class="data row15 col2" >-0.027698</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col3" class="data row15 col3" >0.150830</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col4" class="data row15 col4" >0.163511</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col5" class="data row15 col5" >-0.013170</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col6" class="data row15 col6" >0.134729</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col7" class="data row15 col7" >-0.234039</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col8" class="data row15 col8" >-0.278563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col9" class="data row15 col9" >0.324167</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col10" class="data row15 col10" >-0.447504</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col11" class="data row15 col11" >0.357545</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col12" class="data row15 col12" >-0.011639</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col13" class="data row15 col13" >-0.051801</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col14" class="data row15 col14" >0.968553</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col15" class="data row15 col15" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col16" class="data row15 col16" >0.888787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col17" class="data row15 col17" >0.652686</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col18" class="data row15 col18" >0.866934</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col19" class="data row15 col19" >0.748781</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col20" class="data row15 col20" >0.901129</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col21" class="data row15 col21" >0.906986</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col22" class="data row15 col22" >0.880955</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col23" class="data row15 col23" >0.328692</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col24" class="data row15 col24" >0.354738</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col25" class="data row15 col25" >0.076391</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col26" class="data row15 col26" >0.739517</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col27" class="data row15 col27" >0.156856</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col28" class="data row15 col28" >0.147492</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col29" class="data row15 col29" >-0.129887</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col30" class="data row15 col30" >0.129858</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col31" class="data row15 col31" >-0.114109</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col32" class="data row15 col32" >-0.038391</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col33" class="data row15 col33" >-0.014255</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col34" class="data row15 col34" >0.022813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col35" class="data row15 col35" >0.012371</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col36" class="data row15 col36" >0.021453</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col37" class="data row15 col37" >0.045448</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col38" class="data row15 col38" >-0.015824</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col39" class="data row15 col39" >0.057220</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col40" class="data row15 col40" >0.055798</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col41" class="data row15 col41" >-0.036670</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col42" class="data row15 col42" >0.025994</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col43" class="data row15 col43" >0.328692</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col44" class="data row15 col44" >0.003651</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col45" class="data row15 col45" >-0.004451</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col46" class="data row15 col46" >-0.050003</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col47" class="data row15 col47" >0.320610</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col48" class="data row15 col48" >0.125416</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col49" class="data row15 col49" >0.352397</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col50" class="data row15 col50" >0.093458</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col51" class="data row15 col51" >0.389694</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row15_col52" class="data row15 col52" >0.318980</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row16" class="row_heading level0 row16" >Matches Away</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col0" class="data row16 col0" >0.332956</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col1" class="data row16 col1" >0.096714</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col2" class="data row16 col2" >0.097024</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col3" class="data row16 col3" >0.020715</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col4" class="data row16 col4" >0.096965</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col5" class="data row16 col5" >-0.036611</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col6" class="data row16 col6" >0.143583</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col7" class="data row16 col7" >0.041219</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col8" class="data row16 col8" >-0.065865</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col9" class="data row16 col9" >0.073659</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col10" class="data row16 col10" >-0.323160</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col11" class="data row16 col11" >0.233883</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col12" class="data row16 col12" >0.089184</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col13" class="data row16 col13" >0.028682</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col14" class="data row16 col14" >0.959655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col15" class="data row16 col15" >0.888787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col16" class="data row16 col16" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col17" class="data row16 col17" >0.602975</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col18" class="data row16 col18" >0.824784</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col19" class="data row16 col19" >0.791211</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col20" class="data row16 col20" >0.902485</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col21" class="data row16 col21" >0.885194</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col22" class="data row16 col22" >0.890426</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col23" class="data row16 col23" >0.333069</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col24" class="data row16 col24" >0.251844</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col25" class="data row16 col25" >0.096699</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col26" class="data row16 col26" >0.556705</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col27" class="data row16 col27" >0.134516</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col28" class="data row16 col28" >0.144074</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col29" class="data row16 col29" >-0.127703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col30" class="data row16 col30" >0.120924</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col31" class="data row16 col31" >-0.115337</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col32" class="data row16 col32" >-0.021799</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col33" class="data row16 col33" >0.015152</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col34" class="data row16 col34" >-0.037520</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col35" class="data row16 col35" >-0.040298</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col36" class="data row16 col36" >-0.035337</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col37" class="data row16 col37" >-0.016639</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col38" class="data row16 col38" >-0.079616</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col39" class="data row16 col39" >0.026454</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col40" class="data row16 col40" >-0.004698</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col41" class="data row16 col41" >-0.098553</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col42" class="data row16 col42" >-0.019292</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col43" class="data row16 col43" >0.333069</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col44" class="data row16 col44" >-0.047947</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col45" class="data row16 col45" >-0.044984</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col46" class="data row16 col46" >-0.059197</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col47" class="data row16 col47" >0.139453</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col48" class="data row16 col48" >0.092012</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col49" class="data row16 col49" >0.412580</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col50" class="data row16 col50" >0.032095</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col51" class="data row16 col51" >0.269562</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row16_col52" class="data row16 col52" >0.141820</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row17" class="row_heading level0 row17" >Matches Neutral</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col0" class="data row17 col0" >0.319800</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col1" class="data row17 col1" >0.242782</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col2" class="data row17 col2" >-0.104521</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col3" class="data row17 col3" >0.244587</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col4" class="data row17 col4" >0.044117</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col5" class="data row17 col5" >-0.049165</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col6" class="data row17 col6" >0.144534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col7" class="data row17 col7" >-0.424280</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col8" class="data row17 col8" >-0.465210</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col9" class="data row17 col9" >0.501207</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col10" class="data row17 col10" >-0.626145</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col11" class="data row17 col11" >0.612355</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col12" class="data row17 col12" >-0.171935</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col13" class="data row17 col13" >-0.218735</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col14" class="data row17 col14" >0.736791</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col15" class="data row17 col15" >0.652686</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col16" class="data row17 col16" >0.602975</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col17" class="data row17 col17" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col18" class="data row17 col18" >0.892654</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col19" class="data row17 col19" >0.134094</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col20" class="data row17 col20" >0.794703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col21" class="data row17 col21" >0.789567</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col22" class="data row17 col22" >0.341728</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col23" class="data row17 col23" >0.323200</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col24" class="data row17 col24" >0.719473</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col25" class="data row17 col25" >0.523955</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col26" class="data row17 col26" >0.344447</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col27" class="data row17 col27" >0.139009</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col28" class="data row17 col28" >0.108984</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col29" class="data row17 col29" >-0.138313</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col30" class="data row17 col30" >0.090876</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col31" class="data row17 col31" >-0.078012</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col32" class="data row17 col32" >0.011564</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col33" class="data row17 col33" >0.004759</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col34" class="data row17 col34" >0.034400</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col35" class="data row17 col35" >0.024683</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col36" class="data row17 col36" >0.033787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col37" class="data row17 col37" >0.047029</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col38" class="data row17 col38" >0.004691</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col39" class="data row17 col39" >0.046580</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col40" class="data row17 col40" >0.072052</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col41" class="data row17 col41" >-0.019172</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col42" class="data row17 col42" >0.008014</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col43" class="data row17 col43" >0.323200</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col44" class="data row17 col44" >-0.052003</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col45" class="data row17 col45" >-0.068410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col46" class="data row17 col46" >0.044631</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col47" class="data row17 col47" >0.453306</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col48" class="data row17 col48" >0.061771</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col49" class="data row17 col49" >0.300263</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col50" class="data row17 col50" >0.136115</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col51" class="data row17 col51" >0.145676</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row17_col52" class="data row17 col52" >0.443470</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row18" class="row_heading level0 row18" >Matches Wins</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col0" class="data row18 col0" >0.305614</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col1" class="data row18 col1" >0.227829</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col2" class="data row18 col2" >-0.035578</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col3" class="data row18 col3" >0.194939</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col4" class="data row18 col4" >0.072756</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col5" class="data row18 col5" >-0.084803</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col6" class="data row18 col6" >0.174403</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col7" class="data row18 col7" >-0.352563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col8" class="data row18 col8" >-0.397074</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col9" class="data row18 col9" >0.444523</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col10" class="data row18 col10" >-0.653132</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col11" class="data row18 col11" >0.619111</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col12" class="data row18 col12" >-0.081205</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col13" class="data row18 col13" >-0.151556</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col14" class="data row18 col14" >0.917907</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col15" class="data row18 col15" >0.866934</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col16" class="data row18 col16" >0.824784</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col17" class="data row18 col17" >0.892654</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col18" class="data row18 col18" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col19" class="data row18 col19" >0.399049</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col20" class="data row18 col20" >0.897646</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col21" class="data row18 col21" >0.974527</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col22" class="data row18 col22" >0.616659</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col23" class="data row18 col23" >0.308090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col24" class="data row18 col24" >0.585765</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col25" class="data row18 col25" >0.343138</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col26" class="data row18 col26" >0.523792</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col27" class="data row18 col27" >0.133747</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col28" class="data row18 col28" >0.128103</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col29" class="data row18 col29" >-0.135972</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col30" class="data row18 col30" >0.116113</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col31" class="data row18 col31" >-0.104580</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col32" class="data row18 col32" >0.010434</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col33" class="data row18 col33" >0.012347</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col34" class="data row18 col34" >0.009574</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col35" class="data row18 col35" >0.006372</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col36" class="data row18 col36" >0.002986</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col37" class="data row18 col37" >0.032342</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col38" class="data row18 col38" >-0.026062</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col39" class="data row18 col39" >0.039708</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col40" class="data row18 col40" >0.049833</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col41" class="data row18 col41" >-0.049622</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col42" class="data row18 col42" >0.003009</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col43" class="data row18 col43" >0.308090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col44" class="data row18 col44" >-0.047073</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col45" class="data row18 col45" >-0.052710</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col46" class="data row18 col46" >-0.035503</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col47" class="data row18 col47" >0.411062</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col48" class="data row18 col48" >0.104150</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col49" class="data row18 col49" >0.355594</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col50" class="data row18 col50" >0.095639</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col51" class="data row18 col51" >0.272361</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row18_col52" class="data row18 col52" >0.405927</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row19" class="row_heading level0 row19" >Matches Losses</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col0" class="data row19 col0" >0.257118</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col1" class="data row19 col1" >-0.013347</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col2" class="data row19 col2" >0.124857</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col3" class="data row19 col3" >-0.079348</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col4" class="data row19 col4" >0.159463</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col5" class="data row19 col5" >0.069676</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col6" class="data row19 col6" >0.065934</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col7" class="data row19 col7" >0.214076</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col8" class="data row19 col8" >0.129254</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col9" class="data row19 col9" >-0.129265</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col10" class="data row19 col10" >0.087305</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col11" class="data row19 col11" >-0.220181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col12" class="data row19 col12" >0.164537</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col13" class="data row19 col13" >0.139989</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col14" class="data row19 col14" >0.723876</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col15" class="data row19 col15" >0.748781</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col16" class="data row19 col16" >0.791211</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col17" class="data row19 col17" >0.134094</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col18" class="data row19 col18" >0.399049</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col19" class="data row19 col19" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col20" class="data row19 col20" >0.600098</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col21" class="data row19 col21" >0.526604</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col22" class="data row19 col22" >0.954622</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col23" class="data row19 col23" >0.254382</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col24" class="data row19 col24" >-0.098088</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col25" class="data row19 col25" >-0.240138</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col26" class="data row19 col26" >0.621715</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col27" class="data row19 col27" >0.116199</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col28" class="data row19 col28" >0.120736</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col29" class="data row19 col29" >-0.081410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col30" class="data row19 col30" >0.096816</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col31" class="data row19 col31" >-0.084805</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col32" class="data row19 col32" >-0.069794</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col33" class="data row19 col33" >-0.018450</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col34" class="data row19 col34" >-0.022495</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col35" class="data row19 col35" >-0.031231</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col36" class="data row19 col36" >-0.014365</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col37" class="data row19 col37" >-0.008359</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col38" class="data row19 col38" >-0.053979</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col39" class="data row19 col39" >0.029142</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col40" class="data row19 col40" >-0.007565</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col41" class="data row19 col41" >-0.062524</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col42" class="data row19 col42" >0.003119</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col43" class="data row19 col43" >0.254382</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col44" class="data row19 col44" >0.023464</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col45" class="data row19 col45" >0.019552</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col46" class="data row19 col46" >-0.052780</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col47" class="data row19 col47" >-0.037494</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col48" class="data row19 col48" >0.071775</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col49" class="data row19 col49" >0.310269</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col50" class="data row19 col50" >0.013120</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col51" class="data row19 col51" >0.299335</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row19_col52" class="data row19 col52" >-0.031085</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row20" class="row_heading level0 row20" >Matches Draws</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col0" class="data row20 col0" >0.390689</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col1" class="data row20 col1" >0.160638</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col2" class="data row20 col2" >-0.046584</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col3" class="data row20 col3" >0.149343</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col4" class="data row20 col4" >0.121853</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col5" class="data row20 col5" >-0.031276</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col6" class="data row20 col6" >0.109634</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col7" class="data row20 col7" >-0.145714</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col8" class="data row20 col8" >-0.235089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col9" class="data row20 col9" >0.247548</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col10" class="data row20 col10" >-0.500735</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col11" class="data row20 col11" >0.426214</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col12" class="data row20 col12" >-0.028031</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col13" class="data row20 col13" >-0.044020</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col14" class="data row20 col14" >0.952683</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col15" class="data row20 col15" >0.901129</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col16" class="data row20 col16" >0.902485</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col17" class="data row20 col17" >0.794703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col18" class="data row20 col18" >0.897646</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col19" class="data row20 col19" >0.600098</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col20" class="data row20 col20" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col21" class="data row20 col21" >0.883557</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col22" class="data row20 col22" >0.738945</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col23" class="data row20 col23" >0.391653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col24" class="data row20 col24" >0.422964</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col25" class="data row20 col25" >0.249172</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col26" class="data row20 col26" >0.549031</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col27" class="data row20 col27" >0.168206</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col28" class="data row20 col28" >0.152492</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col29" class="data row20 col29" >-0.148126</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col30" class="data row20 col30" >0.124639</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col31" class="data row20 col31" >-0.121149</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col32" class="data row20 col32" >-0.029824</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col33" class="data row20 col33" >0.002925</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col34" class="data row20 col34" >0.008491</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col35" class="data row20 col35" >-0.003936</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col36" class="data row20 col36" >0.014038</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col37" class="data row20 col37" >0.024931</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col38" class="data row20 col38" >-0.036258</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col39" class="data row20 col39" >0.057748</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col40" class="data row20 col40" >0.042912</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col41" class="data row20 col41" >-0.061015</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col42" class="data row20 col42" >0.007796</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col43" class="data row20 col43" >0.391653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col44" class="data row20 col44" >-0.046126</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col45" class="data row20 col45" >-0.047769</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col46" class="data row20 col46" >-0.011179</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col47" class="data row20 col47" >0.278027</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col48" class="data row20 col48" >0.106606</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col49" class="data row20 col49" >0.366740</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col50" class="data row20 col50" >0.091447</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col51" class="data row20 col51" >0.269195</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row20_col52" class="data row20 col52" >0.275001</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row21" class="row_heading level0 row21" >Goals For</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col0" class="data row21 col0" >0.262763</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col1" class="data row21 col1" >0.215455</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col2" class="data row21 col2" >0.016586</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col3" class="data row21 col3" >0.156559</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col4" class="data row21 col4" >0.098592</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col5" class="data row21 col5" >-0.097014</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col6" class="data row21 col6" >0.196087</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col7" class="data row21 col7" >-0.278837</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col8" class="data row21 col8" >-0.320707</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col9" class="data row21 col9" >0.366552</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col10" class="data row21 col10" >-0.593433</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col11" class="data row21 col11" >0.548189</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col12" class="data row21 col12" >-0.048268</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col13" class="data row21 col13" >-0.142423</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col14" class="data row21 col14" >0.946703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col15" class="data row21 col15" >0.906986</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col16" class="data row21 col16" >0.885194</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col17" class="data row21 col17" >0.789567</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col18" class="data row21 col18" >0.974527</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col19" class="data row21 col19" >0.526604</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col20" class="data row21 col20" >0.883557</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col21" class="data row21 col21" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col22" class="data row21 col22" >0.731666</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col23" class="data row21 col23" >0.264050</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col24" class="data row21 col24" >0.467749</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col25" class="data row21 col25" >0.213723</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col26" class="data row21 col26" >0.582041</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col27" class="data row21 col27" >0.106138</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col28" class="data row21 col28" >0.119372</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col29" class="data row21 col29" >-0.114584</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col30" class="data row21 col30" >0.114264</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col31" class="data row21 col31" >-0.104916</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col32" class="data row21 col32" >-0.000017</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col33" class="data row21 col33" >0.009773</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col34" class="data row21 col34" >-0.018435</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col35" class="data row21 col35" >-0.019337</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col36" class="data row21 col36" >-0.024773</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col37" class="data row21 col37" >0.011045</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col38" class="data row21 col38" >-0.050401</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col39" class="data row21 col39" >0.019281</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col40" class="data row21 col40" >0.017598</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col41" class="data row21 col41" >-0.070229</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col42" class="data row21 col42" >-0.012420</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col43" class="data row21 col43" >0.264050</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col44" class="data row21 col44" >-0.047898</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col45" class="data row21 col45" >-0.045886</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col46" class="data row21 col46" >-0.078898</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col47" class="data row21 col47" >0.340631</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col48" class="data row21 col48" >0.130170</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col49" class="data row21 col49" >0.387284</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col50" class="data row21 col50" >0.054015</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col51" class="data row21 col51" >0.326223</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row21_col52" class="data row21 col52" >0.338771</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row22" class="row_heading level0 row22" >Goals Against</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col0" class="data row22 col0" >0.240312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col1" class="data row22 col1" >0.074271</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col2" class="data row22 col2" >0.112082</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col3" class="data row22 col3" >-0.004881</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col4" class="data row22 col4" >0.159523</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col5" class="data row22 col5" >0.022002</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col6" class="data row22 col6" >0.133568</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col7" class="data row22 col7" >0.051028</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col8" class="data row22 col8" >-0.012519</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col9" class="data row22 col9" >0.034834</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col10" class="data row22 col10" >-0.133458</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col11" class="data row22 col11" >0.007131</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col12" class="data row22 col12" >0.106311</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col13" class="data row22 col13" >0.055000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col14" class="data row22 col14" >0.863563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col15" class="data row22 col15" >0.880955</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col16" class="data row22 col16" >0.890426</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col17" class="data row22 col17" >0.341728</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col18" class="data row22 col18" >0.616659</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col19" class="data row22 col19" >0.954622</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col20" class="data row22 col20" >0.738945</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col21" class="data row22 col21" >0.731666</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col22" class="data row22 col22" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col23" class="data row22 col23" >0.238215</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col24" class="data row22 col24" >0.097556</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col25" class="data row22 col25" >-0.105693</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col26" class="data row22 col26" >0.669181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col27" class="data row22 col27" >0.109863</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col28" class="data row22 col28" >0.120658</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col29" class="data row22 col29" >-0.085356</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col30" class="data row22 col30" >0.107374</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col31" class="data row22 col31" >-0.095501</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col32" class="data row22 col32" >-0.075344</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col33" class="data row22 col33" >-0.018421</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col34" class="data row22 col34" >-0.039320</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col35" class="data row22 col35" >-0.047426</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col36" class="data row22 col36" >-0.035627</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col37" class="data row22 col37" >-0.006246</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col38" class="data row22 col38" >-0.066209</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col39" class="data row22 col39" >0.005815</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col40" class="data row22 col40" >-0.015507</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col41" class="data row22 col41" >-0.080067</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col42" class="data row22 col42" >-0.020504</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col43" class="data row22 col43" >0.238215</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col44" class="data row22 col44" >0.002342</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col45" class="data row22 col45" >0.002645</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col46" class="data row22 col46" >-0.092184</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col47" class="data row22 col47" >0.082882</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col48" class="data row22 col48" >0.101014</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col49" class="data row22 col49" >0.374152</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col50" class="data row22 col50" >0.039089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col51" class="data row22 col51" >0.358090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row22_col52" class="data row22 col52" >0.087727</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row23" class="row_heading level0 row23" >Data Year</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col0" class="data row23 col0" >0.999181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col1" class="data row23 col1" >-0.027040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col2" class="data row23 col2" >-0.055270</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col3" class="data row23 col3" >0.009779</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col4" class="data row23 col4" >0.133515</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col5" class="data row23 col5" >0.119534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col6" class="data row23 col6" >-0.057600</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col7" class="data row23 col7" >0.205147</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col8" class="data row23 col8" >0.118922</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col9" class="data row23 col9" >-0.061889</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col10" class="data row23 col10" >0.049964</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col11" class="data row23 col11" >0.027931</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col12" class="data row23 col12" >0.080312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col13" class="data row23 col13" >0.053047</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col14" class="data row23 col14" >0.354727</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col15" class="data row23 col15" >0.328692</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col16" class="data row23 col16" >0.333069</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col17" class="data row23 col17" >0.323200</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col18" class="data row23 col18" >0.308090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col19" class="data row23 col19" >0.254382</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col20" class="data row23 col20" >0.391653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col21" class="data row23 col21" >0.264050</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col22" class="data row23 col22" >0.238215</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col23" class="data row23 col23" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col24" class="data row23 col24" >0.097259</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col25" class="data row23 col25" >-0.007355</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col26" class="data row23 col26" >0.304464</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col27" class="data row23 col27" >0.301787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col28" class="data row23 col28" >0.258139</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col29" class="data row23 col29" >-0.188787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col30" class="data row23 col30" >0.113885</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col31" class="data row23 col31" >-0.031570</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col32" class="data row23 col32" >0.069974</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col33" class="data row23 col33" >0.110120</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col34" class="data row23 col34" >0.303638</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col35" class="data row23 col35" >0.299721</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col36" class="data row23 col36" >0.265516</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col37" class="data row23 col37" >0.268089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col38" class="data row23 col38" >0.242165</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col39" class="data row23 col39" >0.266412</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col40" class="data row23 col40" >0.334802</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col41" class="data row23 col41" >0.189720</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col42" class="data row23 col42" >0.215572</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col43" class="data row23 col43" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col44" class="data row23 col44" >0.157465</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col45" class="data row23 col45" >0.069642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col46" class="data row23 col46" >0.342408</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col47" class="data row23 col47" >0.083666</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col48" class="data row23 col48" >0.022620</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col49" class="data row23 col49" >0.006655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col50" class="data row23 col50" >0.088625</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col51" class="data row23 col51" >-0.090005</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row23_col52" class="data row23 col52" >0.091841</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row24" class="row_heading level0 row24" >GDP (PPP)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col0" class="data row24 col0" >0.092892</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col1" class="data row24 col1" >0.224033</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col2" class="data row24 col2" >-0.116405</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col3" class="data row24 col3" >0.236739</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col4" class="data row24 col4" >-0.002807</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col5" class="data row24 col5" >0.018187</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col6" class="data row24 col6" >0.120995</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col7" class="data row24 col7" >-0.419915</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col8" class="data row24 col8" >-0.383505</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col9" class="data row24 col9" >0.453588</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col10" class="data row24 col10" >-0.411368</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col11" class="data row24 col11" >0.395999</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col12" class="data row24 col12" >-0.176918</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col13" class="data row24 col13" >-0.220599</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col14" class="data row24 col14" >0.395014</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col15" class="data row24 col15" >0.354738</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col16" class="data row24 col16" >0.251844</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col17" class="data row24 col17" >0.719473</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col18" class="data row24 col18" >0.585765</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col19" class="data row24 col19" >-0.098088</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col20" class="data row24 col20" >0.422964</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col21" class="data row24 col21" >0.467749</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col22" class="data row24 col22" >0.097556</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col23" class="data row24 col23" >0.097259</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col24" class="data row24 col24" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col25" class="data row24 col25" >0.869955</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col26" class="data row24 col26" >0.179482</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col27" class="data row24 col27" >0.103901</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col28" class="data row24 col28" >0.037982</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col29" class="data row24 col29" >-0.099135</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col30" class="data row24 col30" >0.024302</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col31" class="data row24 col31" >-0.005650</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col32" class="data row24 col32" >0.037178</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col33" class="data row24 col33" >0.058852</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col34" class="data row24 col34" >-0.001154</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col35" class="data row24 col35" >-0.018675</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col36" class="data row24 col36" >0.007816</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col37" class="data row24 col37" >0.025435</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col38" class="data row24 col38" >-0.005097</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col39" class="data row24 col39" >-0.033187</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col40" class="data row24 col40" >0.061585</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col41" class="data row24 col41" >-0.024244</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col42" class="data row24 col42" >-0.048828</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col43" class="data row24 col43" >0.097259</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col44" class="data row24 col44" >-0.086181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col45" class="data row24 col45" >-0.074441</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col46" class="data row24 col46" >-0.035020</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col47" class="data row24 col47" >0.392577</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col48" class="data row24 col48" >-0.013153</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col49" class="data row24 col49" >0.126132</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col50" class="data row24 col50" >0.250226</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col51" class="data row24 col51" >0.130241</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row24_col52" class="data row24 col52" >0.378288</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row25" class="row_heading level0 row25" >Population</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col0" class="data row25 col0" >-0.010312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col1" class="data row25 col1" >0.139519</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col2" class="data row25 col2" >-0.043534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col3" class="data row25 col3" >0.131410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col4" class="data row25 col4" >-0.053640</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col5" class="data row25 col5" >0.033152</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col6" class="data row25 col6" >0.093313</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col7" class="data row25 col7" >-0.229838</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col8" class="data row25 col8" >-0.223325</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col9" class="data row25 col9" >0.253114</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col10" class="data row25 col10" >-0.251766</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col11" class="data row25 col11" >0.214778</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col12" class="data row25 col12" >-0.101992</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col13" class="data row25 col13" >-0.091278</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col14" class="data row25 col14" >0.164892</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col15" class="data row25 col15" >0.076391</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col16" class="data row25 col16" >0.096699</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col17" class="data row25 col17" >0.523955</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col18" class="data row25 col18" >0.343138</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col19" class="data row25 col19" >-0.240138</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col20" class="data row25 col20" >0.249172</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col21" class="data row25 col21" >0.213723</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col22" class="data row25 col22" >-0.105693</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col23" class="data row25 col23" >-0.007355</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col24" class="data row25 col24" >0.869955</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col25" class="data row25 col25" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col26" class="data row25 col26" >-0.146692</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col27" class="data row25 col27" >0.084135</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col28" class="data row25 col28" >0.014213</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col29" class="data row25 col29" >-0.085819</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col30" class="data row25 col30" >0.018649</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col31" class="data row25 col31" >-0.011193</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col32" class="data row25 col32" >0.038475</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col33" class="data row25 col33" >0.062798</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col34" class="data row25 col34" >-0.056653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col35" class="data row25 col35" >-0.059582</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col36" class="data row25 col36" >-0.045565</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col37" class="data row25 col37" >-0.050420</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col38" class="data row25 col38" >-0.058976</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col39" class="data row25 col39" >-0.062553</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col40" class="data row25 col40" >-0.005121</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col41" class="data row25 col41" >-0.068876</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col42" class="data row25 col42" >-0.084938</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col43" class="data row25 col43" >-0.007355</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col44" class="data row25 col44" >-0.138649</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col45" class="data row25 col45" >-0.132361</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col46" class="data row25 col46" >-0.018565</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col47" class="data row25 col47" >0.239756</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col48" class="data row25 col48" >-0.058799</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col49" class="data row25 col49" >0.060010</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col50" class="data row25 col50" >0.261225</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col51" class="data row25 col51" >-0.053884</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row25_col52" class="data row25 col52" >0.225653</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row26" class="row_heading level0 row26" >GDP (PPP) Per Capita</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col0" class="data row26 col0" >0.304851</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col1" class="data row26 col1" >0.140413</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col2" class="data row26 col2" >-0.132443</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col3" class="data row26 col3" >0.181289</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col4" class="data row26 col4" >0.227658</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col5" class="data row26 col5" >0.004791</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col6" class="data row26 col6" >0.038937</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col7" class="data row26 col7" >-0.203206</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col8" class="data row26 col8" >-0.205782</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col9" class="data row26 col9" >0.245205</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col10" class="data row26 col10" >-0.239768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col11" class="data row26 col11" >0.197321</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col12" class="data row26 col12" >-0.150388</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col13" class="data row26 col13" >-0.198418</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col14" class="data row26 col14" >0.648047</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col15" class="data row26 col15" >0.739517</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col16" class="data row26 col16" >0.556705</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col17" class="data row26 col17" >0.344447</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col18" class="data row26 col18" >0.523792</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col19" class="data row26 col19" >0.621715</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col20" class="data row26 col20" >0.549031</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col21" class="data row26 col21" >0.582041</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col22" class="data row26 col22" >0.669181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col23" class="data row26 col23" >0.304464</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col24" class="data row26 col24" >0.179482</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col25" class="data row26 col25" >-0.146692</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col26" class="data row26 col26" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col27" class="data row26 col27" >0.116768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col28" class="data row26 col28" >0.087510</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col29" class="data row26 col29" >-0.072598</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col30" class="data row26 col30" >0.027137</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col31" class="data row26 col31" >-0.014396</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col32" class="data row26 col32" >0.004722</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col33" class="data row26 col33" >0.034362</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col34" class="data row26 col34" >0.140865</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col35" class="data row26 col35" >0.101963</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col36" class="data row26 col36" >0.160975</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col37" class="data row26 col37" >0.127238</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col38" class="data row26 col38" >0.108937</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col39" class="data row26 col39" >0.115482</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col40" class="data row26 col40" >0.177444</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col41" class="data row26 col41" >0.097089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col42" class="data row26 col42" >0.119643</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col43" class="data row26 col43" >0.304464</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col44" class="data row26 col44" >0.087364</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col45" class="data row26 col45" >0.109446</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col46" class="data row26 col46" >-0.065385</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col47" class="data row26 col47" >0.225116</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col48" class="data row26 col48" >0.160454</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col49" class="data row26 col49" >0.122134</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col50" class="data row26 col50" >-0.024356</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col51" class="data row26 col51" >0.520000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row26_col52" class="data row26 col52" >0.221028</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row27" class="row_heading level0 row27" >Rank Local (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col0" class="data row27 col0" >0.305324</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col1" class="data row27 col1" >0.055158</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col2" class="data row27 col2" >-0.202140</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col3" class="data row27 col3" >0.154270</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col4" class="data row27 col4" >0.117830</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col5" class="data row27 col5" >-0.032095</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col6" class="data row27 col6" >-0.077813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col7" class="data row27 col7" >0.037470</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col8" class="data row27 col8" >0.002408</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col9" class="data row27 col9" >0.016649</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col10" class="data row27 col10" >0.033726</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col11" class="data row27 col11" >-0.024020</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col12" class="data row27 col12" >-0.013852</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col13" class="data row27 col13" >-0.001272</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col14" class="data row27 col14" >0.155725</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col15" class="data row27 col15" >0.156856</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col16" class="data row27 col16" >0.134516</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col17" class="data row27 col17" >0.139009</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col18" class="data row27 col18" >0.133747</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col19" class="data row27 col19" >0.116199</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col20" class="data row27 col20" >0.168206</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col21" class="data row27 col21" >0.106138</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col22" class="data row27 col22" >0.109863</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col23" class="data row27 col23" >0.301787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col24" class="data row27 col24" >0.103901</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col25" class="data row27 col25" >0.084135</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col26" class="data row27 col26" >0.116768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col27" class="data row27 col27" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col28" class="data row27 col28" >0.901972</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col29" class="data row27 col29" >-0.928570</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col30" class="data row27 col30" >0.644180</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col31" class="data row27 col31" >-0.576163</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col32" class="data row27 col32" >0.142182</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col33" class="data row27 col33" >0.004362</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col34" class="data row27 col34" >-0.166646</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col35" class="data row27 col35" >-0.251748</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col36" class="data row27 col36" >0.013667</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col37" class="data row27 col37" >-0.335932</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col38" class="data row27 col38" >-0.311078</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col39" class="data row27 col39" >0.129737</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col40" class="data row27 col40" >-0.153698</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col41" class="data row27 col41" >-0.248245</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col42" class="data row27 col42" >-0.027860</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col43" class="data row27 col43" >0.301787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col44" class="data row27 col44" >-0.314904</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col45" class="data row27 col45" >-0.173826</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col46" class="data row27 col46" >-0.222124</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col47" class="data row27 col47" >0.641795</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col48" class="data row27 col48" >0.104221</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col49" class="data row27 col49" >0.266725</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col50" class="data row27 col50" >0.255592</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col51" class="data row27 col51" >0.238120</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row27_col52" class="data row27 col52" >0.646986</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row28" class="row_heading level0 row28" >Rank Global (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col0" class="data row28 col0" >0.259107</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col1" class="data row28 col1" >0.101520</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col2" class="data row28 col2" >-0.143813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col3" class="data row28 col3" >0.157662</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col4" class="data row28 col4" >0.048050</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col5" class="data row28 col5" >-0.066137</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col6" class="data row28 col6" >-0.001655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col7" class="data row28 col7" >0.004748</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col8" class="data row28 col8" >-0.029842</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col9" class="data row28 col9" >0.029785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col10" class="data row28 col10" >0.003027</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col11" class="data row28 col11" >0.008650</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col12" class="data row28 col12" >-0.025816</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col13" class="data row28 col13" >-0.016679</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col14" class="data row28 col14" >0.150819</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col15" class="data row28 col15" >0.147492</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col16" class="data row28 col16" >0.144074</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col17" class="data row28 col17" >0.108984</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col18" class="data row28 col18" >0.128103</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col19" class="data row28 col19" >0.120736</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col20" class="data row28 col20" >0.152492</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col21" class="data row28 col21" >0.119372</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col22" class="data row28 col22" >0.120658</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col23" class="data row28 col23" >0.258139</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col24" class="data row28 col24" >0.037982</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col25" class="data row28 col25" >0.014213</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col26" class="data row28 col26" >0.087510</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col27" class="data row28 col27" >0.901972</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col28" class="data row28 col28" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col29" class="data row28 col29" >-0.932396</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col30" class="data row28 col30" >0.742071</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col31" class="data row28 col31" >-0.648367</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col32" class="data row28 col32" >0.261330</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col33" class="data row28 col33" >0.112993</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col34" class="data row28 col34" >-0.281024</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col35" class="data row28 col35" >-0.337383</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col36" class="data row28 col36" >-0.134734</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col37" class="data row28 col37" >-0.381886</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col38" class="data row28 col38" >-0.393041</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col39" class="data row28 col39" >0.011150</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col40" class="data row28 col40" >-0.275117</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col41" class="data row28 col41" >-0.338536</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col42" class="data row28 col42" >-0.133625</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col43" class="data row28 col43" >0.258139</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col44" class="data row28 col44" >-0.309352</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col45" class="data row28 col45" >-0.188979</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col46" class="data row28 col46" >-0.271742</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col47" class="data row28 col47" >0.653811</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col48" class="data row28 col48" >0.074988</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col49" class="data row28 col49" >0.401188</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col50" class="data row28 col50" >0.254559</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col51" class="data row28 col51" >0.246161</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row28_col52" class="data row28 col52" >0.683620</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row29" class="row_heading level0 row29" >Rating (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col0" class="data row29 col0" >-0.185116</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col1" class="data row29 col1" >-0.073758</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col2" class="data row29 col2" >0.173110</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col3" class="data row29 col3" >-0.152516</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col4" class="data row29 col4" >-0.073276</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col5" class="data row29 col5" >0.104324</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col6" class="data row29 col6" >0.043768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col7" class="data row29 col7" >0.006097</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col8" class="data row29 col8" >0.025640</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col9" class="data row29 col9" >-0.026171</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col10" class="data row29 col10" >-0.000073</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col11" class="data row29 col11" >-0.006319</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col12" class="data row29 col12" >0.045467</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col13" class="data row29 col13" >0.052749</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col14" class="data row29 col14" >-0.140144</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col15" class="data row29 col15" >-0.129887</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col16" class="data row29 col16" >-0.127703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col17" class="data row29 col17" >-0.138313</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col18" class="data row29 col18" >-0.135972</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col19" class="data row29 col19" >-0.081410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col20" class="data row29 col20" >-0.148126</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col21" class="data row29 col21" >-0.114584</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col22" class="data row29 col22" >-0.085356</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col23" class="data row29 col23" >-0.188787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col24" class="data row29 col24" >-0.099135</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col25" class="data row29 col25" >-0.085819</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col26" class="data row29 col26" >-0.072598</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col27" class="data row29 col27" >-0.928570</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col28" class="data row29 col28" >-0.932396</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col29" class="data row29 col29" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col30" class="data row29 col30" >-0.684242</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col31" class="data row29 col31" >0.627975</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col32" class="data row29 col32" >-0.247509</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col33" class="data row29 col33" >-0.048813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col34" class="data row29 col34" >0.291487</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col35" class="data row29 col35" >0.366607</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col36" class="data row29 col36" >0.117491</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col37" class="data row29 col37" >0.409459</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col38" class="data row29 col38" >0.423394</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col39" class="data row29 col39" >-0.025960</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col40" class="data row29 col40" >0.266706</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col41" class="data row29 col41" >0.361904</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col42" class="data row29 col42" >0.135760</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col43" class="data row29 col43" >-0.188787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col44" class="data row29 col44" >0.368225</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col45" class="data row29 col45" >0.204300</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col46" class="data row29 col46" >0.302832</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col47" class="data row29 col47" >-0.697075</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col48" class="data row29 col48" >-0.116478</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col49" class="data row29 col49" >-0.371154</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col50" class="data row29 col50" >-0.231379</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col51" class="data row29 col51" >-0.260276</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row29_col52" class="data row29 col52" >-0.704846</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row30" class="row_heading level0 row30" >Average Rank (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col0" class="data row30 col0" >0.114521</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col1" class="data row30 col1" >0.102114</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col2" class="data row30 col2" >-0.069452</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col3" class="data row30 col3" >0.116977</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col4" class="data row30 col4" >0.074083</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col5" class="data row30 col5" >-0.126111</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col6" class="data row30 col6" >0.044981</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col7" class="data row30 col7" >-0.033548</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col8" class="data row30 col8" >-0.063775</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col9" class="data row30 col9" >0.058254</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col10" class="data row30 col10" >-0.086594</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col11" class="data row30 col11" >0.067027</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col12" class="data row30 col12" >-0.087162</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col13" class="data row30 col13" >-0.012541</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col14" class="data row30 col14" >0.129272</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col15" class="data row30 col15" >0.129858</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col16" class="data row30 col16" >0.120924</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col17" class="data row30 col17" >0.090876</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col18" class="data row30 col18" >0.116113</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col19" class="data row30 col19" >0.096816</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col20" class="data row30 col20" >0.124639</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col21" class="data row30 col21" >0.114264</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col22" class="data row30 col22" >0.107374</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col23" class="data row30 col23" >0.113885</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col24" class="data row30 col24" >0.024302</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col25" class="data row30 col25" >0.018649</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col26" class="data row30 col26" >0.027137</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col27" class="data row30 col27" >0.644180</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col28" class="data row30 col28" >0.742071</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col29" class="data row30 col29" >-0.684242</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col30" class="data row30 col30" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col31" class="data row30 col31" >-0.952814</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col32" class="data row30 col32" >0.333018</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col33" class="data row30 col33" >0.169139</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col34" class="data row30 col34" >-0.485183</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col35" class="data row30 col35" >-0.471409</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col36" class="data row30 col36" >-0.364373</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col37" class="data row30 col37" >-0.616410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col38" class="data row30 col38" >-0.667653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col39" class="data row30 col39" >0.031327</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col40" class="data row30 col40" >-0.523472</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col41" class="data row30 col41" >-0.606311</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col42" class="data row30 col42" >-0.192507</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col43" class="data row30 col43" >0.113885</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col44" class="data row30 col44" >-0.375450</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col45" class="data row30 col45" >-0.233574</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col46" class="data row30 col46" >-0.308511</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col47" class="data row30 col47" >0.505907</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col48" class="data row30 col48" >0.130399</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col49" class="data row30 col49" >0.395498</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col50" class="data row30 col50" >0.378033</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col51" class="data row30 col51" >0.272017</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row30_col52" class="data row30 col52" >0.535740</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row31" class="row_heading level0 row31" >Average Rating (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col0" class="data row31 col0" >-0.032236</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col1" class="data row31 col1" >-0.074107</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col2" class="data row31 col2" >0.085403</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col3" class="data row31 col3" >-0.104258</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col4" class="data row31 col4" >-0.086812</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col5" class="data row31 col5" >0.113456</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col6" class="data row31 col6" >-0.010934</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col7" class="data row31 col7" >0.053100</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col8" class="data row31 col8" >0.077593</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col9" class="data row31 col9" >-0.071991</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col10" class="data row31 col10" >0.101664</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col11" class="data row31 col11" >-0.083622</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col12" class="data row31 col12" >0.049743</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col13" class="data row31 col13" >-0.024448</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col14" class="data row31 col14" >-0.117400</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col15" class="data row31 col15" >-0.114109</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col16" class="data row31 col16" >-0.115337</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col17" class="data row31 col17" >-0.078012</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col18" class="data row31 col18" >-0.104580</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col19" class="data row31 col19" >-0.084805</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col20" class="data row31 col20" >-0.121149</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col21" class="data row31 col21" >-0.104916</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col22" class="data row31 col22" >-0.095501</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col23" class="data row31 col23" >-0.031570</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col24" class="data row31 col24" >-0.005650</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col25" class="data row31 col25" >-0.011193</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col26" class="data row31 col26" >-0.014396</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col27" class="data row31 col27" >-0.576163</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col28" class="data row31 col28" >-0.648367</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col29" class="data row31 col29" >0.627975</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col30" class="data row31 col30" >-0.952814</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col31" class="data row31 col31" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col32" class="data row31 col32" >-0.281783</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col33" class="data row31 col33" >-0.150607</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col34" class="data row31 col34" >0.398326</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col35" class="data row31 col35" >0.382957</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col36" class="data row31 col36" >0.271876</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col37" class="data row31 col37" >0.593514</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col38" class="data row31 col38" >0.620569</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col39" class="data row31 col39" >-0.159140</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col40" class="data row31 col40" >0.451685</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col41" class="data row31 col41" >0.549227</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col42" class="data row31 col42" >0.064036</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col43" class="data row31 col43" >-0.031570</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col44" class="data row31 col44" >0.337257</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col45" class="data row31 col45" >0.171236</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col46" class="data row31 col46" >0.287634</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col47" class="data row31 col47" >-0.477593</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col48" class="data row31 col48" >-0.131785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col49" class="data row31 col49" >-0.289809</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col50" class="data row31 col50" >-0.301534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col51" class="data row31 col51" >-0.261846</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row31_col52" class="data row31 col52" >-0.500194</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row32" class="row_heading level0 row32" >1 Year Change Rank (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col0" class="data row32 col0" >0.064162</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col1" class="data row32 col1" >-0.024751</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col2" class="data row32 col2" >-0.051804</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col3" class="data row32 col3" >0.009623</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col4" class="data row32 col4" >0.028418</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col5" class="data row32 col5" >-0.118182</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col6" class="data row32 col6" >-0.053476</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col7" class="data row32 col7" >0.046169</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col8" class="data row32 col8" >0.021785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col9" class="data row32 col9" >-0.033684</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col10" class="data row32 col10" >0.007133</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col11" class="data row32 col11" >0.010165</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col12" class="data row32 col12" >-0.085319</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col13" class="data row32 col13" >-0.062053</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col14" class="data row32 col14" >-0.025592</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col15" class="data row32 col15" >-0.038391</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col16" class="data row32 col16" >-0.021799</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col17" class="data row32 col17" >0.011564</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col18" class="data row32 col18" >0.010434</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col19" class="data row32 col19" >-0.069794</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col20" class="data row32 col20" >-0.029824</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col21" class="data row32 col21" >-0.000017</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col22" class="data row32 col22" >-0.075344</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col23" class="data row32 col23" >0.069974</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col24" class="data row32 col24" >0.037178</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col25" class="data row32 col25" >0.038475</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col26" class="data row32 col26" >0.004722</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col27" class="data row32 col27" >0.142182</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col28" class="data row32 col28" >0.261330</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col29" class="data row32 col29" >-0.247509</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col30" class="data row32 col30" >0.333018</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col31" class="data row32 col31" >-0.281783</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col32" class="data row32 col32" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col33" class="data row32 col33" >0.801438</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col34" class="data row32 col34" >-0.091774</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col35" class="data row32 col35" >-0.091308</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col36" class="data row32 col36" >-0.017388</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col37" class="data row32 col37" >-0.253377</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col38" class="data row32 col38" >-0.183522</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col39" class="data row32 col39" >0.116508</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col40" class="data row32 col40" >-0.124652</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col41" class="data row32 col41" >-0.143851</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col42" class="data row32 col42" >0.034249</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col43" class="data row32 col43" >0.069974</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col44" class="data row32 col44" >-0.197899</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col45" class="data row32 col45" >-0.144375</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col46" class="data row32 col46" >-0.155642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col47" class="data row32 col47" >0.143726</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col48" class="data row32 col48" >0.092770</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col49" class="data row32 col49" >0.051139</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col50" class="data row32 col50" >0.023664</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col51" class="data row32 col51" >0.064875</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row32_col52" class="data row32 col52" >0.158798</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row33" class="row_heading level0 row33" >1 Year Change Rating (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col0" class="data row33 col0" >0.107218</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col1" class="data row33 col1" >-0.039889</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col2" class="data row33 col2" >0.025883</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col3" class="data row33 col3" >-0.045004</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col4" class="data row33 col4" >0.022321</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col5" class="data row33 col5" >-0.010978</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col6" class="data row33 col6" >-0.018344</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col7" class="data row33 col7" >0.060882</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col8" class="data row33 col8" >0.019338</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col9" class="data row33 col9" >-0.032625</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col10" class="data row33 col10" >0.013072</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col11" class="data row33 col11" >-0.004835</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col12" class="data row33 col12" >-0.028497</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col13" class="data row33 col13" >-0.012594</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col14" class="data row33 col14" >0.001094</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col15" class="data row33 col15" >-0.014255</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col16" class="data row33 col16" >0.015152</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col17" class="data row33 col17" >0.004759</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col18" class="data row33 col18" >0.012347</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col19" class="data row33 col19" >-0.018450</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col20" class="data row33 col20" >0.002925</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col21" class="data row33 col21" >0.009773</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col22" class="data row33 col22" >-0.018421</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col23" class="data row33 col23" >0.110120</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col24" class="data row33 col24" >0.058852</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col25" class="data row33 col25" >0.062798</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col26" class="data row33 col26" >0.034362</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col27" class="data row33 col27" >0.004362</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col28" class="data row33 col28" >0.112993</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col29" class="data row33 col29" >-0.048813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col30" class="data row33 col30" >0.169139</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col31" class="data row33 col31" >-0.150607</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col32" class="data row33 col32" >0.801438</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col33" class="data row33 col33" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col34" class="data row33 col34" >0.024148</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col35" class="data row33 col35" >0.028184</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col36" class="data row33 col36" >0.063252</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col37" class="data row33 col37" >-0.108225</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col38" class="data row33 col38" >-0.048222</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col39" class="data row33 col39" >0.141628</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col40" class="data row33 col40" >0.012395</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col41" class="data row33 col41" >-0.049286</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col42" class="data row33 col42" >0.090317</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col43" class="data row33 col43" >0.110120</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col44" class="data row33 col44" >-0.043768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col45" class="data row33 col45" >-0.001318</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col46" class="data row33 col46" >-0.108992</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col47" class="data row33 col47" >0.009710</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col48" class="data row33 col48" >0.022742</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col49" class="data row33 col49" >-0.011550</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col50" class="data row33 col50" >-0.010192</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col51" class="data row33 col51" >0.017151</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row33_col52" class="data row33 col52" >0.026619</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row34" class="row_heading level0 row34" >Matches Total (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col0" class="data row34 col0" >0.306104</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col1" class="data row34 col1" >-0.006771</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col2" class="data row34 col2" >-0.052202</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col3" class="data row34 col3" >0.023674</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col4" class="data row34 col4" >0.115083</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col5" class="data row34 col5" >0.207813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col6" class="data row34 col6" >-0.038219</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col7" class="data row34 col7" >0.010401</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col8" class="data row34 col8" >0.011679</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col9" class="data row34 col9" >0.032784</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col10" class="data row34 col10" >0.092535</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col11" class="data row34 col11" >-0.021473</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col12" class="data row34 col12" >0.083268</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col13" class="data row34 col13" >0.062919</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col14" class="data row34 col14" >-0.000855</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col15" class="data row34 col15" >0.022813</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col16" class="data row34 col16" >-0.037520</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col17" class="data row34 col17" >0.034400</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col18" class="data row34 col18" >0.009574</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col19" class="data row34 col19" >-0.022495</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col20" class="data row34 col20" >0.008491</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col21" class="data row34 col21" >-0.018435</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col22" class="data row34 col22" >-0.039320</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col23" class="data row34 col23" >0.303638</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col24" class="data row34 col24" >-0.001154</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col25" class="data row34 col25" >-0.056653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col26" class="data row34 col26" >0.140865</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col27" class="data row34 col27" >-0.166646</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col28" class="data row34 col28" >-0.281024</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col29" class="data row34 col29" >0.291487</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col30" class="data row34 col30" >-0.485183</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col31" class="data row34 col31" >0.398326</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col32" class="data row34 col32" >-0.091774</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col33" class="data row34 col33" >0.024148</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col34" class="data row34 col34" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col35" class="data row34 col35" >0.961787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col36" class="data row34 col36" >0.952538</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col37" class="data row34 col37" >0.739785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col38" class="data row34 col38" >0.933413</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col39" class="data row34 col39" >0.747155</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col40" class="data row34 col40" >0.950746</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col41" class="data row34 col41" >0.953111</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col42" class="data row34 col42" >0.873380</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col43" class="data row34 col43" >0.303638</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col44" class="data row34 col44" >0.400711</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col45" class="data row34 col45" >0.220267</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col46" class="data row34 col46" >0.622048</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col47" class="data row34 col47" >-0.174203</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col48" class="data row34 col48" >-0.044672</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col49" class="data row34 col49" >-0.694747</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col50" class="data row34 col50" >-0.177569</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col51" class="data row34 col51" >-0.317289</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row34_col52" class="data row34 col52" >-0.192195</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row35" class="row_heading level0 row35" >Matches Home (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col0" class="data row35 col0" >0.302135</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col1" class="data row35 col1" >-0.046243</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col2" class="data row35 col2" >-0.025269</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col3" class="data row35 col3" >-0.021591</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col4" class="data row35 col4" >0.078806</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col5" class="data row35 col5" >0.206087</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col6" class="data row35 col6" >-0.055551</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col7" class="data row35 col7" >0.028806</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col8" class="data row35 col8" >0.027125</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col9" class="data row35 col9" >0.021691</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col10" class="data row35 col10" >0.090088</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col11" class="data row35 col11" >-0.016264</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col12" class="data row35 col12" >0.076981</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col13" class="data row35 col13" >0.059136</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col14" class="data row35 col14" >-0.008503</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col15" class="data row35 col15" >0.012371</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col16" class="data row35 col16" >-0.040298</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col17" class="data row35 col17" >0.024683</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col18" class="data row35 col18" >0.006372</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col19" class="data row35 col19" >-0.031231</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col20" class="data row35 col20" >-0.003936</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col21" class="data row35 col21" >-0.019337</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col22" class="data row35 col22" >-0.047426</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col23" class="data row35 col23" >0.299721</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col24" class="data row35 col24" >-0.018675</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col25" class="data row35 col25" >-0.059582</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col26" class="data row35 col26" >0.101963</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col27" class="data row35 col27" >-0.251748</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col28" class="data row35 col28" >-0.337383</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col29" class="data row35 col29" >0.366607</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col30" class="data row35 col30" >-0.471409</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col31" class="data row35 col31" >0.382957</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col32" class="data row35 col32" >-0.091308</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col33" class="data row35 col33" >0.028184</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col34" class="data row35 col34" >0.961787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col35" class="data row35 col35" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col36" class="data row35 col36" >0.860719</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col37" class="data row35 col37" >0.647510</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col38" class="data row35 col38" >0.878959</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col39" class="data row35 col39" >0.768008</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col40" class="data row35 col40" >0.884918</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col41" class="data row35 col41" >0.907203</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col42" class="data row35 col42" >0.890657</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col43" class="data row35 col43" >0.299721</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col44" class="data row35 col44" >0.370943</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col45" class="data row35 col45" >0.133983</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col46" class="data row35 col46" >0.727074</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col47" class="data row35 col47" >-0.233114</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col48" class="data row35 col48" >-0.069650</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col49" class="data row35 col49" >-0.673604</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col50" class="data row35 col50" >-0.170839</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col51" class="data row35 col51" >-0.413983</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row35_col52" class="data row35 col52" >-0.247980</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row36" class="row_heading level0 row36" >Matches Away (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col0" class="data row36 col0" >0.268532</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col1" class="data row36 col1" >-0.005457</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col2" class="data row36 col2" >-0.077926</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col3" class="data row36 col3" >0.038918</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col4" class="data row36 col4" >0.179654</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col5" class="data row36 col5" >0.151284</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col6" class="data row36 col6" >-0.053040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col7" class="data row36 col7" >0.027291</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col8" class="data row36 col8" >0.018057</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col9" class="data row36 col9" >0.010229</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col10" class="data row36 col10" >0.111694</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col11" class="data row36 col11" >-0.043278</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col12" class="data row36 col12" >0.065275</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col13" class="data row36 col13" >0.057575</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col14" class="data row36 col14" >-0.000592</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col15" class="data row36 col15" >0.021453</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col16" class="data row36 col16" >-0.035337</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col17" class="data row36 col17" >0.033787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col18" class="data row36 col18" >0.002986</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col19" class="data row36 col19" >-0.014365</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col20" class="data row36 col20" >0.014038</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col21" class="data row36 col21" >-0.024773</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col22" class="data row36 col22" >-0.035627</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col23" class="data row36 col23" >0.265516</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col24" class="data row36 col24" >0.007816</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col25" class="data row36 col25" >-0.045565</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col26" class="data row36 col26" >0.160975</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col27" class="data row36 col27" >0.013667</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col28" class="data row36 col28" >-0.134734</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col29" class="data row36 col29" >0.117491</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col30" class="data row36 col30" >-0.364373</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col31" class="data row36 col31" >0.271876</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col32" class="data row36 col32" >-0.017388</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col33" class="data row36 col33" >0.063252</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col34" class="data row36 col34" >0.952538</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col35" class="data row36 col35" >0.860719</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col36" class="data row36 col36" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col37" class="data row36 col37" >0.608531</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col38" class="data row36 col38" >0.842821</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col39" class="data row36 col39" >0.794547</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col40" class="data row36 col40" >0.895481</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col41" class="data row36 col41" >0.898779</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col42" class="data row36 col42" >0.879188</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col43" class="data row36 col43" >0.265516</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col44" class="data row36 col44" >0.249364</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col45" class="data row36 col45" >0.151706</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col46" class="data row36 col46" >0.497768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col47" class="data row36 col47" >-0.072358</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col48" class="data row36 col48" >0.036289</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col49" class="data row36 col49" >-0.658936</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col50" class="data row36 col50" >-0.134033</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col51" class="data row36 col51" >-0.201775</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row36_col52" class="data row36 col52" >-0.092252</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row37" class="row_heading level0 row37" >Matches Neutral (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col0" class="data row37 col0" >0.267942</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col1" class="data row37 col1" >0.107358</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col2" class="data row37 col2" >-0.030840</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col3" class="data row37 col3" >0.099647</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col4" class="data row37 col4" >-0.016577</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col5" class="data row37 col5" >0.265167</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col6" class="data row37 col6" >0.073452</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col7" class="data row37 col7" >-0.095164</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col8" class="data row37 col8" >-0.056763</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col9" class="data row37 col9" >0.111108</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col10" class="data row37 col10" >-0.000054</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col11" class="data row37 col11" >0.034693</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col12" class="data row37 col12" >0.109579</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col13" class="data row37 col13" >0.057092</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col14" class="data row37 col14" >0.021061</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col15" class="data row37 col15" >0.045448</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col16" class="data row37 col16" >-0.016639</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col17" class="data row37 col17" >0.047029</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col18" class="data row37 col18" >0.032342</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col19" class="data row37 col19" >-0.008359</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col20" class="data row37 col20" >0.024931</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col21" class="data row37 col21" >0.011045</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col22" class="data row37 col22" >-0.006246</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col23" class="data row37 col23" >0.268089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col24" class="data row37 col24" >0.025435</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col25" class="data row37 col25" >-0.050420</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col26" class="data row37 col26" >0.127238</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col27" class="data row37 col27" >-0.335932</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col28" class="data row37 col28" >-0.381886</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col29" class="data row37 col29" >0.409459</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col30" class="data row37 col30" >-0.616410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col31" class="data row37 col31" >0.593514</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col32" class="data row37 col32" >-0.253377</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col33" class="data row37 col33" >-0.108225</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col34" class="data row37 col34" >0.739785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col35" class="data row37 col35" >0.647510</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col36" class="data row37 col36" >0.608531</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col37" class="data row37 col37" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col38" class="data row37 col38" >0.873542</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col39" class="data row37 col39" >0.179311</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col40" class="data row37 col40" >0.817181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col41" class="data row37 col41" >0.757899</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col42" class="data row37 col42" >0.367832</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col43" class="data row37 col43" >0.268089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col44" class="data row37 col44" >0.705617</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col45" class="data row37 col45" >0.550391</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col46" class="data row37 col46" >0.348944</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col47" class="data row37 col47" >-0.198046</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col48" class="data row37 col48" >-0.174286</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col49" class="data row37 col49" >-0.506131</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col50" class="data row37 col50" >-0.228621</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col51" class="data row37 col51" >-0.197335</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row37_col52" class="data row37 col52" >-0.210792</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row38" class="row_heading level0 row38" >Matches Wins (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col0" class="data row38 col0" >0.243925</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col1" class="data row38 col1" >0.007259</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col2" class="data row38 col2" >-0.015329</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col3" class="data row38 col3" >0.014066</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col4" class="data row38 col4" >0.042861</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col5" class="data row38 col5" >0.232201</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col6" class="data row38 col6" >-0.003248</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col7" class="data row38 col7" >-0.017483</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col8" class="data row38 col8" >0.001984</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col9" class="data row38 col9" >0.038588</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col10" class="data row38 col10" >0.081719</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col11" class="data row38 col11" >-0.025052</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col12" class="data row38 col12" >0.089838</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col13" class="data row38 col13" >0.047475</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col14" class="data row38 col14" >-0.042525</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col15" class="data row38 col15" >-0.015824</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col16" class="data row38 col16" >-0.079616</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col17" class="data row38 col17" >0.004691</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col18" class="data row38 col18" >-0.026062</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col19" class="data row38 col19" >-0.053979</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col20" class="data row38 col20" >-0.036258</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col21" class="data row38 col21" >-0.050401</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col22" class="data row38 col22" >-0.066209</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col23" class="data row38 col23" >0.242165</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col24" class="data row38 col24" >-0.005097</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col25" class="data row38 col25" >-0.058976</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col26" class="data row38 col26" >0.108937</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col27" class="data row38 col27" >-0.311078</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col28" class="data row38 col28" >-0.393041</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col29" class="data row38 col29" >0.423394</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col30" class="data row38 col30" >-0.667653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col31" class="data row38 col31" >0.620569</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col32" class="data row38 col32" >-0.183522</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col33" class="data row38 col33" >-0.048222</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col34" class="data row38 col34" >0.933413</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col35" class="data row38 col35" >0.878959</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col36" class="data row38 col36" >0.842821</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col37" class="data row38 col37" >0.873542</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col38" class="data row38 col38" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col39" class="data row38 col39" >0.468617</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col40" class="data row38 col40" >0.913000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col41" class="data row38 col41" >0.971411</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col42" class="data row38 col42" >0.667377</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col43" class="data row38 col43" >0.242165</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col44" class="data row38 col44" >0.554721</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col45" class="data row38 col45" >0.354182</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col46" class="data row38 col46" >0.553563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col47" class="data row38 col47" >-0.259513</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col48" class="data row38 col48" >-0.111439</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col49" class="data row38 col49" >-0.635587</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col50" class="data row38 col50" >-0.219452</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col51" class="data row38 col51" >-0.321748</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row38_col52" class="data row38 col52" >-0.275164</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row39" class="row_heading level0 row39" >Matches Losses (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col0" class="data row39 col0" >0.269882</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col1" class="data row39 col1" >-0.038496</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col2" class="data row39 col2" >-0.090208</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col3" class="data row39 col3" >0.020298</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col4" class="data row39 col4" >0.203090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col5" class="data row39 col5" >0.089774</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col6" class="data row39 col6" >-0.089150</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col7" class="data row39 col7" >0.066848</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col8" class="data row39 col8" >0.037375</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col9" class="data row39 col9" >-0.006169</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col10" class="data row39 col10" >0.079245</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col11" class="data row39 col11" >-0.013380</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col12" class="data row39 col12" >0.038024</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col13" class="data row39 col13" >0.072290</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col14" class="data row39 col14" >0.045894</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col15" class="data row39 col15" >0.057220</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col16" class="data row39 col16" >0.026454</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col17" class="data row39 col17" >0.046580</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col18" class="data row39 col18" >0.039708</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col19" class="data row39 col19" >0.029142</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col20" class="data row39 col20" >0.057748</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col21" class="data row39 col21" >0.019281</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col22" class="data row39 col22" >0.005815</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col23" class="data row39 col23" >0.266412</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col24" class="data row39 col24" >-0.033187</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col25" class="data row39 col25" >-0.062553</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col26" class="data row39 col26" >0.115482</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col27" class="data row39 col27" >0.129737</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col28" class="data row39 col28" >0.011150</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col29" class="data row39 col29" >-0.025960</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col30" class="data row39 col30" >0.031327</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col31" class="data row39 col31" >-0.159140</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col32" class="data row39 col32" >0.116508</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col33" class="data row39 col33" >0.141628</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col34" class="data row39 col34" >0.747155</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col35" class="data row39 col35" >0.768008</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col36" class="data row39 col36" >0.794547</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col37" class="data row39 col37" >0.179311</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col38" class="data row39 col38" >0.468617</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col39" class="data row39 col39" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col40" class="data row39 col40" >0.608349</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col41" class="data row39 col41" >0.590212</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col42" class="data row39 col42" >0.955521</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col43" class="data row39 col43" >0.266412</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col44" class="data row39 col44" >-0.045048</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col45" class="data row39 col45" >-0.150479</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col46" class="data row39 col46" >0.551842</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col47" class="data row39 col47" >0.013184</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col48" class="data row39 col48" >0.090778</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col49" class="data row39 col49" >-0.536730</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col50" class="data row39 col50" >-0.009947</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col51" class="data row39 col51" >-0.219166</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row39_col52" class="data row39 col52" >0.000574</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row40" class="row_heading level0 row40" >Matches Draws (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col0" class="data row40 col0" >0.335971</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col1" class="data row40 col1" >0.010474</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col2" class="data row40 col2" >-0.056300</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col3" class="data row40 col3" >0.039207</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col4" class="data row40 col4" >0.092773</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col5" class="data row40 col5" >0.201248</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col6" class="data row40 col6" >-0.025888</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col7" class="data row40 col7" >-0.012807</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col8" class="data row40 col8" >-0.011257</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col9" class="data row40 col9" >0.059246</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col10" class="data row40 col10" >0.084103</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col11" class="data row40 col11" >-0.011379</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col12" class="data row40 col12" >0.085851</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col13" class="data row40 col13" >0.049093</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col14" class="data row40 col14" >0.035327</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col15" class="data row40 col15" >0.055798</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col16" class="data row40 col16" >-0.004698</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col17" class="data row40 col17" >0.072052</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col18" class="data row40 col18" >0.049833</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col19" class="data row40 col19" >-0.007565</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col20" class="data row40 col20" >0.042912</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col21" class="data row40 col21" >0.017598</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col22" class="data row40 col22" >-0.015507</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col23" class="data row40 col23" >0.334802</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col24" class="data row40 col24" >0.061585</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col25" class="data row40 col25" >-0.005121</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col26" class="data row40 col26" >0.177444</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col27" class="data row40 col27" >-0.153698</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col28" class="data row40 col28" >-0.275117</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col29" class="data row40 col29" >0.266706</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col30" class="data row40 col30" >-0.523472</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col31" class="data row40 col31" >0.451685</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col32" class="data row40 col32" >-0.124652</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col33" class="data row40 col33" >0.012395</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col34" class="data row40 col34" >0.950746</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col35" class="data row40 col35" >0.884918</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col36" class="data row40 col36" >0.895481</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col37" class="data row40 col37" >0.817181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col38" class="data row40 col38" >0.913000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col39" class="data row40 col39" >0.608349</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col40" class="data row40 col40" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col41" class="data row40 col41" >0.884770</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col42" class="data row40 col42" >0.736305</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col43" class="data row40 col43" >0.334802</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col44" class="data row40 col44" >0.454376</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col45" class="data row40 col45" >0.320955</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col46" class="data row40 col46" >0.523342</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col47" class="data row40 col47" >-0.138414</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col48" class="data row40 col48" >-0.056663</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col49" class="data row40 col49" >-0.666452</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col50" class="data row40 col50" >-0.223369</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col51" class="data row40 col51" >-0.262394</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row40_col52" class="data row40 col52" >-0.159898</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row41" class="row_heading level0 row41" >Goals For (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col0" class="data row41 col0" >0.192936</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col1" class="data row41 col1" >-0.005749</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col2" class="data row41 col2" >-0.014466</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col3" class="data row41 col3" >0.003581</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col4" class="data row41 col4" >0.078123</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col5" class="data row41 col5" >0.228297</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col6" class="data row41 col6" >-0.013930</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col7" class="data row41 col7" >0.012138</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col8" class="data row41 col8" >0.025741</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col9" class="data row41 col9" >0.005288</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col10" class="data row41 col10" >0.106544</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col11" class="data row41 col11" >-0.045051</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col12" class="data row41 col12" >0.074531</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col13" class="data row41 col13" >0.037171</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col14" class="data row41 col14" >-0.064585</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col15" class="data row41 col15" >-0.036670</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col16" class="data row41 col16" >-0.098553</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col17" class="data row41 col17" >-0.019172</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col18" class="data row41 col18" >-0.049622</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col19" class="data row41 col19" >-0.062524</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col20" class="data row41 col20" >-0.061015</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col21" class="data row41 col21" >-0.070229</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col22" class="data row41 col22" >-0.080067</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col23" class="data row41 col23" >0.189720</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col24" class="data row41 col24" >-0.024244</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col25" class="data row41 col25" >-0.068876</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col26" class="data row41 col26" >0.097089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col27" class="data row41 col27" >-0.248245</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col28" class="data row41 col28" >-0.338536</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col29" class="data row41 col29" >0.361904</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col30" class="data row41 col30" >-0.606311</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col31" class="data row41 col31" >0.549227</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col32" class="data row41 col32" >-0.143851</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col33" class="data row41 col33" >-0.049286</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col34" class="data row41 col34" >0.953111</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col35" class="data row41 col35" >0.907203</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col36" class="data row41 col36" >0.898779</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col37" class="data row41 col37" >0.757899</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col38" class="data row41 col38" >0.971411</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col39" class="data row41 col39" >0.590212</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col40" class="data row41 col40" >0.884770</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col41" class="data row41 col41" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col42" class="data row41 col42" >0.774907</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col43" class="data row41 col43" >0.189720</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col44" class="data row41 col44" >0.416085</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col45" class="data row41 col45" >0.213325</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col46" class="data row41 col46" >0.589273</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col47" class="data row41 col47" >-0.241688</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col48" class="data row41 col48" >-0.083742</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col49" class="data row41 col49" >-0.638217</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col50" class="data row41 col50" >-0.195490</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col51" class="data row41 col51" >-0.323054</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row41_col52" class="data row41 col52" >-0.257469</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row42" class="row_heading level0 row42" >Goals Against (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col0" class="data row42 col0" >0.219553</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col1" class="data row42 col1" >-0.040640</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col2" class="data row42 col2" >-0.067570</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col3" class="data row42 col3" >0.006124</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col4" class="data row42 col4" >0.175602</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col5" class="data row42 col5" >0.147512</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col6" class="data row42 col6" >-0.076957</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col7" class="data row42 col7" >0.043040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col8" class="data row42 col8" >0.034479</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col9" class="data row42 col9" >0.002037</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col10" class="data row42 col10" >0.092964</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col11" class="data row42 col11" >-0.022737</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col12" class="data row42 col12" >0.062837</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col13" class="data row42 col13" >0.069732</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col14" class="data row42 col14" >0.004520</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col15" class="data row42 col15" >0.025994</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col16" class="data row42 col16" >-0.019292</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col17" class="data row42 col17" >0.008014</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col18" class="data row42 col18" >0.003009</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col19" class="data row42 col19" >0.003119</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col20" class="data row42 col20" >0.007796</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col21" class="data row42 col21" >-0.012420</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col22" class="data row42 col22" >-0.020504</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col23" class="data row42 col23" >0.215572</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col24" class="data row42 col24" >-0.048828</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col25" class="data row42 col25" >-0.084938</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col26" class="data row42 col26" >0.119643</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col27" class="data row42 col27" >-0.027860</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col28" class="data row42 col28" >-0.133625</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col29" class="data row42 col29" >0.135760</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col30" class="data row42 col30" >-0.192507</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col31" class="data row42 col31" >0.064036</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col32" class="data row42 col32" >0.034249</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col33" class="data row42 col33" >0.090317</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col34" class="data row42 col34" >0.873380</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col35" class="data row42 col35" >0.890657</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col36" class="data row42 col36" >0.879188</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col37" class="data row42 col37" >0.367832</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col38" class="data row42 col38" >0.667377</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col39" class="data row42 col39" >0.955521</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col40" class="data row42 col40" >0.736305</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col41" class="data row42 col41" >0.774907</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col42" class="data row42 col42" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col43" class="data row42 col43" >0.215572</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col44" class="data row42 col44" >0.124304</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col45" class="data row42 col45" >-0.035805</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col46" class="data row42 col46" >0.615476</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col47" class="data row42 col47" >-0.090626</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col48" class="data row42 col48" >0.035691</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col49" class="data row42 col49" >-0.605725</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col50" class="data row42 col50" >-0.095414</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col51" class="data row42 col51" >-0.271619</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row42_col52" class="data row42 col52" >-0.105209</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row43" class="row_heading level0 row43" >Data Year (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col0" class="data row43 col0" >0.999181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col1" class="data row43 col1" >-0.027040</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col2" class="data row43 col2" >-0.055270</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col3" class="data row43 col3" >0.009779</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col4" class="data row43 col4" >0.133515</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col5" class="data row43 col5" >0.119534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col6" class="data row43 col6" >-0.057600</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col7" class="data row43 col7" >0.205147</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col8" class="data row43 col8" >0.118922</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col9" class="data row43 col9" >-0.061889</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col10" class="data row43 col10" >0.049964</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col11" class="data row43 col11" >0.027931</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col12" class="data row43 col12" >0.080312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col13" class="data row43 col13" >0.053047</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col14" class="data row43 col14" >0.354727</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col15" class="data row43 col15" >0.328692</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col16" class="data row43 col16" >0.333069</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col17" class="data row43 col17" >0.323200</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col18" class="data row43 col18" >0.308090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col19" class="data row43 col19" >0.254382</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col20" class="data row43 col20" >0.391653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col21" class="data row43 col21" >0.264050</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col22" class="data row43 col22" >0.238215</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col23" class="data row43 col23" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col24" class="data row43 col24" >0.097259</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col25" class="data row43 col25" >-0.007355</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col26" class="data row43 col26" >0.304464</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col27" class="data row43 col27" >0.301787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col28" class="data row43 col28" >0.258139</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col29" class="data row43 col29" >-0.188787</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col30" class="data row43 col30" >0.113885</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col31" class="data row43 col31" >-0.031570</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col32" class="data row43 col32" >0.069974</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col33" class="data row43 col33" >0.110120</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col34" class="data row43 col34" >0.303638</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col35" class="data row43 col35" >0.299721</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col36" class="data row43 col36" >0.265516</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col37" class="data row43 col37" >0.268089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col38" class="data row43 col38" >0.242165</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col39" class="data row43 col39" >0.266412</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col40" class="data row43 col40" >0.334802</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col41" class="data row43 col41" >0.189720</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col42" class="data row43 col42" >0.215572</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col43" class="data row43 col43" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col44" class="data row43 col44" >0.157465</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col45" class="data row43 col45" >0.069642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col46" class="data row43 col46" >0.342408</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col47" class="data row43 col47" >0.083666</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col48" class="data row43 col48" >0.022620</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col49" class="data row43 col49" >0.006655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col50" class="data row43 col50" >0.088625</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col51" class="data row43 col51" >-0.090005</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row43_col52" class="data row43 col52" >0.091841</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row44" class="row_heading level0 row44" >GDP (PPP) (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col0" class="data row44 col0" >0.157812</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col1" class="data row44 col1" >-0.018947</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col2" class="data row44 col2" >0.020977</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col3" class="data row44 col3" >-0.026181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col4" class="data row44 col4" >-0.098410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col5" class="data row44 col5" >0.245284</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col6" class="data row44 col6" >-0.003328</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col7" class="data row44 col7" >-0.112362</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col8" class="data row44 col8" >-0.044279</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col9" class="data row44 col9" >0.112632</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col10" class="data row44 col10" >0.027181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col11" class="data row44 col11" >-0.028103</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col12" class="data row44 col12" >0.085363</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col13" class="data row44 col13" >0.071153</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col14" class="data row44 col14" >-0.028563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col15" class="data row44 col15" >0.003651</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col16" class="data row44 col16" >-0.047947</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col17" class="data row44 col17" >-0.052003</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col18" class="data row44 col18" >-0.047073</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col19" class="data row44 col19" >0.023464</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col20" class="data row44 col20" >-0.046126</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col21" class="data row44 col21" >-0.047898</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col22" class="data row44 col22" >0.002342</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col23" class="data row44 col23" >0.157465</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col24" class="data row44 col24" >-0.086181</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col25" class="data row44 col25" >-0.138649</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col26" class="data row44 col26" >0.087364</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col27" class="data row44 col27" >-0.314904</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col28" class="data row44 col28" >-0.309352</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col29" class="data row44 col29" >0.368225</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col30" class="data row44 col30" >-0.375450</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col31" class="data row44 col31" >0.337257</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col32" class="data row44 col32" >-0.197899</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col33" class="data row44 col33" >-0.043768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col34" class="data row44 col34" >0.400711</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col35" class="data row44 col35" >0.370943</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col36" class="data row44 col36" >0.249364</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col37" class="data row44 col37" >0.705617</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col38" class="data row44 col38" >0.554721</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col39" class="data row44 col39" >-0.045048</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col40" class="data row44 col40" >0.454376</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col41" class="data row44 col41" >0.416085</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col42" class="data row44 col42" >0.124304</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col43" class="data row44 col43" >0.157465</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col44" class="data row44 col44" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col45" class="data row44 col45" >0.896704</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col46" class="data row44 col46" >0.225593</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col47" class="data row44 col47" >-0.168984</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col48" class="data row44 col48" >-0.220840</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col49" class="data row44 col49" >-0.298814</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col50" class="data row44 col50" >-0.202426</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col51" class="data row44 col51" >-0.191549</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row44_col52" class="data row44 col52" >-0.174102</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row45" class="row_heading level0 row45" >Population (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col0" class="data row45 col0" >0.069006</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col1" class="data row45 col1" >-0.009853</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col2" class="data row45 col2" >-0.015539</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col3" class="data row45 col3" >0.001018</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col4" class="data row45 col4" >-0.079523</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col5" class="data row45 col5" >0.157189</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col6" class="data row45 col6" >-0.018135</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col7" class="data row45 col7" >-0.127366</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col8" class="data row45 col8" >-0.070009</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col9" class="data row45 col9" >0.114451</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col10" class="data row45 col10" >0.009901</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col11" class="data row45 col11" >-0.013413</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col12" class="data row45 col12" >0.071281</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col13" class="data row45 col13" >0.060996</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col14" class="data row45 col14" >-0.033637</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col15" class="data row45 col15" >-0.004451</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col16" class="data row45 col16" >-0.044984</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col17" class="data row45 col17" >-0.068410</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col18" class="data row45 col18" >-0.052710</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col19" class="data row45 col19" >0.019552</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col20" class="data row45 col20" >-0.047769</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col21" class="data row45 col21" >-0.045886</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col22" class="data row45 col22" >0.002645</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col23" class="data row45 col23" >0.069642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col24" class="data row45 col24" >-0.074441</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col25" class="data row45 col25" >-0.132361</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col26" class="data row45 col26" >0.109446</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col27" class="data row45 col27" >-0.173826</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col28" class="data row45 col28" >-0.188979</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col29" class="data row45 col29" >0.204300</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col30" class="data row45 col30" >-0.233574</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col31" class="data row45 col31" >0.171236</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col32" class="data row45 col32" >-0.144375</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col33" class="data row45 col33" >-0.001318</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col34" class="data row45 col34" >0.220267</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col35" class="data row45 col35" >0.133983</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col36" class="data row45 col36" >0.151706</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col37" class="data row45 col37" >0.550391</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col38" class="data row45 col38" >0.354182</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col39" class="data row45 col39" >-0.150479</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col40" class="data row45 col40" >0.320955</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col41" class="data row45 col41" >0.213325</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col42" class="data row45 col42" >-0.035805</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col43" class="data row45 col43" >0.069642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col44" class="data row45 col44" >0.896704</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col45" class="data row45 col45" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col46" class="data row45 col46" >-0.057467</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col47" class="data row45 col47" >-0.056489</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col48" class="data row45 col48" >-0.153336</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col49" class="data row45 col49" >-0.224251</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col50" class="data row45 col50" >-0.201891</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col51" class="data row45 col51" >0.017337</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row45_col52" class="data row45 col52" >-0.064001</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row46" class="row_heading level0 row46" >GDP (PPP) Per Capita (2)</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col0" class="data row46 col0" >0.344897</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col1" class="data row46 col1" >-0.071821</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col2" class="data row46 col2" >0.087310</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col3" class="data row46 col3" >-0.103554</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col4" class="data row46 col4" >0.060064</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col5" class="data row46 col5" >0.199662</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col6" class="data row46 col6" >-0.007781</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col7" class="data row46 col7" >0.114020</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col8" class="data row46 col8" >0.110052</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col9" class="data row46 col9" >-0.043993</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col10" class="data row46 col10" >0.150828</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col11" class="data row46 col11" >-0.092119</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col12" class="data row46 col12" >0.044468</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col13" class="data row46 col13" >0.096833</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col14" class="data row46 col14" >-0.042417</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col15" class="data row46 col15" >-0.050003</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col16" class="data row46 col16" >-0.059197</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col17" class="data row46 col17" >0.044631</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col18" class="data row46 col18" >-0.035503</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col19" class="data row46 col19" >-0.052780</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col20" class="data row46 col20" >-0.011179</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col21" class="data row46 col21" >-0.078898</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col22" class="data row46 col22" >-0.092184</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col23" class="data row46 col23" >0.342408</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col24" class="data row46 col24" >-0.035020</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col25" class="data row46 col25" >-0.018565</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col26" class="data row46 col26" >-0.065385</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col27" class="data row46 col27" >-0.222124</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col28" class="data row46 col28" >-0.271742</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col29" class="data row46 col29" >0.302832</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col30" class="data row46 col30" >-0.308511</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col31" class="data row46 col31" >0.287634</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col32" class="data row46 col32" >-0.155642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col33" class="data row46 col33" >-0.108992</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col34" class="data row46 col34" >0.622048</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col35" class="data row46 col35" >0.727074</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col36" class="data row46 col36" >0.497768</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col37" class="data row46 col37" >0.348944</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col38" class="data row46 col38" >0.553563</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col39" class="data row46 col39" >0.551842</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col40" class="data row46 col40" >0.523342</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col41" class="data row46 col41" >0.589273</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col42" class="data row46 col42" >0.615476</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col43" class="data row46 col43" >0.342408</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col44" class="data row46 col44" >0.225593</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col45" class="data row46 col45" >-0.057467</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col46" class="data row46 col46" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col47" class="data row46 col47" >-0.236965</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col48" class="data row46 col48" >-0.079166</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col49" class="data row46 col49" >-0.373200</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col50" class="data row46 col50" >0.091921</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col51" class="data row46 col51" >-0.707645</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row46_col52" class="data row46 col52" >-0.241473</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row47" class="row_heading level0 row47" >Elo_rating_diff</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col0" class="data row47 col0" >0.082644</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col1" class="data row47 col1" >0.270399</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col2" class="data row47 col2" >-0.203178</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col3" class="data row47 col3" >0.320416</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col4" class="data row47 col4" >0.013143</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col5" class="data row47 col5" >-0.098104</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col6" class="data row47 col6" >0.107157</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col7" class="data row47 col7" >-0.672655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col8" class="data row47 col8" >-0.691653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col9" class="data row47 col9" >0.734996</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col10" class="data row47 col10" >-0.452090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col11" class="data row47 col11" >0.430250</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col12" class="data row47 col12" >-0.162623</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col13" class="data row47 col13" >-0.129915</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col14" class="data row47 col14" >0.284766</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col15" class="data row47 col15" >0.320610</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col16" class="data row47 col16" >0.139453</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col17" class="data row47 col17" >0.453306</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col18" class="data row47 col18" >0.411062</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col19" class="data row47 col19" >-0.037494</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col20" class="data row47 col20" >0.278027</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col21" class="data row47 col21" >0.340631</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col22" class="data row47 col22" >0.082882</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col23" class="data row47 col23" >0.083666</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col24" class="data row47 col24" >0.392577</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col25" class="data row47 col25" >0.239756</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col26" class="data row47 col26" >0.225116</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col27" class="data row47 col27" >0.641795</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col28" class="data row47 col28" >0.653811</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col29" class="data row47 col29" >-0.697075</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col30" class="data row47 col30" >0.505907</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col31" class="data row47 col31" >-0.477593</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col32" class="data row47 col32" >0.143726</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col33" class="data row47 col33" >0.009710</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col34" class="data row47 col34" >-0.174203</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col35" class="data row47 col35" >-0.233114</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col36" class="data row47 col36" >-0.072358</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col37" class="data row47 col37" >-0.198046</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col38" class="data row47 col38" >-0.259513</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col39" class="data row47 col39" >0.013184</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col40" class="data row47 col40" >-0.138414</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col41" class="data row47 col41" >-0.241688</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col42" class="data row47 col42" >-0.090626</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col43" class="data row47 col43" >0.083666</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col44" class="data row47 col44" >-0.168984</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col45" class="data row47 col45" >-0.056489</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col46" class="data row47 col46" >-0.236965</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col47" class="data row47 col47" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col48" class="data row47 col48" >0.069512</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col49" class="data row47 col49" >0.296011</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col50" class="data row47 col50" >0.208477</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col51" class="data row47 col51" >0.290098</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row47_col52" class="data row47 col52" >0.996716</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row48" class="row_heading level0 row48" >Home_advantage</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col0" class="data row48 col0" >0.019894</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col1" class="data row48 col1" >0.039548</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col2" class="data row48 col2" >0.040090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col3" class="data row48 col3" >0.008241</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col4" class="data row48 col4" >0.794244</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col5" class="data row48 col5" >-0.702118</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col6" class="data row48 col6" >0.058971</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col7" class="data row48 col7" >-0.042544</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col8" class="data row48 col8" >0.020017</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col9" class="data row48 col9" >-0.013239</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col10" class="data row48 col10" >-0.117504</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col11" class="data row48 col11" >0.112734</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col12" class="data row48 col12" >-0.065403</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col13" class="data row48 col13" >-0.015386</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col14" class="data row48 col14" >0.109368</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col15" class="data row48 col15" >0.125416</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col16" class="data row48 col16" >0.092012</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col17" class="data row48 col17" >0.061771</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col18" class="data row48 col18" >0.104150</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col19" class="data row48 col19" >0.071775</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col20" class="data row48 col20" >0.106606</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col21" class="data row48 col21" >0.130170</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col22" class="data row48 col22" >0.101014</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col23" class="data row48 col23" >0.022620</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col24" class="data row48 col24" >-0.013153</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col25" class="data row48 col25" >-0.058799</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col26" class="data row48 col26" >0.160454</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col27" class="data row48 col27" >0.104221</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col28" class="data row48 col28" >0.074988</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col29" class="data row48 col29" >-0.116478</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col30" class="data row48 col30" >0.130399</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col31" class="data row48 col31" >-0.131785</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col32" class="data row48 col32" >0.092770</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col33" class="data row48 col33" >0.022742</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col34" class="data row48 col34" >-0.044672</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col35" class="data row48 col35" >-0.069650</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col36" class="data row48 col36" >0.036289</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col37" class="data row48 col37" >-0.174286</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col38" class="data row48 col38" >-0.111439</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col39" class="data row48 col39" >0.090778</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col40" class="data row48 col40" >-0.056663</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col41" class="data row48 col41" >-0.083742</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col42" class="data row48 col42" >0.035691</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col43" class="data row48 col43" >0.022620</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col44" class="data row48 col44" >-0.220840</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col45" class="data row48 col45" >-0.153336</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col46" class="data row48 col46" >-0.079166</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col47" class="data row48 col47" >0.069512</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col48" class="data row48 col48" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col49" class="data row48 col49" >0.080575</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col50" class="data row48 col50" >0.130801</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col51" class="data row48 col51" >0.171031</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row48_col52" class="data row48 col52" >0.066295</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row49" class="row_heading level0 row49" >Relative_experience</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col0" class="data row49 col0" >0.006154</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col1" class="data row49 col1" >0.087769</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col2" class="data row49 col2" >0.062642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col3" class="data row49 col3" >0.032856</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col4" class="data row49 col4" >-0.000479</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col5" class="data row49 col5" >-0.132134</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col6" class="data row49 col6" >0.114542</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col7" class="data row49 col7" >-0.048738</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col8" class="data row49 col8" >-0.066596</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col9" class="data row49 col9" >0.061703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col10" class="data row49 col10" >-0.212514</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col11" class="data row49 col11" >0.146912</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col12" class="data row49 col12" >-0.081937</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col13" class="data row49 col13" >-0.094119</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col14" class="data row49 col14" >0.397826</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col15" class="data row49 col15" >0.352397</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col16" class="data row49 col16" >0.412580</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col17" class="data row49 col17" >0.300263</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col18" class="data row49 col18" >0.355594</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col19" class="data row49 col19" >0.310269</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col20" class="data row49 col20" >0.366740</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col21" class="data row49 col21" >0.387284</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col22" class="data row49 col22" >0.374152</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col23" class="data row49 col23" >0.006655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col24" class="data row49 col24" >0.126132</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col25" class="data row49 col25" >0.060010</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col26" class="data row49 col26" >0.122134</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col27" class="data row49 col27" >0.266725</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col28" class="data row49 col28" >0.401188</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col29" class="data row49 col29" >-0.371154</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col30" class="data row49 col30" >0.395498</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col31" class="data row49 col31" >-0.289809</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col32" class="data row49 col32" >0.051139</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col33" class="data row49 col33" >-0.011550</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col34" class="data row49 col34" >-0.694747</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col35" class="data row49 col35" >-0.673604</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col36" class="data row49 col36" >-0.658936</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col37" class="data row49 col37" >-0.506131</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col38" class="data row49 col38" >-0.635587</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col39" class="data row49 col39" >-0.536730</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col40" class="data row49 col40" >-0.666452</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col41" class="data row49 col41" >-0.638217</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col42" class="data row49 col42" >-0.605725</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col43" class="data row49 col43" >0.006655</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col44" class="data row49 col44" >-0.298814</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col45" class="data row49 col45" >-0.224251</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col46" class="data row49 col46" >-0.373200</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col47" class="data row49 col47" >0.296011</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col48" class="data row49 col48" >0.080575</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col49" class="data row49 col49" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col50" class="data row49 col50" >0.132207</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col51" class="data row49 col51" >0.297127</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row49_col52" class="data row49 col52" >0.314777</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row50" class="row_heading level0 row50" >Relative_population</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col0" class="data row50 col0" >0.084347</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col1" class="data row50 col1" >0.224610</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col2" class="data row50 col2" >0.049408</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col3" class="data row50 col3" >0.145442</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col4" class="data row50 col4" >0.160143</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col5" class="data row50 col5" >-0.025911</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col6" class="data row50 col6" >0.224340</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col7" class="data row50 col7" >-0.084076</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col8" class="data row50 col8" >-0.067435</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col9" class="data row50 col9" >0.071847</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col10" class="data row50 col10" >-0.052703</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col11" class="data row50 col11" >0.012540</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col12" class="data row50 col12" >-0.034572</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col13" class="data row50 col13" >0.054745</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col14" class="data row50 col14" >0.079791</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col15" class="data row50 col15" >0.093458</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col16" class="data row50 col16" >0.032095</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col17" class="data row50 col17" >0.136115</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col18" class="data row50 col18" >0.095639</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col19" class="data row50 col19" >0.013120</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col20" class="data row50 col20" >0.091447</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col21" class="data row50 col21" >0.054015</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col22" class="data row50 col22" >0.039089</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col23" class="data row50 col23" >0.088625</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col24" class="data row50 col24" >0.250226</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col25" class="data row50 col25" >0.261225</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col26" class="data row50 col26" >-0.024356</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col27" class="data row50 col27" >0.255592</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col28" class="data row50 col28" >0.254559</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col29" class="data row50 col29" >-0.231379</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col30" class="data row50 col30" >0.378033</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col31" class="data row50 col31" >-0.301534</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col32" class="data row50 col32" >0.023664</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col33" class="data row50 col33" >-0.010192</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col34" class="data row50 col34" >-0.177569</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col35" class="data row50 col35" >-0.170839</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col36" class="data row50 col36" >-0.134033</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col37" class="data row50 col37" >-0.228621</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col38" class="data row50 col38" >-0.219452</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col39" class="data row50 col39" >-0.009947</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col40" class="data row50 col40" >-0.223369</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col41" class="data row50 col41" >-0.195490</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col42" class="data row50 col42" >-0.095414</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col43" class="data row50 col43" >0.088625</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col44" class="data row50 col44" >-0.202426</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col45" class="data row50 col45" >-0.201891</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col46" class="data row50 col46" >0.091921</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col47" class="data row50 col47" >0.208477</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col48" class="data row50 col48" >0.130801</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col49" class="data row50 col49" >0.132207</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col50" class="data row50 col50" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col51" class="data row50 col51" >-0.052218</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row50_col52" class="data row50 col52" >0.221268</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row51" class="row_heading level0 row51" >Relative_GDP_per_capita</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col0" class="data row51 col0" >-0.088840</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col1" class="data row51 col1" >0.171901</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col2" class="data row51 col2" >-0.200309</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col3" class="data row51 col3" >0.243060</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col4" class="data row51 col4" >0.129389</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col5" class="data row51 col5" >-0.127645</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col6" class="data row51 col6" >0.023997</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col7" class="data row51 col7" >-0.163334</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col8" class="data row51 col8" >-0.169190</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col9" class="data row51 col9" >0.158316</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col10" class="data row51 col10" >-0.199415</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col11" class="data row51 col11" >0.155931</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col12" class="data row51 col12" >-0.185442</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col13" class="data row51 col13" >-0.230776</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col14" class="data row51 col14" >0.324838</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col15" class="data row51 col15" >0.389694</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col16" class="data row51 col16" >0.269562</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col17" class="data row51 col17" >0.145676</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col18" class="data row51 col18" >0.272361</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col19" class="data row51 col19" >0.299335</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col20" class="data row51 col20" >0.269195</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col21" class="data row51 col21" >0.326223</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col22" class="data row51 col22" >0.358090</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col23" class="data row51 col23" >-0.090005</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col24" class="data row51 col24" >0.130241</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col25" class="data row51 col25" >-0.053884</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col26" class="data row51 col26" >0.520000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col27" class="data row51 col27" >0.238120</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col28" class="data row51 col28" >0.246161</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col29" class="data row51 col29" >-0.260276</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col30" class="data row51 col30" >0.272017</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col31" class="data row51 col31" >-0.261846</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col32" class="data row51 col32" >0.064875</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col33" class="data row51 col33" >0.017151</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col34" class="data row51 col34" >-0.317289</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col35" class="data row51 col35" >-0.413983</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col36" class="data row51 col36" >-0.201775</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col37" class="data row51 col37" >-0.197335</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col38" class="data row51 col38" >-0.321748</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col39" class="data row51 col39" >-0.219166</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col40" class="data row51 col40" >-0.262394</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col41" class="data row51 col41" >-0.323054</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col42" class="data row51 col42" >-0.271619</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col43" class="data row51 col43" >-0.090005</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col44" class="data row51 col44" >-0.191549</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col45" class="data row51 col45" >0.017337</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col46" class="data row51 col46" >-0.707645</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col47" class="data row51 col47" >0.290098</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col48" class="data row51 col48" >0.171031</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col49" class="data row51 col49" >0.297127</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col50" class="data row51 col50" >-0.052218</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col51" class="data row51 col51" >1.000000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row51_col52" class="data row51 col52" >0.290677</td>
            </tr>
            <tr>
                        <th id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131level0_row52" class="row_heading level0 row52" >Relative_ELO_rating</th>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col0" class="data row52 col0" >0.091312</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col1" class="data row52 col1" >0.272704</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col2" class="data row52 col2" >-0.198575</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col3" class="data row52 col3" >0.319642</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col4" class="data row52 col4" >0.008687</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col5" class="data row52 col5" >-0.098073</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col6" class="data row52 col6" >0.112000</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col7" class="data row52 col7" >-0.662025</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col8" class="data row52 col8" >-0.681077</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col9" class="data row52 col9" >0.723067</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col10" class="data row52 col10" >-0.446640</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col11" class="data row52 col11" >0.425818</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col12" class="data row52 col12" >-0.158286</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col13" class="data row52 col13" >-0.123604</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col14" class="data row52 col14" >0.283473</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col15" class="data row52 col15" >0.318980</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col16" class="data row52 col16" >0.141820</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col17" class="data row52 col17" >0.443470</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col18" class="data row52 col18" >0.405927</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col19" class="data row52 col19" >-0.031085</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col20" class="data row52 col20" >0.275001</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col21" class="data row52 col21" >0.338771</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col22" class="data row52 col22" >0.087727</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col23" class="data row52 col23" >0.091841</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col24" class="data row52 col24" >0.378288</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col25" class="data row52 col25" >0.225653</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col26" class="data row52 col26" >0.221028</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col27" class="data row52 col27" >0.646986</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col28" class="data row52 col28" >0.683620</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col29" class="data row52 col29" >-0.704846</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col30" class="data row52 col30" >0.535740</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col31" class="data row52 col31" >-0.500194</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col32" class="data row52 col32" >0.158798</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col33" class="data row52 col33" >0.026619</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col34" class="data row52 col34" >-0.192195</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col35" class="data row52 col35" >-0.247980</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col36" class="data row52 col36" >-0.092252</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col37" class="data row52 col37" >-0.210792</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col38" class="data row52 col38" >-0.275164</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col39" class="data row52 col39" >0.000574</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col40" class="data row52 col40" >-0.159898</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col41" class="data row52 col41" >-0.257469</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col42" class="data row52 col42" >-0.105209</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col43" class="data row52 col43" >0.091841</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col44" class="data row52 col44" >-0.174102</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col45" class="data row52 col45" >-0.064001</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col46" class="data row52 col46" >-0.241473</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col47" class="data row52 col47" >0.996716</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col48" class="data row52 col48" >0.066295</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col49" class="data row52 col49" >0.314777</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col50" class="data row52 col50" >0.221268</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col51" class="data row52 col51" >0.290677</td>
                        <td id="T_28a43e28_bfd5_11eb_9d9d_74d83eb26131row52_col52" class="data row52 col52" >1.000000</td>
            </tr>
    </tbody></table>



## 4. Modelling

* Select Modelling Technique
* Generate Test Design
* Build Model
* Assess Model

### Updated WC model
* https://github.com/deacona/the-ball-is-round/blob/master/reports/intl_01_world_cup_2018.md
* https://github.com/deacona/the-ball-is-round/blob/master/notebooks/intl_01_world_cup_2018.ipynb

### "Soccernomics"
* goal diff = (0.6666 * home adv) + (0.5 * relative experience) + (0.1 * relative population) + (0.1 * relative gdp/head) + ...
* e.g. England vs Germany at Euro 96
    * Home = England = 1
    * Exp = 84k v 84k = 0
    * Pop = 57 v 81 = -0.4
    * GDP/h = 1627492 / 57 v 2633828 / 81 = -0.1
    * GD = (0.6666 * 1) + (0.5 * 0) + (0.1 * -0.4) + (0.1 * -0.1) = 0.6
* http://www.soccernomics-agency.com/wordpress/wp-content/uploads/2017/10/soccer-convergence-1.pdf

### Dixon-Coles (and other probability models)
* https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling-dixon-coles-and-time-weighting/
* http://www.statsandsnakeoil.com/2018/06/05/modelling-the-world-cup-with-regista/
* http://opisthokonta.net/?cat=48

    GD Train data has shape: (116, 4)
    GD Test data has shape: (29, 4)
    ------
    GT Train data has shape: (116, 4)
    GT Test data has shape: (29, 4)
    

    Wall time: 354 ms
    




    (9, 9)



## 5. Evaluation

* Evaluate Results
* Review Process
* Determine Next Steps

```
# % correct score, goal diff, result, points
# vs historic trends (goals, W/D/L)
```

    Goal difference model
    
    Evaluating Dummy (mean)...
    
    {'MedAE': 1.7672413793103448, 'RMSE': 2.126935713445986, 'R^2': -0.03441068515497525, 'Name': 'Dummy (mean)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_1.png)
    


    
    --------------------
    
    Evaluating Dummy (median)...
    
    {'MedAE': 2.0, 'RMSE': 2.181426297094443, 'R^2': -0.0880913539967374, 'Name': 'Dummy (median)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_3.png)
    


    
    --------------------
    
    Evaluating Linear Reg...
    
    {'MedAE': 1.3408721774714916, 'RMSE': 2.1069949071529743, 'R^2': -0.015105644400317697, 'Name': 'Linear Reg'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_5.png)
    


    
    --------------------
    
    Evaluating Lasso...
    
    {'MedAE': 1.7672413793103448, 'RMSE': 2.126935713445986, 'R^2': -0.03441068515497525, 'Name': 'Lasso'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_7.png)
    


    
    --------------------
    
    Evaluating Ridge...
    
    {'MedAE': 1.3456764737303994, 'RMSE': 2.1067469028217567, 'R^2': -0.014866691966765488, 'Name': 'Ridge'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_9.png)
    


    
    --------------------
    
    Evaluating Random Forest...
    
    {'MedAE': 2.05, 'RMSE': 2.341004058091314, 'R^2': -0.25310829255029876, 'Name': 'Random Forest'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_11.png)
    


    
    --------------------
    
    Evaluating Gradient Boost...
    
    {'MedAE': 1.9483445480740613, 'RMSE': 2.374543520921922, 'R^2': -0.2892719631442813, 'Name': 'Gradient Boost'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_13.png)
    


    
    --------------------
    
    Evaluating SVM (linear)...
    
    {'MedAE': 1.5054012420818588, 'RMSE': 2.1560661787620234, 'R^2': -0.06293925226113095, 'Name': 'SVM (linear)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_15.png)
    


    
    --------------------
    
    Evaluating SVM (rbf)...
    
    {'MedAE': 1.5770912891176907, 'RMSE': 2.3009319170660696, 'R^2': -0.21057529764670413, 'Name': 'SVM (rbf)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_17.png)
    


    
    --------------------
    
    9 models evaluated
    ==============
    ==============
    Goal total model
    
    Evaluating Dummy (mean)...
    
    {'MedAE': 0.5948275862068964, 'RMSE': 1.3739388944244812, 'R^2': -0.0569657123834888, 'Name': 'Dummy (mean)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_19.png)
    


    
    --------------------
    
    Evaluating Dummy (median)...
    
    {'MedAE': 1.0, 'RMSE': 1.364576478442026, 'R^2': -0.04260985352862878, 'Name': 'Dummy (median)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_21.png)
    


    
    --------------------
    
    Evaluating Linear Reg...
    
    {'MedAE': 0.8280960396830523, 'RMSE': 1.5078586652816524, 'R^2': -0.2730554936784533, 'Name': 'Linear Reg'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_23.png)
    


    
    --------------------
    
    Evaluating Lasso...
    
    {'MedAE': 0.5948275862068964, 'RMSE': 1.3739388944244812, 'R^2': -0.0569657123834888, 'Name': 'Lasso'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_25.png)
    


    
    --------------------
    
    Evaluating Ridge...
    
    {'MedAE': 0.8265290359807271, 'RMSE': 1.50686684320468, 'R^2': -0.2713812926290584, 'Name': 'Ridge'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_27.png)
    


    
    --------------------
    
    Evaluating Random Forest...
    
    {'MedAE': 1.0350000000000001, 'RMSE': 1.5069537273580988, 'R^2': -0.27152790952803696, 'Name': 'Random Forest'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_29.png)
    


    
    --------------------
    
    Evaluating Gradient Boost...
    
    {'MedAE': 1.2533755838600227, 'RMSE': 1.5987162422889896, 'R^2': -0.431096229856595, 'Name': 'Gradient Boost'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_31.png)
    


    
    --------------------
    
    Evaluating SVM (linear)...
    
    {'MedAE': 1.001224233463077, 'RMSE': 1.4610249166757023, 'R^2': -0.1952019918847081, 'Name': 'SVM (linear)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_33.png)
    


    
    --------------------
    
    Evaluating SVM (rbf)...
    
    {'MedAE': 0.8934104387017276, 'RMSE': 1.4251456278222854, 'R^2': -0.1372201670315054, 'Name': 'SVM (rbf)'}
    


    
![png](intl_02_euro_2020_files/intl_02_euro_2020_32_35.png)
    


    
    --------------------
    
    9 models evaluated
    




<style  type="text/css" >
#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row0_col1,#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row3_col1{
            background-color:  #005b25;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row0_col2,#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row3_col2{
            background-color:  #fee8de;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row0_col3,#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row3_col3{
            background-color:  #f14432;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row1_col1{
            background-color:  #278f48;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row1_col2{
            background-color:  #fcb296;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row1_col3{
            background-color:  #8a0812;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row2_col1,#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row4_col1{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row2_col2,#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row2_col3,#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row4_col2{
            background-color:  #fff5f0;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row4_col3{
            background-color:  #fff4ef;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row5_col1{
            background-color:  #e4f5df;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row5_col2{
            background-color:  #a50f15;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row5_col3,#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row6_col2{
            background-color:  #67000d;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row6_col1{
            background-color:  #f7fcf5;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row6_col3{
            background-color:  #aa1016;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row7_col1{
            background-color:  #0d7836;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row7_col2{
            background-color:  #fdcebb;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row7_col3{
            background-color:  #fcc1a8;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row8_col1{
            background-color:  #bce4b5;
            color:  #000000;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row8_col2{
            background-color:  #d21f20;
            color:  #f1f1f1;
        }#T_2aafc67a_bfd5_11eb_a608_74d83eb26131row8_col3{
            background-color:  #fca082;
            color:  #000000;
        }</style><table id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Name</th>        <th class="col_heading level0 col1" >R^2</th>        <th class="col_heading level0 col2" >RMSE</th>        <th class="col_heading level0 col3" >MedAE</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row0_col0" class="data row0 col0" >Dummy (mean)</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row0_col1" class="data row0 col1" >-0.034411</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row0_col2" class="data row0 col2" >2.126936</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row0_col3" class="data row0 col3" >1.767241</td>
            </tr>
            <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row1_col0" class="data row1 col0" >Dummy (median)</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row1_col1" class="data row1 col1" >-0.088091</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row1_col2" class="data row1 col2" >2.181426</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row1_col3" class="data row1 col3" >2.000000</td>
            </tr>
            <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row2_col0" class="data row2 col0" >Linear Reg</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row2_col1" class="data row2 col1" >-0.015106</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row2_col2" class="data row2 col2" >2.106995</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row2_col3" class="data row2 col3" >1.340872</td>
            </tr>
            <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row3_col0" class="data row3 col0" >Lasso</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row3_col1" class="data row3 col1" >-0.034411</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row3_col2" class="data row3 col2" >2.126936</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row3_col3" class="data row3 col3" >1.767241</td>
            </tr>
            <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row4_col0" class="data row4 col0" >Ridge</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row4_col1" class="data row4 col1" >-0.014867</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row4_col2" class="data row4 col2" >2.106747</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row4_col3" class="data row4 col3" >1.345676</td>
            </tr>
            <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row5_col0" class="data row5 col0" >Random Forest</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row5_col1" class="data row5 col1" >-0.253108</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row5_col2" class="data row5 col2" >2.341004</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row5_col3" class="data row5 col3" >2.050000</td>
            </tr>
            <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row6_col0" class="data row6 col0" >Gradient Boost</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row6_col1" class="data row6 col1" >-0.289272</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row6_col2" class="data row6 col2" >2.374544</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row6_col3" class="data row6 col3" >1.948345</td>
            </tr>
            <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row7" class="row_heading level0 row7" >7</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row7_col0" class="data row7 col0" >SVM (linear)</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row7_col1" class="data row7 col1" >-0.062939</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row7_col2" class="data row7 col2" >2.156066</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row7_col3" class="data row7 col3" >1.505401</td>
            </tr>
            <tr>
                        <th id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131level0_row8" class="row_heading level0 row8" >8</th>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row8_col0" class="data row8 col0" >SVM (rbf)</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row8_col1" class="data row8 col1" >-0.210575</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row8_col2" class="data row8 col2" >2.300932</td>
                        <td id="T_2aafc67a_bfd5_11eb_a608_74d83eb26131row8_col3" class="data row8 col3" >1.577091</td>
            </tr>
    </tbody></table>






<style  type="text/css" >
#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row0_col1,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row3_col1{
            background-color:  #005020;
            color:  #f1f1f1;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row0_col2,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row3_col2{
            background-color:  #ffeee7;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row0_col3,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row1_col2,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row3_col3{
            background-color:  #fff5f0;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row1_col1{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row1_col3,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row7_col3{
            background-color:  #f03f2e;
            color:  #f1f1f1;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row2_col1{
            background-color:  #95d391;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row2_col2{
            background-color:  #f0402f;
            color:  #f1f1f1;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row2_col3,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row4_col3{
            background-color:  #fc997a;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row4_col1,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row5_col1{
            background-color:  #94d390;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row4_col2,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row5_col2{
            background-color:  #f14130;
            color:  #f1f1f1;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row5_col3{
            background-color:  #e22e27;
            color:  #f1f1f1;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row6_col1{
            background-color:  #f7fcf5;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row6_col2,#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row6_col3{
            background-color:  #67000d;
            color:  #f1f1f1;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row7_col1{
            background-color:  #48ae60;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row7_col2{
            background-color:  #fc8666;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row8_col1{
            background-color:  #218944;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row8_col2{
            background-color:  #fcb89e;
            color:  #000000;
        }#T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row8_col3{
            background-color:  #fb7858;
            color:  #000000;
        }</style><table id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Name</th>        <th class="col_heading level0 col1" >R^2</th>        <th class="col_heading level0 col2" >RMSE</th>        <th class="col_heading level0 col3" >MedAE</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row0_col0" class="data row0 col0" >Dummy (mean)</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row0_col1" class="data row0 col1" >-0.056966</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row0_col2" class="data row0 col2" >1.373939</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row0_col3" class="data row0 col3" >0.594828</td>
            </tr>
            <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row1_col0" class="data row1 col0" >Dummy (median)</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row1_col1" class="data row1 col1" >-0.042610</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row1_col2" class="data row1 col2" >1.364576</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row1_col3" class="data row1 col3" >1.000000</td>
            </tr>
            <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row2_col0" class="data row2 col0" >Linear Reg</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row2_col1" class="data row2 col1" >-0.273055</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row2_col2" class="data row2 col2" >1.507859</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row2_col3" class="data row2 col3" >0.828096</td>
            </tr>
            <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row3_col0" class="data row3 col0" >Lasso</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row3_col1" class="data row3 col1" >-0.056966</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row3_col2" class="data row3 col2" >1.373939</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row3_col3" class="data row3 col3" >0.594828</td>
            </tr>
            <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row4_col0" class="data row4 col0" >Ridge</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row4_col1" class="data row4 col1" >-0.271381</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row4_col2" class="data row4 col2" >1.506867</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row4_col3" class="data row4 col3" >0.826529</td>
            </tr>
            <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row5_col0" class="data row5 col0" >Random Forest</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row5_col1" class="data row5 col1" >-0.271528</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row5_col2" class="data row5 col2" >1.506954</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row5_col3" class="data row5 col3" >1.035000</td>
            </tr>
            <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row6_col0" class="data row6 col0" >Gradient Boost</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row6_col1" class="data row6 col1" >-0.431096</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row6_col2" class="data row6 col2" >1.598716</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row6_col3" class="data row6 col3" >1.253376</td>
            </tr>
            <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row7" class="row_heading level0 row7" >7</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row7_col0" class="data row7 col0" >SVM (linear)</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row7_col1" class="data row7 col1" >-0.195202</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row7_col2" class="data row7 col2" >1.461025</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row7_col3" class="data row7 col3" >1.001224</td>
            </tr>
            <tr>
                        <th id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131level0_row8" class="row_heading level0 row8" >8</th>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row8_col0" class="data row8 col0" >SVM (rbf)</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row8_col1" class="data row8 col1" >-0.137220</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row8_col2" class="data row8 col2" >1.425146</td>
                        <td id="T_2ab3e3e2_bfd5_11eb_956a_74d83eb26131row8_col3" class="data row8 col3" >0.893410</td>
            </tr>
    </tbody></table>






    (Pipeline(steps=[('standardizer', StandardScaler()),
                     ('estimator', LinearRegression())]),
     Pipeline(steps=[('standardizer', StandardScaler()), ('estimator', Lasso())]))



## 6. Deployment

* Plan Deployment
* Plan Monitoring and Maintenance
* Produce Final Report
* Review Project




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
      <td>173</td>
      <td>104</td>
      <td>2021-06-21</td>
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
      <td>173</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2010.36</td>
      <td>7.07837</td>
      <td>2000</td>
      <td>2004</td>
      <td>2012</td>
      <td>2016</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>Team_1</th>
      <td>173</td>
      <td>30</td>
      <td>Germany</td>
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
      <th>Team_2</th>
      <td>173</td>
      <td>30</td>
      <td>France</td>
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
      <td>173</td>
      <td>2</td>
      <td>Model</td>
      <td>145</td>
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
      <td>145</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.42069</td>
      <td>1.35231</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Actual_score_2</th>
      <td>145</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.11034</td>
      <td>0.972663</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Actual_goal_diff</th>
      <td>145</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.310345</td>
      <td>1.75799</td>
      <td>-4</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Actual_goal_total</th>
      <td>145</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.53103</td>
      <td>1.56815</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Actual_result</th>
      <td>145</td>
      <td>3</td>
      <td>Win</td>
      <td>60</td>
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
      <td>173</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.21965</td>
      <td>0.428987</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Predicted_score_2</th>
      <td>173</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.976879</td>
      <td>0.240004</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Predicted_goal_diff</th>
      <td>173</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.242775</td>
      <td>0.569595</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Predicted_goal_total</th>
      <td>173</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.19653</td>
      <td>0.398529</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Predicted_result</th>
      <td>173</td>
      <td>3</td>
      <td>Draw</td>
      <td>133</td>
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
      <td>145</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.234483</td>
      <td>0.425144</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Correct_goal_diff</th>
      <td>145</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.172414</td>
      <td>0.379049</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Correct_score</th>
      <td>145</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0896552</td>
      <td>0.286677</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Points</th>
      <td>145</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.496552</td>
      <td>0.979825</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
      <th>Goals per game</th>
      <th>Goals per game (actual)</th>
      <th>% games won</th>
      <th>% games won (actual)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>28</td>
      <td>0.21</td>
      <td>11%</td>
      <td>7%</td>
      <td>4%</td>
      <td>2.07</td>
      <td>2.75</td>
      <td>21%</td>
      <td>86%</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>27</td>
      <td>0.89</td>
      <td>41%</td>
      <td>33%</td>
      <td>15%</td>
      <td>2.26</td>
      <td>2.41</td>
      <td>26%</td>
      <td>70%</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>31</td>
      <td>0.35</td>
      <td>23%</td>
      <td>10%</td>
      <td>3%</td>
      <td>2.29</td>
      <td>2.61</td>
      <td>28%</td>
      <td>87%</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>24</td>
      <td>0.42</td>
      <td>17%</td>
      <td>12%</td>
      <td>12%</td>
      <td>2.12</td>
      <td>2.50</td>
      <td>12%</td>
      <td>83%</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>35</td>
      <td>0.60</td>
      <td>26%</td>
      <td>23%</td>
      <td>11%</td>
      <td>2.20</td>
      <td>2.40</td>
      <td>26%</td>
      <td>77%</td>
    </tr>
    <tr>
      <th>Overall</th>
      <td>145</td>
      <td>0.50</td>
      <td>23%</td>
      <td>17%</td>
      <td>9%</td>
      <td>2.19</td>
      <td>2.53</td>
      <td>23%</td>
      <td>81%</td>
    </tr>
  </tbody>
</table>
</div>


