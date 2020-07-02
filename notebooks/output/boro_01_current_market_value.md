# Boro Player Predictions - Current Market Value

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
      <th>240</th>
      <td>NaN</td>
      <td>Centre Forward</td>
      <td>Bartholomew Ogbeche</td>
      <td>1984-10-01</td>
      <td>178.0</td>
      <td>both</td>
      <td>2011-10-01</td>
      <td>NaT</td>
      <td>0.450</td>
      <td>11/12</td>
      <td>F</td>
      <td>26</td>
    </tr>
    <tr>
      <th>518</th>
      <td>7.0</td>
      <td>Central Midfield</td>
      <td>Grant Leadbitter</td>
      <td>1986-01-07</td>
      <td>177.0</td>
      <td>right</td>
      <td>2012-07-01</td>
      <td>2017-06-30</td>
      <td>1.500</td>
      <td>15/16</td>
      <td>M</td>
      <td>30</td>
    </tr>
    <tr>
      <th>611</th>
      <td>NaN</td>
      <td>Keeper</td>
      <td>Tomás Mejías</td>
      <td>1989-01-30</td>
      <td>195.0</td>
      <td>right</td>
      <td>2014-07-05</td>
      <td>2018-06-30</td>
      <td>0.225</td>
      <td>17/18</td>
      <td>G</td>
      <td>29</td>
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
      <td>1.880</td>
      <td>09/10</td>
      <td>D</td>
      <td>22</td>
    </tr>
    <tr>
      <th>274</th>
      <td>NaN</td>
      <td>Right-Back</td>
      <td>Justin Hoyte</td>
      <td>1984-11-20</td>
      <td>180.0</td>
      <td>right</td>
      <td>2008-08-01</td>
      <td>NaT</td>
      <td>1.130</td>
      <td>12/13</td>
      <td>D</td>
      <td>27</td>
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
      <th>618</th>
      <td>NaN</td>
      <td>Centre-Back</td>
      <td>Daniel Ayala</td>
      <td>1990-11-07</td>
      <td>190.0</td>
      <td>right</td>
      <td>2014-01-24</td>
      <td>2020-06-30</td>
      <td>1.800</td>
      <td>17/18</td>
      <td>D</td>
      <td>27</td>
    </tr>
    <tr>
      <th>198</th>
      <td>NaN</td>
      <td>Left-Back</td>
      <td>Joe Bennett</td>
      <td>1990-03-28</td>
      <td>177.0</td>
      <td>left</td>
      <td>2008-07-01</td>
      <td>NaT</td>
      <td>0.188</td>
      <td>11/12</td>
      <td>D</td>
      <td>21</td>
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
      <td>101.00000</td>
      <td>364</td>
      <td>364</td>
      <td>364</td>
      <td>356.000000</td>
      <td>324</td>
      <td>351</td>
      <td>169</td>
      <td>330.000000</td>
      <td>364</td>
      <td>364</td>
      <td>364.000000</td>
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
      <td>12</td>
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
      <td>2020-06-30 00:00:00</td>
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
      <td>201</td>
      <td>31</td>
      <td>28</td>
      <td>NaN</td>
      <td>47</td>
      <td>134</td>
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
      <td>2000-08-09 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2020-01-31 00:00:00</td>
      <td>2023-06-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>17.49505</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>183.286517</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.696327</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.826923</td>
    </tr>
    <tr>
      <th>std</th>
      <td>10.85046</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.028752</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.776398</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.696900</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.00000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>167.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.038000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>8.00000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>179.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.375000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>18.00000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>183.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.130000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.00000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>188.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.250000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>40.00000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>199.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.800000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.000000</td>
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
      <td>27.747253</td>
    </tr>
    <tr>
      <th>Position</th>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Name</th>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Date of birth</th>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Height</th>
      <td>97.802198</td>
    </tr>
    <tr>
      <th>Foot</th>
      <td>89.010989</td>
    </tr>
    <tr>
      <th>Joined</th>
      <td>96.428571</td>
    </tr>
    <tr>
      <th>Contract expires</th>
      <td>46.428571</td>
    </tr>
    <tr>
      <th>Market value</th>
      <td>90.659341</td>
    </tr>
    <tr>
      <th>Season</th>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Position group</th>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>100.000000</td>
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


![png](boro_01_current_market_value_files/boro_01_current_market_value_20_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_21_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_22_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_23_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_24_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_25_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_26_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_27_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_28_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_29_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_30_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_31_0.png)


    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir\lib\site-packages\seaborn\distributions.py:283: UserWarning: Data must have variance to compute a kernel density estimate.
      warnings.warn(msg, UserWarning)
    


![png](boro_01_current_market_value_files/boro_01_current_market_value_32_1.png)


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
      <th>665</th>
      <td>5.0</td>
      <td>Right-Back</td>
      <td>Ryan Shotton</td>
      <td>30.0</td>
      <td>0.0</td>
      <td>33.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>1.58</td>
      <td>2787.0</td>
      <td>18/19</td>
      <td>Championship</td>
      <td>D</td>
    </tr>
    <tr>
      <th>977</th>
      <td>NaN</td>
      <td>Centre Back</td>
      <td>Chris Riggott</td>
      <td>28.0</td>
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
      <th>693</th>
      <td>8.0</td>
      <td>Defensive Midfield</td>
      <td>Adam Clayton</td>
      <td>30.0</td>
      <td>0.0</td>
      <td>35.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>1.63</td>
      <td>2481.0</td>
      <td>18/19</td>
      <td>Championship</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1288</th>
      <td>4.0</td>
      <td>Centre Back</td>
      <td>Rhys Williams</td>
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
      <td>13/14</td>
      <td>FA Cup</td>
      <td>D</td>
    </tr>
    <tr>
      <th>2489</th>
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
      <th>1123</th>
      <td>NaN</td>
      <td>Keeper</td>
      <td>Luke Coddington</td>
      <td>16.0</td>
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
      <td>11/12</td>
      <td>FA Cup</td>
      <td>G</td>
    </tr>
    <tr>
      <th>2471</th>
      <td>4.0</td>
      <td>Centre-Back</td>
      <td>Daniel Ayala</td>
      <td>28.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>3.00</td>
      <td>197.0</td>
      <td>18/19</td>
      <td>League Cup</td>
      <td>D</td>
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
      <td>532.000000</td>
      <td>1262</td>
      <td>1262</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262.000000</td>
      <td>1262</td>
      <td>1262</td>
      <td>1262</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>20</td>
      <td>199</td>
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
      <td>17.060150</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.679081</td>
      <td>6.629160</td>
      <td>5.971474</td>
      <td>0.544374</td>
      <td>0.419176</td>
      <td>0.706022</td>
      <td>0.018225</td>
      <td>0.019810</td>
      <td>1.160063</td>
      <td>1.160063</td>
      <td>0.870642</td>
      <td>433.809033</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>10.905697</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.687628</td>
      <td>11.956319</td>
      <td>10.930571</td>
      <td>1.683294</td>
      <td>1.241388</td>
      <td>1.842733</td>
      <td>0.145187</td>
      <td>0.144979</td>
      <td>2.769447</td>
      <td>2.822205</td>
      <td>1.028689</td>
      <td>847.415074</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>90.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.000000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.560000</td>
      <td>270.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>42.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.000000</td>
      <td>46.000000</td>
      <td>46.000000</td>
      <td>17.000000</td>
      <td>11.000000</td>
      <td>13.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>20.000000</td>
      <td>23.000000</td>
      <td>3.000000</td>
      <td>4140.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** So the data is looking broadly in good shape


![png](boro_01_current_market_value_files/boro_01_current_market_value_40_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_41_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_42_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_43_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_44_0.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_45_0.png)


    C:\Users\adeacon\AppData\Local\Continuum\miniconda3\envs\tbir\lib\site-packages\seaborn\distributions.py:283: UserWarning: Data must have variance to compute a kernel density estimate.
      warnings.warn(msg, UserWarning)
    


![png](boro_01_current_market_value_files/boro_01_current_market_value_46_1.png)



![png](boro_01_current_market_value_files/boro_01_current_market_value_47_0.png)


## 3. Data Preperation

* Select Data
* Clean Data
* Construct Data
* Integrate Data
* Format Data

    Final dataset created with index from Brad Jones (09/10) to Rudy Gestede (19/20).
    


![png](boro_01_current_market_value_files/boro_01_current_market_value_52_0.png)


**ANALYSIS:** Most players join in their teens or mid-twenties.


![png](boro_01_current_market_value_files/boro_01_current_market_value_54_0.png)


**ANALYSIS:** I'm going to leave out `Position`, `Date of birth`, `Joined`, and `Contract expires` from the model for now. `Contract expires` is populated in less than half of records. The others are encoded in derived features now.

