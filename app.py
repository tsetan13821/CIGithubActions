import streamlit as st

# Streamlit ui
st.title("Power Calculator")
st.write("Enter a number to caluculate its square, cube and fourth power.")

# Get user input
number = st.number_input("Enter a number", value=1, step = 1)
# Calculate powers
square = number ** 2    
cube = number ** 3
fourth_power = number ** 4  
# Display results
st.write(f"Square: {square}")
st.write(f"Cube: {cube}")
st.write(f"Fourth Power: {fourth_power}")   