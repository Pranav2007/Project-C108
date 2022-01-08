import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv('data.csv')
r = df["Avg Rating"]
fig3 = ff.create_distplot([r], ["Result"])
fig3.show()