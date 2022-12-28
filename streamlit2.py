import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px



st.write("Streamlit Play with officehours :) creating dataframes and plotly plots")

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))


  

st.dataframe(df)  # Same as st.write(df)

lst = [['Geek', 25], ['is', 30], 
       ['for', 26], ['Geeksforgeeks', 22]] 

# creating df object with columns specified    
df2 = pd.DataFrame(lst, columns =['Tag', 'number']) 

df2.plot()

st.dataframe(df2)  # Same as st.write(df)


#another dataframe https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart
df3 = px.data.gapminder()

fig = px.scatter(
    df3.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)

st.dataframe(df3)
