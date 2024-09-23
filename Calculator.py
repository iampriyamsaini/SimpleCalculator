import streamlit as st


st.title("Simple Calculator")

st.write("")  
st.write("")


a = st.number_input("Enter 1st number: ")
b = st.number_input("Enter 2nd number: ")
addition = a+b
sub = a-b
mul = a*b

# creating buttons
if st.button("Add"):
  st.write("Sum of both numbers is",addition)
if st.button("Subtract"):
  st.write("Subraction is",sub)
if st.button("Multiply"):
  st.write("Multiplication of both numbers is",mul)


# using expection handling to avoid ZeroDivisionError
if st.button("Divide"):
    try:
        div = a / b
        st.write("Division of both numbers is", div)
    except ZeroDivisionError:
        st.write("Division by zero is not allowed, Please try with other numbers.")



# using free spaces 
st.write("")  
st.write("")
st.write("")  
st.write("")
st.write("")  
st.write("")


from PIL import Image
image = Image.open("IMG_20240211_154055_785.jpg")
st.image(image, width=200)
st.markdown("##### Made by Priyam for you with love")
  