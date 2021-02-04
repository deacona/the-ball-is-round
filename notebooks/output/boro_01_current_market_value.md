# Boro Player Predictions - Current Market Value

Written report for this analysis can be found [here](../reports/boro_01_market_value.md)

## 1. Business Understanding

* Determine Busines Objectives
* Situation Assessment
* Determine Data Mining Goal
* Produce Project Plan

The aim of this project is to see if we can use data on players at Middlesbrough Football Club to make preditions about the player's and the team's current and future performance.

We have player data from Transfermarkt, ESPN, WhoScored and Fly Me To The Moon (fanzine).

"Performance" could be measured in many different ways: Results on the pitch, market value, fan popularity, churn, ...

A number of key performance metrics will be investigated in turn, looking at how predictable each is...

1) Current market value

2) Current fan popularity

3) Current performance rating

... and more TBC ...


## 2. Data Understanding

* Collect Initial Data
* Describe Data
* Explore Data
* Verify Data Quality

    Loading Transfermarkt general information...
    tmk_cnt_mbr_all_0910.csv
    tmk_cnt_mbr_all_1011.csv
    tmk_cnt_mbr_all_1112.csv
    tmk_cnt_mbr_all_1213.csv
    tmk_cnt_mbr_all_1314.csv
    tmk_cnt_mbr_all_1415.csv
    tmk_cnt_mbr_all_1516.csv
    tmk_cnt_mbr_all_1617.csv
    tmk_cnt_mbr_all_1718.csv
    tmk_cnt_mbr_all_1819.csv
    tmk_cnt_mbr_all_1920.csv
    

    Random sample of records...
    




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
      <th>Shirt number</th>
      <th>Position</th>
      <th>Name</th>
      <th>Date of birth</th>
      <th>Height</th>
      <th>Foot</th>
      <th>Joined</th>
      <th>Contract expires</th>
      <th>Market value</th>
      <th>Season</th>
      <th>Position group</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>547</th>
      <td>6.0</td>
      <td>Centre-Back</td>
      <td>Ben Gibson</td>
      <td>1993-01-15</td>
      <td>185.0</td>
      <td>left</td>
      <td>2011-07-01</td>
      <td>2021-06-30</td>
      <td>510.000</td>
      <td>16/17</td>
      <td>D</td>
      <td>24</td>
    </tr>
    <tr>
      <th>424</th>
      <td>3.0</td>
      <td>Left-Back</td>
      <td>George Friend</td>
      <td>1987-10-19</td>
      <td>188.0</td>
      <td>left</td>
      <td>2012-07-30</td>
      <td>2018-06-30</td>
      <td>0.975</td>
      <td>14/15</td>
      <td>D</td>
      <td>26</td>
    </tr>
    <tr>
      <th>643</th>
      <td>NaN</td>
      <td>Central Midfield</td>
      <td>Grant Leadbitter</td>
      <td>1986-01-07</td>
      <td>177.0</td>
      <td>right</td>
      <td>2012-07-01</td>
      <td>2018-06-30</td>
      <td>180.000</td>
      <td>17/18</td>
      <td>M</td>
      <td>32</td>
    </tr>
    <tr>
      <th>28</th>
      <td>NaN</td>
      <td>Left-Back</td>
      <td>Andrew Taylor</td>
      <td>1986-08-01</td>
      <td>178.0</td>
      <td>left</td>
      <td>2005-07-01</td>
      <td>NaT</td>
      <td>188.000</td>
      <td>09/10</td>
      <td>D</td>
      <td>22</td>
    </tr>
    <tr>
      <th>711</th>
      <td>NaN</td>
      <td>Centre-Forward</td>
      <td>Britt Assombalonga</td>
      <td>1992-12-06</td>
      <td>177.0</td>
      <td>NaN</td>
      <td>2017-07-17</td>
      <td>2021-06-30</td>
      <td>900.000</td>
      <td>18/19</td>
      <td>F</td>
      <td>26</td>
    </tr>
    <tr>
      <th>48</th>
      <td>NaN</td>
      <td>Defensive Midfield</td>
      <td>Isaiah Osbourne</td>
      <td>1987-11-05</td>
      <td>188.0</td>
      <td>right</td>
      <td>2009-11-06</td>
      <td>NaT</td>
      <td>0.375</td>
      <td>09/10</td>
      <td>M</td>
      <td>21</td>
    </tr>
    <tr>
      <th>677</th>
      <td>NaN</td>
      <td>Left-Back</td>
      <td>George Friend</td>
      <td>1987-10-19</td>
      <td>188.0</td>
      <td>left</td>
      <td>2012-07-30</td>
      <td>2020-06-30</td>
      <td>135.000</td>
      <td>18/19</td>
      <td>D</td>
      <td>31</td>
    </tr>
    <tr>
      <th>168</th>
      <td>NaN</td>
      <td>Centre Forward</td>
      <td>Leroy Lita</td>
      <td>1984-12-28</td>
      <td>176.0</td>
      <td>right</td>
      <td>2009-07-01</td>
      <td>NaT</td>
      <td>150.000</td>
      <td>10/11</td>
      <td>F</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



    Summary of whole data source...
    

    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\ipykernel_launcher.py:3: FutureWarning: Treating datetime data as categorical rather than numeric in `.describe` is deprecated and will be removed in a future version of pandas. Specify `datetime_is_numeric=True` to silence this warning and adopt the future behavior now.
      This is separate from the ipykernel package so we can avoid doing imports until
    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\ipykernel_launcher.py:3: FutureWarning: Treating datetime data as categorical rather than numeric in `.describe` is deprecated and will be removed in a future version of pandas. Specify `datetime_is_numeric=True` to silence this warning and adopt the future behavior now.
      This is separate from the ipykernel package so we can avoid doing imports until
    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\ipykernel_launcher.py:3: FutureWarning: Treating datetime data as categorical rather than numeric in `.describe` is deprecated and will be removed in a future version of pandas. Specify `datetime_is_numeric=True` to silence this warning and adopt the future behavior now.
      This is separate from the ipykernel package so we can avoid doing imports until
    




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
      <th>Shirt number</th>
      <th>Position</th>
      <th>Name</th>
      <th>Date of birth</th>
      <th>Height</th>
      <th>Foot</th>
      <th>Joined</th>
      <th>Contract expires</th>
      <th>Market value</th>
      <th>Season</th>
      <th>Position group</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>119.000</td>
      <td>362</td>
      <td>362</td>
      <td>362</td>
      <td>354.000</td>
      <td>322</td>
      <td>349</td>
      <td>167</td>
      <td>328.000</td>
      <td>362</td>
      <td>362</td>
      <td>362.000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>19</td>
      <td>171</td>
      <td>169</td>
      <td>NaN</td>
      <td>3</td>
      <td>126</td>
      <td>11</td>
      <td>NaN</td>
      <td>11</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>Centre Back</td>
      <td>Ben Gibson</td>
      <td>1993-01-15 00:00:00</td>
      <td>NaN</td>
      <td>right</td>
      <td>2010-07-01 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>NaN</td>
      <td>09/10</td>
      <td>M</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>53</td>
      <td>9</td>
      <td>9</td>
      <td>NaN</td>
      <td>199</td>
      <td>31</td>
      <td>27</td>
      <td>NaN</td>
      <td>47</td>
      <td>133</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>first</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1973-08-27 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2000-07-01 00:00:00</td>
      <td>2016-05-31 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>last</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2000-10-11 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2020-07-31 00:00:00</td>
      <td>2023-06-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>17.345</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>183.302</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>146.639</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.807</td>
    </tr>
    <tr>
      <th>std</th>
      <td>10.966</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.960</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>191.985</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.706</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>170.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.038</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16.000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>8.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>179.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.375</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21.000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>183.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>113.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>25.000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>188.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>216.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>42.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>199.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1080.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.000</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** So the data is looking broadly in good shape, but there are a few missing values to consider...




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
      <th>% populated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Shirt number</th>
      <td>32.873</td>
    </tr>
    <tr>
      <th>Position</th>
      <td>100.000</td>
    </tr>
    <tr>
      <th>Name</th>
      <td>100.000</td>
    </tr>
    <tr>
      <th>Date of birth</th>
      <td>100.000</td>
    </tr>
    <tr>
      <th>Height</th>
      <td>97.790</td>
    </tr>
    <tr>
      <th>Foot</th>
      <td>88.950</td>
    </tr>
    <tr>
      <th>Joined</th>
      <td>96.409</td>
    </tr>
    <tr>
      <th>Contract expires</th>
      <td>46.133</td>
    </tr>
    <tr>
      <th>Market value</th>
      <td>90.608</td>
    </tr>
    <tr>
      <th>Season</th>
      <td>100.000</td>
    </tr>
    <tr>
      <th>Position group</th>
      <td>100.000</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>100.000</td>
    </tr>
  </tbody>
