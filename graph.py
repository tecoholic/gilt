import json
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

ydparser = lambda d: pd.datetime.strptime(d, "%b %d %Y")
rdparser = lambda d: pd.datetime.strptime(d, "%d %b %Y")
yields = pd.read_csv("yields.csv", parse_dates=[0], date_parser=ydparser)
rates = pd.read_csv("rbi-rates.csv", parse_dates=[0], date_parser=rdparser)
sbi = pd.read_csv("SBI Magnum Gilt Fund.csv", parse_dates=[0])
udparser = lambda d: pd.datetime.strptime(d, "%d-%m-%Y")
uti = pd.read_csv("UTI GILT Fund.csv", parse_dates=[0], date_parser=udparser)
idfc = pd.read_csv("IDFC_G_Sec_Fund.csv", parse_dates=[0])

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=yields["date"], y=yields["price"], mode="lines", name="10Yr Yield"), secondary_y=False)
fig.add_trace(go.Scatter(x=rates["date"], y=rates["rate"], mode="lines", name="Repo Rate"), secondary_y=False)
fig.add_trace(go.Scatter(x=sbi["DATE"], y=sbi["NAV"], mode="lines", name="SBI Magnum GILT - Direct - Growth"), secondary_y=True)
fig.add_trace(go.Scatter(x=uti["date"], y=uti["nav"], mode="lines", name="UTI GILT - Direct - Growth"), secondary_y=True)
fig.add_trace(go.Scatter(x=idfc["Date"], y=idfc["NAV"], mode="lines", name="IDFC GSec Fund - Direct - Growth"), secondary_y=True)

fig.update_layout(title_text="Rates, Yields and GILT NAVs")
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Repo Rate <i>&</i> 10 Yr Benchmark Yield", secondary_y=False)
fig.update_yaxes(title_text="Mutual Fund NAV", secondary_y=True)

fig.show()