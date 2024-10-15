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
        self.blocos = [Bloco() for _ in range(self.tamanho)]  # Inicializa os blocos
        self.mapa_bits = [0] * self.tamanho  # Inicializa o mapa de bits, todos os blocos começam livres (0)

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
        # Imprime o estado de cada bloco no disco
        for i, bloco in enumerate(self.blocos):
            prox = bloco.proximo if bloco.proximo is not None else "None"
            print(f"Bloco {i}: {bloco.caractere}, próximo: {prox}")

    def imprimir_mapa_bits(self):
        # Imprime o estado atual do mapa de bits (livre = 0, ocupado = 1)
        print("Mapa de Bits:", self.mapa_bits)

class SistemaArquivos:
    def __init__(self, tamanho_disco):
        self.disco = Disco(tamanho_disco)
        self.tabela_arquivos = []

    def criar_arquivo(self, nome, conteudo):
        tamanho = len(conteudo)

        # Verifica se há blocos livres suficientes no mapa de bits
        blocos_disponiveis = self.disco.mapa_bits.count(0)
        if blocos_disponiveis < tamanho:
            print("Memória insuficiente!")
            return

        # Alocar blocos para o arquivo
        endereco_inicial = self.disco.alocar_bloco()
        bloco_atual = endereco_inicial

        for i, caractere in enumerate(conteudo):
            proximo_bloco = None
            if i < tamanho - 1:
                proximo_bloco = self.disco.alocar_bloco()

            self.disco.blocos[bloco_atual] = Bloco(caractere, proximo_bloco)
            bloco_atual = proximo_bloco

        # Adicionar o arquivo à tabela de arquivos
        novo_arquivo = TabelaArquivos(nome, tamanho, endereco_inicial)
        self.tabela_arquivos.append(novo_arquivo)
        print(f"Arquivo '{nome}' criado com sucesso.")

    def ler_arquivo(self, nome):
        arquivo = next((a for a in self.tabela_arquivos if a.nome == nome), None)
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
            proximo = bloco.proximo
            self.disco.blocos[endereco] = Bloco()  # Limpa o bloco
            self.disco.liberar_bloco(endereco)  # Libera o bloco no mapa de bits
            endereco = proximo

        self.tabela_arquivos.remove(arquivo)
        print(f"Arquivo '{nome}' excluído com sucesso.")

    def imprimir_tabela_arquivos(self):
        for arquivo in self.tabela_arquivos:
            print(f"Nome: {arquivo.nome}, Tamanho: {arquivo.tamanho}, Endereço: {arquivo.endereco_inicial}")

# Testando o sistema de arquivos com mapa de bits
'''sistema = SistemaArquivos(96)

print("=== Teste: Criação de Arquivos ===")
sistema.criar_arquivo('f01.file', 'PERNAMBUCO')
sistema.criar_arquivo('f02.file', 'São Paulo')
sistema.criar_arquivo('f03.file', 'Alagoas')

print("\n=== Estado do Disco ===")
sistema.disco.imprimir_disco()

print("\n=== Mapa de Bits ===")
sistema.disco.imprimir_mapa_bits()

print("\n=== Tabela de Arquivos ===")
sistema.imprimir_tabela_arquivos()

print("\n=== Teste: Exclusão de Arquivo ===")
sistema.excluir_arquivo('f02.file')

print("\n=== Estado do Disco Após Exclusão ===")
sistema.disco.imprimir_disco()

print("\n=== Mapa de Bits Após Exclusão ===")
sistema.disco.imprimir_mapa_bits()

print("\n=== Tabela de Arquivos Após Exclusão ===")
sistema.imprimir_tabela_arquivos()

print('\n=== Teste: Adicionar novo arquivo ===')
sistema.criar_arquivo('f04.file', 'Santa Catarina')

print("\n=== Estado do Disco Após Acréscimo ===")
sistema.disco.imprimir_disco()

print("\n=== Mapa de Bits Após Acréscimo ===")
sistema.disco.imprimir_mapa_bits()

print("\n=== Tabela de Arquivos Após Acréscimo ===")
sistema.imprimir_tabela_arquivos()
'''