</table>
</div>



    Players with missing Joined dates...
    




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
      <th>156</th>
      <th>220</th>
      <th>300</th>
      <th>374</th>
      <th>454</th>
      <th>26</th>
      <th>120</th>
      <th>194</th>
      <th>266</th>
      <th>348</th>
      <th>416</th>
      <th>490</th>
      <th>547</th>
      <th>616</th>
      <th>24</th>
      <th>122</th>
      <th>282</th>
      <th>364</th>
      <th>440</th>
      <th>512</th>
      <th>60</th>
      <th>154</th>
      <th>218</th>
      <th>298</th>
      <th>102</th>
      <th>182</th>
      <th>250</th>
      <th>334</th>
      <th>406</th>
      <th>482</th>
      <th>542</th>
      <th>92</th>
      <th>174</th>
      <th>242</th>
      <th>322</th>
      <th>396</th>
      <th>476</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Name</th>
      <td>Adam Reach</td>
      <td>Adam Reach</td>
      <td>Adam Reach</td>
      <td>Adam Reach</td>
      <td>Adam Reach</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Bruno Pilatos</td>
      <td>Bruno Pilatos</td>
      <td>Bryn Morris</td>
      <td>Bryn Morris</td>
      <td>Bryn Morris</td>
      <td>Bryn Morris</td>
      <td>Cameron Park</td>
      <td>Cameron Park</td>
      <td>Cameron Park</td>
      <td>Cameron Park</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Luke Williams</td>
      <td>Luke Williams</td>
      <td>Luke Williams</td>
      <td>Luke Williams</td>
      <td>Luke Williams</td>
      <td>Luke Williams</td>
    </tr>
    <tr>
      <th>Season</th>
      <td>10/11</td>
      <td>11/12</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>09/10</td>
      <td>10/11</td>
      <td>11/12</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>15/16</td>
      <td>16/17</td>
      <td>17/18</td>
      <td>09/10</td>
      <td>10/11</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>15/16</td>
      <td>09/10</td>
      <td>10/11</td>
      <td>11/12</td>
      <td>12/13</td>
      <td>10/11</td>
      <td>11/12</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>15/16</td>
      <td>16/17</td>
      <td>09/10</td>
      <td>10/11</td>
      <td>11/12</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
    </tr>
    <tr>
      <th>Joined</th>
      <td>NaT</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>NaT</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>NaT</td>
      <td>2010-07-01 00:00:00</td>
      <td>NaT</td>
      <td>2014-01-01 00:00:00</td>
      <td>2014-01-01 00:00:00</td>
      <td>2014-01-01 00:00:00</td>
      <td>NaT</td>
      <td>NaT</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>NaT</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>2011-07-01 00:00:00</td>
      <td>NaT</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
      <td>2010-07-01 00:00:00</td>
    </tr>
  </tbody>
</table>
</div>



    Players with missing Contract expires dates...
    




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
      <th>156</th>
      <th>220</th>
      <th>300</th>
      <th>374</th>
      <th>454</th>
      <th>26</th>
      <th>120</th>
      <th>194</th>
      <th>266</th>
      <th>348</th>
      <th>416</th>
      <th>490</th>
      <th>547</th>
      <th>616</th>
      <th>282</th>
      <th>364</th>
      <th>440</th>
      <th>512</th>
      <th>102</th>
      <th>182</th>
      <th>250</th>
      <th>334</th>
      <th>406</th>
      <th>482</th>
      <th>542</th>
      <th>384</th>
      <th>466</th>
      <th>470</th>
      <th>603</th>
      <th>661</th>
      <th>330</th>
      <th>400</th>
      <th>486</th>
      <th>611</th>
      <th>726</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Name</th>
      <td>Adam Reach</td>
      <td>Adam Reach</td>
      <td>Adam Reach</td>
      <td>Adam Reach</td>
      <td>Adam Reach</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Ben Gibson</td>
      <td>Bryn Morris</td>
      <td>Bryn Morris</td>
      <td>Bryn Morris</td>
      <td>Bryn Morris</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Connor Ripley</td>
      <td>Lee Tomlin</td>
      <td>Lee Tomlin</td>
      <td>Patrick Bamford</td>
      <td>Patrick Bamford</td>
      <td>Patrick Bamford</td>
      <td>Tomás Mejías</td>
      <td>Tomás Mejías</td>
      <td>Tomás Mejías</td>
      <td>Tomás Mejías</td>
      <td>Tomás Mejías</td>
    </tr>
    <tr>
      <th>Season</th>
      <td>10/11</td>
      <td>11/12</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>09/10</td>
      <td>10/11</td>
      <td>11/12</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>15/16</td>
      <td>16/17</td>
      <td>17/18</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>15/16</td>
      <td>10/11</td>
      <td>11/12</td>
      <td>12/13</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>15/16</td>
      <td>16/17</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>14/15</td>
      <td>16/17</td>
      <td>17/18</td>
      <td>13/14</td>
      <td>14/15</td>
      <td>15/16</td>
      <td>17/18</td>
      <td>19/20</td>
    </tr>
    <tr>
      <th>Contract expires</th>
      <td>NaT</td>
      <td>2019-06-30 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>NaT</td>
      <td>2019-06-30 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>2019-06-30 00:00:00</td>
      <td>2021-06-30 00:00:00</td>
      <td>2022-06-30 00:00:00</td>
      <td>NaT</td>
      <td>2016-06-30 00:00:00</td>
      <td>2016-06-30 00:00:00</td>
      <td>2016-06-30 00:00:00</td>
      <td>NaT</td>
      <td>NaT</td>
      <td>NaT</td>
      <td>NaT</td>
      <td>NaT</td>
      <td>2018-06-30 00:00:00</td>
      <td>2018-06-30 00:00:00</td>
      <td>NaT</td>
      <td>2017-06-30 00:00:00</td>
      <td>NaT</td>
      <td>2021-06-30 00:00:00</td>
      <td>2021-06-30 00:00:00</td>
      <td>NaT</td>
      <td>2018-06-30 00:00:00</td>
      <td>2018-06-30 00:00:00</td>
      <td>2018-06-30 00:00:00</td>
      <td>2021-06-30 00:00:00</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** _Possibly_ we could back fill some missing `Joined` and `Contract expires` dates but this might have some undesired consequences because the date _might_ not be valid for that particular season. We'll leave them as Nulls for now.




    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_20_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_21_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_22_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_23_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_24_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_25_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_26_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_27_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_28_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_29_1.png)
    





    Text(0.5, 1.08, 'Pair plots of Shirt number, Height, Market value and Age')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_30_1.png)
    





    Text(0.5, 1.08, 'Pair plots of Shirt number, Height, Market value and Age grouped by Position group')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_31_1.png)
    


    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\seaborn\distributions.py:305: UserWarning: Dataset has 0 variance; skipping density estimate.
      warnings.warn(msg, UserWarning)
    




    Text(0.5, 1.08, 'Pair plots of Shirt number, Height, Market value and Age grouped by Foot')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_32_2.png)
    


    Loading Transfermarkt performance summary...
    tmk_psm_mbr_chm_0910.csv
    tmk_psm_mbr_chm_1011.csv
    tmk_psm_mbr_chm_1112.csv
    tmk_psm_mbr_chm_1213.csv
    tmk_psm_mbr_chm_1314.csv
    tmk_psm_mbr_chm_1415.csv
    tmk_psm_mbr_chm_1516.csv
    tmk_psm_mbr_chm_1718.csv
    tmk_psm_mbr_chm_1819.csv
    tmk_psm_mbr_chm_1920.csv
    tmk_psm_mbr_cpo_1415.csv
    tmk_psm_mbr_cpo_1718.csv
    tmk_psm_mbr_fac_0910.csv
    tmk_psm_mbr_fac_1011.csv
    tmk_psm_mbr_fac_1112.csv
    tmk_psm_mbr_fac_1213.csv
    tmk_psm_mbr_fac_1314.csv
    tmk_psm_mbr_fac_1415.csv
    tmk_psm_mbr_fac_1516.csv
    tmk_psm_mbr_fac_1617.csv
    tmk_psm_mbr_fac_1718.csv
    tmk_psm_mbr_fac_1819.csv
    tmk_psm_mbr_fac_1920.csv
    tmk_psm_mbr_lec_0910.csv
    tmk_psm_mbr_lec_1011.csv
    tmk_psm_mbr_lec_1112.csv
    tmk_psm_mbr_lec_1213.csv
    tmk_psm_mbr_lec_1314.csv
    tmk_psm_mbr_lec_1415.csv
    tmk_psm_mbr_lec_1516.csv
    tmk_psm_mbr_lec_1617.csv
    tmk_psm_mbr_lec_1718.csv
    tmk_psm_mbr_lec_1819.csv
    tmk_psm_mbr_lec_1920.csv
    tmk_psm_mbr_prm_1617.csv
    

    Random sample of records...
    




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
      <th>Shirt number</th>
      <th>Position</th>
      <th>Name</th>
      <th>Age</th>
      <th>In squad</th>
      <th>Games started</th>
      <th>Goals</th>
      <th>Assists</th>
      <th>Yellow cards</th>
      <th>Second yellow cards</th>
      <th>Red cards</th>
      <th>Substitutions on</th>
      <th>Substitutions off</th>
      <th>PPG</th>
      <th>Minutes played</th>
      <th>Season</th>
      <th>Competition</th>
      <th>Position group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>965</th>
      <td>NaN</td>
      <td>Right-Back</td>
      <td>Justin Hoyte</td>
      <td>24.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>90.0</td>
      <td>09/10</td>
      <td>FA Cup</td>
      <td>D</td>
    </tr>
    <tr>
      <th>1922</th>
      <td>NaN</td>
      <td>Right Midfield</td>
      <td>Barry Robson</td>
      <td>31.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>90.0</td>
      <td>10/11</td>
      <td>League Cup</td>
      <td>M</td>
    </tr>
    <tr>
      <th>331</th>
      <td>NaN</td>
      <td>Centre Forward</td>
      <td>Lukas Jutkiewicz</td>
      <td>23.0</td>
      <td>29.0</td>
      <td>24.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>10.0</td>
      <td>1.08</td>
      <td>1527.0</td>
      <td>12/13</td>
      <td>Championship</td>
      <td>F</td>
    </tr>
    <tr>
      <th>1806</th>
      <td>NaN</td>
      <td>Defensive Midfield</td>
      <td>Didier Digard</td>
      <td>22.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>09/10</td>
      <td>League Cup</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1499</th>
      <td>NaN</td>
      <td>Right-Back</td>
      <td>Calum Chambers</td>
      <td>22.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.00</td>
      <td>180.0</td>
      <td>16/17</td>
      <td>FA Cup</td>
      <td>D</td>
    </tr>
    <tr>
      <th>2493</th>
      <td>NaN</td>
      <td>Centre-Back</td>
      <td>Sam Stubbs</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>18/19</td>
      <td>League Cup</td>
      <td>D</td>
    </tr>
    <tr>
      <th>1603</th>
      <td>8.0</td>
      <td>Central Midfield</td>
      <td>Adam Clayton</td>
      <td>29.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.50</td>
      <td>115.0</td>
      <td>17/18</td>
      <td>FA Cup</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2633</th>
      <td>1.0</td>
      <td>Keeper</td>
      <td>Dimitrios Konstantopoulos</td>
      <td>38.0</td>
      <td>15.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.00</td>
      <td>90.0</td>
      <td>16/17</td>
      <td>Premier League</td>
      <td>G</td>
    </tr>
  </tbody>
