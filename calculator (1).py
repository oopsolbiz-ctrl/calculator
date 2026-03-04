import streamlit as st

st.title("Welcome to Abdullah's ⌨️ Calculator")

# 1. Initialize memory
if "calc_display" not in st.session_state:
    st.session_state.calc_display = ""

# 2. Logic Functions (The "Waiters")
def update_display(label):
    if label == "=":
        try:
            # Calculate and update state
            st.session_state.calc_display = str(eval(st.session_state.calc_display))
        except:
            st.session_state.calc_display = "Error"
    elif label == "AC":
        st.session_state.calc_display = ""
    else:
        # Append the new character
        st.session_state.calc_display += label

# 3. The Display Box (Linked to memory via key)
st.text_input("Input", key="calc_display", label_visibility="collapsed")

# 4. The Button Grid
button_layout = [
    ["(", ")", "%", "AC"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in button_layout:
    cols = st.columns(4)
    for i, label in enumerate(row):
        # We use 'on_click' to call our function and 'args' to pass the label
        cols[i].button(label, key=f"btn_{label}", on_click=update_display, args=(label,))



