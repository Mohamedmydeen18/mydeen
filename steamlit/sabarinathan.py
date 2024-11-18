import streamlit as st
from numpy import random
import time
st.title("Guessing game")
st.write("---")
c=st.number_input("Enter(0,1,2):",0,3)
st.write(f"your number is{c}")
a=random.randint(0,3)
st.write("computer guessed  number",a)
if a==c:
    if st.button(f"click for check"):
            st.write ("clicked")
            with st.spinner("wait....."):
                time.sleep(3)
                st.write("you win")
                st.balloons()
else:
    if st.button(f"click for check"):
            with st.spinner("wait..."):
                time.sleep(3)    
                st.write("you lost")