</table>
</div>



    Summary of whole data source...
    




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
      <th>Shirt number</th>
      <th>Position</th>
      <th>Name</th>
      <th>Age</th>
      <th>In squad</th>
      <th>Games started</th>
      <th>Goals</th>
      <th>Assists</th>
      <th>Yellow cards</th>
      <th>Second yellow cards</th>
      <th>Red cards</th>
      <th>Substitutions on</th>
      <th>Substitutions off</th>
      <th>PPG</th>
      <th>Minutes played</th>
      <th>Season</th>
      <th>Competition</th>
      <th>Position group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>526.000</td>
      <td>1263</td>
      <td>1263</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263.000</td>
      <td>1263</td>
      <td>1263</td>
      <td>1263</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>20</td>
      <td>200</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>Centre Back</td>
      <td>Ben Gibson</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14/15</td>
      <td>League Cup</td>
      <td>M</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>176</td>
      <td>29</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>160</td>
      <td>403</td>
      <td>465</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>17.101</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.689</td>
      <td>7.289</td>
      <td>6.070</td>
      <td>0.553</td>
      <td>0.426</td>
      <td>0.716</td>
      <td>0.019</td>
      <td>0.020</td>
      <td>1.184</td>
      <td>1.184</td>
      <td>0.870</td>
      <td>440.517</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>10.939</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.686</td>
      <td>12.462</td>
      <td>11.112</td>
      <td>1.717</td>
      <td>1.259</td>
      <td>1.859</td>
      <td>0.148</td>
      <td>0.145</td>
      <td>2.813</td>
      <td>2.868</td>
      <td>1.027</td>
      <td>859.479</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.250</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.000</td>
      <td>2.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>90.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.000</td>
      <td>5.000</td>
      <td>4.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.560</td>
      <td>270.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>42.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.000</td>
      <td>46.000</td>
      <td>46.000</td>
      <td>17.000</td>
      <td>11.000</td>
      <td>13.000</td>
      <td>2.000</td>
      <td>2.000</td>
      <td>20.000</td>
      <td>23.000</td>
      <td>3.000</td>
      <td>4140.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** So the data is looking broadly in good shape




    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_40_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_41_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_42_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_43_1.png)
    





    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_44_1.png)
    





    Text(0.5, 1.08, 'Pair plots of usage, goals, assists, yellow cards, PPG')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_45_1.png)
    


    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\seaborn\distributions.py:305: UserWarning: Dataset has 0 variance; skipping density estimate.
      warnings.warn(msg, UserWarning)
    




    Text(0.5, 1.08, 'Pair plots of usage, goals, assists, yellow cards, PPG by Position group')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_46_2.png)
    





    Text(0.5, 1.08, 'Pair plots of usage, goals, assists, yellow cards, PPG by Competition')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_47_1.png)
    


## 3. Data Preperation

* Select Data
* Clean Data
* Construct Data
* Integrate Data
* Format Data

    Final dataset created with index from Brad Jones (09/10) to Rudy Gestede (19/20).
    




    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_52_1.png)
    


**ANALYSIS:** Most players join in their teens or mid-twenties.




    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_54_1.png)
    


**ANALYSIS:** I'm going to leave out `Position`, `Date of birth`, `Joined`, and `Contract expires` from the model for now. `Contract expires` is populated in less than half of records. The others are encoded in derived features now.

<s>**ANALYSIS:** `Foot` and `Position group` will be one-hot encoded</s>




    Index(['Shirt number', 'Position', 'Name', 'Age', 'In squad', 'Games started',
           'Goals', 'Assists', 'Yellow cards', 'Second yellow cards', 'Red cards',
           'Substitutions on', 'Substitutions off', 'PPG', 'Minutes played',
           'Season', 'Competition', 'Position group'],
          dtype='object')



    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\ipykernel_launcher.py:24: RuntimeWarning: invalid value encountered in double_scalars
    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\ipykernel_launcher.py:26: RuntimeWarning: invalid value encountered in double_scalars
    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\ipykernel_launcher.py:27: RuntimeWarning: invalid value encountered in double_scalars
    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\ipykernel_launcher.py:28: RuntimeWarning: invalid value encountered in double_scalars
    

    Random sample of records...
    




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
      <th>Age</th>
      <th>Age when joined</th>
      <th>Appearances</th>
      <th>Assists</th>
      <th>Assists p90</th>
      <th>Competition</th>
      <th>Foot</th>
      <th>Games started</th>
      <th>Goals</th>
      <th>Goals p90</th>
      <th>Height</th>
      <th>In squad</th>
      <th>Market value</th>
      <th>Minutes played</th>
      <th>PPG</th>
      <th>Position group</th>
      <th>Red cards</th>
      <th>Second yellow cards</th>
      <th>Shirt number</th>
      <th>Substitutions off</th>
      <th>Substitutions on</th>
      <th>Years in team</th>
      <th>Yellow cards</th>
      <th>Yellow cards p90</th>
    </tr>
    <tr>
      <th>Player key</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Barry Robson (11/12)</th>
      <td>32.0</td>
      <td>31.152</td>
      <td>39.0</td>
      <td>10.0</td>
      <td>0.272</td>
      <td>Championship, FA Cup, League Cup</td>
      <td>left</td>
      <td>39.0</td>
      <td>9.0</td>
      <td>0.244</td>
      <td>180.0</td>
      <td>39.0</td>
      <td>113.00</td>
      <td>3314.0</td>
      <td>1.592</td>
      <td>M</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>2.497</td>
      <td>13.0</td>
      <td>0.353</td>
    </tr>
    <tr>
      <th>Adam Jackson (13/14)</th>
      <td>19.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>Championship</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>D</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>Stewart Downing (17/18)</th>
      <td>33.0</td>
      <td>30.982</td>
      <td>53.0</td>
      <td>7.0</td>
      <td>0.174</td>
      <td>Championship, Championship Playoffs, FA Cup, L...</td>
      <td>left</td>
      <td>47.0</td>
      <td>3.0</td>
      <td>0.075</td>
      <td>180.0</td>
      <td>47.0</td>
      <td>225.00</td>
      <td>3616.0</td>
      <td>1.701</td>
      <td>M</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>19.0</td>
      <td>19.0</td>
      <td>6.0</td>
      <td>2.960</td>
      <td>1.0</td>
      <td>0.025</td>
    </tr>
    <tr>
      <th>Marvin Johnson (17/18)</th>
      <td>27.0</td>
      <td>26.749</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>0.243</td>
      <td>Championship, Championship Playoffs, FA Cup, L...</td>
      <td>left</td>
      <td>18.0</td>
      <td>1.0</td>
      <td>0.121</td>
      <td>178.0</td>
      <td>25.0</td>
      <td>180.00</td>
      <td>741.0</td>
      <td>1.684</td>
      <td>M</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>21.0</td>
      <td>2.0</td>
      <td>12.0</td>
      <td>0.832</td>
      <td>0.0</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>Sean St. Ledger (09/10)</th>
      <td>24.0</td>
      <td>24.715</td>
      <td>16.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>Championship, FA Cup, League Cup</td>
      <td>right</td>
      <td>15.0</td>
      <td>2.0</td>
      <td>0.142</td>
      <td>182.0</td>
      <td>15.0</td>
      <td>0.75</td>
      <td>1268.0</td>
      <td>1.070</td>
      <td>D</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.791</td>
      <td>0.0</td>
      <td>0.000</td>
    </tr>
  </tbody>
</table>
</div>



    Summary of whole dataset...
    




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
      <th>Age</th>
      <th>Age when joined</th>
      <th>Appearances</th>
      <th>Assists</th>
      <th>Assists p90</th>
      <th>Competition</th>
      <th>Foot</th>
      <th>Games started</th>
      <th>Goals</th>
      <th>Goals p90</th>
      <th>Height</th>
      <th>In squad</th>
      <th>Market value</th>
      <th>Minutes played</th>
      <th>PPG</th>
      <th>Position group</th>
      <th>Red cards</th>
      <th>Second yellow cards</th>
      <th>Shirt number</th>
      <th>Substitutions off</th>
      <th>Substitutions on</th>
      <th>Years in team</th>
      <th>Yellow cards</th>
      <th>Yellow cards p90</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>444.000</td>
      <td>349.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444</td>
      <td>322</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>354.000</td>
      <td>444.000</td>
      <td>328.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>349.000</td>
      <td>444.000</td>
      <td>444.000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Championship, FA Cup, League Cup</td>
      <td>right</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>274</td>
      <td>199</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>167</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>24.574</td>
      <td>23.852</td>
      <td>20.637</td>
      <td>1.212</td>
      <td>0.070</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17.268</td>
      <td>1.572</td>
      <td>0.095</td>
      <td>183.302</td>
      <td>20.734</td>
      <td>146.639</td>
      <td>1253.092</td>
      <td>1.264</td>
      <td>NaN</td>
      <td>0.056</td>
      <td>0.054</td>
      <td>6.678</td>
      <td>3.369</td>
      <td>3.369</td>
      <td>2.437</td>
      <td>2.036</td>
      <td>0.105</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.630</td>
      <td>4.751</td>
      <td>18.423</td>
      <td>2.083</td>
      <td>0.138</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.873</td>
      <td>2.998</td>
      <td>0.185</td>
      <td>5.960</td>
      <td>17.093</td>
      <td>191.985</td>
      <td>1270.250</td>
      <td>0.836</td>
      <td>NaN</td>
      <td>0.250</td>
      <td>0.246</td>
      <td>10.716</td>
      <td>4.587</td>
      <td>4.470</td>
      <td>1.998</td>
      <td>2.978</td>
      <td>0.162</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000</td>
      <td>16.356</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>170.000</td>
      <td>0.000</td>
      <td>0.038</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-0.082</td>
      <td>0.000</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>21.000</td>
      <td>19.409</td>
      <td>2.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>179.000</td>
      <td>4.000</td>
      <td>0.375</td>
      <td>96.500</td>
      <td>0.779</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.914</td>
      <td>0.000</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>24.000</td>
      <td>23.907</td>
      <td>17.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>183.000</td>
      <td>18.000</td>
      <td>113.000</td>
      <td>837.000</td>
      <td>1.355</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>2.000</td>
      <td>1.000</td>
      <td>1.955</td>
      <td>1.000</td>
      <td>0.037</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>27.000</td>
      <td>26.495</td>
      <td>38.000</td>
      <td>2.000</td>
      <td>0.105</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.000</td>
      <td>2.000</td>
      <td>0.111</td>
      <td>188.000</td>
      <td>36.000</td>
      <td>216.000</td>
      <td>2154.500</td>
      <td>1.700</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>11.000</td>
      <td>5.000</td>
      <td>5.000</td>
      <td>3.411</td>
      <td>3.000</td>
      <td>0.172</td>
    </tr>
    <tr>
      <th>max</th>
      <td>40.000</td>
      <td>37.608</td>
      <td>73.000</td>
      <td>12.000</td>
      <td>1.406</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>53.000</td>
      <td>19.000</td>
      <td>1.593</td>
      <td>199.000</td>
      <td>55.000</td>
      <td>1080.000</td>
      <td>4770.000</td>
      <td>3.000</td>
      <td>NaN</td>
      <td>2.000</td>
      <td>2.000</td>
      <td>42.000</td>
      <td>27.000</td>
      <td>22.000</td>
      <td>10.998</td>
      <td>13.000</td>
      <td>1.800</td>
    </tr>
  </tbody>
