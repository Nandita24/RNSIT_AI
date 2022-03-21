import streamlit as lt
import joblib
model = joblib.load('spam-ham')
st.title('SPAM HAM CLASSIFIER')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('Predict'):
  st.tile(op[0])
     

      
