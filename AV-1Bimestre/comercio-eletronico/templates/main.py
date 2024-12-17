from templates.loginUI import LoginUI
from templates.manterclienteUI import ManterClienteUI

def main():
    st.sidebar.title("Menu")
    escolha = st.sidebar.radio("Escolha uma opção", ["Login", "Cadastrar Cliente"])

    if escolha == "Login":
        LoginUI.main()
    elif escolha == "Cadastrar Cliente":
        ManterClienteUI.main()

if __name__ == "__main__":
    main()