</table>
</div>






    Text(0, 0.5, 'Number of players')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_65_1.png)
    





<style  type="text/css" >
#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col20{
            background-color:  #b40426;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col1{
            background-color:  #cd423b;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col16{
            background-color:  #b7cff9;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col11{
            background-color:  #9ebeff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col7{
            background-color:  #6687ed;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col20{
            background-color:  #85a8fc;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col2{
            background-color:  #7699f6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col15{
            background-color:  #a6c4fe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col1{
            background-color:  #9fbfff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col10{
            background-color:  #aec9fc;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col13{
            background-color:  #6f92f3;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col0{
            background-color:  #6282ea;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col13{
            background-color:  #485fd1;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col5{
            background-color:  #a5c3fe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col1{
            background-color:  #afcafc;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col1{
            background-color:  #89acfd;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col14{
            background-color:  #a2c1ff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col5{
            background-color:  #b2ccfb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col11{
            background-color:  #8fb1fe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col0{
            background-color:  #d55042;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col10{
            background-color:  #92b4fe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col8{
            background-color:  #5b7ae5;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col4{
            background-color:  #8caffe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col7{
            background-color:  #81a4fb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col8{
            background-color:  #7396f5;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col11{
            background-color:  #9bbcff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col4{
            background-color:  #88abfd;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col18{
            background-color:  #7b9ff9;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col14{
            background-color:  #5673e0;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col12{
            background-color:  #4c66d6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col20{
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col20{
            background-color:  #a3c2fe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col6{
            background-color:  #82a6fb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col1{
            background-color:  #96b7ff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col7{
            background-color:  #b3cdfb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col16{
            background-color:  #f7b093;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col18{
            background-color:  #adc9fd;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col5{
            background-color:  #bb1b2c;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col6{
            background-color:  #f5c0a7;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col9{
            background-color:  #e8765c;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col10{
            background-color:  #ccd9ed;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col11{
            background-color:  #d65244;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col19{
            background-color:  #9abbff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col12{
            background-color:  #7ea1fa;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col4{
            background-color:  #bbd1f8;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col16{
            background-color:  #f39475;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col17{
            background-color:  #f6a385;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col2{
            background-color:  #f7a889;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col17{
            background-color:  #abc8fd;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col18{
            background-color:  #6a8bef;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col1{
            background-color:  #a7c5fe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col3{
            background-color:  #f7b599;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col5{
            background-color:  #f1cdba;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col3{
            background-color:  #f7ba9f;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col6{
            background-color:  #f6bda2;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col1{
            background-color:  #b6cefa;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col12{
            background-color:  #465ecf;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col6{
            background-color:  #e9d5cb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col10{
            background-color:  #9dbdff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col11{
            background-color:  #f2cbb7;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col13{
            background-color:  #5d7ce6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col15{
            background-color:  #97b8ff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col16{
            background-color:  #f7b194;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col16{
            background-color:  #d8dce2;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col15{
            background-color:  #90b2fe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col19{
            background-color:  #ead5c9;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col9{
            background-color:  #f2c9b4;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col1{
            background-color:  #b9d0f9;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col0{
            background-color:  #5470de;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col0{
            background-color:  #7597f6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col0{
            background-color:  #7295f4;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col13{
            background-color:  #5977e3;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col7{
            background-color:  #cdd9ec;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col17{
            background-color:  #c3d5f4;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col6{
            background-color:  #8db0fe;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col8{
            background-color:  #5e7de7;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col3{
            background-color:  #a1c0ff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col2{
            background-color:  #ba162b;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col3{
            background-color:  #f2cab5;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col9{
            background-color:  #e67259;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col10{
            background-color:  #cedaeb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col5{
            background-color:  #be242e;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col16{
            background-color:  #f6a586;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col20{
            background-color:  #f0cdbb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col19{
            background-color:  #f4987a;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col1,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col19{
            background-color:  #a9c6fd;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col2{
            background-color:  #f6bfa6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col9{
            background-color:  #d2dbe8;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col1{
            background-color:  #bfd3f6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col9{
            background-color:  #dadce0;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col7,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col4{
            background-color:  #688aef;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col13{
            background-color:  #5a78e4;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col14{
            background-color:  #4f69d9;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col16{
            background-color:  #f6a283;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col17{
            background-color:  #efcebd;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col7{
            background-color:  #779af7;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col19{
            background-color:  #cbd8ee;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col7{
            background-color:  #c5d6f2;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col14{
            background-color:  #4358cb;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col14{
            background-color:  #7093f3;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col16{
            background-color:  #dbdcde;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col16{
            background-color:  #6c8ff1;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col9,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col4{
            background-color:  #7da0f9;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col18{
            background-color:  #5f7fe8;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col6{
            background-color:  #4a63d3;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col20{
            background-color:  #3e51c5;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col8{
            background-color:  #4257c9;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col0{
            background-color:  #80a3fa;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col5{
            background-color:  #e57058;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col20{
            background-color:  #98b9ff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col11{
            background-color:  #ee8468;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col16,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col19{
            background-color:  #f4c6af;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col17{
            background-color:  #ead4c8;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col19{
            background-color:  #f5c1a9;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col2{
            background-color:  #d5dbe5;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col5{
            background-color:  #b5cdfa;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col5{
            background-color:  #cfdaea;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col11,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col3{
            background-color:  #bcd2f7;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col14{
            background-color:  #4b64d5;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col13,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col10,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col8{
            background-color:  #5875e1;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col14{
            background-color:  #4055c8;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col10{
            background-color:  #c4d5f3;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col2{
            background-color:  #d24b40;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col11{
            background-color:  #e5d8d1;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col9{
            background-color:  #ed8366;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col10{
            background-color:  #c7d7f0;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col15{
            background-color:  #8badfd;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col16{
            background-color:  #f4c5ad;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col19{
            background-color:  #f39577;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col4,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col15,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col2{
            background-color:  #bed2f6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col9{
            background-color:  #aac7fd;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col20,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col6,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col11{
            background-color:  #84a7fc;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col10{
            background-color:  #6b8df0;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col13{
            background-color:  #6788ee;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col8,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col10{
            background-color:  #86a9fc;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col0{
            background-color:  #455cce;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col7{
            background-color:  #6384eb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col0{
            background-color:  #4e68d8;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col2,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col10{
            background-color:  #bad0f8;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col14{
            background-color:  #516ddb;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col17,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col6{
            background-color:  #c9d7f0;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col2{
            background-color:  #f59d7e;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col3{
            background-color:  #f7b79b;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col17{
            background-color:  #f7b396;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col6{
            background-color:  #f7ad90;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col12,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col18,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col3,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col5,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col19,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col4{
            background-color:  #799cf8;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col13{
            background-color:  #7a9df8;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col14,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col0,#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col17{
            background-color:  #5572df;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col19{
            background-color:  #e1dad6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col2{
            background-color:  #f7aa8c;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col3{
            background-color:  #d6dce4;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col5{
            background-color:  #e6d7cf;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col7{
            background-color:  #3c4ec2;
            color:  #f1f1f1;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col8{
            background-color:  #94b6ff;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col3{
            background-color:  #eed0c0;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col5{
            background-color:  #f59c7d;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col11{
            background-color:  #f59f80;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col16{
            background-color:  #ebd3c6;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col12{
            background-color:  #6e90f2;
            color:  #000000;
        }#T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col16{
            background-color:  #c0d4f5;
            color:  #000000;
        }</style><table id="T_a50c324c_5f55_11eb_9dec_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Age</th>        <th class="col_heading level0 col1" >Age when joined</th>        <th class="col_heading level0 col2" >Appearances</th>        <th class="col_heading level0 col3" >Assists</th>        <th class="col_heading level0 col4" >Assists p90</th>        <th class="col_heading level0 col5" >Games started</th>        <th class="col_heading level0 col6" >Goals</th>        <th class="col_heading level0 col7" >Goals p90</th>        <th class="col_heading level0 col8" >Height</th>        <th class="col_heading level0 col9" >In squad</th>        <th class="col_heading level0 col10" >Market value</th>        <th class="col_heading level0 col11" >Minutes played</th>        <th class="col_heading level0 col12" >PPG</th>        <th class="col_heading level0 col13" >Red cards</th>        <th class="col_heading level0 col14" >Second yellow cards</th>        <th class="col_heading level0 col15" >Shirt number</th>        <th class="col_heading level0 col16" >Substitutions off</th>        <th class="col_heading level0 col17" >Substitutions on</th>        <th class="col_heading level0 col18" >Years in team</th>        <th class="col_heading level0 col19" >Yellow cards</th>        <th class="col_heading level0 col20" >Yellow cards p90</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row0" class="row_heading level0 row0" >Age</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col0" class="data row0 col0" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col1" class="data row0 col1" >0.903</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col2" class="data row0 col2" >0.255</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col3" class="data row0 col3" >0.123</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col4" class="data row0 col4" >-0.030</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col5" class="data row0 col5" >0.286</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col6" class="data row0 col6" >0.100</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col7" class="data row0 col7" >0.058</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col8" class="data row0 col8" >0.115</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col9" class="data row0 col9" >0.234</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col10" class="data row0 col10" >0.132</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col11" class="data row0 col11" >0.304</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col12" class="data row0 col12" >0.158</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col13" class="data row0 col13" >0.117</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col14" class="data row0 col14" >0.010</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col15" class="data row0 col15" >0.183</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col16" class="data row0 col16" >0.150</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col17" class="data row0 col17" >0.036</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col18" class="data row0 col18" >0.060</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col19" class="data row0 col19" >0.239</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row0_col20" class="data row0 col20" >0.190</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row1" class="row_heading level0 row1" >Age when joined</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col0" class="data row1 col0" >0.903</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col1" class="data row1 col1" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col2" class="data row1 col2" >0.127</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col3" class="data row1 col3" >0.079</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col4" class="data row1 col4" >-0.066</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col5" class="data row1 col5" >0.144</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col6" class="data row1 col6" >0.089</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col7" class="data row1 col7" >0.052</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col8" class="data row1 col8" >0.074</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col9" class="data row1 col9" >0.096</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col10" class="data row1 col10" >0.143</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col11" class="data row1 col11" >0.150</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col12" class="data row1 col12" >0.081</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col13" class="data row1 col13" >0.049</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col14" class="data row1 col14" >-0.037</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col15" class="data row1 col15" >0.178</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col16" class="data row1 col16" >0.112</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col17" class="data row1 col17" >0.010</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col18" class="data row1 col18" >-0.363</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col19" class="data row1 col19" >0.142</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row1_col20" class="data row1 col20" >0.149</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row2" class="row_heading level0 row2" >Appearances</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col0" class="data row2 col0" >0.255</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col1" class="data row2 col1" >0.127</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col2" class="data row2 col2" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col3" class="data row2 col3" >0.612</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col4" class="data row2 col4" >0.212</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col5" class="data row2 col5" >0.977</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col6" class="data row2 col6" >0.578</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col7" class="data row2 col7" >0.241</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col8" class="data row2 col8" >-0.186</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col9" class="data row2 col9" >0.814</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col10" class="data row2 col10" >0.372</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col11" class="data row2 col11" >0.894</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col12" class="data row2 col12" >0.279</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col13" class="data row2 col13" >0.227</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col14" class="data row2 col14" >0.178</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col15" class="data row2 col15" >0.263</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col16" class="data row2 col16" >0.693</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col17" class="data row2 col17" >0.652</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col18" class="data row2 col18" >0.032</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col19" class="data row2 col19" >0.660</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row2_col20" class="data row2 col20" >0.278</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row3" class="row_heading level0 row3" >Assists</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col0" class="data row3 col0" >0.123</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col1" class="data row3 col1" >0.079</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col2" class="data row3 col2" >0.612</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col3" class="data row3 col3" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col4" class="data row3 col4" >0.510</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col5" class="data row3 col5" >0.613</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col6" class="data row3 col6" >0.594</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col7" class="data row3 col7" >0.273</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col8" class="data row3 col8" >-0.249</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col9" class="data row3 col9" >0.505</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col10" class="data row3 col10" >0.206</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col11" class="data row3 col11" >0.574</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col12" class="data row3 col12" >0.169</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col13" class="data row3 col13" >0.238</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col14" class="data row3 col14" >0.079</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col15" class="data row3 col15" >0.136</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col16" class="data row3 col16" >0.587</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col17" class="data row3 col17" >0.344</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col18" class="data row3 col18" >-0.009</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col19" class="data row3 col19" >0.473</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row3_col20" class="data row3 col20" >0.173</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row4" class="row_heading level0 row4" >Assists p90</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col0" class="data row4 col0" >-0.030</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col1" class="data row4 col1" >-0.066</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col2" class="data row4 col2" >0.212</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col3" class="data row4 col3" >0.510</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col4" class="data row4 col4" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col5" class="data row4 col5" >0.177</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col6" class="data row4 col6" >0.265</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col7" class="data row4 col7" >0.279</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col8" class="data row4 col8" >-0.196</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col9" class="data row4 col9" >0.145</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col10" class="data row4 col10" >0.079</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col11" class="data row4 col11" >0.121</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col12" class="data row4 col12" >0.270</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col13" class="data row4 col13" >0.088</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col14" class="data row4 col14" >0.010</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col15" class="data row4 col15" >0.051</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col16" class="data row4 col16" >0.273</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col17" class="data row4 col17" >0.247</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col18" class="data row4 col18" >-0.018</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col19" class="data row4 col19" >0.102</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row4_col20" class="data row4 col20" >0.037</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row5" class="row_heading level0 row5" >Games started</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col0" class="data row5 col0" >0.286</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col1" class="data row5 col1" >0.144</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col2" class="data row5 col2" >0.977</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col3" class="data row5 col3" >0.613</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col4" class="data row5 col4" >0.177</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col5" class="data row5 col5" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col6" class="data row5 col6" >0.537</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col7" class="data row5 col7" >0.179</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col8" class="data row5 col8" >-0.137</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col9" class="data row5 col9" >0.822</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col10" class="data row5 col10" >0.378</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col11" class="data row5 col11" >0.968</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col12" class="data row5 col12" >0.267</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col13" class="data row5 col13" >0.225</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col14" class="data row5 col14" >0.200</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col15" class="data row5 col15" >0.229</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col16" class="data row5 col16" >0.637</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col17" class="data row5 col17" >0.475</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col18" class="data row5 col18" >0.083</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col19" class="data row5 col19" >0.708</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row5_col20" class="data row5 col20" >0.278</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row6" class="row_heading level0 row6" >Goals</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col0" class="data row6 col0" >0.100</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col1" class="data row6 col1" >0.089</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col2" class="data row6 col2" >0.578</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col3" class="data row6 col3" >0.594</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col4" class="data row6 col4" >0.265</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col5" class="data row6 col5" >0.537</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col6" class="data row6 col6" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col7" class="data row6 col7" >0.594</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col8" class="data row6 col8" >-0.164</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col9" class="data row6 col9" >0.406</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col10" class="data row6 col10" >0.322</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col11" class="data row6 col11" >0.456</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col12" class="data row6 col12" >0.140</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col13" class="data row6 col13" >0.093</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col14" class="data row6 col14" >0.035</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col15" class="data row6 col15" >0.098</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col16" class="data row6 col16" >0.646</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col17" class="data row6 col17" >0.473</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col18" class="data row6 col18" >-0.105</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col19" class="data row6 col19" >0.332</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row6_col20" class="data row6 col20" >0.131</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row7" class="row_heading level0 row7" >Goals p90</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col0" class="data row7 col0" >0.058</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col1" class="data row7 col1" >0.052</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col2" class="data row7 col2" >0.241</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col3" class="data row7 col3" >0.273</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col4" class="data row7 col4" >0.279</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col5" class="data row7 col5" >0.179</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col6" class="data row7 col6" >0.594</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col7" class="data row7 col7" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col8" class="data row7 col8" >-0.156</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col9" class="data row7 col9" >0.109</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col10" class="data row7 col10" >0.262</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col11" class="data row7 col11" >0.096</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col12" class="data row7 col12" >0.241</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col13" class="data row7 col13" >0.016</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col14" class="data row7 col14" >-0.005</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col15" class="data row7 col15" >0.002</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col16" class="data row7 col16" >0.326</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col17" class="data row7 col17" >0.357</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col18" class="data row7 col18" >-0.150</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col19" class="data row7 col19" >0.062</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row7_col20" class="data row7 col20" >0.038</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row8" class="row_heading level0 row8" >Height</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col0" class="data row8 col0" >0.115</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col1" class="data row8 col1" >0.074</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col2" class="data row8 col2" >-0.186</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col3" class="data row8 col3" >-0.249</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col4" class="data row8 col4" >-0.196</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col5" class="data row8 col5" >-0.137</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col6" class="data row8 col6" >-0.164</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col7" class="data row8 col7" >-0.156</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col8" class="data row8 col8" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col9" class="data row8 col9" >-0.099</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col10" class="data row8 col10" >-0.065</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col11" class="data row8 col11" >-0.063</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col12" class="data row8 col12" >-0.010</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col13" class="data row8 col13" >0.001</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col14" class="data row8 col14" >-0.013</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col15" class="data row8 col15" >0.055</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col16" class="data row8 col16" >-0.304</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col17" class="data row8 col17" >-0.271</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col18" class="data row8 col18" >0.047</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col19" class="data row8 col19" >-0.181</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row8_col20" class="data row8 col20" >-0.074</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row9" class="row_heading level0 row9" >In squad</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col0" class="data row9 col0" >0.234</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col1" class="data row9 col1" >0.096</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col2" class="data row9 col2" >0.814</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col3" class="data row9 col3" >0.505</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col4" class="data row9 col4" >0.145</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col5" class="data row9 col5" >0.822</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col6" class="data row9 col6" >0.406</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col7" class="data row9 col7" >0.109</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col8" class="data row9 col8" >-0.099</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col9" class="data row9 col9" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col10" class="data row9 col10" >0.125</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col11" class="data row9 col11" >0.785</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col12" class="data row9 col12" >0.277</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col13" class="data row9 col13" >0.204</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col14" class="data row9 col14" >0.173</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col15" class="data row9 col15" >0.173</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col16" class="data row9 col16" >0.504</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col17" class="data row9 col17" >0.438</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col18" class="data row9 col18" >0.085</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col19" class="data row9 col19" >0.567</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row9_col20" class="data row9 col20" >0.267</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row10" class="row_heading level0 row10" >Market value</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col0" class="data row10 col0" >0.132</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col1" class="data row10 col1" >0.143</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col2" class="data row10 col2" >0.372</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col3" class="data row10 col3" >0.206</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col4" class="data row10 col4" >0.079</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col5" class="data row10 col5" >0.378</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col6" class="data row10 col6" >0.322</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col7" class="data row10 col7" >0.262</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col8" class="data row10 col8" >-0.065</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col9" class="data row10 col9" >0.125</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col10" class="data row10 col10" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col11" class="data row10 col11" >0.350</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col12" class="data row10 col12" >0.048</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col13" class="data row10 col13" >0.084</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col14" class="data row10 col14" >-0.017</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col15" class="data row10 col15" >0.207</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col16" class="data row10 col16" >0.338</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col17" class="data row10 col17" >0.171</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col18" class="data row10 col18" >-0.124</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col19" class="data row10 col19" >0.304</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row10_col20" class="data row10 col20" >0.137</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row11" class="row_heading level0 row11" >Minutes played</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col0" class="data row11 col0" >0.304</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col1" class="data row11 col1" >0.150</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col2" class="data row11 col2" >0.894</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col3" class="data row11 col3" >0.574</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col4" class="data row11 col4" >0.121</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col5" class="data row11 col5" >0.968</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col6" class="data row11 col6" >0.456</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col7" class="data row11 col7" >0.096</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col8" class="data row11 col8" >-0.063</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col9" class="data row11 col9" >0.785</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col10" class="data row11 col10" >0.350</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col11" class="data row11 col11" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col12" class="data row11 col12" >0.237</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col13" class="data row11 col13" >0.201</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col14" class="data row11 col14" >0.211</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col15" class="data row11 col15" >0.177</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col16" class="data row11 col16" >0.506</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col17" class="data row11 col17" >0.246</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col18" class="data row11 col18" >0.139</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col19" class="data row11 col19" >0.718</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row11_col20" class="data row11 col20" >0.254</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row12" class="row_heading level0 row12" >PPG</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col0" class="data row12 col0" >0.158</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col1" class="data row12 col1" >0.081</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col2" class="data row12 col2" >0.279</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col3" class="data row12 col3" >0.169</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col4" class="data row12 col4" >0.270</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col5" class="data row12 col5" >0.267</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col6" class="data row12 col6" >0.140</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col7" class="data row12 col7" >0.241</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col8" class="data row12 col8" >-0.010</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col9" class="data row12 col9" >0.277</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col10" class="data row12 col10" >0.048</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col11" class="data row12 col11" >0.237</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col12" class="data row12 col12" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col13" class="data row12 col13" >0.033</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col14" class="data row12 col14" >0.057</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col15" class="data row12 col15" >0.067</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col16" class="data row12 col16" >0.184</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col17" class="data row12 col17" >0.199</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col18" class="data row12 col18" >0.052</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col19" class="data row12 col19" >0.157</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row12_col20" class="data row12 col20" >0.153</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row13" class="row_heading level0 row13" >Red cards</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col0" class="data row13 col0" >0.117</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col1" class="data row13 col1" >0.049</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col2" class="data row13 col2" >0.227</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col3" class="data row13 col3" >0.238</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col4" class="data row13 col4" >0.088</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col5" class="data row13 col5" >0.225</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col6" class="data row13 col6" >0.093</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col7" class="data row13 col7" >0.016</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col8" class="data row13 col8" >0.001</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col9" class="data row13 col9" >0.204</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col10" class="data row13 col10" >0.084</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col11" class="data row13 col11" >0.201</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col12" class="data row13 col12" >0.033</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col13" class="data row13 col13" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col14" class="data row13 col14" >-0.013</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col15" class="data row13 col15" >0.133</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col16" class="data row13 col16" >0.189</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col17" class="data row13 col17" >0.137</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col18" class="data row13 col18" >0.101</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col19" class="data row13 col19" >0.249</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row13_col20" class="data row13 col20" >0.155</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row14" class="row_heading level0 row14" >Second yellow cards</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col0" class="data row14 col0" >0.010</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col1" class="data row14 col1" >-0.037</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col2" class="data row14 col2" >0.178</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col3" class="data row14 col3" >0.079</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col4" class="data row14 col4" >0.010</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col5" class="data row14 col5" >0.200</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col6" class="data row14 col6" >0.035</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col7" class="data row14 col7" >-0.005</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col8" class="data row14 col8" >-0.013</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col9" class="data row14 col9" >0.173</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col10" class="data row14 col10" >-0.017</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col11" class="data row14 col11" >0.211</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col12" class="data row14 col12" >0.057</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col13" class="data row14 col13" >-0.013</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col14" class="data row14 col14" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col15" class="data row14 col15" >0.044</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col16" class="data row14 col16" >0.052</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col17" class="data row14 col17" >0.023</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col18" class="data row14 col18" >0.063</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col19" class="data row14 col19" >0.285</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row14_col20" class="data row14 col20" >0.140</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row15" class="row_heading level0 row15" >Shirt number</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col0" class="data row15 col0" >0.183</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col1" class="data row15 col1" >0.178</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col2" class="data row15 col2" >0.263</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col3" class="data row15 col3" >0.136</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col4" class="data row15 col4" >0.051</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col5" class="data row15 col5" >0.229</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col6" class="data row15 col6" >0.098</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col7" class="data row15 col7" >0.002</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col8" class="data row15 col8" >0.055</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col9" class="data row15 col9" >0.173</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col10" class="data row15 col10" >0.207</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col11" class="data row15 col11" >0.177</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col12" class="data row15 col12" >0.067</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col13" class="data row15 col13" >0.133</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col14" class="data row15 col14" >0.044</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col15" class="data row15 col15" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col16" class="data row15 col16" >0.187</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col17" class="data row15 col17" >0.273</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col18" class="data row15 col18" >-0.200</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col19" class="data row15 col19" >0.114</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row15_col20" class="data row15 col20" >0.091</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row16" class="row_heading level0 row16" >Substitutions off</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col0" class="data row16 col0" >0.150</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col1" class="data row16 col1" >0.112</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col2" class="data row16 col2" >0.693</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col3" class="data row16 col3" >0.587</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col4" class="data row16 col4" >0.273</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col5" class="data row16 col5" >0.637</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col6" class="data row16 col6" >0.646</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col7" class="data row16 col7" >0.326</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col8" class="data row16 col8" >-0.304</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col9" class="data row16 col9" >0.504</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col10" class="data row16 col10" >0.338</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col11" class="data row16 col11" >0.506</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col12" class="data row16 col12" >0.184</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col13" class="data row16 col13" >0.189</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col14" class="data row16 col14" >0.052</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col15" class="data row16 col15" >0.187</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col16" class="data row16 col16" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col17" class="data row16 col17" >0.593</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col18" class="data row16 col18" >-0.100</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col19" class="data row16 col19" >0.429</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row16_col20" class="data row16 col20" >0.217</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row17" class="row_heading level0 row17" >Substitutions on</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col0" class="data row17 col0" >0.036</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col1" class="data row17 col1" >0.010</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col2" class="data row17 col2" >0.652</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col3" class="data row17 col3" >0.344</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col4" class="data row17 col4" >0.247</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col5" class="data row17 col5" >0.475</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col6" class="data row17 col6" >0.473</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col7" class="data row17 col7" >0.357</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col8" class="data row17 col8" >-0.271</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col9" class="data row17 col9" >0.438</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col10" class="data row17 col10" >0.171</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col11" class="data row17 col11" >0.246</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col12" class="data row17 col12" >0.199</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col13" class="data row17 col13" >0.137</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col14" class="data row17 col14" >0.023</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col15" class="data row17 col15" >0.273</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col16" class="data row17 col16" >0.593</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col17" class="data row17 col17" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col18" class="data row17 col18" >-0.159</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col19" class="data row17 col19" >0.208</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row17_col20" class="data row17 col20" >0.160</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row18" class="row_heading level0 row18" >Years in team</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col0" class="data row18 col0" >0.060</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col1" class="data row18 col1" >-0.363</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col2" class="data row18 col2" >0.032</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col3" class="data row18 col3" >-0.009</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col4" class="data row18 col4" >-0.018</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col5" class="data row18 col5" >0.083</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col6" class="data row18 col6" >-0.105</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col7" class="data row18 col7" >-0.150</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col8" class="data row18 col8" >0.047</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col9" class="data row18 col9" >0.085</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col10" class="data row18 col10" >-0.124</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col11" class="data row18 col11" >0.139</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col12" class="data row18 col12" >0.052</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col13" class="data row18 col13" >0.101</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col14" class="data row18 col14" >0.063</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col15" class="data row18 col15" >-0.200</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col16" class="data row18 col16" >-0.100</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col17" class="data row18 col17" >-0.159</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col18" class="data row18 col18" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col19" class="data row18 col19" >0.045</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row18_col20" class="data row18 col20" >-0.090</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row19" class="row_heading level0 row19" >Yellow cards</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col0" class="data row19 col0" >0.239</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col1" class="data row19 col1" >0.142</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col2" class="data row19 col2" >0.660</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col3" class="data row19 col3" >0.473</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col4" class="data row19 col4" >0.102</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col5" class="data row19 col5" >0.708</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col6" class="data row19 col6" >0.332</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col7" class="data row19 col7" >0.062</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col8" class="data row19 col8" >-0.181</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col9" class="data row19 col9" >0.567</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col10" class="data row19 col10" >0.304</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col11" class="data row19 col11" >0.718</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col12" class="data row19 col12" >0.157</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col13" class="data row19 col13" >0.249</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col14" class="data row19 col14" >0.285</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col15" class="data row19 col15" >0.114</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col16" class="data row19 col16" >0.429</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col17" class="data row19 col17" >0.208</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col18" class="data row19 col18" >0.045</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col19" class="data row19 col19" >1.000</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row19_col20" class="data row19 col20" >0.552</td>
            </tr>
            <tr>
                        <th id="T_a50c324c_5f55_11eb_9dec_74d83eb26131level0_row20" class="row_heading level0 row20" >Yellow cards p90</th>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col0" class="data row20 col0" >0.190</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col1" class="data row20 col1" >0.149</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col2" class="data row20 col2" >0.278</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col3" class="data row20 col3" >0.173</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col4" class="data row20 col4" >0.037</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col5" class="data row20 col5" >0.278</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col6" class="data row20 col6" >0.131</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col7" class="data row20 col7" >0.038</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col8" class="data row20 col8" >-0.074</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col9" class="data row20 col9" >0.267</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col10" class="data row20 col10" >0.137</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col11" class="data row20 col11" >0.254</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col12" class="data row20 col12" >0.153</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col13" class="data row20 col13" >0.155</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col14" class="data row20 col14" >0.140</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col15" class="data row20 col15" >0.091</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col16" class="data row20 col16" >0.217</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col17" class="data row20 col17" >0.160</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col18" class="data row20 col18" >-0.090</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col19" class="data row20 col19" >0.552</td>
                        <td id="T_a50c324c_5f55_11eb_9dec_74d83eb26131row20_col20" class="data row20 col20" >1.000</td>
            </tr>
    </tbody></table>



