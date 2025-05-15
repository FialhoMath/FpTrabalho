import os

os.system("cls")
Pets = []

def calcular_idade(nascimento):
    try:
        dia_nasc, mes_nasc, ano_nasc = map(int, nascimento.split("/"))
        # Obter data atual manualmente (substitua conforme necessário)
        dia_atual = 20
        mes_atual = 5
        ano_atual = 2025

        idade = ano_atual - ano_nasc
        if (mes_atual, dia_atual) < (mes_nasc, dia_nasc):
            idade -= 1
        return idade
    except:
        return 0

def gerar_recomendacoes(especie, idade):
    especie = especie.lower()
    recomendacoes = []
    if especie == "cachorro":
        if 0 < idade < 1:
            recomendacoes.extend([
                "Alimentacao: duas vezes ao dia.",
                "Brinquedos: bolas para corrida.",
                "Atividade: passeios diarios."
            ])
        elif 1 <= idade < 5:
            recomendacoes.extend([
                "Alimentacao: tres vezes ao dia.",
                "Brinquedos: resistentes para mordida.",
                "Atividade: passeios e brincadeiras."
            ])
        elif 5 <= idade < 10:
            recomendacoes.extend([
                "Alimentacao: tres vezes ao dia.",
                "Brinquedos: gasto moderado de energia.",
                "Atividade: caminhadas regulares."
            ])
        else:
            recomendacoes.extend([
                "Alimentacao: duas vezes ao dia.",
                "Brinquedos: atividades leves.",
                "Atividade: pequenas caminhadas."
            ])
    elif especie == "gato":
        if 0 < idade < 1:
            recomendacoes.extend([
                "Alimentacao: duas vezes ao dia.",
                "Brinquedos: bolas leves e penas.",
                "Atividade: exploracao e brincadeiras."
            ])
        elif 1 <= idade < 5:
            recomendacoes.extend([
                "Alimentacao: tres vezes ao dia.",
                "Brinquedos: arranhadores e ratinhos.",
                "Atividade: atividades noturnas."
            ])
        elif 5 <= idade < 10:
            recomendacoes.extend([
                "Alimentacao: duas vezes ao dia.",
                "Brinquedos: moderacao.",
                "Atividade: ambiente enriquecido."
                ])
        else:
            recomendacoes.extend([
                "Alimentacao: leve e controlada.",
                "Brinquedos: suaves.",
                "Atividade: baixo impacto."
                ])
    return " | ".join(recomendacoes)

def carregar_pets():
    try:
        with open("cadastro_PET", "r") as file:
            for linha in file:
                dados = linha.strip().split("|")
                if len(dados) == 6:
                    nome, especie, raca, nascimento, peso, recomendacoes = dados
                    Pets.append({
                        "nome": nome,
                        "especie": especie,
                        "raca": raca,
                        "nascimento": nascimento,
                        "peso": peso,
                        "recomendacoes": recomendacoes
                    })
    except FileNotFoundError:
        pass

def salvar_pets():
    with open("cadastro_PET", "w") as file:
        for pet in Pets:
            linha = f"{pet['nome']}|{pet['especie']}|{pet['raca']}|{pet['nascimento']}|{pet['peso']}|{pet['recomendacoes']}\n"
            file.write(linha)

