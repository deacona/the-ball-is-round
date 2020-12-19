
# European Club data - Analysis of goals


## Problem

What patterns can we see in the goals scored around European club football?


## Plan

We wanted to look at
* Overall pattern of data
* Distributions by Season, Month, Day of week, Country and Tier
* Highest and lowest (mean) averages by Team (home and away), Manager (home and away), Stadium and Referee
* A geographic representation of goals


## Data

We have compiled 28 seasons of data on matches played in domestic club competitions.

Where possible we have included data on managers (home and away teams), referees and stadiums (name and lat/lon).

![Data summary](figures/club_01_summary.JPG)


## Analysis

Overall, most matches have 2 or 3 goals and it follows a normal distribution from there (with a long tail to the right for infrequent high scoring matches).

![Histogram](figures/club_01_hist.PNG)

![Map](figures/club_01_map.PNG)


## Conclusions

Generally, the number of goals in matches is pretty consistent however we break down the data.

When we start looking at groups with most or fewest goals, whilst not significantly far from the overall mean, we could speculate about where you are most (or least) likely to see goals...

Our fantasy gauranteed goal feast would be:

| |Home|Away|
|-----|-----|-----|
|Team|PSV Eindhoven|Erzurumspor|
|Manager|Unai Emery|Malky Mackay|
|Stadium|Camp Nou||
|Referee|G Beaton||

Our nightmare goal-free zone would be:

| |Home|Away|
|-----|-----|-----|
|Team|Badajoz*|Reus Deportiu|
|Manager|Gerhard Struber|Mikel Arteta|
|Stadium|Stade François Coty||
|Referee|G Cain||

(* this should be poor old Reus Deportiu but they can't play themselves so the next worst is Badajoz)

