from database import (
    criar_tabela,
    adicionar_funcionario,
    buscar_funcionarios,
    desativar_funcionario,
    contar_ativos_inativos,
    buscar_avancado
)
from service import (
    listar_funcionarios,
    ler_int,
    validar_nome,
    validar_cargo
)

def menu():
    print("\n====== WORKFORCE CLI ======")
    print("1 - Cadastrar funcionário")
    print("2 - Listar todos")
    print("3 - Listar ativos")
    print("4 - Desativar funcionário")
    print("5 - Relatório (ativos / inativos)")
    print("6 - Busca avançada")
    print("0 - Sair")

def cadastrar():
    nome = input("Nome: ")
    ok, nome_ou_msg = validar_nome(nome)
    if not ok:
        print("Erro:", nome_ou_msg)
        return
    cargo = input("Cargo: ")
    ok, cargo_ou_msg = validar_cargo(cargo)
    if not ok:
        print("Erro:", cargo_ou_msg)
        return
    novo_id = adicionar_funcionario(nome_ou_msg, cargo_ou_msg)
    print(f"Funcionário cadastrado com ID {novo_id}.")

def listar_todos():
    funcionarios = buscar_funcionarios()
    linhas = listar_funcionarios(funcionarios)
    if not linhas:
        print("Nenhum funcionário cadastrado.")
        return
    for linha in linhas:
        print(linha)

def listar_ativos():
    funcionarios = buscar_funcionarios(apenas_ativos=True)
    linhas = listar_funcionarios(funcionarios)
    if not linhas:
        print("Nenhum funcionário ativo.")
        return
    for linha in linhas:
        print(linha)

def desativar():
    funcionario_id = ler_int("ID para desativar: ")
    if funcionario_id is None:
        print("ID inválido.")
        return
    if desativar_funcionario(funcionario_id):
        print("Funcionário desativado.")
    else:
        print("ID não encontrado ou já inativo.")

def relatorio():
    ativos, inativos = contar_ativos_inativos()
    print("\n--- RELATÓRIO ---")
    print(f"Ativos:   {ativos}")
    print(f"Inativos: {inativos}")
    print(f"Total:    {ativos + inativos}")

def busca_avancada():
    nome = input("Parte do nome (ENTER para ignorar): ").strip()
    cargo = input("Parte do cargo (ENTER para ignorar): ").strip()
    print("Situação:")
    print("1 - Todos")
    print("2 - Apenas ativos")
    print("3 - Apenas inativos")
    escolha = input("Escolha: ").strip()
    apenas_ativos = None
    if escolha == "2":
        apenas_ativos = True
    elif escolha == "3":
        apenas_ativos = False
    funcionarios = buscar_avancado(
        nome_parte=nome if nome else None,
        cargo_parte=cargo if cargo else None,
        apenas_ativos=apenas_ativos
    )
    linhas = listar_funcionarios(funcionarios)
    if not linhas:
        print("Nenhum resultado.")
        return
    for linha in linhas:
        print(linha)

def main():
    criar_tabela()
    while True:
        menu()
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar_todos()
        elif opcao == "3":
            listar_ativos()
        elif opcao == "4":
            desativar()
        elif opcao == "5":
            relatorio()
        elif opcao == "6":
            busca_avancada()
        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()