**ANALYSIS**: I'll remove `Games started` and `Age when joined` as they are closely correlated with other features.




    Index(['Age', 'Age when joined', 'Appearances', 'Assists', 'Assists p90',
           'Competition', 'Foot', 'Games started', 'Goals', 'Goals p90', 'Height',
           'In squad', 'Market value', 'Minutes played', 'PPG', 'Position group',
           'Red cards', 'Second yellow cards', 'Shirt number', 'Substitutions off',
           'Substitutions on', 'Years in team', 'Yellow cards',
           'Yellow cards p90'],
          dtype='object')






    (444, 24)



## 4. Modelling

* Select Modelling Technique
* Generate Test Design
* Build Model
* Assess Model

    
    
    Selected numeric features are: ['Shirt number', 'Height', 'Age', 'Years in team', 'In squad', 'Appearances', 'Substitutions on', 'Substitutions off', 'Goals', 'Assists', 'Yellow cards', 'Second yellow cards', 'Red cards', 'PPG', 'Minutes played', 'Goals p90', 'Assists p90', 'Yellow cards p90']
    

    
    
    Selected categorical features are: ['Foot', 'Position group', 'Competition']
    

    
    
    Dropping nulls during data preparation: False
    

    
    
    Train data has shape: (295, 21)
    Test data has shape: (33, 21)
    

    
    
    Full model grid-space to tune hyperparameters across...
    




    GridSearchCV(cv=KFold(n_splits=10, random_state=4, shuffle=True),
                 estimator=Pipeline(steps=[('preprocessor',
                                            ColumnTransformer(transformers=[('num',
                                                                             Pipeline(steps=[('imputer',
                                                                                              SimpleImputer(strategy='median')),
                                                                                             ('scaler',
                                                                                              MinMaxScaler())]),
                                                                             ['Shirt '
                                                                              'number',
                                                                              'Height',
                                                                              'Age',
                                                                              'Years '
                                                                              'in '
                                                                              'team',
                                                                              'In '
                                                                              'squad',
                                                                              'Appearances',
                                                                              'Substitutions '
                                                                              'on',
                                                                              'Substitutions '
                                                                              'off',...
                                                                              'PPG',
                                                                              'Minutes '
                                                                              'played',
                                                                              'Goals '
                                                                              'p90',
                                                                              'Assists '
                                                                              'p90',
                                                                              'Yellow '
                                                                              'cards '
                                                                              'p90']),
                                                                            ('cat',
                                                                             Pipeline(steps=[('imputer',
                                                                                              SimpleImputer(fill_value='missing',
                                                                                                            strategy='constant')),
                                                                                             ('onehot',
                                                                                              OneHotEncoder(handle_unknown='ignore'))]),
                                                                             ['Foot',
                                                                              'Position '
                                                                              'group',
                                                                              'Competition'])])),
                                           ('estimator',
                                            GradientBoostingRegressor())]),
                 param_grid={'estimator__random_state': [4]})



    
    
    Final tuned model...
    




    Pipeline(steps=[('preprocessor',
                     ColumnTransformer(transformers=[('num',
                                                      Pipeline(steps=[('imputer',
                                                                       SimpleImputer(strategy='median')),
                                                                      ('scaler',
                                                                       MinMaxScaler())]),
                                                      ['Shirt number', 'Height',
                                                       'Age', 'Years in team',
                                                       'In squad', 'Appearances',
                                                       'Substitutions on',
                                                       'Substitutions off', 'Goals',
                                                       'Assists', 'Yellow cards',
                                                       'Second yellow cards',
                                                       'Red cards', 'PPG',
                                                       'Minutes played',
                                                       'Goals p90', 'Assists p90',
                                                       'Yellow cards p90']),
                                                     ('cat',
                                                      Pipeline(steps=[('imputer',
                                                                       SimpleImputer(fill_value='missing',
                                                                                     strategy='constant')),
                                                                      ('onehot',
                                                                       OneHotEncoder(handle_unknown='ignore'))]),
                                                      ['Foot', 'Position group',
                                                       'Competition'])])),
                    ('estimator', GradientBoostingRegressor(random_state=4))])



