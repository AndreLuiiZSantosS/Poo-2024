# templates/loginUI.py
import streamlit as st
from views import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")

        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            if c is None:
                st.write("E-mail ou senha inválidos.")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.success(f"Bem-vindo(a), {c['nome']}!")
                st.experimental_rerun()
