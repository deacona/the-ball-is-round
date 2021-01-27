#!/usr/bin/env python
# coding: utf-8

# # European Club data - Analysis of goals
# 
# Written report for this analysis can be found [here](../reports/club_01_goals_around_europe.md)

# In[1]:


## our packaged code
from src import utilities


# In[2]:


## suppress warnings
import warnings
warnings.filterwarnings('ignore')


# In[3]:


from scipy.stats import norm  
import numpy as np
import pandas as pd


# In[4]:


## visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import seaborn as sns
# sns.set()
sns.set(rc={'figure.figsize':(10, 5)})

# from mpl_toolkits.basemap import Basemap


# In[5]:


df = utilities.get_master("fulldata")

df = df[df.HomeAway == "Home"]

df.dropna(subset=['TotalGoals'], inplace=True)

df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")
df["Month"] = df["Date"].apply(lambda x: x.strftime("%m"))
df["Day_Of_Week"] = df["Date"].apply(lambda x: x.strftime("%w"))

attrib_cols = ["Date", "Month", "Day_Of_Week", "HomeAway", "Season", "Country", "Tier", "Team", "TeamOpp", "Manager", "ManagerOpp", "Referee", 
               "Stadium", "Latitude", "Longitude"]
metric_cols = ["TotalGoals"]

df = df[attrib_cols + metric_cols]

df.shape


# In[6]:


df.describe(include="all").T.fillna("")


# ## Overall Trends

# In[7]:


mean = df.TotalGoals.mean()
std = df.TotalGoals.std()
low = mean - std
high = mean + std

mean, std, low, high


# In[8]:


df.TotalGoals.plot(kind='hist', density=True, bins=range(int(df.TotalGoals.max()+1)))

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth=2)
# title = "Fit results: mu = %.2f,  std = %.2f" % (mean, std)
# plt.title(title)

plt.axvline(x=mean, linewidth=3, color='g', linestyle="--", label="mu")

plt.savefig("../reports/figures/club_01_hist.PNG")
plt.show()


# In[9]:


for col in ["Season", "Month", "Day_Of_Week", "Country", "Tier"]:
    print("\n#######\n")
    GpG = df[[col, "TotalGoals"]].groupby(col)
    print(GpG.describe(include="all"))
#     df[[col, "TotalGoals"]].boxplot(by=col, showmeans=True, widths=0.7, figsize=(10,5)).get_figure().gca().set_title("")
    sns.boxplot(x=col, y="TotalGoals", data=df.sort_values(by=col), showmeans=True, width=0.6)
    plt.xticks(rotation=90)
    
    plt.savefig("../reports/figures/club_01_boxplot_{0}.PNG".format(col))
    plt.show()
    


# ## Most and Fewest Goals

# In[10]:


min_games = 30
top_n = 10

tops_list = []

for col in ["Team", "TeamOpp", "Manager", "ManagerOpp", "Stadium", "Referee"]:
    print("\n#######\n")
    for txt, asc, hilo in [("Top", False, high), ("Bottom", True, low)]:
        print("{0} {1} average goals by {2} (minimum {3} matches)...".format(txt, top_n, col, min_games))
        top = df[df[col].isin(df[col].value_counts()[df[col].value_counts() > min_games].index)].groupby(col).TotalGoals
        top = pd.DataFrame(top.mean().sort_values(ascending=asc).head(top_n))
        top["Variable"] = col
        tops_list.append(top)
        print(top)
        top.plot(kind="bar", figsize=(10,5))
        plt.xticks(rotation=90)
        plt.axhline(y=mean, linewidth=3, color='k', linestyle="--", label="Overall mean")
        plt.axhline(y=hilo, linewidth=3, color='r', linestyle="--", label="1 stdev from mean")
        plt.legend(bbox_to_anchor=(1.1, 1.05))
        plt.show()
    


# In[11]:


tops = pd.concat(tops_list, axis=0) #.sort_values(by="TotalGoals", ascending=False).head(30)
tops["Value (Variable)"] = tops.index + " (" + tops.Variable + ")"
tops.set_index("Value (Variable)", inplace=True)
tops.drop(columns="Variable", inplace=True)
# tops

# tops = pd.concat(tops_list, axis=0) #.sort_values(by="TotalGoals", ascending=False).head(30)
top_n = 30

for txt, asc, hilo in [("Top", False, high), ("Bottom", True, low)]:
#     print("{0} {1} average goals by {2} (minimum {3} matches)...".format(txt, top_n, col, min_games))
#     top = df[df[col].isin(df[col].value_counts()[df[col].value_counts() > min_games].index)].groupby(col).TotalGoals
#     top = pd.DataFrame(top.mean().sort_values(ascending=asc).head(top_n))
#     top["Variable"] = col
#     tops_list.append(top)
    tmp = tops.sort_values(by="TotalGoals", ascending=asc).head(top_n)
    print(tmp)
    tmp.plot(kind="bar", figsize=(10,5))
    plt.xticks(rotation=90)
    plt.axhline(y=mean, linewidth=3, color='k', linestyle="--", label="Overall mean")
    plt.axhline(y=hilo, linewidth=3, color='r', linestyle="--", label="1 stdev from mean")
    plt.legend(bbox_to_anchor=(1.1, 1.05))
    
    plt.savefig("../reports/figures/club_01_bar_{0}.PNG".format(txt), bbox_inches='tight')
    plt.show()
    


# In[12]:


atts = ["Country", "Tier"]
for col in ["Manager", "ManagerOpp", "Stadium", "Referee", "Latitude", "Longitude"]:
#     for att in ["Country", "Tier"]:
    print("\n#######\n")
    print("Sample size and means with {0} by {1}".format(col, ", ".join(atts)))
    print(df.loc[pd.notnull(df[col]), ].groupby(atts).TotalGoals.agg(["size", "mean"]).sort_index())


# ## Mapping Goals

# In[13]:


# mapdata=df.dropna(subset=['Latitude', 'Longitude'])
mapdata = df.dropna(subset=['Latitude', 'Longitude']).groupby(['Latitude', 'Longitude', 'Country']).TotalGoals    .mean().reset_index()

# fg = sns.FacetGrid(data=mapdata, hue='Country', height=6, aspect=.9)
# fg.map(plt.scatter, 'Longitude', 'Latitude').add_legend()

# sns.lmplot(x='Longitude', y='Latitude', s='TotalGoals', hue='Country', data=mapdata, fit_reg=False, 
#            x_jitter=0.1, y_jitter=0.1, markers="o", palette="viridis", height=7)

sns.relplot(x="Longitude", y="Latitude", hue="Country", size="TotalGoals",
            sizes=(100, 400), alpha=.5, palette="muted", aspect=1.2,
            height=7, data=mapdata)

plt.savefig("../reports/figures/club_01_map.PNG")


# In[14]:


# # Extract the data we're interested in
# lat = df.groupby(['Stadium'])[["Latitude"]].max().values
# lon = df.groupby(['Stadium'])[["Longitude"]].max().values

# # print lat, lon

# # 1. Draw the map background
# fig = plt.figure(figsize=(8, 8))
# m = Basemap(projection='lcc', resolution='h', 
#             lat_0=46., lon_0=-3.,
#             width=3E6, height=3E6)
# m.shadedrelief()
# m.drawcoastlines(color='gray')
# m.drawcountries(color='black')

# # 2. scatter stadium data
# m.scatter(lon, lat, latlon=True,
#           color='r', s=40,
#           alpha=0.5)

