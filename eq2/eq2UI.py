import streamlit as st
from eq2 import  EQ2

class EQ2UI:
    def main():
        st.header("Equação do segundo grau")
        a = st.text_input("a")
        b = st.text_input("b")
        c = st.text_input("c")
        x = int(st.text_input("x"))
        if st.button("Calcular"):
            eq = EQ2(int(a),int(b),int(c))
            st.write(eq)
            st.write(f"Delta = {eq.calc_delt()}")
            st.write(f"x1 =  {eq.bhask1()}")
            st.write(f"x2 =  {eq.bhask2()}")
            st.write(f"y =  {eq.y(x)}")
           