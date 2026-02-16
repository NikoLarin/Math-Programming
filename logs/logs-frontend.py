from logs import single_log, double_log, natural_log_equation, exponential_equation
import sympy as sp
import streamlit as st

st.title('Math')

logs_tab, tbd = st.tabs(["Logs", "tbd"])

with logs_tab: 
    st.header('Logs Equations',text_alignment='center',divider=True)
    st.text('Enter the base, exponent, and expression separated by commas')
    st.header('Single Log')
    equation = st.chat_input('Base, Exponent, Expression')

    if equation:
        try:
            parts = equation.split(',')
            if len(parts) == 3:
                base = float(parts[0].strip())
                exponent = float(parts[1].strip())
                expression = parts[2].strip()
                result = single_log(base, exponent, expression)
                st.text(f'Result: {result}')
            else:
                st.error('Please enter exactly 3 values separated by commas')
        except ValueError:
            st.error('Base and exponent must be numbers')

with tbd:
    st.header('Future Sections')