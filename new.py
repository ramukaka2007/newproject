import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Advanced Scientific Calculator", layout="centered")

# ---------- DARK MODE CSS ----------
dark_css = """
<style>
body {
    background-color: #0e1117;
    color: white;
}
[data-testid="stAppViewContainer"]{
    background-color:#0e1117;
}
.css-1d391kg, .stButton>button {
    background-color: #1f2937 !important;
    color: white !important;
    border-radius: 10px;
}
.stTextInput>div>div>input {
    background-color: #1f2937;
    color: white;
}
.stSelectbox>div>div {
    background-color: #1f2937;
    color: white;
}
</style>
"""
st.markdown(dark_css, unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("✨ Advanced Scientific & Graphing Calculator")
st.write("Mobile-friendly • Dark Mode • Scientific Functions • Graph Plotting")

# ---------- EXPRESSION INPUT ----------
st.subheader("🧮 Calculator")
expression = st.text_input("Enter expression", "sin(45) + sqrt(16) + 2**5")

# ---------- BUTTON UI ----------
buttons = [
    ["7", "8", "9", "/", "sin("],
    ["4", "5", "6", "*", "cos("],
    ["1", "2", "3", "-", "tan("],
    ["0", ".", "+", "sqrt(", "log("],
    ["(", ")", "pi", "e", "factorial("]
]

for row in buttons:
    cols = st.columns(5)
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            expression += btn

# ---------- CALCULATE ----------
if st.button("Calculate"):
    try:
        allowed = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
        allowed["pi"] = math.pi
        allowed["e"] = math.e
        allowed["sqrt"] = math.sqrt
        allowed["log"] = math.log
        allowed["sin"] = lambda x: math.sin(math.radians(x))
        allowed["cos"] = lambda x: math.cos(math.radians(x))
        allowed["tan"] = lambda x: math.tan(math.radians(x))

        result = eval(expression, {"__builtins__": {}}, allowed)
        st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"Error: {e}")

# ---------- GRAPHING CALCULATOR ----------
st.subheader("📈 Graph Plotter")
func = st.text_input("Enter function of x (e.g., sin(x), x**2, log(x))", "sin(x)")
xmin = st.number_input("X-min", -10.0)
xmax = st.number_input("X-max", 10.0)

if st.button("Plot Graph"):
    try:
        x = np.linspace(xmin, xmax, 500)
        allowed_np = {
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "log": np.log,
            "sqrt": np.sqrt,
            "pi": np.pi,
            "e": np.e,
            "exp": np.exp,
            "abs": np.abs,
            "x": x
        }

        y = eval(func, {"__builtins__": {}}, allowed_np)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"Graph of: {func}")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Plot Error: {e}")
