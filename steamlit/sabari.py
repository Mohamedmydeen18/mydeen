import streamlit as st
import time
st.write("# Train ticket")
text=st.text_input("enter your name:")
st.write(f"your name is:{text}")
num=st.slider("Age",0,100,0)
st.write(f"your age is:{num}")
st.write("your gender")
gender=st.radio("gender:",['male','female','others'])
st.write(f"your gender:{gender}")   
if num<5:
    st.write("you have a special tickets")
elif 5<num<60:
    st.write("you have a $40 tickets")
    a=st.text_input("where are you from?")
    st.write(f"you from: {a}")
    st.write ("only train for salem,coimbatore ,erode")
    b=st.text_input("where did you go?")
    st.write(f"you want to go:{b}")
    st.write("#click the button for booking the train")
    if b=='salem' or "coimbatore" or "erode":
        if st.button(f"click for book"):
            st.write ("clicked")
            with st.spinner("wait....."):
                time.sleep(2)    
            st.success("your train booked")       
else:
    st.write ("you have no tickets because it is a not safable for you")
    st.wrie ("please go in bus")        