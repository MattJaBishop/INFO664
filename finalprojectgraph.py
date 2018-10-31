#test code

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

import pandas as pd


df = pd.read_csv('New_York_City_Population_by_Borough__1950_-_2040.csv')

df.head()