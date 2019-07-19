# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:22:13 2019

@author: admin
"""
import pandas
import plotly

import plotly
dir (plotly)

studentlist= [["steve",32,"male"],["lia",28,"female"],["vin",45,"male"],["katie",38,"female"]]
print(studentlist)

studentlistdf = pandas.DataFrame(studentlist, columns = ["name","age","gender"],index = [1,2,3,4])
print(studentlistdf)


#graph our data
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])

plot([agename])


import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go


df = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")

                   
                   
womenoccupation = go.Bar(x = df["occupation"],  y=df["women"])
                   
plot([womenoccupation])
                   
                   
fig = go.Figure(data=[womenoccupation])
                   
                   
plot(fig)
       




            