def adicionar_pet():
    nome = input("Nome do PET: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    peso = input("Peso (em kg): ")

    idade = calcular_idade(nascimento)
    recomendacoes = gerar_recomendacoes(especie, idade)

    Pets.append({
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "nascimento": nascimento,
        "peso": peso,
        "recomendacoes": recomendacoes
    })
    salvar_pets()
    print("Pet cadastrado com sucesso!\n")

def visualizar_pets():
    if not Pets:
        print("Nenhum pet cadastrado.\n")
        return

    for i, pet in enumerate(Pets):
        idade = calcular_idade(pet['nascimento'])
        print(f"[{i}] Nome: {pet['nome']}, Espécie: {pet['especie']}, Raça: {pet['raca']}, "
              f"Nascimento: {pet['nascimento']}, Idade: {idade} anos, Peso: {pet['peso']}")
        print(f"Recomendações: {pet['recomendacoes']}")
    print()

def editar_pet():
    visualizar_pets()
    if not Pets:
        return

    try:
        indice = int(input("Índice do PET a editar: "))
        if 0 <= indice < len(Pets):
            pet = Pets[indice]
            pet["nome"] = input(f"Novo nome ({pet['nome']}): ") or pet["nome"]
            pet["especie"] = input(f"Nova espécie ({pet['especie']}): ") or pet["especie"]
            pet["raca"] = input(f"Nova raça ({pet['raca']}): ") or pet["raca"]
            pet["nascimento"] = input(f"Nova data de nascimento ({pet['nascimento']}): ") or pet["nascimento"]
            pet["peso"] = input(f"Novo peso ({pet['peso']}): ") or pet["peso"]

            idade = calcular_idade(pet["nascimento"])
            pet["recomendacoes"] = gerar_recomendacoes(pet["especie"], idade)

            salvar_pets()
            print("Cadastro atualizado!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def excluir_pet():
    visualizar_pets()
    if not Pets:
        return

    try:
        indice = int(input("Índice do PET a excluir: "))
        if 0 <= indice < len(Pets):
            removido = Pets.pop(indice)
            salvar_pets()
            print(f"{removido['nome']} removido com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def registrar_eventos():
    if not Pets:
        print("Nenhum pet para registrar eventos.\n")
        return

    for pet in Pets:
        print(f"\nRegistrando eventos para {pet['nome']}:")
        if input("Registrar vacinação? (S/N): ").strip().lower() == "s":
            data = input("Data da vacinação (dd/mm/aaaa): ")
            obs = input("Observações: ")
            print(f"Vacina registrada: {data}, Obs: {obs}")

        if input("Registrar consulta veterinária? (S/N): ").strip().lower() == "s":
            data = input("Data da consulta (dd/mm/aaaa): ")
            obs = input("Observações: ")
            print(f"Consulta registrada: {data}, Obs: {obs}")

        if input("Registrar aplicação de remédio? (S/N): ").strip().lower() == "s":
            data = input("Data da aplicação (dd/mm/aaaa): ")
            obs = input("Observações: ")
            print(f"Remédio registrado: {data}, Obs: {obs}")
    print()

# Programa principal
carregar_pets()

while True:
    print("==== MENU ====")
    print("1 - Adicionar PET")
    print("2 - Visualizar PETs")
    print("3 - Editar PET")
    print("4 - Excluir PET")
    print("5 - Registrar eventos")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_pet()
    elif opcao == "2":
        visualizar_pets()
    elif opcao == "3":
        editar_pet()
    elif opcao == "4":
        excluir_pet()
    elif opcao == "5":
        registrar_eventos()
    elif opcao == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.\n")

def create_task(tipo_da_task: int, valor: int) -> str:
    if tipo_da_task == 1:
        return create_task_1(valor)
    elif tipo_da_task == 2:
        return create_task_2(valor)
    else:
        print("Tipo de task inválido!")
        return ""

def create_task_1(meses: int) -> str:
    return f"Levar ao veterinário a cada {meses} mês(es)"

def create_task_2(passeios: int) -> str:
    return f"Fazer {passeios} passeio(s) por semana"

def adicionar_tarefas():
    visualizar_pets()
    if not Pets:
        return

    try:
        indice = int(input("Escolha o índice do PET para adicionar tarefas: "))
        if 0 <= indice < len(Pets):
            print("Tipos de tarefas disponíveis:")
            print("1 - Veterinário")
            print("2 - Passeios")
            tipo = int(input("Escolha o tipo da tarefa (1 ou 2): "))
            valor = int(input("Digite o valor correspondente (meses para veterinário ou passeios por semana): "))
            tarefa = create_task(tipo, valor)
            if "tarefas" not in Pets[indice]:
                Pets[indice]["tarefas"] = []
            Pets[indice]["tarefas"].append(tarefa)
            salvar_pets()
            print("Tarefa adicionada com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")
