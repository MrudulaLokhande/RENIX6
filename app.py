import streamlit as st
import joblib
model = joblib.load('spam-ham') #We are loading the pipelined model using joblib
st.title('SPAM-HAM CLASSIFIER')  #It creates a title in webapp
ip = st.txt_input('Enter the message') #It creates a text box in the webapp
op = model.predict([ip])
if st.button('Predict'): #It creates a button named Predict.
  st.title(op[0])  #st.button will create a button with the named Predict
