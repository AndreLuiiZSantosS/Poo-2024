import streamlit as st
import time
from views import View

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    @staticmethod
    def inserir():
        st.subheader("Preencha os dados para criar sua conta")

        nome = st.text_input("Informe o nome completo")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o telefone")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Criar Conta"):
            if not nome or not email or not senha:
                st.error("Os campos Nome, E-mail e Senha são obrigatórios!")
            elif len(senha) < 6:
                st.error("A senha deve ter pelo menos 6 caracteres.")
            else:
                try:
                    View.cliente_inserir(nome, email, fone, senha)
                    st.success("Conta criada com sucesso!")
                    time.sleep(2)
                    st.experimental_rerun()
                except Exception as e:
                    st.error(f"Erro ao criar a conta: {e}")
