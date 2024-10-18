from rich.console import Console
from prettytable import PrettyTable

console = Console()
class Bloco:
    def __init__(self, caractere=None, proximo=None):
        self.caractere = caractere
        self.proximo = proximo  # Ponteiro para o próximo bloco, seja livre ou não

class TabelaArquivos:
    def __init__(self, nome, tamanho, endereco_inicial):
        self.nome = nome
        self.tamanho = tamanho
        self.endereco_inicial = endereco_inicial

class Disco:
    def __init__(self, tamanho):
        self.tamanho = tamanho // 3  # Cada bloco tem 3 bytes
        self.blocos = []
        for _ in range(self.tamanho):
            self.blocos.append(Bloco())  # Inicializa os blocos
        self.mapa_bits = []
        for _ in range(self.tamanho):
            self.mapa_bits.append(0)  # Inicializa o mapa de bits, todos os blocos começam livres (0)

    def alocar_bloco(self):
        # Percorre o mapa de bits para encontrar o primeiro bloco livre (0)
        for i in range(self.tamanho):
            if self.mapa_bits[i] == 0:  # Se o bloco está livre
                self.mapa_bits[i] = 1  # Marca o bloco como ocupado
                return i  # Retorna o índice do bloco alocado
        return None  # Se nenhum bloco estiver livre, retorna None

    def liberar_bloco(self, indice):
        # Libera o bloco no mapa de bits
        self.mapa_bits[indice] = 0  # Marca o bloco como livre

    def imprimir_disco(self):
        table = PrettyTable()
        table.field_names = ["Bloco", "Conteúdo", "Próximo"]

        for i in range(len(self.blocos)):
            bloco = self.blocos[i]
            conteudo = bloco.caractere if bloco.caractere is not None else "None"
            proximo = bloco.proximo if bloco.proximo is not None else "None"
            table.add_row([i, conteudo, proximo])

        console.print("\n[bold underline]Estado do Disco:[/bold underline]")
        console.print(table)

    def imprimir_mapa_bits(self):
        console.print("\n[bold underline]Mapa de Bits:[/bold underline]", str(self.mapa_bits)) 

class SistemaArquivos:
    def __init__(self, tamanho_disco):
        self.disco = Disco(tamanho_disco)
        self.tabela_arquivos = []

    def criar_arquivo(self, nome, conteudo):
        for arquivo in self.tabela_arquivos:
            if arquivo.nome == nome:
                console.print(f"[bold red]Erro: O arquivo '{nome}' já existe![/bold red]")
                return
        
        tamanho = len(conteudo)

        # Verifica se há blocos livres suficientes no mapa de bits
        blocos_disponiveis = 0
        for bit in self.disco.mapa_bits:
            if bit == 0:
                blocos_disponiveis += 1

        if blocos_disponiveis < tamanho:
            console.print("[bold red]Memória insuficiente![/bold red]")
            return

        # Alocar blocos para o arquivo
        endereco_inicial = self.disco.alocar_bloco()
        bloco_atual = endereco_inicial

        for i in range(tamanho):
            caractere = conteudo[i]
            proximo_bloco = None
            if i < tamanho - 1:
                proximo_bloco = self.disco.alocar_bloco()

            self.disco.blocos[bloco_atual] = Bloco(caractere, proximo_bloco)
            bloco_atual = proximo_bloco

        # Adicionar o arquivo à tabela de arquivos
        novo_arquivo = TabelaArquivos(nome, tamanho, endereco_inicial)
        self.tabela_arquivos.append(novo_arquivo)
        console.print(f"Arquivo '[bold]{nome}[/bold]' criado com sucesso.")

    def ler_arquivo(self, nome):
        arquivo = None
        for a in self.tabela_arquivos:
            if a.nome == nome:
                arquivo = a
                break
        
        if arquivo is None:
            console.print(f"Arquivo '{nome}' [bold red]não[/bold red] encontrado.")
            return

        endereco = arquivo.endereco_inicial
        conteudo = []
        while endereco is not None:
            bloco = self.disco.blocos[endereco]
            conteudo.append(bloco.caractere)
            endereco = bloco.proximo

        print(f"Conteúdo de '{nome}': {''.join(conteudo)}")

    def excluir_arquivo(self, nome):
        arquivo = None
        for a in self.tabela_arquivos:
            if a.nome == nome:
                arquivo = a
                break

        if arquivo is None:
            console.print(f"Arquivo '{nome}' [bold red]não[/bold red] encontrado.")
            return

        endereco = arquivo.endereco_inicial

        while endereco is not None:
            bloco = self.disco.blocos[endereco]
            proximo = bloco.proximo
            self.disco.blocos[endereco] = Bloco()  # Limpa o bloco
            self.disco.liberar_bloco(endereco)  # Libera o bloco no mapa de bits
            endereco = proximo

        self.tabela_arquivos.remove(arquivo)
        console.print(f"Arquivo '{nome}' [bold blue]excluído[/bold blue] com sucesso.")

    def imprimir_tabela_arquivos(self):
        table = PrettyTable()
        table.field_names = ["Nome", "Tamanho", "Endereço Inicial"]

        for arquivo in self.tabela_arquivos:
            table.add_row([arquivo.nome, arquivo.tamanho, arquivo.endereco_inicial])

        console.print("\n[bold underline]Tabela de Arquivos:[/bold underline]")
        print(table)

# Testando o sistema de arquivos com mapa de bits
'''sistema = SistemaArquivos(96)

print("=== Teste: Criação de Arquivos ===")
sistema.criar_arquivo('f01.file', 'PERNAMBUCO')
sistema.criar_arquivo('f02.file', 'São Paulo')
sistema.criar_arquivo('f03.file', 'Alagoas')

sistema.disco.imprimir_disco()
sistema.disco.imprimir_mapa_bits()
sistema.imprimir_tabela_arquivos()

print("\n=== Teste: Exclusão de Arquivo ===")
sistema.excluir_arquivo('f02.file')

sistema.disco.imprimir_disco()
sistema.disco.imprimir_mapa_bits()
sistema.imprimir_tabela_arquivos()

print('\n=== Teste: Adicionar novo arquivo ===')
sistema.criar_arquivo('f04.file', 'Santa Catarina')

sistema.disco.imprimir_disco()
sistema.disco.imprimir_mapa_bits()
sistema.imprimir_tabela_arquivos()

print('\n=== Teste: Adicionar novo arquivo sem espaço ===')
sistema.criar_arquivo('f05.file', 'Rio de Janeiro')
'''