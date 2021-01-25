
# Messi event data

Computational notebook for this analysis can be found [here](../notebooks/messi_01_finding_leo.ipynb)


## Problem

Where does Lionel Messi take his shots from? Where do they go? Does he differ from the average player? Has his shooting changed over time?


## Plan

I wanted to look at
* Shots, goals and expected goals
* General trends over time
* Plots of start and end locations


## Data

I have compiled 16 seasons of data on 485 matches played by Lionel Messi for Barcelona in La Liga.

I have performed some simple binning of the data and calculated metrics for shot efficiency (goals per shots) and skill (goals vs expected goals)


## Analysis

## Messi versus the rest

<p>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th> </th>
      <th>Messi</th>
      <th>Other players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>shot</th>
      <td>4.457732</td>
      <td>20.290722</td>
    </tr>
    <tr>
      <th>goal</th>
      <td>0.915464</td>
      <td>2.476289</td>
    </tr>
    <tr>
      <th>statsbomb_xg</th>
      <td>0.700319</td>
      <td>2.392000</td>
    </tr>
    <tr>
      <th>shot_skill_diff</th>
      <td>0.215145</td>
      <td>0.084289</td>
    </tr>
    <tr>
      <th>shot_skill_%</th>
      <td>1.307210</td>
      <td>1.035238</td>
    </tr>
    <tr>
      <th>shot_efficiency_%</th>
      <td>0.205365</td>
      <td>0.122040</td>
    </tr>
  </tbody>
</table>
</p>

Immediately we can see that Messi takes 18% of all shots in these matches and scores with 20% of those shots. He averages almost a goal a game, exceeding his expected goals by about 30%.


### Trends over time

![png](figures/messi_01_finding_leo_14_0.png)
![png](figures/messi_01_finding_leo_14_1.png)
![png](figures/messi_01_finding_leo_14_2.png)

We can see a consistent increase in shots and goals through Messi's early career before levelling out to fairly consistent values from 2009/2010 onwards. There isn't a mass of variation between calendar months. There's something of a peak in August but also the summer months will be based on a amuch smaller sample. Theer are dips in April and November. Interestingly, Messi appears (on average) to take more shots and score more goals as a match progresses.


### Where does he shoot from?

![png](figures/messi_01_finding_leo_17_0.png)
![png](figures/messi_01_finding_leo_17_1.png)
![png](figures/messi_01_finding_leo_19_0.png)
![png](figures/messi_01_finding_leo_19_1.png)

Messi takes most of his shots and scores most of his goals from central locations in the 18 yard box.


![png](figures/messi_01_finding_leo_19_3.png)
![png](figures/messi_01_finding_leo_20_0.png)

He has a curious little hotspot on the left corner of the "D" where he has far exceeded his expected total of goals. Partly this is driven by him taking lots of shots from there as the skill percentage is not so prominant. Conversely, there are spots outside the box near the left corner and centrally at about 30m from goal where he does (on average) exceed the xG by a large margin - but this is from much smaller number of shots. We might say he underperforms his xG in other zones to the left - both close to goal and far out - but then he doesn't shoot from these areas much either.


### Where does he shoot to?

![png](figures/messi_01_finding_leo_23_0.png)
![png](figures/messi_01_finding_leo_23_1.png)

Messi's shots are mostly low with most goals being scored in the bottom corners.


![png](figures/messi_01_finding_leo_26_0.png)

Similar, to open play, Messi likes to shoot his penalties low and to the corners. He slightly favours the natural side for a left-footer.


## Conclusions

Messi is obviously an exceptional player and this is reflected in his shots data. Whether it's instinctive or deliberate, he does appear to shoot from and to locations which are most likely to result in goals. He combines volume, efficiency and skill in one very productive package.