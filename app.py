import streamlit as st

st.header('Calculator App')
st.write('This is a calculator application developed using streamlit')
btn= st.button('Click Me')
if btn:
    st.balloons()


num1= st.number_input('Enter the first number',value=0)
option= st.selectbox('Select the operation',("+","-","/","*"))
num2= st.number_input('Enter the second number',value=0)
btn2=st.button('Calculate')
if btn2:
    if option=="+":
        st.subheader(f' Added result is {num1+num2} ' )
    elif option=="-":
        st.subheader(f' Subtract is {num1-num2} ')
    elif option=="*":
        st.subheader(f' Multiply is {num1*num2}'  )
    elif option=="/":
        st.subheader(f' Division is {num1/num2}'  )
    