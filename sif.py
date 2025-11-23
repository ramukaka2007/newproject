import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator")

st.title("🔢 Scientific Calculator")

# Input expression
expression = st.text_input("Enter expression (e.g., sin(30), log(10), sqrt(16), 2**5):")

# Buttons
if st.button("Calculate"):
    try:
        # Allowed functions
        allowed_math = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
        allowed_math["pi"] = math.pi
        allowed_math["e"] = math.e

        result = eval(expression, {"__builtins__": {}}, allowed_math)
        st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"Error: {e}")

st.write("### 👉 Supported Functions")
st.write("""
- sin(x), cos(x), tan(x)
- log(x), log10(x)
- sqrt(x), pow(x, y)
- factorial(x)
- radians(x), degrees(x)
- pi, e
- Normal math: +, -, *, /, ** (power)
""")
