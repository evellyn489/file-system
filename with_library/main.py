from file_system_style import SistemaArquivos
from rich.console import Console
from time import sleep

console = Console()

def menu():

    console.print("="*5 + ' [bold magenta]SISTEMA DE ARQUIVOS[/bold magenta] ' + "="*5)
    print()

    sleep(1)

    console.print('[bold cyan]Bem-vindo ao Sistema de Arquivos[bold cyan]')
    sleep(1)

    print()

    qtd_memoria = int(input('Quantos bytes tem a memória do sistema?'))
    print()

    sistema = SistemaArquivos(qtd_memoria)

    while True:
        sleep(2)
        console.print("="*5 + " [bold cyan]Menu[/bold cyan] " + "="*5)
        console.print('[bold blue]O que você deseja fazer?[/bold blue]')
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
            console.print("[bold]Saindo do programa...[/bold]")
            sleep(1)
            break
        
        else:
            print("Opção inválida, tente novamente.")

menu()
        

