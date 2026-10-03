
import os

alunos_cadastrados = {}


def imprimir_título(titulo=str):
    print('---' * 10)
    print(titulo.center(30))
    print('---' * 10)


def pressione_enter():
    input('\nAperte ENTER para continuar...')


def imprimir_menu():
    imprimir_título('Menu')
    print("""
1 - Adicionar aluno
2 - Listar todos os alunos
3 - Buscar aluno pelo nome
4 - Atualizar aluno
5 - Remover aluno 
6 - Mostrar Média geral das notas
7 - Sair
    """)


def main():
    while True:
        os.system('cls')
        imprimir_menu()
        escolha = input("-\nEscolha de 1 a 7: ")
        if escolha == '1':
            adicionar_aluno('Aluno Cadastrado com Sucesso!')
        elif escolha == '2':
            listar_todos_alunos()
        elif escolha == '3':
            buscar_aluno_pelo_nome()
        elif escolha == '4':
            atualizar_cadastro_aluno()
        elif escolha == '5':
            remover_aluno()
        elif escolha == '6':
            media_geral_turmas()
        elif escolha == '7': 
            print('\n- Desligando Sistema...')
            break
        else:
            print('\nERRO! Digite apenas números de 1 a 6.')
            pressione_enter()


def adicionar_aluno(mensagem=str):
    global alunos_cadastrados
    while True:
        try:
            os.system('cls')
            imprimir_título('Adicionar Aluno')
            nome = str(input('Nome do aluno: ').capitalize())
            idade = int(input('Qual idade do aluno: '))
            nota = float(input('Qual a nota do aluno: '))

            if nota >= 0 and nota <= 10 and idade > 0:
                alunos_cadastrados[nome] = [idade, nota]
                print(f"\n- {mensagem} \n")
                pressione_enter()
                break
            else:
                print('\nErro! A nota do deve aluno deve ter valores de 0 a 10. ')
                pressione_enter()

        except Exception:
            print('\nERRO! DIgite valores Válidos')
            pressione_enter()


def listar_todos_alunos():
    global alunos_cadastrados
    for nome, idade_nota in alunos_cadastrados.items():
        print(f'- Nome: {nome} | Idade: {idade_nota[0]} | Nota: {idade_nota[1]:.2f} ')
    input('\nAperte ENTER para continuar...')


def buscar_aluno_pelo_nome():
    global alunos_cadastrados
    imprimir_título('Buscar ALuno')
    buscar_nome = input("Digite o nome do aluno: ")
    aluno_nao_encontrado = True
    for aluno in alunos_cadastrados.keys():
        if aluno == buscar_nome:
            print(f'- Nome: {buscar_nome} | Idade: {alunos_cadastrados[buscar_nome][0]} | Nota: {alunos_cadastrados[buscar_nome][1]:.2f} ')
            aluno_nao_encontrado = False
            break
    if aluno_nao_encontrado:
        print("Aluno não encontrado.")
    pressione_enter()


def remover_aluno():
    global alunos_cadastrados
    imprimir_título('Remover Aluno')
    buscar_nome = str(input("Digite o nome do aluno: "))
    for aluno in alunos_cadastrados.keys():
            if aluno == buscar_nome:
                print('Aluno Removido.')
                alunos_cadastrados.pop(buscar_nome)
                break
            else: 
                print("Aluno não encontrado.")
    pressione_enter()


def atualizar_cadastro_aluno():
    global alunos_cadastrados
    os.system('cls')
    imprimir_título('Atualizar o Cadastro do ALuno')
    buscar_nome = input("Digite o nome do aluno: ")
    aluno_nao_encontrado = True
    for aluno in alunos_cadastrados.keys():
        if aluno == buscar_nome:
            if aluno == buscar_nome:
                alunos_cadastrados.pop(buscar_nome)
                aluno_nao_encontrado = False
                print(alunos_cadastrados)
                adicionar_aluno("Aluno Atualizado com Sucesso!") 
                break
               
    if aluno_nao_encontrado:
        print("Aluno não encontrado.")
    pressione_enter()


def media_geral_turmas():
    global alunos_cadastrados
    quantidade_alunos = 0
    total = 0
    for aluno in alunos_cadastrados.values():
        total += aluno[1]
        quantidade_alunos += 1
    media = total / quantidade_alunos
    print(f'\n - Média total da turma: {media:.2f}')
    pressione_enter()
        

if __name__ == "__main__":
    main()