<s>**ANALYSIS:** `Foot` and `Position group` will be one-hot encoded</s>




    Index(['Shirt number', 'Position', 'Name', 'Age', 'In squad', 'Games started',
           'Goals', 'Assists', 'Yellow cards', 'Second yellow cards', 'Red cards',
           'Substitutions on', 'Substitutions off', 'PPG', 'Minutes played',
           'Season', 'Competition', 'Position group'],
          dtype='object')




    [1;31mSignature:[0m [0mpsm_agg[0m[1;33m([0m[0mx[0m[1;33m)[0m[1;33m[0m[1;33m[0m[0m
    [1;31mDocstring:[0m <no docstring>
    [1;31mFile:[0m      c:\users\adeacon\documents\github\the-ball-is-round\notebooks\<ipython-input-43-eea62cfa5409>
    [1;31mType:[0m      function
    


    <ipython-input-43-eea62cfa5409>:24: RuntimeWarning: invalid value encountered in double_scalars
      d["PPG"] = ((x["PPG"] * x["Appearances"]).sum() / x["Appearances"].sum())
    <ipython-input-43-eea62cfa5409>:26: RuntimeWarning: invalid value encountered in double_scalars
      d["Goals p90"] = x["Goals"].sum() * 90 / x["Minutes played"].sum()
    <ipython-input-43-eea62cfa5409>:27: RuntimeWarning: invalid value encountered in double_scalars
      d["Assists p90"] = x["Assists"].sum() * 90 / x["Minutes played"].sum()
    <ipython-input-43-eea62cfa5409>:28: RuntimeWarning: invalid value encountered in double_scalars
      d["Yellow cards p90"] = x["Yellow cards"].sum() * 90 / x["Minutes played"].sum()
    

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
      <td>31.151906</td>
      <td>39.0</td>
      <td>10.0</td>
      <td>0.271575</td>
      <td>Championship, FA Cup, League Cup</td>
      <td>left</td>
      <td>39.0</td>
      <td>9.0</td>
      <td>0.244418</td>
      <td>180.0</td>
      <td>39.0</td>
      <td>1.13</td>
      <td>3314.0</td>
      <td>1.592051</td>
      <td>M</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>2.496971</td>
      <td>13.0</td>
      <td>0.353048</td>
    </tr>
    <tr>
      <th>Adam Jackson (13/14)</th>
      <td>19.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>Championship</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>D</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Stewart Downing (17/18)</th>
      <td>33.0</td>
      <td>30.982156</td>
      <td>53.0</td>
      <td>7.0</td>
      <td>0.174226</td>
      <td>Championship, Championship Playoffs, FA Cup, L...</td>
      <td>left</td>
      <td>47.0</td>
      <td>3.0</td>
      <td>0.074668</td>
      <td>180.0</td>
      <td>47.0</td>
      <td>2.25</td>
      <td>3616.0</td>
      <td>1.701132</td>
      <td>M</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>19.0</td>
      <td>19.0</td>
      <td>6.0</td>
      <td>2.959677</td>
      <td>1.0</td>
      <td>0.024889</td>
    </tr>
    <tr>
      <th>Marvin Johnson (17/18)</th>
      <td>27.0</td>
      <td>26.749351</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>0.242915</td>
      <td>Championship, Championship Playoffs, FA Cup, L...</td>
      <td>left</td>
      <td>18.0</td>
      <td>1.0</td>
      <td>0.121457</td>
      <td>178.0</td>
      <td>25.0</td>
      <td>1.80</td>
      <td>741.0</td>
      <td>1.684000</td>
      <td>M</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>21.0</td>
      <td>2.0</td>
      <td>12.0</td>
      <td>0.832324</td>
      <td>0.0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Richard Smallwood (14/15)</th>
      <td>23.0</td>
      <td>19.504850</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>Championship, Championship Playoffs, FA Cup, L...</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>180.0</td>
      <td>2.0</td>
      <td>0.45</td>
      <td>20.0</td>
      <td>3.000000</td>
      <td>M</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>4.999418</td>
      <td>0.0</td>
      <td>0.000000</td>
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
      <td>443.000000</td>
      <td>351.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443</td>
      <td>324</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>356.000000</td>
      <td>443.000000</td>
      <td>330.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>351.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
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
      <td>201</td>
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
      <td>24.546275</td>
      <td>23.871039</td>
      <td>20.316027</td>
      <td>1.194131</td>
      <td>0.070201</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17.011287</td>
      <td>1.550790</td>
      <td>0.094877</td>
      <td>183.286517</td>
      <td>18.884876</td>
      <td>1.696327</td>
      <td>1235.817156</td>
      <td>1.267362</td>
      <td>NaN</td>
      <td>0.056433</td>
      <td>0.051919</td>
      <td>6.693002</td>
      <td>3.304740</td>
      <td>3.304740</td>
      <td>2.447119</td>
      <td>2.011287</td>
      <td>0.104350</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.633588</td>
      <td>4.733915</td>
      <td>18.171740</td>
      <td>2.060897</td>
      <td>0.138105</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.677963</td>
      <td>2.948889</td>
      <td>0.184480</td>
      <td>6.028752</td>
      <td>17.262750</td>
      <td>1.776398</td>
      <td>1257.427002</td>
      <td>0.840662</td>
      <td>NaN</td>
      <td>0.249838</td>
      <td>0.241628</td>
      <td>10.722988</td>
      <td>4.533899</td>
      <td>4.420709</td>
      <td>2.005552</td>
      <td>2.957062</td>
      <td>0.162198</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000000</td>
      <td>16.356256</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>167.000000</td>
      <td>0.000000</td>
      <td>0.038000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.265577</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>21.000000</td>
      <td>19.409023</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>179.000000</td>
      <td>3.000000</td>
      <td>0.375000</td>
      <td>96.000000</td>
      <td>0.769134</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.913092</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>24.000000</td>
      <td>23.907404</td>
      <td>17.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>183.000000</td>
      <td>15.000000</td>
      <td>1.130000</td>
      <td>828.000000</td>
      <td>1.356522</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.960341</td>
      <td>1.000000</td>
      <td>0.025568</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>27.000000</td>
      <td>26.554960</td>
      <td>37.000000</td>
      <td>2.000000</td>
      <td>0.107387</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.000000</td>
      <td>2.000000</td>
      <td>0.110328</td>
      <td>188.000000</td>
      <td>34.000000</td>
      <td>2.250000</td>
      <td>2124.000000</td>
      <td>1.702066</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>11.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>3.422384</td>
      <td>3.000000</td>
      <td>0.173961</td>
    </tr>
    <tr>
      <th>max</th>
      <td>40.000000</td>
      <td>37.607891</td>
      <td>73.000000</td>
      <td>12.000000</td>
      <td>1.406250</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>53.000000</td>
      <td>19.000000</td>
      <td>1.592920</td>
      <td>199.000000</td>
      <td>55.000000</td>
      <td>10.800000</td>
      <td>4770.000000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>42.000000</td>
      <td>27.000000</td>
      <td>22.000000</td>
      <td>10.998172</td>
      <td>13.000000</td>
      <td>1.800000</td>
    </tr>
  </tbody>
</table>
</div>




![png](boro_01_current_market_value_files/boro_01_current_market_value_65_0.png)





<style  type="text/css" >
    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col0 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col1 {
            background-color:  #cd423b;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col2 {
            background-color:  #b5cdfa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col3 {
            background-color:  #9ebeff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col4 {
            background-color:  #6a8bef;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col5 {
            background-color:  #b5cdfa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col6 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col7 {
            background-color:  #7597f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col8 {
            background-color:  #a5c3fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col9 {
            background-color:  #97b8ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col10 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col11 {
            background-color:  #abc8fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col12 {
            background-color:  #6b8df0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col13 {
            background-color:  #6282ea;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col14 {
            background-color:  #485fd1;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col15 {
            background-color:  #a7c5fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col16 {
            background-color:  #afcafc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col17 {
            background-color:  #86a9fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col18 {
            background-color:  #a3c2fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col19 {
            background-color:  #adc9fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col20 {
            background-color:  #8fb1fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col0 {
            background-color:  #d55042;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col1 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col2 {
            background-color:  #90b2fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col3 {
            background-color:  #90b2fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col4 {
            background-color:  #5e7de7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col5 {
            background-color:  #89acfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col6 {
            background-color:  #80a3fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col7 {
            background-color:  #7295f4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col8 {
            background-color:  #98b9ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col9 {
            background-color:  #7093f3;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col10 {
            background-color:  #8badfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col11 {
            background-color:  #799cf8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col12 {
            background-color:  #516ddb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col13 {
            background-color:  #4e68d8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col14 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col15 {
            background-color:  #a5c3fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col16 {
            background-color:  #a5c3fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col17 {
            background-color:  #80a3fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col18 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col19 {
            background-color:  #90b2fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col20 {
            background-color:  #81a4fb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col0 {
            background-color:  #97b8ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col1 {
            background-color:  #b3cdfb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col2 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col3 {
            background-color:  #f7b194;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col4 {
            background-color:  #aec9fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col5 {
            background-color:  #bb1b2c;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col6 {
            background-color:  #f5c1a9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col7 {
            background-color:  #adc9fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col8 {
            background-color:  #5977e3;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col9 {
            background-color:  #f18d6f;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col10 {
            background-color:  #c7d7f0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col11 {
            background-color:  #d75445;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col12 {
            background-color:  #94b6ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col13 {
            background-color:  #85a8fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col14 {
            background-color:  #81a4fb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col15 {
            background-color:  #bad0f8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col16 {
            background-color:  #f39475;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col17 {
            background-color:  #f7a688;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col18 {
            background-color:  #9abbff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col19 {
            background-color:  #f7aa8c;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col20 {
            background-color:  #abc8fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col0 {
            background-color:  #688aef;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col1 {
            background-color:  #a6c4fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col2 {
            background-color:  #f7b89c;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col3 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col4 {
            background-color:  #f1cdba;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col5 {
            background-color:  #f7bca1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col6 {
            background-color:  #f6bda2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col7 {
            background-color:  #b5cdfa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col8 {
            background-color:  #465ecf;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col9 {
            background-color:  #e2dad5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col10 {
            background-color:  #97b8ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col11 {
            background-color:  #f1cdba;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col12 {
            background-color:  #6e90f2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col13 {
            background-color:  #8caffe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col14 {
            background-color:  #5b7ae5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col15 {
            background-color:  #98b9ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col16 {
            background-color:  #f7b396;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col17 {
            background-color:  #d5dbe5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col18 {
            background-color:  #8fb1fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col19 {
            background-color:  #e7d7ce;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col20 {
            background-color:  #89acfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col0 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col1 {
            background-color:  #80a3fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col2 {
            background-color:  #a7c5fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col3 {
            background-color:  #f2cab5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col4 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col5 {
            background-color:  #93b5fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col6 {
            background-color:  #b5cdfa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col7 {
            background-color:  #b6cefa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col8 {
            background-color:  #506bda;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col9 {
            background-color:  #80a3fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col10 {
            background-color:  #7396f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col11 {
            background-color:  #6e90f2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col12 {
            background-color:  #90b2fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col13 {
            background-color:  #5977e3;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col14 {
            background-color:  #4a63d3;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col15 {
            background-color:  #81a4fb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col16 {
            background-color:  #ccd9ed;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col17 {
            background-color:  #c0d4f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col18 {
            background-color:  #89acfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col19 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col20 {
            background-color:  #5d7ce6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col0 {
            background-color:  #a1c0ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col1 {
            background-color:  #b7cff9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col2 {
            background-color:  #bb1b2c;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col3 {
            background-color:  #f7b093;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col4 {
            background-color:  #a5c3fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col5 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col6 {
            background-color:  #f2cbb7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col7 {
            background-color:  #9abbff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col8 {
            background-color:  #6485ec;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col9 {
            background-color:  #f08a6c;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col10 {
            background-color:  #c9d7f0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col11 {
            background-color:  #be242e;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col12 {
            background-color:  #90b2fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col13 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col14 {
            background-color:  #86a9fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col15 {
            background-color:  #b1cbfc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col16 {
            background-color:  #f7a688;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col17 {
            background-color:  #eed0c0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col18 {
            background-color:  #a7c5fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col19 {
            background-color:  #f59c7d;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col20 {
            background-color:  #abc8fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col0 {
            background-color:  #6282ea;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col1 {
            background-color:  #a9c6fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col2 {
            background-color:  #f5c0a7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col3 {
            background-color:  #f7b599;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col4 {
            background-color:  #bcd2f7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col5 {
            background-color:  #f0cdbb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col6 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col7 {
            background-color:  #f6bea4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col8 {
            background-color:  #5b7ae5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col9 {
            background-color:  #cbd8ee;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col10 {
            background-color:  #bcd2f7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col11 {
            background-color:  #d8dce2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col12 {
            background-color:  #6485ec;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col13 {
            background-color:  #5a78e4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col14 {
            background-color:  #5572df;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col15 {
            background-color:  #8fb1fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col16 {
            background-color:  #f6a283;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col17 {
            background-color:  #eed0c0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col18 {
            background-color:  #7699f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col19 {
            background-color:  #c9d7f0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col20 {
            background-color:  #7da0f9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col0 {
            background-color:  #5470de;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col1 {
            background-color:  #9fbfff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col2 {
            background-color:  #b1cbfc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col3 {
            background-color:  #c5d6f2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col4 {
            background-color:  #c0d4f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col5 {
            background-color:  #94b6ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col6 {
            background-color:  #f6bda2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col7 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col8 {
            background-color:  #5e7de7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col9 {
            background-color:  #7699f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col10 {
            background-color:  #afcafc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col11 {
            background-color:  #6788ee;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col12 {
            background-color:  #86a9fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col13 {
            background-color:  #4358cb;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col14 {
            background-color:  #4961d2;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col15 {
            background-color:  #7396f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col16 {
            background-color:  #d8dce2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col17 {
            background-color:  #d9dce1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col18 {
            background-color:  #6b8df0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col19 {
            background-color:  #799cf8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col20 {
            background-color:  #5f7fe8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col0 {
            background-color:  #6485ec;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col1 {
            background-color:  #a3c2fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col2 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col3 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col4 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col5 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col6 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col7 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col8 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col9 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col10 {
            background-color:  #4e68d8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col11 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col12 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col13 {
            background-color:  #4055c8;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col14 {
            background-color:  #465ecf;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col15 {
            background-color:  #81a4fb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col16 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col17 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col18 {
            background-color:  #a2c1ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col19 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col20 {
            background-color:  #445acc;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col0 {
            background-color:  #89acfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col1 {
            background-color:  #abc8fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col2 {
            background-color:  #ee8468;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col3 {
            background-color:  #efcebd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col4 {
            background-color:  #9dbdff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col5 {
            background-color:  #ee8669;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col6 {
            background-color:  #d5dbe5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col7 {
            background-color:  #86a9fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col8 {
            background-color:  #6f92f3;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col9 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col10 {
            background-color:  #7093f3;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col11 {
            background-color:  #f49a7b;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col12 {
            background-color:  #9ebeff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col13 {
            background-color:  #6c8ff1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col14 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col15 {
            background-color:  #8fb1fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col16 {
            background-color:  #f1cdba;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col17 {
            background-color:  #e4d9d2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col18 {
            background-color:  #a5c3fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col19 {
            background-color:  #f1cdba;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col20 {
            background-color:  #a2c1ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col0 {
            background-color:  #6687ed;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col1 {
            background-color:  #b5cdfa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col2 {
            background-color:  #ccd9ed;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col3 {
            background-color:  #abc8fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col4 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col5 {
            background-color:  #c6d6f1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col6 {
            background-color:  #c0d4f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col7 {
            background-color:  #b1cbfc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col8 {
            background-color:  #7396f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col9 {
            background-color:  #6180e9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col10 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col11 {
            background-color:  #b1cbfc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col12 {
            background-color:  #3d50c3;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col13 {
            background-color:  #5875e1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col14 {
            background-color:  #3f53c6;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col15 {
            background-color:  #afcafc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col16 {
            background-color:  #d5dbe5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col17 {
            background-color:  #aac7fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col18 {
            background-color:  #6e90f2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col19 {
            background-color:  #b9d0f9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col20 {
            background-color:  #779af7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col0 {
            background-color:  #a6c4fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col1 {
            background-color:  #b9d0f9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col2 {
            background-color:  #d44e41;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col3 {
            background-color:  #f7bca1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col4 {
            background-color:  #94b6ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col5 {
            background-color:  #be242e;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col6 {
            background-color:  #e4d9d2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col7 {
            background-color:  #80a3fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col8 {
            background-color:  #779af7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col9 {
            background-color:  #f4987a;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col10 {
            background-color:  #c1d4f4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col11 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col12 {
            background-color:  #85a8fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col13 {
            background-color:  #7b9ff9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col14 {
            background-color:  #89acfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col15 {
            background-color:  #a2c1ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col16 {
            background-color:  #f3c7b1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col17 {
            background-color:  #bed2f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col18 {
            background-color:  #b5cdfa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col19 {
            background-color:  #f39778;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col20 {
            background-color:  #a5c3fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col0 {
            background-color:  #7597f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col1 {
            background-color:  #a7c5fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col2 {
            background-color:  #bbd1f8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col3 {
            background-color:  #a9c6fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col4 {
            background-color:  #bed2f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col5 {
            background-color:  #aec9fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col6 {
            background-color:  #90b2fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col7 {
            background-color:  #abc8fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col8 {
            background-color:  #88abfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col9 {
            background-color:  #b2ccfb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col10 {
            background-color:  #6687ed;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col11 {
            background-color:  #94b6ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col12 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col13 {
            background-color:  #465ecf;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col14 {
            background-color:  #5a78e4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col15 {
            background-color:  #89acfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col16 {
            background-color:  #b7cff9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col17 {
            background-color:  #b3cdfb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col18 {
            background-color:  #9dbdff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col19 {
            background-color:  #94b6ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col20 {
            background-color:  #82a6fb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col0 {
            background-color:  #6687ed;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col1 {
            background-color:  #9fbfff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col2 {
            background-color:  #aac7fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col3 {
            background-color:  #bcd2f7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col4 {
            background-color:  #8caffe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col5 {
            background-color:  #9fbfff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col6 {
            background-color:  #81a4fb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col7 {
            background-color:  #688aef;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col8 {
            background-color:  #89acfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col9 {
            background-color:  #81a4fb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col10 {
            background-color:  #7a9df8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col11 {
            background-color:  #86a9fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col12 {
            background-color:  #4055c8;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col13 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col14 {
            background-color:  #455cce;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col15 {
            background-color:  #9abbff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col16 {
            background-color:  #b6cefa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col17 {
            background-color:  #a1c0ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col18 {
            background-color:  #aec9fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col19 {
            background-color:  #adc9fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col20 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col0 {
            background-color:  #4055c8;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col1 {
            background-color:  #85a8fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col2 {
            background-color:  #9dbdff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col3 {
            background-color:  #8badfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col4 {
            background-color:  #7295f4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col5 {
            background-color:  #98b9ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col6 {
            background-color:  #7295f4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col7 {
            background-color:  #6384eb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col8 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col9 {
            background-color:  #8caffe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col10 {
            background-color:  #5875e1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col11 {
            background-color:  #89acfd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col12 {
            background-color:  #4a63d3;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col13 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col14 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col15 {
            background-color:  #7ea1fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col16 {
            background-color:  #96b7ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col17 {
            background-color:  #85a8fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col18 {
            background-color:  #a1c0ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col19 {
            background-color:  #b9d0f9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col20 {
            background-color:  #7ea1fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col0 {
            background-color:  #7b9ff9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col1 {
            background-color:  #bed2f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col2 {
            background-color:  #b2ccfb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col3 {
            background-color:  #9ebeff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col4 {
            background-color:  #7ea1fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col5 {
            background-color:  #9ebeff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col6 {
            background-color:  #82a6fb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col7 {
            background-color:  #6384eb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col8 {
            background-color:  #93b5fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col9 {
            background-color:  #6e90f2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col10 {
            background-color:  #a1c0ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col11 {
            background-color:  #7da0f9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col12 {
            background-color:  #4f69d9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col13 {
            background-color:  #6788ee;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col14 {
            background-color:  #5470de;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col15 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col16 {
            background-color:  #b5cdfa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col17 {
            background-color:  #c3d5f4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col18 {
            background-color:  #5b7ae5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col19 {
            background-color:  #85a8fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col20 {
            background-color:  #6e90f2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col0 {
            background-color:  #7295f4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col1 {
            background-color:  #afcafc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col2 {
            background-color:  #f59f80;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col3 {
            background-color:  #f7b89c;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col4 {
            background-color:  #bed2f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col5 {
            background-color:  #f7b599;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col6 {
            background-color:  #f7ad90;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col7 {
            background-color:  #c4d5f3;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col8 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col9 {
            background-color:  #dfdbd9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col10 {
            background-color:  #c0d4f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col11 {
            background-color:  #e3d9d3;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col12 {
            background-color:  #7396f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col13 {
            background-color:  #779af7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col14 {
            background-color:  #5a78e4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col15 {
            background-color:  #a6c4fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col16 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col17 {
            background-color:  #f7b599;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col18 {
            background-color:  #779af7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col19 {
            background-color:  #dcdddd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col20 {
            background-color:  #96b7ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col0 {
            background-color:  #4e68d8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col1 {
            background-color:  #96b7ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col2 {
            background-color:  #f7ad90;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col3 {
            background-color:  #d5dbe5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col4 {
            background-color:  #b9d0f9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col5 {
            background-color:  #e3d9d3;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col6 {
            background-color:  #e7d7ce;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col7 {
            background-color:  #cdd9ec;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col8 {
            background-color:  #455cce;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col9 {
            background-color:  #d1dae9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col10 {
            background-color:  #93b5fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col11 {
            background-color:  #96b7ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col12 {
            background-color:  #799cf8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col13 {
            background-color:  #6788ee;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col14 {
            background-color:  #536edd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col15 {
            background-color:  #bed2f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col16 {
            background-color:  #f7b194;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col17 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col18 {
            background-color:  #6a8bef;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col19 {
            background-color:  #a1c0ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col20 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col0 {
            background-color:  #5673e0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col1 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col2 {
            background-color:  #7295f4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col3 {
            background-color:  #7699f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col4 {
            background-color:  #6788ee;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col5 {
            background-color:  #7699f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col6 {
            background-color:  #485fd1;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col7 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col8 {
            background-color:  #97b8ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col9 {
            background-color:  #6788ee;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col10 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col11 {
            background-color:  #7597f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col12 {
            background-color:  #445acc;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col13 {
            background-color:  #5f7fe8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col14 {
            background-color:  #5a78e4;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col15 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col16 {
            background-color:  #6b8df0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col17 {
            background-color:  #516ddb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col18 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col19 {
            background-color:  #7396f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col20 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col0 {
            background-color:  #8fb1fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col1 {
            background-color:  #b6cefa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col2 {
            background-color:  #f7aa8c;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col3 {
            background-color:  #edd1c2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col4 {
            background-color:  #8db0fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col5 {
            background-color:  #f59f80;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col6 {
            background-color:  #c7d7f0;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col7 {
            background-color:  #7699f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col8 {
            background-color:  #5b7ae5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col9 {
            background-color:  #ecd3c5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col10 {
            background-color:  #b5cdfa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col11 {
            background-color:  #f5a081;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col12 {
            background-color:  #6a8bef;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col13 {
            background-color:  #8caffe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col14 {
            background-color:  #a2c1ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col15 {
            background-color:  #92b4fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col16 {
            background-color:  #ead5c9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col17 {
            background-color:  #b2ccfb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col18 {
            background-color:  #9ebeff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col19 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col20 {
            background-color:  #f1cdba;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col0 {
            background-color:  #7ea1fa;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col1 {
            background-color:  #b7cff9;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col2 {
            background-color:  #bad0f8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col3 {
            background-color:  #aac7fd;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col4 {
            background-color:  #7a9df8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col5 {
            background-color:  #b2ccfb;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col6 {
            background-color:  #8db0fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col7 {
            background-color:  #6e90f2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col8 {
            background-color:  #779af7;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col9 {
            background-color:  #a1c0ff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col10 {
            background-color:  #84a7fc;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col11 {
            background-color:  #9dbdff;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col12 {
            background-color:  #6788ee;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col13 {
            background-color:  #6e90f2;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col14 {
            background-color:  #7396f5;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col15 {
            background-color:  #8caffe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col16 {
            background-color:  #bed2f6;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col17 {
            background-color:  #a7c5fe;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col18 {
            background-color:  #7a9df8;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col19 {
            background-color:  #f3c7b1;
            color:  #000000;
        }    #T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col20 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }</style><table id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Age</th>        <th class="col_heading level0 col1" >Age when joined</th>        <th class="col_heading level0 col2" >Appearances</th>        <th class="col_heading level0 col3" >Assists</th>        <th class="col_heading level0 col4" >Assists p90</th>        <th class="col_heading level0 col5" >Games started</th>        <th class="col_heading level0 col6" >Goals</th>        <th class="col_heading level0 col7" >Goals p90</th>        <th class="col_heading level0 col8" >Height</th>        <th class="col_heading level0 col9" >In squad</th>        <th class="col_heading level0 col10" >Market value</th>        <th class="col_heading level0 col11" >Minutes played</th>        <th class="col_heading level0 col12" >PPG</th>        <th class="col_heading level0 col13" >Red cards</th>        <th class="col_heading level0 col14" >Second yellow cards</th>        <th class="col_heading level0 col15" >Shirt number</th>        <th class="col_heading level0 col16" >Substitutions off</th>        <th class="col_heading level0 col17" >Substitutions on</th>        <th class="col_heading level0 col18" >Years in team</th>        <th class="col_heading level0 col19" >Yellow cards</th>        <th class="col_heading level0 col20" >Yellow cards p90</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row0" class="row_heading level0 row0" >Age</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col0" class="data row0 col0" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col1" class="data row0 col1" >0.900996</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col2" class="data row0 col2" >0.258555</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col3" class="data row0 col3" >0.125336</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col4" class="data row0 col4" >-0.026358</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col5" class="data row0 col5" >0.288462</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col6" class="data row0 col6" >0.102279</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col7" class="data row0 col7" >0.061125</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col8" class="data row0 col8" >0.113264</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col9" class="data row0 col9" >0.221408</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col10" class="data row0 col10" >0.117090</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col11" class="data row0 col11" >0.304200</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col12" class="data row0 col12" >0.160212</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col13" class="data row0 col13" >0.115977</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col14" class="data row0 col14" >-0.003161</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col15" class="data row0 col15" >0.181333</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col16" class="data row0 col16" >0.152413</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col17" class="data row0 col17" >0.039790</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col18" class="data row0 col18" >0.066960</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col19" class="data row0 col19" >0.236661</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row0_col20" class="data row0 col20" >0.188848</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row1" class="row_heading level0 row1" >Age when joined</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col0" class="data row1 col0" >0.900996</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col1" class="data row1 col1" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col2" class="data row1 col2" >0.131922</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col3" class="data row1 col3" >0.077928</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col4" class="data row1 col4" >-0.068412</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col5" class="data row1 col5" >0.147501</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col6" class="data row1 col6" >0.089730</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col7" class="data row1 col7" >0.050570</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col8" class="data row1 col8" >0.066208</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col9" class="data row1 col9" >0.101115</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col10" class="data row1 col10" >0.136889</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col11" class="data row1 col11" >0.152172</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col12" class="data row1 col12" >0.085178</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col13" class="data row1 col13" >0.053806</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col14" class="data row1 col14" >-0.050958</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col15" class="data row1 col15" >0.172524</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col16" class="data row1 col16" >0.113852</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col17" class="data row1 col17" >0.016547</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col18" class="data row1 col18" >-0.360585</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col19" class="data row1 col19" >0.141121</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row1_col20" class="data row1 col20" >0.148697</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row2" class="row_heading level0 row2" >Appearances</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col0" class="data row2 col0" >0.258555</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col1" class="data row2 col1" >0.131922</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col2" class="data row2 col2" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col3" class="data row2 col3" >0.610032</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col4" class="data row2 col4" >0.211990</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col5" class="data row2 col5" >0.976616</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col6" class="data row2 col6" >0.578162</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col7" class="data row2 col7" >0.243098</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col8" class="data row2 col8" >-0.170048</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col9" class="data row2 col9" >0.763202</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col10" class="data row2 col10" >0.344950</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col11" class="data row2 col11" >0.892679</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col12" class="data row2 col12" >0.278416</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col13" class="data row2 col13" >0.219318</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col14" class="data row2 col14" >0.175568</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col15" class="data row2 col15" >0.247172</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col16" class="data row2 col16" >0.690395</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col17" class="data row2 col17" >0.647042</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col18" class="data row2 col18" >0.031789</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col19" class="data row2 col19" >0.655910</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row2_col20" class="data row2 col20" >0.277310</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row3" class="row_heading level0 row3" >Assists</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col0" class="data row3 col0" >0.125336</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col1" class="data row3 col1" >0.077928</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col2" class="data row3 col2" >0.610032</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col3" class="data row3 col3" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col4" class="data row3 col4" >0.507668</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col5" class="data row3 col5" >0.611500</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col6" class="data row3 col6" >0.594013</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col7" class="data row3 col7" >0.271628</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col8" class="data row3 col8" >-0.244851</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col9" class="data row3 col9" >0.482540</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col10" class="data row3 col10" >0.175731</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col11" class="data row3 col11" >0.571887</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col12" class="data row3 col12" >0.168285</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col13" class="data row3 col13" >0.237923</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col14" class="data row3 col14" >0.061494</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col15" class="data row3 col15" >0.126682</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col16" class="data row3 col16" >0.583726</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col17" class="data row3 col17" >0.338919</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col18" class="data row3 col18" >-0.014848</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col19" class="data row3 col19" >0.468894</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row3_col20" class="data row3 col20" >0.171598</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row4" class="row_heading level0 row4" >Assists p90</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col0" class="data row4 col0" >-0.026358</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col1" class="data row4 col1" >-0.068412</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col2" class="data row4 col2" >0.211990</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col3" class="data row4 col3" >0.507668</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col4" class="data row4 col4" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col5" class="data row4 col5" >0.176049</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col6" class="data row4 col6" >0.264478</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col7" class="data row4 col7" >0.275785</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col8" class="data row4 col8" >-0.206189</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col9" class="data row4 col9" >0.150289</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col10" class="data row4 col10" >0.062661</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col11" class="data row4 col11" >0.119566</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col12" class="data row4 col12" >0.266670</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col13" class="data row4 col13" >0.091145</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col14" class="data row4 col14" >0.005090</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col15" class="data row4 col15" >0.047953</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col16" class="data row4 col16" >0.269139</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col17" class="data row4 col17" >0.247051</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col18" class="data row4 col18" >-0.031969</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col19" class="data row4 col19" >0.099751</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row4_col20" class="data row4 col20" >0.033540</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row5" class="row_heading level0 row5" >Games started</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col0" class="data row5 col0" >0.288462</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col1" class="data row5 col1" >0.147501</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col2" class="data row5 col2" >0.976616</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col3" class="data row5 col3" >0.611500</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col4" class="data row5 col4" >0.176049</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col5" class="data row5 col5" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col6" class="data row5 col6" >0.537869</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col7" class="data row5 col7" >0.180663</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col8" class="data row5 col8" >-0.123370</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col9" class="data row5 col9" >0.769108</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col10" class="data row5 col10" >0.348770</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col11" class="data row5 col11" >0.967807</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col12" class="data row5 col12" >0.265845</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col13" class="data row5 col13" >0.216438</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col14" class="data row5 col14" >0.193944</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col15" class="data row5 col15" >0.213407</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col16" class="data row5 col16" >0.633307</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col17" class="data row5 col17" >0.467992</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col18" class="data row5 col18" >0.083192</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col19" class="data row5 col19" >0.705072</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row5_col20" class="data row5 col20" >0.278026</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row6" class="row_heading level0 row6" >Goals</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col0" class="data row6 col0" >0.102279</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col1" class="data row6 col1" >0.089730</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col2" class="data row6 col2" >0.578162</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col3" class="data row6 col3" >0.594013</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col4" class="data row6 col4" >0.264478</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col5" class="data row6 col5" >0.537869</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col6" class="data row6 col6" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col7" class="data row6 col7" >0.593822</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col8" class="data row6 col8" >-0.158428</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col9" class="data row6 col9" >0.387819</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col10" class="data row6 col10" >0.304181</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col11" class="data row6 col11" >0.456306</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col12" class="data row6 col12" >0.140300</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col13" class="data row6 col13" >0.092833</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col14" class="data row6 col14" >0.042331</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col15" class="data row6 col15" >0.095583</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col16" class="data row6 col16" >0.649061</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col17" class="data row6 col17" >0.469047</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col18" class="data row6 col18" >-0.106063</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col19" class="data row6 col19" >0.333721</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row6_col20" class="data row6 col20" >0.132644</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row7" class="row_heading level0 row7" >Goals p90</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col0" class="data row7 col0" >0.061125</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col1" class="data row7 col1" >0.050570</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col2" class="data row7 col2" >0.243098</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col3" class="data row7 col3" >0.271628</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col4" class="data row7 col4" >0.275785</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col5" class="data row7 col5" >0.180663</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col6" class="data row7 col6" >0.593822</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col7" class="data row7 col7" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col8" class="data row7 col8" >-0.149441</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col9" class="data row7 col9" >0.116905</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col10" class="data row7 col10" >0.256754</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col11" class="data row7 col11" >0.096441</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col12" class="data row7 col12" >0.239299</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col13" class="data row7 col13" >0.017258</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col14" class="data row7 col14" >-0.000539</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col15" class="data row7 col15" >0.001438</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col16" class="data row7 col16" >0.326453</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col17" class="data row7 col17" >0.358562</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col18" class="data row7 col18" >-0.148328</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col19" class="data row7 col19" >0.063021</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row7_col20" class="data row7 col20" >0.038569</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row8" class="row_heading level0 row8" >Height</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col0" class="data row8 col0" >0.113264</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col1" class="data row8 col1" >0.066208</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col2" class="data row8 col2" >-0.170048</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col3" class="data row8 col3" >-0.244851</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col4" class="data row8 col4" >-0.206189</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col5" class="data row8 col5" >-0.123370</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col6" class="data row8 col6" >-0.158428</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col7" class="data row8 col7" >-0.149441</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col8" class="data row8 col8" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col9" class="data row8 col9" >-0.082039</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col10" class="data row8 col10" >-0.067006</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col11" class="data row8 col11" >-0.052678</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col12" class="data row8 col12" >0.007870</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col13" class="data row8 col13" >0.010496</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col14" class="data row8 col14" >-0.006257</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col15" class="data row8 col15" >0.047759</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col16" class="data row8 col16" >-0.299955</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col17" class="data row8 col17" >-0.252515</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col18" class="data row8 col18" >0.063536</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col19" class="data row8 col19" >-0.160931</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row8_col20" class="data row8 col20" >-0.053055</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row9" class="row_heading level0 row9" >In squad</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col0" class="data row9 col0" >0.221408</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col1" class="data row9 col1" >0.101115</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col2" class="data row9 col2" >0.763202</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col3" class="data row9 col3" >0.482540</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col4" class="data row9 col4" >0.150289</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col5" class="data row9 col5" >0.769108</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col6" class="data row9 col6" >0.387819</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col7" class="data row9 col7" >0.116905</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col8" class="data row9 col8" >-0.082039</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col9" class="data row9 col9" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col10" class="data row9 col10" >0.051447</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col11" class="data row9 col11" >0.733443</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col12" class="data row9 col12" >0.302692</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col13" class="data row9 col13" >0.150490</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col14" class="data row9 col14" >0.184767</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col15" class="data row9 col15" >0.094165</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col16" class="data row9 col16" >0.470527</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col17" class="data row9 col17" >0.409585</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col18" class="data row9 col18" >0.072339</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col19" class="data row9 col19" >0.526645</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row9_col20" class="data row9 col20" >0.248787</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row10" class="row_heading level0 row10" >Market value</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col0" class="data row10 col0" >0.117090</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col1" class="data row10 col1" >0.136889</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col2" class="data row10 col2" >0.344950</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col3" class="data row10 col3" >0.175731</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col4" class="data row10 col4" >0.062661</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col5" class="data row10 col5" >0.348770</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col6" class="data row10 col6" >0.304181</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col7" class="data row10 col7" >0.256754</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col8" class="data row10 col8" >-0.067006</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col9" class="data row10 col9" >0.051447</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col10" class="data row10 col10" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col11" class="data row10 col11" >0.320965</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col12" class="data row10 col12" >0.016658</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col13" class="data row10 col13" >0.085411</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col14" class="data row10 col14" >-0.033499</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col15" class="data row10 col15" >0.209681</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col16" class="data row10 col16" >0.314466</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col17" class="data row10 col17" >0.163877</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col18" class="data row10 col18" >-0.140711</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col19" class="data row10 col19" >0.274550</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row10_col20" class="data row10 col20" >0.117421</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row11" class="row_heading level0 row11" >Minutes played</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col0" class="data row11 col0" >0.304200</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col1" class="data row11 col1" >0.152172</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col2" class="data row11 col2" >0.892679</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col3" class="data row11 col3" >0.571887</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col4" class="data row11 col4" >0.119566</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col5" class="data row11 col5" >0.967807</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col6" class="data row11 col6" >0.456306</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col7" class="data row11 col7" >0.096441</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col8" class="data row11 col8" >-0.052678</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col9" class="data row11 col9" >0.733443</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col10" class="data row11 col10" >0.320965</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col11" class="data row11 col11" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col12" class="data row11 col12" >0.234778</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col13" class="data row11 col13" >0.192197</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col14" class="data row11 col14" >0.200474</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col15" class="data row11 col15" >0.163216</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col16" class="data row11 col16" >0.500984</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col17" class="data row11 col17" >0.237128</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col18" class="data row11 col18" >0.138704</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col19" class="data row11 col19" >0.716849</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row11_col20" class="data row11 col20" >0.255826</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row12" class="row_heading level0 row12" >PPG</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col0" class="data row12 col0" >0.160212</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col1" class="data row12 col1" >0.085178</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col2" class="data row12 col2" >0.278416</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col3" class="data row12 col3" >0.168285</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col4" class="data row12 col4" >0.266670</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col5" class="data row12 col5" >0.265845</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col6" class="data row12 col6" >0.140300</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col7" class="data row12 col7" >0.239299</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col8" class="data row12 col8" >0.007870</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col9" class="data row12 col9" >0.302692</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col10" class="data row12 col10" >0.016658</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col11" class="data row12 col11" >0.234778</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col12" class="data row12 col12" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col13" class="data row12 col13" >0.029201</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col14" class="data row12 col14" >0.058818</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col15" class="data row12 col15" >0.075189</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col16" class="data row12 col16" >0.184309</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col17" class="data row12 col17" >0.201639</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col18" class="data row12 col18" >0.039308</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col19" class="data row12 col19" >0.155542</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row12_col20" class="data row12 col20" >0.150259</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row13" class="row_heading level0 row13" >Red cards</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col0" class="data row13 col0" >0.115977</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col1" class="data row13 col1" >0.053806</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col2" class="data row13 col2" >0.219318</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col3" class="data row13 col3" >0.237923</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col4" class="data row13 col4" >0.091145</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col5" class="data row13 col5" >0.216438</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col6" class="data row13 col6" >0.092833</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col7" class="data row13 col7" >0.017258</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col8" class="data row13 col8" >0.010496</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col9" class="data row13 col9" >0.150490</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col10" class="data row13 col10" >0.085411</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col11" class="data row13 col11" >0.192197</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col12" class="data row13 col12" >0.029201</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col13" class="data row13 col13" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col14" class="data row13 col14" >-0.011167</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col15" class="data row13 col15" >0.133158</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col16" class="data row13 col16" >0.178523</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col17" class="data row13 col17" >0.133931</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col18" class="data row13 col18" >0.108985</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col19" class="data row13 col19" >0.238002</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row13_col20" class="data row13 col20" >0.153016</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row14" class="row_heading level0 row14" >Second yellow cards</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col0" class="data row14 col0" >-0.003161</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col1" class="data row14 col1" >-0.050958</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col2" class="data row14 col2" >0.175568</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col3" class="data row14 col3" >0.061494</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col4" class="data row14 col4" >0.005090</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col5" class="data row14 col5" >0.193944</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col6" class="data row14 col6" >0.042331</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col7" class="data row14 col7" >-0.000539</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col8" class="data row14 col8" >-0.006257</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col9" class="data row14 col9" >0.184767</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col10" class="data row14 col10" >-0.033499</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col11" class="data row14 col11" >0.200474</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col12" class="data row14 col12" >0.058818</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col13" class="data row14 col13" >-0.011167</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col14" class="data row14 col14" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col15" class="data row14 col15" >0.035854</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col16" class="data row14 col16" >0.059872</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col17" class="data row14 col17" >0.033870</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col18" class="data row14 col18" >0.059122</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col19" class="data row14 col19" >0.274657</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row14_col20" class="data row14 col20" >0.137649</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row15" class="row_heading level0 row15" >Shirt number</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col0" class="data row15 col0" >0.181333</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col1" class="data row15 col1" >0.172524</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col2" class="data row15 col2" >0.247172</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col3" class="data row15 col3" >0.126682</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col4" class="data row15 col4" >0.047953</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col5" class="data row15 col5" >0.213407</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col6" class="data row15 col6" >0.095583</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col7" class="data row15 col7" >0.001438</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col8" class="data row15 col8" >0.047759</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col9" class="data row15 col9" >0.094165</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col10" class="data row15 col10" >0.209681</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col11" class="data row15 col11" >0.163216</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col12" class="data row15 col12" >0.075189</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col13" class="data row15 col13" >0.133158</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col14" class="data row15 col14" >0.035854</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col15" class="data row15 col15" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col16" class="data row15 col16" >0.175369</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col17" class="data row15 col17" >0.259182</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col18" class="data row15 col18" >-0.217082</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col19" class="data row15 col19" >0.104568</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row15_col20" class="data row15 col20" >0.086899</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row16" class="row_heading level0 row16" >Substitutions off</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col0" class="data row16 col0" >0.152413</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col1" class="data row16 col1" >0.113852</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col2" class="data row16 col2" >0.690395</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col3" class="data row16 col3" >0.583726</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col4" class="data row16 col4" >0.269139</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col5" class="data row16 col5" >0.633307</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col6" class="data row16 col6" >0.649061</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col7" class="data row16 col7" >0.326453</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col8" class="data row16 col8" >-0.299955</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col9" class="data row16 col9" >0.470527</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col10" class="data row16 col10" >0.314466</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col11" class="data row16 col11" >0.500984</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col12" class="data row16 col12" >0.184309</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col13" class="data row16 col13" >0.178523</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col14" class="data row16 col14" >0.059872</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col15" class="data row16 col15" >0.175369</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col16" class="data row16 col16" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col17" class="data row16 col17" >0.591923</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col18" class="data row16 col18" >-0.101272</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col19" class="data row16 col19" >0.418244</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row16_col20" class="data row16 col20" >0.211061</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row17" class="row_heading level0 row17" >Substitutions on</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col0" class="data row17 col0" >0.039790</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col1" class="data row17 col1" >0.016547</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col2" class="data row17 col2" >0.647042</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col3" class="data row17 col3" >0.338919</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col4" class="data row17 col4" >0.247051</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col5" class="data row17 col5" >0.467992</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col6" class="data row17 col6" >0.469047</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col7" class="data row17 col7" >0.358562</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col8" class="data row17 col8" >-0.252515</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col9" class="data row17 col9" >0.409585</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col10" class="data row17 col10" >0.163877</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col11" class="data row17 col11" >0.237128</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col12" class="data row17 col12" >0.201639</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col13" class="data row17 col13" >0.133931</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col14" class="data row17 col14" >0.033870</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col15" class="data row17 col15" >0.259182</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col16" class="data row17 col16" >0.591923</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col17" class="data row17 col17" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col18" class="data row17 col18" >-0.157537</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col19" class="data row17 col19" >0.195653</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row17_col20" class="data row17 col20" >0.153895</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row18" class="row_heading level0 row18" >Years in team</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col0" class="data row18 col0" >0.066960</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col1" class="data row18 col1" >-0.360585</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col2" class="data row18 col2" >0.031789</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col3" class="data row18 col3" >-0.014848</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col4" class="data row18 col4" >-0.031969</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col5" class="data row18 col5" >0.083192</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col6" class="data row18 col6" >-0.106063</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col7" class="data row18 col7" >-0.148328</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col8" class="data row18 col8" >0.063536</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col9" class="data row18 col9" >0.072339</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col10" class="data row18 col10" >-0.140711</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col11" class="data row18 col11" >0.138704</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col12" class="data row18 col12" >0.039308</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col13" class="data row18 col13" >0.108985</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col14" class="data row18 col14" >0.059122</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col15" class="data row18 col15" >-0.217082</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col16" class="data row18 col16" >-0.101272</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col17" class="data row18 col17" >-0.157537</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col18" class="data row18 col18" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col19" class="data row18 col19" >0.047260</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row18_col20" class="data row18 col20" >-0.089632</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row19" class="row_heading level0 row19" >Yellow cards</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col0" class="data row19 col0" >0.236661</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col1" class="data row19 col1" >0.141121</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col2" class="data row19 col2" >0.655910</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col3" class="data row19 col3" >0.468894</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col4" class="data row19 col4" >0.099751</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col5" class="data row19 col5" >0.705072</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col6" class="data row19 col6" >0.333721</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col7" class="data row19 col7" >0.063021</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col8" class="data row19 col8" >-0.160931</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col9" class="data row19 col9" >0.526645</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col10" class="data row19 col10" >0.274550</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col11" class="data row19 col11" >0.716849</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col12" class="data row19 col12" >0.155542</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col13" class="data row19 col13" >0.238002</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col14" class="data row19 col14" >0.274657</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col15" class="data row19 col15" >0.104568</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col16" class="data row19 col16" >0.418244</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col17" class="data row19 col17" >0.195653</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col18" class="data row19 col18" >0.047260</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col19" class="data row19 col19" >1.000000</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row19_col20" class="data row19 col20" >0.553733</td>
            </tr>
            <tr>
                        <th id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131level0_row20" class="row_heading level0 row20" >Yellow cards p90</th>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col0" class="data row20 col0" >0.188848</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col1" class="data row20 col1" >0.148697</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col2" class="data row20 col2" >0.277310</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col3" class="data row20 col3" >0.171598</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col4" class="data row20 col4" >0.033540</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col5" class="data row20 col5" >0.278026</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col6" class="data row20 col6" >0.132644</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col7" class="data row20 col7" >0.038569</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col8" class="data row20 col8" >-0.053055</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col9" class="data row20 col9" >0.248787</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col10" class="data row20 col10" >0.117421</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col11" class="data row20 col11" >0.255826</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col12" class="data row20 col12" >0.150259</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col13" class="data row20 col13" >0.153016</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col14" class="data row20 col14" >0.137649</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col15" class="data row20 col15" >0.086899</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col16" class="data row20 col16" >0.211061</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col17" class="data row20 col17" >0.153895</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col18" class="data row20 col18" >-0.089632</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col19" class="data row20 col19" >0.553733</td>
                        <td id="T_9736a2d9_bc9e_11ea_be44_74d83eb26131row20_col20" class="data row20 col20" >1.000000</td>
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






    (443, 24)



## 4. Modelling

* Select Modelling Technique
* Generate Test Design
* Build Model
* Assess Model

    
    
    Selected numeric features are: ['Shirt number', 'Height', 'Age', 'Years in team', 'In squad', 'Appearances', 'Substitutions on', 'Substitutions off', 'Goals', 'Assists', 'Yellow cards', 'Second yellow cards', 'Red cards', 'PPG', 'Minutes played', 'Goals p90', 'Assists p90', 'Yellow cards p90']
    

    
    
    Selected categorical features are: ['Foot', 'Position group', 'Competition']
    

    
    
    Dropping nulls during data preparation: False
    

    
    
    Train data has shape: (297, 21)
    Test data has shape: (33, 21)
    

    
    
    Full model grid-space to tune hyperparameters across...
    




    GridSearchCV(cv=KFold(n_splits=10, random_state=4, shuffle=True),
                 error_score=nan,
                 estimator=Pipeline(memory=None,
                                    steps=[('preprocessor',
                                            ColumnTransformer(n_jobs=None,
                                                              remainder='drop',
                                                              sparse_threshold=0.3,
                                                              transformer_weights=None,
                                                              transformers=[('num',
                                                                             Pipeline(memory=None,
                                                                                      steps=[('imputer',
                                                                                              SimpleImputer(add_indicator=False,
                                                                                                            copy=True,
                                                                                                            fill_value=None,
                                                                                                            miss...
                                                                  n_jobs=None,
                                                                  oob_score=False,
                                                                  random_state=None,
                                                                  verbose=0,
                                                                  warm_start=False))],
                                    verbose=False),
                 iid='deprecated', n_jobs=None,
                 param_grid={'estimator__max_depth': [2, 4, 6],
                             'estimator__min_samples_split': [2, 4, 6],
                             'estimator__n_estimators': [10, 20, 30],
                             'estimator__random_state': [4]},
                 pre_dispatch='2*n_jobs', refit=True, return_train_score=False,
                 scoring=None, verbose=0)



    
    
    Final tuned model...
    




    Pipeline(memory=None,
             steps=[('preprocessor',
                     ColumnTransformer(n_jobs=None, remainder='drop',
                                       sparse_threshold=0.3,
                                       transformer_weights=None,
                                       transformers=[('num',
                                                      Pipeline(memory=None,
                                                               steps=[('imputer',
                                                                       SimpleImputer(add_indicator=False,
                                                                                     copy=True,
                                                                                     fill_value=None,
                                                                                     missing_values=nan,
                                                                                     strategy='median',
                                                                                     verbose=0)),
                                                                      ('scaler',
                                                                       MinMaxScaler(copy=True,
                                                                                    feature_ran...
                     RandomForestRegressor(bootstrap=True, ccp_alpha=0.0,
                                           criterion='mse', max_depth=6,
                                           max_features='auto', max_leaf_nodes=None,
                                           max_samples=None,
                                           min_impurity_decrease=0.0,
                                           min_impurity_split=None,
                                           min_samples_leaf=1, min_samples_split=2,
                                           min_weight_fraction_leaf=0.0,
                                           n_estimators=30, n_jobs=None,
                                           oob_score=False, random_state=4,
                                           verbose=0, warm_start=False))],
             verbose=False)



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
      <td>0.467582</td>
      <td>0.638176</td>
    </tr>
    <tr>
      <th>RMSE</th>
      <td>0.890574</td>
      <td>1.761232</td>
    </tr>
    <tr>
      <th>R^2</th>
      <td>0.739628</td>
      <td>0.217696</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** Switching from linear regression models to a random forest ensemble has massively improved the training scores... and also caused a smaller uptick in test scores. Seems like I'm heading in the right direction...


![png](boro_01_current_market_value_files/boro_01_current_market_value_93_0.png)


**ANALYSIS:** Scores are converging slowly now so more data could well help.


![png](boro_01_current_market_value_files/boro_01_current_market_value_95_0.png)


**ANALYSIS:** Out predictions are still undershooting in general but we're getting closer all the time!


    [1;31mSignature:[0m [0mshow_significant_features[0m[1;33m([0m[0mfeatures[0m[1;33m,[0m [0mlabels[0m[1;33m)[0m[1;33m[0m[1;33m[0m[0m
    [1;31mDocstring:[0m <no docstring>
    [1;31mFile:[0m      c:\users\adeacon\documents\github\the-ball-is-round\notebooks\<ipython-input-71-4326b65b49ab>
    [1;31mType:[0m      function
    


    
    Significant training features:
    Minutes played       0.144 +/- 0.014
    Shirt number         0.142 +/- 0.017
    Appearances          0.118 +/- 0.012
    Goals                0.117 +/- 0.014
    Age                  0.091 +/- 0.009
    Goals p90            0.086 +/- 0.012
    Years in team        0.077 +/- 0.010
    In squad             0.076 +/- 0.010
    PPG                  0.049 +/- 0.009
    Yellow cards         0.045 +/- 0.006
    Foot_left            0.042 +/- 0.006
    Height               0.040 +/- 0.007
    Substitutions off    0.032 +/- 0.004
    Foot_missing         0.024 +/- 0.005
    Yellow cards p90     0.022 +/- 0.003
    Assists p90          0.021 +/- 0.005
    Foot_both            0.016 +/- 0.005
    Substitutions on     0.013 +/- 0.002
    Assists              0.006 +/- 0.002
    
    Significant testing features:
    Appearances          0.055 +/- 0.024
    

**ANALYSIS:** `Minutes played`, `Shirt number` (!), `Appearances` and `Goals` are particularly influencing the model... but only `Appearances` is generalising to new predictions.

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
      <td>443.000000</td>
      <td>351.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443</td>
      <td>324</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>356.000000</td>
      <td>443.000000</td>
      <td>330.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>351.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
      <td>443.000000</td>
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
      <td>201</td>
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
      <td>24.546275</td>
      <td>23.871039</td>
      <td>20.316027</td>
      <td>1.194131</td>
      <td>0.070201</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17.011287</td>
      <td>1.550790</td>
      <td>0.094877</td>
      <td>183.286517</td>
      <td>18.884876</td>
      <td>1.696327</td>
      <td>1235.817156</td>
      <td>1.267362</td>
      <td>NaN</td>
      <td>0.056433</td>
      <td>0.051919</td>
      <td>6.693002</td>
      <td>3.304740</td>
      <td>3.304740</td>
      <td>2.447119</td>
      <td>2.011287</td>
      <td>0.104350</td>
      <td>1.510444</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.633588</td>
      <td>4.733915</td>
      <td>18.171740</td>
      <td>2.060897</td>
      <td>0.138105</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.677963</td>
      <td>2.948889</td>
      <td>0.184480</td>
      <td>6.028752</td>
      <td>17.262750</td>
      <td>1.776398</td>
      <td>1257.427002</td>
      <td>0.840662</td>
      <td>NaN</td>
      <td>0.249838</td>
      <td>0.241628</td>
      <td>10.722988</td>
      <td>4.533899</td>
      <td>4.420709</td>
      <td>2.005552</td>
      <td>2.957062</td>
      <td>0.162198</td>
      <td>1.026292</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000000</td>
      <td>16.356256</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>167.000000</td>
      <td>0.000000</td>
      <td>0.038000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.265577</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.314464</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>21.000000</td>
      <td>19.409023</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>179.000000</td>
      <td>3.000000</td>
      <td>0.375000</td>
      <td>96.000000</td>
      <td>0.769134</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.913092</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.777207</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>24.000000</td>
      <td>23.907404</td>
      <td>17.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>183.000000</td>
      <td>15.000000</td>
      <td>1.130000</td>
      <td>828.000000</td>
      <td>1.356522</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.960341</td>
      <td>1.000000</td>
      <td>0.025568</td>
      <td>1.297218</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>27.000000</td>
      <td>26.554960</td>
      <td>37.000000</td>
      <td>2.000000</td>
      <td>0.107387</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.000000</td>
      <td>2.000000</td>
      <td>0.110328</td>
      <td>188.000000</td>
      <td>34.000000</td>
      <td>2.250000</td>
      <td>2124.000000</td>
      <td>1.702066</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>11.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>3.422384</td>
      <td>3.000000</td>
      <td>0.173961</td>
      <td>1.948017</td>
    </tr>
    <tr>
      <th>max</th>
      <td>40.000000</td>
      <td>37.607891</td>
      <td>73.000000</td>
      <td>12.000000</td>
      <td>1.406250</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>53.000000</td>
      <td>19.000000</td>
      <td>1.592920</td>
      <td>199.000000</td>
      <td>55.000000</td>
      <td>10.800000</td>
      <td>4770.000000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>42.000000</td>
      <td>27.000000</td>
      <td>22.000000</td>
      <td>10.998172</td>
      <td>13.000000</td>
      <td>1.800000</td>
      <td>8.196122</td>
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
      <td>113.000000</td>
      <td>21.000000</td>
      <td>113.000000</td>
      <td>113.000000</td>
      <td>113.000000</td>
      <td>113</td>
      <td>22</td>
      <td>113.000000</td>
      <td>113.000000</td>
      <td>113.000000</td>
      <td>28.000000</td>
      <td>113.000000</td>
      <td>0.0</td>
      <td>113.000000</td>
      <td>113.000000</td>
      <td>113</td>
      <td>113.000000</td>
      <td>113.0</td>
      <td>113.000000</td>
      <td>113.000000</td>
      <td>113.000000</td>
      <td>21.000000</td>
      <td>113.000000</td>
      <td>113.000000</td>
      <td>113.000000</td>
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
      <td>37</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>48</td>
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
      <td>21.672566</td>
      <td>18.725068</td>
      <td>6.725664</td>
      <td>0.318584</td>
      <td>0.047352</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.203540</td>
      <td>0.539823</td>
      <td>0.077697</td>
      <td>182.178571</td>
      <td>6.902655</td>
      <td>NaN</td>
      <td>338.035398</td>
      <td>1.046543</td>
      <td>NaN</td>
      <td>0.008850</td>
      <td>0.0</td>
      <td>1.256637</td>
      <td>1.230088</td>
      <td>1.522124</td>
      <td>1.486032</td>
      <td>0.504425</td>
      <td>0.041544</td>
      <td>1.045695</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.281277</td>
      <td>1.369572</td>
      <td>9.135144</td>
      <td>1.045957</td>
      <td>0.177414</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.338936</td>
      <td>1.500211</td>
      <td>0.210946</td>
      <td>5.683332</td>
      <td>8.596059</td>
      <td>NaN</td>
      <td>535.756857</td>
      <td>1.114036</td>
      <td>NaN</td>
      <td>0.094072</td>
      <td>0.0</td>
      <td>5.725536</td>
      <td>2.546036</td>
      <td>2.542838</td>
      <td>0.997234</td>
      <td>1.303319</td>
      <td>0.097388</td>
      <td>0.787317</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000000</td>
      <td>17.054423</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>172.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.334025</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.344642</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>19.000000</td>
      <td>17.686879</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>178.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.991122</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.459586</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>20.000000</td>
      <td>18.404211</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>182.500000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>77.000000</td>
      <td>0.830000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.999336</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.777676</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.000000</td>
      <td>19.055833</td>
      <td>9.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>185.000000</td>
      <td>11.000000</td>
      <td>NaN</td>
      <td>387.000000</td>
      <td>1.857931</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>2.001410</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.354743</td>
    </tr>
    <tr>
      <th>max</th>
      <td>33.000000</td>
      <td>21.881353</td>
      <td>35.000000</td>
      <td>9.000000</td>
      <td>1.406250</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.000000</td>
      <td>11.000000</td>
      <td>1.592920</td>
      <td>196.000000</td>
      <td>33.000000</td>
      <td>NaN</td>
      <td>2520.000000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>0.0</td>
      <td>34.000000</td>
      <td>14.000000</td>
      <td>14.000000</td>
      <td>4.000082</td>
      <td>7.000000</td>
      <td>0.500000</td>
      <td>5.732973</td>
    </tr>
  </tbody>
</table>
</div>



**ANALYSIS:** The player's missing actual Market values are mostly young players.

~~**ANALYSIS:** The model seems to particularly struggle with young players who we don't have much information about.~~
