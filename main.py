import re
from random import random
from faker import Faker


def valida_nome(nome):
    padrao = "^[A-Z][a-z]+\s[A-Z][a-z]+$"
    matches = re.search(padrao, nome)
    if matches:
        return 'Válido'
    else:
        return 'Inválido'


def valida_email(email):
    padrao = r"(^[a-z]+@[a-z]+(\.[a-z-.]+\.br$|\.br$))"
    # padrao = r"(^[a-z]+@[a-z]+\.[a-z-.]+$)"
    matches = re.search(padrao, email)
    if matches:
        return 'Válido'
    else:
        return 'Inválido'

def valida_senha(senha):
    padrao = "^(?=.*[0-9])(?=.*[A-Z])[0-9a-zA-Z]{8}$"
    matches = re.search(padrao, senha)
    if matches:
        return 'Válido'
    else:
        return 'Inválido'


def valida_cpf(p_cpf):
    padrao = "^([0-9]){3}\.([0-9]){3}\.([0-9]){3}-([0-9]){2}$"
    matches = re.search(padrao, p_cpf)
    if matches:
        return 'Válido'
    else:
        return 'Inválido'


def valida_telefone(p_telefone):
    padrao = "(^([(]\d{2}[)]\s[9]\d{4}[-]\d{4})|([(]\d{2}[)]\s[9]\d{4}\d{4})|(\d{2}\s[9]\d{8})$)+"
    matches = re.search(padrao, p_telefone)
    if matches:
        return 'Válido'
    else:
        return 'Inválido'


def valida_data(p_data):
    padrao = "\d{2}/\d{2}/\d{4}\s((0|1)[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])"
    matches = re.search(padrao, p_data)
    if matches:
        return 'Válido'
    else:
        return 'Inválido'


def valida_numeros(p_numero):
    padrao = "^(([+-]{0,1}[0-9]{1,}[.][0-9]+)|([+-]{0,1}[0-9]{1,})$)+"
    matches = re.search(padrao, p_numero)
    if matches:
        return 'Válido'
    else:
        return 'Inválido'


def testes():
    nomes = ["Alan Turing", "Noam Chomsky", "Ada Lovelace", "1Alan", "Alan", "A1an", "A1an Turing"]
    emails = ["a@a.br", "divulga@ufpa.br", "@", "a@.br", "T@teste.br"]
    senhas = ["518R2r5e", "F123456A", "1234567T", "ropsSoq0", "F1234567A", "abcdefgH", "1234567HI"]
    cpfs = ["123.456.789-09", "000.000.000-00", "123.456.789-0", "111.111.11-11"]
    telefones = ["(91) 99999-9999", "(91) 999999999", "91 999999999", "(91) 59999-9999", "99 99999-9999",
                 "(94)95555-5555"]
    datas = ["31/08/2019 20:14:55", "99/99/9999 23:59:59", "99/99/9999 3:9:9", "9/9/99 99:99:99"]
    numeros = ["-25.467", "1", "-1", "+1", "64.2", "1.", ".2", "+64,2"]

    print("Executando testes definidos no exercício..." + "\r\n")
    for nome in nomes:
        print(nome + " : " + valida_nome(nome))
    for email in emails:
        print(email + " : " + valida_email(email))
    for senha in senhas:
        print(senha + " : " + valida_senha(senha))
    for cpf in cpfs:
        print(cpf + " : " + valida_cpf(cpf))
    for telefone in telefones:
        print(telefone + " : " + valida_telefone(telefone))
    for data in datas:
        print(data + " : " + valida_data(data))
    for numero in numeros:
        print(numero + " : " + valida_numeros(numero))

def gera_dataset(p_qtde):
    exp = Faker('pt_BR')
    lst_nome = []
    lst_email = []
    lst_senha = []
    lst_cpf = []
    lst_telefone = []
    lst_data = []
    lst_numero = []
    i = 0
    while i < p_qtde:
        data = exp.date_of_birth()
        data_nasc = str((data.strftime('%d/%m/%Y %T')))
        numero = (random() + 10 * random())
        lst_nome.append(exp.name())
        lst_email.append(exp.email())
        lst_senha.append(exp.password())
        lst_cpf.append(exp.cpf())
        lst_telefone.append(exp.phone_number())
        lst_data.append(data_nasc)
        lst_numero.append(numero)

        i = i + 1
    else:
        print(lst_nome)
        for nome in lst_nome:
            print("Nome: " + nome + " - " + valida_nome(nome))
        print(lst_email)
        for email in lst_email:
            print(email + " : " + valida_email(email))
        print(lst_senha)
        for senha in lst_senha:
            print(senha + " : " + valida_senha(senha))
        print(lst_cpf)
        for cpf in lst_cpf:
            print(cpf + " : " + valida_cpf(cpf))
        print(lst_telefone)
        for telefone in lst_telefone:
            print(telefone + " : " + valida_telefone(telefone))
        print(lst_data)
        for data in lst_data:
            print(str(data) + " : " + valida_data(str(data)))
        print(lst_numero)
        for numero in lst_numero:
            print(str(numero) + " : " + valida_numeros(str(numero)))


def menu():
    opcao = input("Opções Disponíveis:" + "\r\n" +
                  "1. Validar nome:" + "\r\n" +
                  "2. Validar e-mail:" + "\r\n" +
                  "3. Validar senha:" + "\r\n" +
                  "4. Validar cpf:" + "\r\n" +
                  "5. Validar data:" + "\r\n" +
                  "6. Validar numero:" + "\r\n" +
                  "7. Validar telefone:" + "\r\n" +
                  "8. Executar testes pre-definidos:" + "\r\n" +
                  "9. Executar testes com dados aleatórios: " + "\r\n" + "\r\n"
                                                                         "Escolha sua opção: ")
    if opcao == "1":
        nome = input("Digite o Nome:")
        print(nome + " : " + valida_nome(nome))
    elif opcao == "2":
        email = input("Digite o e-mail:")
        print(email + " : " + valida_email(email))
    elif opcao == "3":
        senha = input("Digite a senha:")
        print(senha + " : " + valida_senha(senha))
    elif opcao == "4":
        cpf = input("Digite o cpf:")
        print(cpf + " : " + valida_cpf(cpf))
    elif opcao == "5":
        data = input("Digite a data:")
        print(data + " : " + valida_data(data))
    elif opcao == "6":
        numero = input("Digite o numero:")
        print(numero + " : " + valida_numeros(numero))
    elif opcao == "7":
        telefone = input("Digite o telefone:")
        print(telefone + " : " + valida_telefone(telefone))
    elif opcao == "8":
        testes()
    elif opcao == "9":
        qtde = int(input("Digite a quantidade de testes:"))
        gera_dataset(qtde)
    else:
        opcao = input("Opção Inválida. Digite q para sair ou qualquer outra tecla para repetir o menu: ")
        if opcao == "q":
            return
        else:
            menu()


menu()
