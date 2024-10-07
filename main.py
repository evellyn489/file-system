from file_system import SistemaArquivos

def menu():
    sistema = SistemaArquivos(32)

    while True:
        print("="*5 + " Menu " + "="*5)
        print("1. Criar Arquivo")
        print("2. Ler Arquivo")
        print("3. Excluir Arquivo")
        print("4. Imprimir Disco")
        print("5. Imprimir Tabela de Arquivos")
        print("6. Sair")
        
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input('Digite o nome do arquivo: ')
            conteudo = input('Digite o conteúdo do arquivo: ')
            sistema.criar_arquivo(nome, conteudo)

        elif opcao == 2:
            nome = input("Digite o nome do arquivo a ser lido: ")
            sistema.ler_arquivo(nome)
        
        elif opcao == 3:
            nome = input("Digite o nome do arquivo a ser excluído: ")
            sistema.excluir_arquivo(nome)
        
        elif opcao == 4:
            sistema.disco.imprimir_disco()
        
        elif opcao == 5:
            sistema.imprimir_tabela_arquivos()
        
        elif opcao == 6:
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida, tente novamente.")

menu()
        

