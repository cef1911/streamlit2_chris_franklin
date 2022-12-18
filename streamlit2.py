from collections import namedtuple
import altair as alt
import math
import pandas as pdpip
import streamlit as st

"""
# Welcome to Chris Franklin's Streamlit Web App for Deploying Datascience Projects!
This is inspired from the StreamLit.io site.
See the website for more info https://streamlit.io/

My name is Chris Franklin. I work as in data science as a fulltime as business analyst for a Fortune 500 company and outside of work I work on several data science projects. My sentiment analysis, time-series, nlp, and data visualizations of all types.
Here is my LinkedIn info
https://www.linkedin.com/in/christopherefranklin/

Here my my personal applied data science lab website
https://franklydata.wixsite.com/franklydata


Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
