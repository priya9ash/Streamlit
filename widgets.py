import streamlit as st
import pandas as pd
st.title("Streamit Text input")

name= st.text_input("Enter your name")
name2= st.text_input('Enter another name')

if name:

    st.write(f'Hello, {name} loves {name2}')


age= st.slider('Select your age ', 0,100,25) 

st.write(f"Your age is {age}")
data= {
"Name":['John','Jane','Jack','Jill'],"Age": [23,45,67,34],'City':['New York','Los Angels','Chicago','Houston']


}
df=pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)




uploaded_file= st.file_uploader('Choose a CSV file',type ='csv')
if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)
