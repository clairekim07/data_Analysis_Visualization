import csv
import pandas as panda

#this is a library containing the small modules and methods
import plotly.graph_objects as go

df = panda.read_csv("level.csv")

#we're grouping the different levels and caluculating the mean of the attempts
print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h"
    ))

fig.show()