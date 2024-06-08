def minissistema_help():
    comando = ""
    while comando != "FIM":
        comando = input("digite o comando (ou 'FIM' para sair): ")
        if comando != "FIM" and comando:
            help(comando)
        elif comando == "FIM":
            print("encerrando o programa...")

minissistema_help()