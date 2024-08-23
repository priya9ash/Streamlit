import streamlit  as st 
import pandas as pd 
import numpy as np
##title of the application

st.title("Hello Steamlit")

##Display a Simple Text

st.write("This is a simple text")

## create a dataframe

df= pd.DataFrame({

    'first column': [1,2,3,4],
    'second column': [10,20,30,40]


})

st.write("here is the dataframe")
st.write(df)

# create a line chart
chart_data= pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.line_chart(chart_data)