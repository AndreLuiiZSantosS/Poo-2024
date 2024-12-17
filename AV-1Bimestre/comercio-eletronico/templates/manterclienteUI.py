import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()

    @staticmethod
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado.")
        else:
            dic = [obj.__dict__ for obj in clientes]
            df = pd.DataFrame(dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome do cliente")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o telefone")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            if nome and email and senha:
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Cliente inserido com sucesso.")
                time.sleep(2)
                st.experimental_rerun()
            else:
                st.error("Por favor, preencha todos os campos obrigatórios!")

    @staticmethod
    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado.")
        else:
            cliente_opcoes = {f"{c.nome} ({c.email})": c for c in clientes}
            selecionado = st.selectbox("Selecione um cliente para atualizar", cliente_opcoes.keys())
            cliente = cliente_opcoes[selecionado]

            nome = st.text_input("Informe o novo nome do cliente", cliente.nome)
            email = st.text_input("Informe o novo e-mail", cliente.email)
            fone = st.text_input("Informe o novo telefone", cliente.fone)
            senha = st.text_input("Informe a nova senha", cliente.senha, type="password")

            if st.button("Atualizar"):
                if nome and email and senha:
                    View.cliente_atualizar(cliente.id, nome, email, fone, senha)
                    st.success("Cliente atualizado com sucesso.")
                    time.sleep(2)
                    st.experimental_rerun()
                else:
                    st.error("Por favor, preencha todos os campos obrigatórios!")

    @staticmethod
    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado.")
        else:
            cliente_opcoes = {f"{c.nome} ({c.email})": c for c in clientes}
            selecionado = st.selectbox("Selecione um cliente para excluir", cliente_opcoes.keys())
            cliente = cliente_opcoes[selecionado]

            if st.button("Excluir"):
                View.cliente_excluir(cliente.id)
                st.success("Cliente excluído com sucesso.")
                time.sleep(2)
                st.experimental_rerun()
