import  streamlit as st
a=st.slider("date of booking:",0,30)
if a==16:
    b=int(input("enter you age:"))
    if b<=10:
        st.write("the ticket price is 20")
    elif 10<b<=60:
        st.write("the ticket price is 50")
    else:
        st.write("the ticket price is 25")
elif a==17:
    b=int(input("enter you age:"))
    if b<=10:
        st.write("the ticket price is 15")
    elif 10<b<=60:
        st.write("the ticket price is 30")
    else:
        st.write("the ticket price is 20")
else:
    st.write("only ticket are available in he 16,17")