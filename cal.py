import streamlit as st
st.title("My First Calculator")
col1, col2 = st.columns(2)
num1 = col1.number_input("First number😃😃", value=0.0)
num2 = col2.number_input("Second number😃😃", value=0.0)
operation = st.selectbox(
    "Select operation", 
    ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"]
)
if operation == "Add (+)":
    result = num1 + num2
elif operation == "Subtract (-)":
    result = num1 - num2
elif operation == "Multiply (*)":
    result = num1 * num2
elif operation == "Divide (/)":
    result = num1 / num2 if num2 != 0 else "Error (cannot divide by zero)"
st.subheader(f"**Result:** {result}")
