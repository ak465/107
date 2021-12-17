import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

data=df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(data, x="student_id", y="level", color="attempt", size="attempt")

fig.show()
