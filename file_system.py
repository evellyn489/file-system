class Bloco:
    def __init__(self, caractere=None, proximo=None):
        self.caractere = caractere 
        self.proximo = proximo  

class TabelaArquivos:
    def __init__(self, nome, tamanho, endereco_inicial):
        self.nome = nome  # Nome do arquivo
        self.tamanho = tamanho  # Tamanho em caracteres
        self.endereco_inicial = endereco_inicial  # Endereço do primeiro bloco no array

class Disco:
    def __init__(self, tamanho):
        self.blocos = []  

        for _ in range(tamanho):  
            bloco = Bloco() 
            self.blocos.append(bloco) 

        self.livre = list(range(tamanho))  # Lista de blocos livres (por índice)
    
    def imprimir_disco(self):
        for i, bloco in enumerate(self.blocos):
            if bloco.proximo is not None:
                prox = bloco.proximo
            else:
                prox = "None"

            print(f"Bloco {i}: {bloco.caractere}, próximo: {prox}")

class SistemaArquivos:
    def __init__(self, tamanho_disco):
        self.disco = Disco(tamanho_disco)
        self.tabela_arquivos = []  

    def criar_arquivo(self, nome, conteudo):
        tamanho = len(conteudo)

        if len(self.disco.livre) < tamanho:
            print("Memória insuficiente!")
            return
 
        # Alocar blocos para o arquivo
        endereco_inicial = self.disco.livre.pop(0) 
        bloco_atual = endereco_inicial

        for i, caractere in enumerate(conteudo):
            if i < tamanho - 1:
                proximo_bloco = self.disco.livre.pop(0)
                self.disco.blocos[bloco_atual] = Bloco(caractere, proximo_bloco)
                bloco_atual = proximo_bloco
            else:
                self.disco.blocos[bloco_atual] = Bloco(caractere, None)

        # Adicionar arquivo à tabela de arquivos
        novo_arquivo = TabelaArquivos(nome, tamanho, endereco_inicial)
        self.tabela_arquivos.append(novo_arquivo)
        print(f"Arquivo '{nome}' criado com sucesso.")

    def ler_arquivo(self, nome):
        arquivo = None
        for a in self.tabela_arquivos:
            if a.nome == nome:
                arquivo = a
                break

        if arquivo is None:
            print(f"Arquivo '{nome}' não encontrado.")
            return
        
        endereco = arquivo.endereco_inicial
        conteudo = []
        while endereco is not None:
            bloco = self.disco.blocos[endereco]
            conteudo.append(bloco.caractere)
            endereco = bloco.proximo
        
        print(f"Conteúdo de '{nome}': {''.join(conteudo)}")

    def excluir_arquivo(self, nome):
        arquivo = next((a for a in self.tabela_arquivos if a.nome == nome), None)
        if arquivo is None:
            print(f"Arquivo '{nome}' não encontrado.")
            return

        endereco = arquivo.endereco_inicial

        while endereco is not None:
            bloco = self.disco.blocos[endereco]
            self.disco.livre.append(endereco)
            proximo = bloco.proximo
            self.disco.blocos[endereco] = Bloco() 
            endereco = proximo

        self.disco.livre.sort()

        self.tabela_arquivos.remove(arquivo)
        print(f"Arquivo '{nome}' excluído com sucesso.")

    def imprimir_tabela_arquivos(self):
        for arquivo in self.tabela_arquivos:
            print(f"Nome: {arquivo.nome}, Tamanho: {arquivo.tamanho}, Endereço: {arquivo.endereco_inicial}")

'''sistema = SistemaArquivos(32)

print("=== Teste: Criação de Arquivos ===")
sistema.criar_arquivo('f01.file', 'PERNAMBUCO')
sistema.criar_arquivo('f02.file', 'São Paulo')
sistema.criar_arquivo('f03.file', 'Alagoas')

print("\n=== Estado do Disco ===")
sistema.disco.imprimir_disco()

print("\n=== Tabela de Arquivos ===")
sistema.imprimir_tabela_arquivos()

print("\n=== Teste: Leitura de Arquivo ===")
sistema.ler_arquivo('f01.file')
sistema.ler_arquivo('f02.file')

print("\n=== Teste: Exclusão de Arquivo ===")
sistema.excluir_arquivo('f02.file')

print("\n=== Estado do Disco Após Exclusão ===")
sistema.disco.imprimir_disco()

print("\n=== Tabela de Arquivos Após Exclusão ===")
sistema.imprimir_tabela_arquivos()

print('\n=== Adicionar novo arquivo ===')
sistema.criar_arquivo('f04.file', 'Santa Catarina')

print("\n=== Estado do Disco Após Acréscimo ===")
sistema.disco.imprimir_disco()

print("\n=== Tabela de Arquivos Após Acréscimo ===")
sistema.imprimir_tabela_arquivos()

print("\n=== Teste: Leitura de Arquivo ===")
sistema.ler_arquivo('f04.file')'''