# 📂 File System
<p>Este projeto implementa um sistema de arquivos utilizando lista encadeada para armazenar dados e um mapa de bits para gerenciar a alocação de blocos de memória. O sistema possui funcionalidades básicas como criar, ler e excluir arquivos. Ele foi desenvolvido em duas versões: uma com estilização e outra sem.</p>

## ⚙️ Funcionalidades
<ul>
  <li>📄 <strong>Criação de Arquivos</strong>: Armazena o conteúdo em blocos de memória gerenciados pelo mapa de bits.</li>
  <li>🔍 <strong>Leitura de Arquivos</strong>: Permite acessar o conteúdo dos arquivos armazenados no sistema.</li>
  <li>🗑️ <strong>Exclusão de Arquivos</strong>: Libera os blocos de memória ocupados por arquivos excluídos.</li>
  <li>📊 <strong>Impressão de Tabela de Arquivos</strong>: Exibe os arquivos armazenados com nome, tamanho e endereço inicial.</li>
  <li>🖥️ <strong>Impressão de Disco e Mapa de Bits</strong>: Mostra o estado atual do disco e o mapa de bits para visualização dos blocos livres e ocupados.</li>
</ul>

## 🛠️ Estrutura do Projeto
<ul>
  <li>🧱 <strong>Bloco</strong>: Representa um bloco de memória que armazena um caractere e o ponteiro para o próximo bloco.</li>
  <li>📂 <strong>TabelaArquivos</strong>: Gerencia a tabela de arquivos que contém o nome, tamanho e endereço inicial de cada arquivo.</li>
  <li>💾 <strong>Disco</strong>: Implementa o disco virtual, com blocos de 3 bytes cada, e gerencia o mapa de bits para alocação e liberação de blocos.</li>
  <li>🗄️ <strong>SistemaArquivos</strong>: Controla o sistema de arquivos, fornecendo as funções de criação, leitura e exclusão de arquivos.</li>
</ul>

## 🧩 Pré-requisitos
<ul>
  <li>🐍 Python 3.0+</li>
  <li>📚 Bibliotecas <strong>rich</strong> e <strong>prettytable</strong> para a versão estilizada</li>
</ul>

## 🐍 Como Fazer a Instalação do Python
<ol>
  <li>📥 Instalar Python: Caso ainda não tenha o Python instalado, faça o download e instale a versão mais recente do Python 3 a partir do <a href="https://www.python.org/downloads/">site oficial</a>.</li>
  <li>✅ Verificar a Instalação: Após instalar o Python, abra o terminal ou prompt de comando e verifique se a instalação foi bem-sucedida com o seguinte comando: <code>python --version</code> ou <code>python3 --version</code>.</li>
</ol>

## 📦 Como Fazer a Instalação das Dependências
<p>Após instalar o Python, instale as bibliotecas necessárias executando o seguinte comando no terminal:</p>

<pre><code>pip install rich prettytable</code></pre>

## 🚀 Como Executar

### 🎨 Versão Estilizada
<p>A versão estilizada do sistema de arquivos utiliza as bibliotecas <strong>rich</strong> e <strong>prettytable</strong> para uma interface mais agradável. Para executar essa versão:</p>
<ol>
  <li>⚙️ Clone o repositório.</li>
  <li>📦 Instale as dependências.</li>
  <li>📁 Dentro da pasta <code>with_library</code>, execute o script principal (<code>main.py</code>).</li>
</ol>

### 🔧 Versão sem Estilização
<p>Se preferir uma versão mais simples, sem a estilização das saídas, siga os passos:</p>
<ol>
  <li>⚙️ Clone o repositório.</li>
  <li>📁 Dentro da pasta <code>without_library</code>, execute o script principal (<code>main.py</code>).</li>
</ol>

## 📝 Observações
<p>No final dos arquivos <code>file_system.py</code>, há comentários com um exemplo de implementação. Basta retirar as aspas do comentário e executar esse arquivo para visualizar a implementação do exemplo.</p>

## 👥 Desenvolvedores
<ul>
  <li>👩‍💻 Evellyn Rodrigues da Rocha</li>
  <li>👩‍💻 Lara Fernanda Amorim Alves Cavalcante</li>
</ul>

## 🎓 Considerações Finais
<p>Este é um trabalho de gerenciamento de sistemas de arquivos solicitado pelo professor Tércio de Moraes, na disciplina de Sistemas Operacionais da Universidade Federal de Alagoas (UFAL).</p>
