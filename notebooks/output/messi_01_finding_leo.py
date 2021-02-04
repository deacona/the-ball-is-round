#!/usr/bin/env python
# coding: utf-8

# # Messi data exploration
# 
# Written report for this analysis can be found [here](../reports/messi_01_finding_leo.md)

# In[1]:


import pandas as pd


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


from src import utilities


# In[4]:


df = utilities.get_master("events_shot")
df.shape


# In[5]:


df.describe(include="all").T


# In[6]:


total_matches = len(df.match_date.unique())
total_matches


# In[7]:


messi_fullname = "Lionel AndrÃ©s Messi Cuccittini"
messi_fullname


# In[ ]:





# In[8]:


df["shot"] = 1
df["goal"] = 0
df.loc[df.outcome == "Goal", "goal"] = 1

df["shot_skill_diff"] = df.goal - df.statsbomb_xg

df["is_Messi"] = (df.player == messi_fullname)
df["month"] = df.match_date.str.split("-", expand=True)[1]
df["10_minute_bin"] = df.minute.round(-1)

df["start_location_x_bin"] = 5 * (df.start_location_x / 5).round()
df["start_location_y_bin"] = 5 * (df.start_location_y / 5).round()

df["end_location_y_bin"] = 4 * (df.end_location_y / 4).round()
df["end_location_z_bin"] = 1 * (df.end_location_z / 1).round()

df.iloc[:, -10:].describe(include="all").T


# In[9]:


## shots, goals, xg, efficiency, skill
summary = df.groupby(["is_Messi", "match_date"])[["shot", "goal", "statsbomb_xg", "shot_skill_diff"]].sum()            .sum(level="is_Messi") / total_matches
summary["shot_skill_%"] = summary.goal / summary.statsbomb_xg
summary["shot_efficiency_%"] = summary.goal / summary.shot
summary.sort_index(ascending=False).T


# In[10]:


## volume
print("Messi take {0:.1f}% of all shots taken in these matches".format(100 * summary.iloc[1, 0] / summary.shot.sum()))


# In[ ]:





# ## Trends over time

# In[11]:


for x_col in ["season_name", "month", "minute", "10_minute_bin"]:
    x_disp = x_col.title().replace("_", " ")
    x_agg = "mean"
    x_data = df[df.is_Messi].groupby("match_date").agg({x_col: max,
                                                       "statsbomb_xg": sum,
                                                       "goal": sum,
                                                       "shot": sum,}).sort_values(by=x_col)

    ax = sns.lineplot(data=x_data, x=x_col, y="statsbomb_xg", estimator=x_agg, color="g")
    ax.set(xlabel=x_disp, ylabel='per match')
    plt.setp(ax.get_xticklabels(), rotation=90)

    sns.lineplot(data=x_data, x=x_col, y="goal", estimator=x_agg, color="r")
    sns.lineplot(data=x_data, x=x_col, y="shot", estimator=x_agg, color="b")

    ax.legend(handles=ax.lines, labels=["xG","Goals","Shots"])
    plt.title("Messi: Shots, Goals and xG by {1}".format(x_agg, x_disp))

    plt.show()


# In[ ]:





# ## Where shots are taken from

# In[12]:


for metric_col in ["shot", "goal"]:
    data = df[(df.is_Messi) & (df.type == "Open Play") & (df[metric_col] == 1)]

    plt.hist2d(data.start_location_y, data.start_location_x, bins=11, range=[[20, 60], [90, 120]], cmap="Reds")
#     plt.hexbin(data.start_location_y, data.start_location_x, gridsize=13, cmap="Reds")
#     sns.jointplot(x="start_location_y", y="start_location_x", data=data, kind="hex")

    cb = plt.colorbar()
    cb.set_label("{0}s".format(metric_col.title()))

    ax = plt.gca()
    ax.set_aspect('equal')
    utilities.draw_pen_box(ax)

    plt.title("Messi: Open play {0} heatmap".format(metric_col))
    plt.show()


# In[13]:


def plot_contour_map(data, title, cmap, plot_type="contour", plot_elevation="pitch", plot_range=[[20, 60], [90, 120]]):
    x = data.columns
    y = data.index
    z = data.values
    data_extent = [x.min(), x.max(), y.min(), y.max()]
#     print(data_extent)

    if plot_type == "contour":
        plt.contour(x, y, z, 10, cmap=cmap)
    elif plot_type == "contourf":
        plt.contourf(x, y, z, 10, cmap=cmap)
    elif plot_type == "imshow":
        plt.imshow(z, extent=data_extent, origin="lower", cmap=cmap)

#     cb = 
    plt.colorbar()