## 5. Evaluation

* Evaluate Results
* Review Process
* Determine Next Steps

    Model scores
    




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
      <th>Train</th>
      <th>Test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MedAE</th>
      <td>30.674</td>
      <td>72.180</td>
    </tr>
    <tr>
      <th>RMSE</th>
      <td>59.879</td>
      <td>231.422</td>
    </tr>
    <tr>
      <th>R^2</th>
      <td>0.900</td>
      <td>-0.207</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** Switching from random forest to gradient boost has improved the training scores further... but the test scores are (arguably) slightly worse.


    
![png](boro_01_current_market_value_files/boro_01_current_market_value_93_0.png)
    


**ANALYSIS:** Scores are converging slowly now so more data could well help.

    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\seaborn\_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir2\lib\site-packages\seaborn\_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    




    Text(0, 0.5, 'Market value (predicted)')




    
![png](boro_01_current_market_value_files/boro_01_current_market_value_95_2.png)
    


**ANALYSIS:** Our predictions are still undershooting in general but the training data is getting very close (overfitting?)

    
    Significant training features:
    Minutes played       0.267 +/- 0.023
    Age                  0.132 +/- 0.015
    Shirt number         0.124 +/- 0.021
    Years in team        0.115 +/- 0.012
    In squad             0.114 +/- 0.013
    Goals                0.076 +/- 0.011
    Position group       0.066 +/- 0.009
    Appearances          0.062 +/- 0.008
    PPG                  0.050 +/- 0.005
    Substitutions off    0.048 +/- 0.008
    Height               0.046 +/- 0.005
    Competition          0.042 +/- 0.006
    Yellow cards p90     0.028 +/- 0.003
    Assists p90          0.025 +/- 0.004
    Foot                 0.020 +/- 0.002
    Yellow cards         0.020 +/- 0.003
    Goals p90            0.019 +/- 0.004
    Substitutions on     0.010 +/- 0.002
    Red cards            0.004 +/- 0.001
    Assists              0.004 +/- 0.001
    Second yellow cards  0.002 +/- 0.001
    
    Significant testing features:
    Substitutions on     0.022 +/- 0.011
    

