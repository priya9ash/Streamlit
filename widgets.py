import streamlit as st
st.title("Streamit Text input")

name= st.text_input("Enter your name")
name2= st.text_input('Enter another name')

if name:

    st.write(f'Hello, {name} loves {name2}')


age= st.slider('Select your age ', 0,100,25) 

st.write("Your age is {age}")
