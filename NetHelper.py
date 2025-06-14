#importação da biblioteca subprocess para executar ferramentas de linha de comando do windows e processar a saída delas no terminal
import subprocess

#Função ipconfig para executar o comando ipconfig e obter as configurações de rede do dispositivo
def ipConfig():
    try:
        result = subprocess.run('ipconfig', capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)
#Função ipconfigAll para executar o comando ipconfig /all e obter mais detalhes das configurações de rede do dispositivo
def ipConfigAll():
    try:
        result = subprocess.run('ipconfig/all', capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)
#função ping para testar conectividade com um dispositivo diferente, seja po Ip ou pelo nome do site
def ping():
    #a variavel ip é criada uma vez que o comando ping necessita de um valor de ip ou nome de site
    ip=input("digite o ip/site:")
    print("Aguarde um instante...")
    try:
        result = subprocess.run('ping '+ip, capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)
#função igual a Ping mas com a opção de escolher um número de pacotes
def pingN():
    ip=input("digite o ip/site:")
    #para evitar erros a variavel pacotes foi introduzida com valor nulo
    pacotes=None
    #O valor pacotes entrará em loop até conseguir um valor inteiro válido. Se botar um valor real ou caractere o valor de pacotes
    #não será atribuido e que continuará o loop
    while pacotes==None:
        try:
            pacotes=int(input("Digite quantos pacotes serão enviados"))
        except:
            print("Inválido! Digite um valor inteiro")
    #Como o comando do sub process somente aceita string o valor de pacotes é convertido em string e atribuido a variavel n
    n=str(pacotes)
    print("Aguarde um instante...")
    try:
        result = subprocess.run('ping -n '+n+' '+ip, capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)
#Consultar servidores de nomes DNS e obter informações sobre nomes de domínio e endereços IP
def nslookup():
    #a variavel ip é criada pois um parametro para o comando nslookup é o ip ou o nome do site
    ip=input("digite o site/Ip:")
    try:
        result = subprocess.run('nslookup '+ip, capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)
#Rastrear a rota que um pacote IP percorre até o destino na rede
def tracert():
    #a variavel ip é criada pois um parametro para o comando tracert é o ip ou o nome do site
    ip=input("digite o ip/site:")
    print("Aguarde um instante...")
    try:
        result = subprocess.run('tracert '+ip, capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)
#exibe informações detalhadas sobre as conexões de rede do sistema
def netstat():
    print("Aguarde um instante...")
    try:
        result = subprocess.run('netstat', capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)
#Listar todas as conexões de rede ativas e portas de escuta, juntamente com o ID do processo associado
def netstatano():
    print("Aguarde um instante...")
    try:
        result = subprocess.run('netstat -ano', capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)

def arp():
    try:
        result = subprocess.run('arp -a', capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)

def route():
    try:
        result = subprocess.run('route print', capture_output=True, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ",e)

def opcoes():
    global opcao
    opcao=input("1 ipConfig: Mostrar informações como endereço IP, máscara de sub-rede, gateway padrão e configurações de DNS\n"
                "2 ipConfigAll: Exibir informações detalhadas sobre todas as configurações de rede, incluindo endereços MAC, servidores DNS e DHCP\n"
                "3 ping: Testar conectividade\n"
                "4 ping -n: Testar conectividade com seleção de quantos pacotes enviar\n"
                "5 nslookup: Obter informações sobre nomes de domínio e endereços IP\n"
                "6 tracert: Rastrear o caminho de um pacote de dados até um destino\n"
                "7 netstat: Exibir estatísticas sobre as conexões de rede, tabelas de roteamento e interfaces de rede \n"
                "8 netstat -ano: Exibir todas as portas abertas e conexões ativas numericamente, incluindo o ID do processo\n"
                "9 arp-a: Exibir a tabela de ARP atual, mostrando os endereços IP e seus respectivos endereços MAC\n"
                "10 route print: Exibir a tabela de roteamento IP\n"
                "11 Finalizar\n\n")

#apresentações
print("\nSeja bem vindo!\nEsse programa foi criado para ajudar técnicos em informáica e técnicos em redes a solucionar problemas de conexão.\n")
opcoes()
while opcao!="11":
    if opcao=="1":
        ipConfig()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="2":
        ipConfigAll()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="3":
        ping()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="4":
        pingN()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="5":
        nslookup()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="6":
        tracert()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="7":
        netstat()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="8":
        netstatano()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="9":
        arp()
        input("Pressione enter para prosseguir\n")
        opcoes()
    elif opcao=="10":
        route()
        input("Pressione enter para prosseguir\n")
        opcoes()
    else:
        print("Opção invalida! Por favor selecione uma opção valida.\n")
        opcoes()
print("Obrigado por usar o NetHelper")