**ANALYSIS:** `Minutes played`, `Goals`, `Appearances`, `Age`, `Position group` and `In squad` are particularly influencing the model. Of those, only `In squad` - along with `Yellow cards` and `Assists` - are generalising to new predictions.

## 6. Deployment

* Plan Deployment
* Plan Monitoring and Maintenance
* Produce Final Report
* Review Project

    Summary of whole dataset (with predictions)...
    




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
      <th>Age</th>
      <th>Age when joined</th>
      <th>Appearances</th>
      <th>Assists</th>
      <th>Assists p90</th>
      <th>Competition</th>
      <th>Foot</th>
      <th>Games started</th>
      <th>Goals</th>
      <th>Goals p90</th>
      <th>Height</th>
      <th>In squad</th>
      <th>Market value</th>
      <th>Minutes played</th>
      <th>PPG</th>
      <th>Position group</th>
      <th>Red cards</th>
      <th>Second yellow cards</th>
      <th>Shirt number</th>
      <th>Substitutions off</th>
      <th>Substitutions on</th>
      <th>Years in team</th>
      <th>Yellow cards</th>
      <th>Yellow cards p90</th>
      <th>Market value (prediction)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>444.000</td>
      <td>349.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444</td>
      <td>322</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>354.000</td>
      <td>444.000</td>
      <td>328.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>349.000</td>
      <td>444.000</td>
      <td>444.000</td>
      <td>444.000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Championship, FA Cup, League Cup</td>
      <td>right</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>274</td>
      <td>199</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>167</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>24.574</td>
      <td>23.852</td>
      <td>20.637</td>
      <td>1.212</td>
      <td>0.070</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17.268</td>
      <td>1.572</td>
      <td>0.095</td>
      <td>183.302</td>
      <td>20.734</td>
      <td>146.639</td>
      <td>1253.092</td>
      <td>1.264</td>
      <td>NaN</td>
      <td>0.056</td>
      <td>0.054</td>
      <td>6.678</td>
      <td>3.369</td>
      <td>3.369</td>
      <td>2.437</td>
      <td>2.036</td>
      <td>0.105</td>
      <td>121.183</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.630</td>
      <td>4.751</td>
      <td>18.423</td>
      <td>2.083</td>
      <td>0.138</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.873</td>
      <td>2.998</td>
      <td>0.185</td>
      <td>5.960</td>
      <td>17.093</td>
      <td>191.985</td>
      <td>1270.250</td>
      <td>0.836</td>
      <td>NaN</td>
      <td>0.250</td>
      <td>0.246</td>
      <td>10.716</td>
      <td>4.587</td>
      <td>4.470</td>
      <td>1.998</td>
      <td>2.978</td>
      <td>0.162</td>
      <td>144.072</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000</td>
      <td>16.356</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>170.000</td>
      <td>0.000</td>
      <td>0.038</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-0.082</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-41.834</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>21.000</td>
      <td>19.409</td>
      <td>2.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>179.000</td>
      <td>4.000</td>
      <td>0.375</td>
      <td>96.500</td>
      <td>0.779</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.914</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>21.555</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>24.000</td>
      <td>23.907</td>
      <td>17.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>183.000</td>
      <td>18.000</td>
      <td>113.000</td>
      <td>837.000</td>
      <td>1.355</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>2.000</td>
      <td>1.000</td>
      <td>1.955</td>
      <td>1.000</td>
      <td>0.037</td>
      <td>80.313</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>27.000</td>
      <td>26.495</td>
      <td>38.000</td>
      <td>2.000</td>
      <td>0.105</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.000</td>
      <td>2.000</td>
      <td>0.111</td>
      <td>188.000</td>
      <td>36.000</td>
      <td>216.000</td>
      <td>2154.500</td>
      <td>1.700</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>11.000</td>
      <td>5.000</td>
      <td>5.000</td>
      <td>3.411</td>
      <td>3.000</td>
      <td>0.172</td>
      <td>169.356</td>
    </tr>
    <tr>
      <th>max</th>
      <td>40.000</td>
      <td>37.608</td>
      <td>73.000</td>
      <td>12.000</td>
      <td>1.406</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>53.000</td>
      <td>19.000</td>
      <td>1.593</td>
      <td>199.000</td>
      <td>55.000</td>
      <td>1080.000</td>
      <td>4770.000</td>
      <td>3.000</td>
      <td>NaN</td>
      <td>2.000</td>
      <td>2.000</td>
      <td>42.000</td>
      <td>27.000</td>
      <td>22.000</td>
      <td>10.998</td>
      <td>13.000</td>
      <td>1.800</td>
      <td>1005.237</td>
    </tr>
  </tbody>
