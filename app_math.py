import random
import streamlit as st

st.set_page_config(page_title="Math App", page_icon="➕")
st.title("Fibbonacci Calculator")

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

fib_number = st.slider("Select a number to calculate its Fibonacci value", 0, 50, 1)
st.write(f"Fibonacci value: {fibonacci(fib_number)}")
data = [0] * 51
for i in range(51):
    data[i] = fibonacci(i)
    
st.line_chart(data)

st.title("🎲 Virtual dice")

st.number_input("Number of dice", min_value=1, max_value=10, value=2, step=1, key="num_dice")
dice_values = [random.randint(1, 6) for _ in range(st.session_state.num_dice)]
for i in range(st.session_state.num_dice):
    st.write(f"🎲 number {i+1}: {dice_values[i]}")
    
st.write("Sum of dice: " + str(sum(dice_values)))
st.write('')
st.caption("Click the button to roll the dice again.")
st.button("Roll Dice")
    