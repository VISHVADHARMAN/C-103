import pandas as pd 
import plotly.express as px

#df=pd.read_csv("D:/C-103/line_chart.csv")
#fig=px.line(df,x="Year",y="Per capita income",color="Country",title="Per Capita Income")
#fig.show()

#df=pd.read_csv("D:/C-103/data.csv")
#fig=px.bar(df,x="Country",y="InternetUsers")
#fig.show()

df=pd.read_csv("D:/C-103/data.csv")
fig=px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60)
fig.show()