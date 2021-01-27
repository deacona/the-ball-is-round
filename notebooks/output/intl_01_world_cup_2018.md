# International data - World Cup 2018 predictions

Ported from Excel - see original [here](models/World cup 2018 CALC.xlsx)

### 1. Input data on team fixtures and performance




    ['Russia']



    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 64 entries, 1 to 88
    Data columns (total 4 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   Date    64 non-null     object
     1   Time    64 non-null     object
     2   Team1   64 non-null     object
     3   Team2   64 non-null     object
    dtypes: object(4)
    memory usage: 2.5+ KB
    




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
      <th>Date</th>
      <th>Time</th>
      <th>Team1</th>
      <th>Team2</th>
      <th>HomeAdv1</th>
      <th>HomeAdv2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Thursday, Jun 14 2018</td>
      <td>16:00</td>
      <td>Russia</td>
      <td>Saudi Arabia</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Friday, Jun 15 2018</td>
      <td>13:00</td>
      <td>Egypt</td>
      <td>Uruguay</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Friday, Jun 15 2018</td>
      <td>16:00</td>
      <td>Morocco</td>
      <td>Iran</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Friday, Jun 15 2018</td>
      <td>19:00</td>
      <td>Portugal</td>
      <td>Spain</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Saturday, Jun 16 2018</td>
      <td>11:00</td>
      <td>France</td>
      <td>Australia</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 100 entries, 0 to 99
    Data columns (total 4 columns):
     #   Column     Non-Null Count  Dtype 
    ---  ------     --------------  ----- 
     0   Team       100 non-null    object
     1   EloRank    100 non-null    int64 
     2   EloRating  100 non-null    int64 
     3   FIFARank   100 non-null    object
    dtypes: int64(2), object(2)
    memory usage: 3.2+ KB
    




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
      <th>Team</th>
      <th>EloRank</th>
      <th>EloRating</th>
      <th>FIFARank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Brazil</td>
      <td>1</td>
      <td>2131</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Germany</td>
      <td>2</td>
      <td>2092</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>3</td>
      <td>2049</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>France</td>
      <td>4</td>
      <td>1987</td>
      <td>7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Argentina</td>
      <td>5</td>
      <td>1985</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 32 entries, 0 to 31
    Data columns (total 2 columns):
     #   Column            Non-Null Count  Dtype 
    ---  ------            --------------  ----- 
     0   Team              32 non-null     object
     1   QualifyGoalsRank  32 non-null     int64 
    dtypes: int64(1), object(1)
    memory usage: 640.0+ bytes
    




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
      <th>Team</th>
      <th>QualifyGoalsRank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Russia</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Saudi Arabia</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Egypt</td>
      <td>26</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Uruguay</td>
      <td>11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Portugal</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 64 entries, 0 to 63
    Data columns (total 14 columns):
     #   Column             Non-Null Count  Dtype 
    ---  ------             --------------  ----- 
     0   Date               64 non-null     object
     1   Time               64 non-null     object
     2   Team1              64 non-null     object
     3   Team2              64 non-null     object
     4   HomeAdv1           64 non-null     int64 
     5   HomeAdv2           64 non-null     int64 
     6   EloRank1           64 non-null     int64 
     7   EloRating1         64 non-null     int64 
     8   FIFARank1          64 non-null     object
     9   EloRank2           64 non-null     int64 
     10  EloRating2         64 non-null     int64 
     11  FIFARank2          64 non-null     object
     12  QualifyGoalsRank1  64 non-null     int64 
     13  QualifyGoalsRank2  64 non-null     int64 
    dtypes: int64(8), object(6)
    memory usage: 7.5+ KB
    

### 2. Build model and make predictions




    (4.0, 19.0)






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
      <td>64</td>
      <td>25</td>
      <td>Monday, Jun 25 2018</td>
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
      <td>64</td>
      <td>8</td>
      <td>19:00</td>
      <td>25</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Team1</th>
      <td>64</td>
      <td>32</td>
      <td>France</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Team2</th>
      <td>64</td>
      <td>32</td>
      <td>England</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>HomeAdv1</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.046875</td>
      <td>0.213042</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>HomeAdv2</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.03125</td>
      <td>0.175368</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>EloRank1</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19.1562</td>
      <td>15.9187</td>
      <td>1</td>
      <td>6</td>
      <td>16.5</td>
      <td>27</td>
      <td>63</td>
    </tr>
    <tr>
      <th>EloRating1</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1864.58</td>
      <td>137.747</td>
      <td>1597</td>
      <td>1751</td>
      <td>1855</td>
      <td>1967</td>
      <td>2131</td>
    </tr>
    <tr>
      <th>FIFARank1</th>
      <td>64</td>
      <td>32</td>
      <td>7</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>EloRank2</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22.5625</td>
      <td>16.9742</td>
      <td>1</td>
      <td>8</td>
      <td>17</td>
      <td>40</td>
      <td>63</td>
    </tr>
    <tr>
      <th>EloRating2</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1832.72</td>
      <td>127.319</td>
      <td>1597</td>
      <td>1714</td>
      <td>1853</td>
      <td>1935</td>
      <td>2131</td>
    </tr>
    <tr>
      <th>FIFARank2</th>
      <td>64</td>
      <td>32</td>
      <td>13</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>QualifyGoalsRank1</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.7031</td>
      <td>8.78975</td>
      <td>1</td>
      <td>8</td>
      <td>14.5</td>
      <td>21.25</td>
      <td>31</td>
    </tr>
    <tr>
      <th>QualifyGoalsRank2</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17.25</td>
      <td>9.12871</td>
      <td>1</td>
      <td>9.5</td>
      <td>17.5</td>
      <td>26</td>
      <td>31</td>
    </tr>
    <tr>
      <th>EloRatingDiff</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>31.8594</td>
      <td>189.312</td>
      <td>-361</td>
      <td>-98</td>
      <td>11</td>
      <td>201.5</td>
      <td>386</td>
    </tr>
    <tr>
      <th>EloRatingDiffWithHomeAdv</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>33.4219</td>
      <td>186.007</td>
      <td>-361</td>
      <td>-94.5</td>
      <td>11</td>
      <td>198.5</td>
      <td>386</td>
    </tr>
    <tr>
      <th>WinExpectency1Square</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.42217</td>
      <td>1.63615</td>
      <td>1.10839</td>
      <td>1.31897</td>
      <td>1.93866</td>
      <td>2.72288</td>
      <td>8.98914</td>
    </tr>
    <tr>
      <th>WinExpectency1</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.539381</td>
      <td>0.226661</td>
      <td>0.111245</td>
      <td>0.367262</td>
      <td>0.515825</td>
      <td>0.758166</td>
      <td>0.902207</td>
    </tr>
    <tr>
      <th>RawGoalDiff</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.109375</td>
      <td>0.892956</td>
      <td>-2</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>RawGoalDiffAbs</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.703125</td>
      <td>0.554339</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>EitherWins</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.65625</td>
      <td>0.478714</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>QualifyGoalsRankAvg</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.9766</td>
      <td>6.27633</td>
      <td>4.5</td>
      <td>11.375</td>
      <td>15.25</td>
      <td>21</td>
      <td>28.5</td>
    </tr>
    <tr>
      <th>ApplyGoalBoost</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.703125</td>
      <td>0.460493</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Goals1</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.10938</td>
      <td>0.715302</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Goals2</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>0.734631</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>GoalDiff</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.109375</td>
      <td>0.892956</td>
      <td>-2</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>GoalDiffAbs</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.703125</td>
      <td>0.554339</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>GoalTotal</th>
      <td>64</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.10938</td>
      <td>1.1425</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### 3. Evaluate predictions against historic trends

                         Historic Predictions     %Diff
    % games 0 goals         0.082       0.125     0.344
    % games 1 goals         0.205    0.171875 -0.192727
    % games 2 goals         0.257     0.21875 -0.174857
    % games 3 goals         0.213      0.4375  0.513143
    % games 4 goals         0.133    0.046875  -1.83733
    % games 5 goals         0.067           0         1
    % games 6 goals         0.028           0         1
    % games 7 goals          0.01           0         1
    AverageGoalsPerGame       2.5     2.10938 -0.185185
    % games drawn        0.221751     0.34375  0.354905
    % games won          0.778249     0.65625 -0.185903
    

### 4. Compare predictions to actual results




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
      <th>Date</th>
      <th>Time</th>
      <th>Team1</th>
      <th>Team2</th>
      <th>Actual1</th>
      <th>Actual2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Thursday, Jun 14 2018</td>
      <td>16:00</td>
      <td>Russia</td>
      <td>Saudi Arabia</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Friday, Jun 15 2018</td>
      <td>13:00</td>
      <td>Egypt</td>
      <td>Uruguay</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Friday, Jun 15 2018</td>
      <td>16:00</td>
      <td>Morocco</td>
      <td>Iran</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Friday, Jun 15 2018</td>
      <td>19:00</td>
      <td>Portugal</td>
      <td>Spain</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Saturday, Jun 16 2018</td>
      <td>11:00</td>
      <td>France</td>
      <td>Australia</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



                     Predictions  Maximum  % of Maximum
    CorrectResult             34       64      0.531250
    CorrectGoalDiff           21       64      0.328125
    CorrectScore               5       64      0.078125
    PointsScored              60      192      0.312500
    




    0.3125



### 5. Improve the model?




    99






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
      <th>Parameters</th>
      <th>%PointsScored</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>35</th>
      <td>(4.0, 16.0)</td>
      <td>0.322917</td>
    </tr>
    <tr>
      <th>43</th>
      <td>(4.0, 24.0)</td>
      <td>0.322917</td>
    </tr>
    <tr>
      <th>42</th>
      <td>(4.0, 23.0)</td>
      <td>0.322917</td>
    </tr>
    <tr>
      <th>33</th>
      <td>(4.0, 14.0)</td>
      <td>0.322917</td>
    </tr>
    <tr>
      <th>34</th>
      <td>(4.0, 15.0)</td>
      <td>0.322917</td>
    </tr>
    <tr>
      <th>41</th>
      <td>(4.0, 22.0)</td>
      <td>0.322917</td>
    </tr>
    <tr>
      <th>36</th>
      <td>(4.0, 17.0)</td>
      <td>0.317708</td>
    </tr>
    <tr>
      <th>40</th>
      <td>(4.0, 21.0)</td>
      <td>0.317708</td>
    </tr>
    <tr>
      <th>37</th>
      <td>(4.0, 18.0)</td>
      <td>0.317708</td>
    </tr>
    <tr>
      <th>39</th>
      <td>(4.0, 20.0)</td>
      <td>0.317708</td>
    </tr>
  </tbody>
</table>
</div>



                         Historic Predictions     %Diff
    % games 0 goals         0.082    0.140625  0.416889
    % games 1 goals         0.205    0.265625  0.228235
    % games 2 goals         0.257     0.21875 -0.174857
    % games 3 goals         0.213     0.34375  0.380364
    % games 4 goals         0.133     0.03125    -3.256
    % games 5 goals         0.067           0         1
    % games 6 goals         0.028           0         1
    % games 7 goals          0.01           0         1
    AverageGoalsPerGame       2.5     1.85938 -0.344538
    % games drawn        0.221751     0.34375  0.354905
    % games won          0.778249     0.65625 -0.185903
                     Predictions  Maximum  % of Maximum
    CorrectResult             34       64      0.531250
    CorrectGoalDiff           21       64      0.328125
    CorrectScore               7       64      0.109375
    PointsScored              62      192      0.322917
    




    0.3229166666666667


