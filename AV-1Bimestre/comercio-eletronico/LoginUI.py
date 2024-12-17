import streamlit as st
from views import View
import time

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")

        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"):
            if not email or not senha:
                st.error("Por favor, preencha o e-mail e a senha.")
            else:
                try:
                    c = View.cliente_autenticar(email, senha)
                    if c is None:
                        st.error("E-mail ou senha inválidos.")
                    else:
                        # Armazena informações do cliente na sessão
                        st.session_state["cliente_id"] = c["id"]
                        st.session_state["cliente_nome"] = c["nome"]
                        st.success(f"Bem-vindo, {c['nome']}!")
                        time.sleep(1)
                        st.experimental_rerun()
                except Exception as e:
                    st.error(f"Erro ao autenticar: {e}")
