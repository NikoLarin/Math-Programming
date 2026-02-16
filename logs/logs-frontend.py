from logs import single_log, double_log, natural_log_equation, exponential_equation
import sympy as sp
import streamlit as st

st.title('Math')

logs_tab, tbd = st.tabs(["Logs", "tbd"])

with logs_tab: 
    st.header('Logs Equations',text_alignment='center',divider=True)
    st.markdown('Enter values separated by commas (e.g., 2, 3, 8)')

    st.header('Single Log')
    equation = st.text_input('Base, Exponent, Expression')
    
    if equation:
        try:
            parts = equation.split(',')
            base = parts[0].strip()
            exponent = parts[1].strip()
            expression = parts[2].strip()

            base = int(base) if base.isdigit() else base
            exponent = int(exponent) if exponent.isdigit() else exponent
            expression = sp.sympify(expression)

            st.write(single_log(base, exponent, expression))
            base = int(parts[0].strip())
            exponent = int(parts[1].strip())
            expression = int(parts[2].strip())
            st.write(single_log(base, exponent, expression))
        except (ValueError, IndexError):
            print()
        
with tbd:
    st.header('Future Sections')