#     cb.set_label("{0}".format(metric_col))

    ax = plt.gca()
    ax.set_aspect('equal')
    
    if plot_elevation == "goal":
        utilities.draw_posts(ax)
    else:
        utilities.draw_pen_box(ax)

    plt.xlim(plot_range[0])
    plt.ylim(plot_range[1])
    plt.title(title)
    plt.show() 


# In[14]:


plot_type = "contourf"
cmap = "seismic" #coolwarm

for metric_col in ["shot", "goal", "statsbomb_xg", "shot_skill_diff"]:
    data = df[(df.is_Messi) & (df.type == "Open Play")]            .groupby(["start_location_x_bin", "start_location_y_bin"])[metric_col].sum().unstack().fillna(0)
    
    title = "Messi: Open play {0} map".format(metric_col)
    
    plot_contour_map(data, title, cmap, plot_type)


# In[15]:


plot_type = "imshow"
cmap = "Reds" #coolwarm

data = df[(df.is_Messi) & (df.type == "Open Play")]            .groupby(["start_location_x_bin", "start_location_y_bin"])["goal"].sum().unstack().fillna(0)    / df[(df.is_Messi) & (df.type == "Open Play")]            .groupby(["start_location_x_bin", "start_location_y_bin"])["statsbomb_xg"].sum().unstack().fillna(0)
    
title = "Messi: Open play shot skill % map"

plot_contour_map(data, title, cmap, plot_type, plot_range=[[20, 60], [85, 120]])


# In[ ]:





# ## Where shots end up

# In[16]:


for metric_col in ["shot", "goal"]:
    data = df[(df.is_Messi) & (df.type == "Open Play") & (df[metric_col] == 1)].dropna(subset=["end_location_z"])

    plt.hist2d(data.end_location_y, data.end_location_z, bins=14, range=[[35, 45], [0, 4]], cmap="Reds")
#     plt.hexbin(data.end_location_y, data.end_location_z, gridsize=17, cmap="Reds")
#     g = sns.jointplot(x="start_location_y", y="start_location_x", data=data, kind="hex")

    cb = plt.colorbar()
    cb.set_label("{0}s".format(metric_col.title()))

    ax = plt.gca()
    ax.set_aspect('equal')
    utilities.draw_posts(ax)

    plt.title("Messi: Open play {0} heatmap".format(metric_col))
    plt.show()


# In[17]:


# plot_type = "contourf"
# cmap = "Reds" #coolwarm

# for metric_col in [#"shot", "goal", "statsbomb_xg", 
#     "shot_skill_diff"]:
#     data = df[(df.is_Messi) & (df.type == "Open Play")]\
#             .groupby(["end_location_z_bin", "end_location_y_bin"])[metric_col].sum().unstack().fillna(0)
    
#     title = "Messi: Open play {0} map".format(metric_col)
    
#     plot_contour_map(data, title, cmap, plot_type, plot_elevation="goal", plot_range=[[25, 55], [0, 4]])


# In[18]:


plot_type = "contourf"
cmap = "Reds" #coolwarm

data = (df[(df.is_Messi) & (df.type == "Open Play")]            .groupby(["end_location_z_bin", "end_location_y_bin"])["goal"].sum().unstack().fillna(0)    / df[(df.is_Messi) & (df.type == "Open Play")]            .groupby(["end_location_z_bin", "end_location_y_bin"])["shot"].sum().unstack().fillna(1))#\
#     - (df[(~df.is_Messi) & (df.type == "Open Play")]\
#             .groupby(["end_location_z_bin", "end_location_y_bin"])["goal"].sum().unstack().fillna(0)\
#     / df[(~df.is_Messi) & (df.type == "Open Play")]\
#             .groupby(["end_location_z_bin", "end_location_y_bin"])["shot"].sum().unstack().fillna(0))
    
title = "Messi: Open play shot efficiency map"

plot_contour_map(data, title, cmap, plot_type, plot_elevation="goal", plot_range=[[35, 45], [0, 4]])


# In[19]:


pens = df[(df.is_Messi) & (df.type == "Penalty")]

sns.relplot(x='end_location_y', y='end_location_z', size='statsbomb_xg', style="outcome", hue="outcome",
            sizes=(100, 400), alpha=.7, height=10, #aspect=2, 
                data=pens)

ax = plt.gca()
ax.set_aspect('equal')
utilities.draw_posts(ax)
pens_perc = 100 * pens[pens.outcome == "Goal"].shape[0] / pens.shape[0]
plt.title("Messi: All {0} of his penalties ({1:.1f}% scored)".format(pens.shape[0], pens_perc))
plt.show()