</table>
</div>



    Summary of unseen records in dataset (no labels)...
    




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
      <th>Age</th>
      <th>Age when joined</th>
      <th>Appearances</th>
      <th>Assists</th>
      <th>Assists p90</th>
      <th>Competition</th>
      <th>Foot</th>
      <th>Games started</th>
      <th>Goals</th>
      <th>Goals p90</th>
      <th>Height</th>
      <th>In squad</th>
      <th>Market value</th>
      <th>Minutes played</th>
      <th>PPG</th>
      <th>Position group</th>
      <th>Red cards</th>
      <th>Second yellow cards</th>
      <th>Shirt number</th>
      <th>Substitutions off</th>
      <th>Substitutions on</th>
      <th>Years in team</th>
      <th>Yellow cards</th>
      <th>Yellow cards p90</th>
      <th>Market value (prediction)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>116.000</td>
      <td>21.000</td>
      <td>116.000</td>
      <td>116.000</td>
      <td>116.000</td>
      <td>116</td>
      <td>22</td>
      <td>116.000</td>
      <td>116.000</td>
      <td>116.000</td>
      <td>28.000</td>
      <td>116.000</td>
      <td>0.0</td>
      <td>116.000</td>
      <td>116.000</td>
      <td>116</td>
      <td>116.0</td>
      <td>116.0</td>
      <td>116.000</td>
      <td>116.000</td>
      <td>116.000</td>
      <td>21.000</td>
      <td>116.000</td>
      <td>116.000</td>
      <td>116.000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Championship, FA Cup, League Cup</td>
      <td>left</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>49</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>21.922</td>
      <td>18.725</td>
      <td>6.974</td>
      <td>0.345</td>
      <td>0.051</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.509</td>
      <td>0.543</td>
      <td>0.076</td>
      <td>182.179</td>
      <td>8.224</td>
      <td>NaN</td>
      <td>369.828</td>
      <td>1.033</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.922</td>
      <td>1.259</td>
      <td>1.466</td>
      <td>1.486</td>
      <td>0.560</td>
      <td>0.044</td>
      <td>56.342</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.386</td>
      <td>1.370</td>
      <td>9.302</td>
      <td>1.064</td>
      <td>0.178</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.620</td>
      <td>1.488</td>
      <td>0.208</td>
      <td>5.683</td>
      <td>8.971</td>
      <td>NaN</td>
      <td>568.992</td>
      <td>1.103</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.442</td>
      <td>2.575</td>
      <td>2.483</td>
      <td>0.997</td>
      <td>1.347</td>
      <td>0.095</td>
      <td>77.773</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000</td>
      <td>17.054</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>172.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.334</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-41.834</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>19.000</td>
      <td>17.687</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>178.000</td>
      <td>1.000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.991</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-4.422</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>21.000</td>
      <td>18.404</td>
      <td>3.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>182.500</td>
      <td>4.000</td>
      <td>NaN</td>
      <td>90.000</td>
      <td>0.823</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.999</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>26.569</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.250</td>
      <td>19.056</td>
      <td>9.250</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>185.000</td>
      <td>13.250</td>
      <td>NaN</td>
      <td>447.750</td>
      <td>1.851</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>2.000</td>
      <td>2.001</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>92.591</td>
    </tr>
    <tr>
      <th>max</th>
      <td>33.000</td>
      <td>21.881</td>
      <td>35.000</td>
      <td>9.000</td>
      <td>1.406</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.000</td>
      <td>11.000</td>
      <td>1.593</td>
      <td>196.000</td>
      <td>33.000</td>
      <td>NaN</td>
      <td>2520.000</td>
      <td>3.000</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>34.000</td>
      <td>14.000</td>
      <td>14.000</td>
      <td>4.000</td>
      <td>7.000</td>
      <td>0.500</td>
      <td>318.935</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** The player's missing actual Market values are mostly young players who haven't been used much.

    Predictions below zero
    




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
      <th>Age</th>
      <th>Age when joined</th>
      <th>Appearances</th>
      <th>Assists</th>
      <th>Assists p90</th>
      <th>Competition</th>
      <th>Foot</th>
      <th>Games started</th>
      <th>Goals</th>
      <th>Goals p90</th>
      <th>Height</th>
      <th>In squad</th>
      <th>Market value</th>
      <th>Minutes played</th>
      <th>PPG</th>
      <th>Position group</th>
      <th>Red cards</th>
      <th>Second yellow cards</th>
      <th>Shirt number</th>
      <th>Substitutions off</th>
      <th>Substitutions on</th>
      <th>Years in team</th>
      <th>Yellow cards</th>
      <th>Yellow cards p90</th>
      <th>Market value (prediction)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>34.000</td>
      <td>7.000</td>
      <td>34.000</td>
      <td>34.000</td>
      <td>34.000</td>
      <td>34</td>
      <td>6</td>
      <td>34.000</td>
      <td>34.0</td>
      <td>34.0</td>
      <td>12.000</td>
      <td>34.000</td>
      <td>0.0</td>
      <td>34.000</td>
      <td>34.000</td>
      <td>34</td>
      <td>34.0</td>
      <td>34.0</td>
      <td>34.0</td>
      <td>34.000</td>
      <td>34.000</td>
      <td>7.000</td>
      <td>34.000</td>
      <td>34.000</td>
      <td>34.000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Championship, FA Cup, League Cup</td>
      <td>left</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>18.824</td>
      <td>18.137</td>
      <td>1.294</td>
      <td>0.029</td>
      <td>0.041</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.794</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>181.917</td>
      <td>3.382</td>
      <td>NaN</td>
      <td>38.941</td>
      <td>0.922</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.088</td>
      <td>0.500</td>
      <td>1.500</td>
      <td>0.059</td>
      <td>0.015</td>
      <td>-13.471</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2.844</td>
      <td>0.603</td>
      <td>1.624</td>
      <td>0.171</td>
      <td>0.241</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.067</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.760</td>
      <td>4.314</td>
      <td>NaN</td>
      <td>72.866</td>
      <td>1.309</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.288</td>
      <td>0.707</td>
      <td>1.041</td>
      <td>0.343</td>
      <td>0.086</td>
      <td>11.265</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000</td>
      <td>17.457</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>174.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.496</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-41.834</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>17.000</td>
      <td>17.572</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>178.000</td>
      <td>1.000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.001</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-23.129</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>18.500</td>
      <td>18.377</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>182.000</td>
      <td>2.000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>1.002</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-7.276</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>19.750</td>
      <td>18.499</td>
      <td>2.750</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.750</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>185.000</td>
      <td>4.000</td>
      <td>NaN</td>
      <td>48.500</td>
      <td>2.375</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>2.001</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>-6.203</td>
    </tr>
    <tr>
      <th>max</th>
      <td>32.000</td>
      <td>18.985</td>
      <td>4.000</td>
      <td>1.000</td>
      <td>1.406</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>191.000</td>
      <td>23.000</td>
      <td>NaN</td>
      <td>360.000</td>
      <td>3.000</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.000</td>
      <td>2.000</td>
      <td>3.001</td>
      <td>2.000</td>
      <td>0.500</td>
      <td>-1.380</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** The model seems to particularly struggle with young players who we don't have much information about.
