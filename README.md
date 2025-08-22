<div align="center">
  <h1>Redução de Dimensionalidade com PCA para Processamento de Imagens</h1>
</div>

Este projeto demonstra a aplicação da Análise de Componentes Principais (PCA) para redução de dimensionalidade, especificamente no contexto de compressão e reconstrução de imagens. Ele inclui funcionalidades básicas de processamento de imagens e uma implementação de PCA para visualizar o efeito da redução de componentes na qualidade da imagem.

## 🚀 Funcionalidades

-   **Leitura e Salvamento de Imagens:** Suporte para formatos comuns de imagem (ex: `.jpg`, `.png`).
-   **Conversões de Cor:** Transformação de imagens para escala de cinza e preto e branco.
-   **Redimensionamento de Imagens:** Ajuste das dimensões de uma imagem.
-   **Análise de Componentes Principais (PCA):**
    -   Implementação do algoritmo PCA para matrizes.
    -   Aplicação do PCA para compressão de imagens em escala de cinza.
    -   Reconstrução de imagens a partir de um número reduzido de componentes principais.
-   **Visualização:** Exibição de imagens originais e processadas para comparação.

## 📂 Estrutura do Projeto

```
dimensionality-reduction/
├── data/
│   ├── raw/                  # Imagens de entrada originais (ex: museu.jpg)
│   └── processed/            # Imagens salvas após o processamento
├── src/
│   ├── image.py              # Funções para manipulação e processamento de imagens
│   ├── matrix.py             # Funções para operações de matrizes, incluindo a implementação do PCA
│   └── imports.py            # (Duplicado, ver nota abaixo)
├── utils/
│   └── imports.py            # Configuração do logger e importações gerais
├── main.py                   # Script principal para executar as demonstrações
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

**Nota sobre `imports.py`:** Observa-se que há dois arquivos `imports.py` (`src/imports.py` e `utils/imports.py`) com conteúdo idêntico. Para manter a clareza e evitar redundância, é recomendado consolidar a configuração do logger e as importações gerais em um único local, preferencialmente em `utils/imports.py`, e remover `src/imports.py`. Os módulos em `src/` devem importar de `utils/imports.py`.

## 🛠️ Configuração do Ambiente

Siga os passos abaixo para configurar e executar o projeto em sua máquina:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/dimensionality-reduction.git
    cd dimensionality-reduction
    ```
    *(Substitua `https://github.com/seu-usuario/dimensionality-reduction.git` pelo URL real do seu repositório.)*

2.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Como Executar

Após configurar o ambiente, execute o script principal `main.py`:

```bash
python main.py
```

O script irá:

1.  Carregar a imagem `data/raw/museu.jpg`.
2.  Demonstrar diversas operações de processamento de imagem:
    -   Conversão para escala de cinza e preto e branco.
    -   Redimensionamento para diferentes tamanhos.
3.  Aplicar a Análise de Componentes Principais (PCA) na imagem em escala de cinza para compressão, exibindo a imagem original em escala de cinza e suas reconstruções com diferentes números de componentes principais (100, 50 e 20, se aplicável ao tamanho da imagem).

Todas as imagens resultantes serão exibidas em janelas separadas para fácil comparação.

## 💡 Conceitos Chave (PCA)

A **Análise de Componentes Principais (PCA)** é uma técnica estatística utilizada para reduzir a dimensionalidade de um conjunto de dados, mantendo a maior parte da variância (informação) presente nos dados. No contexto de imagens, uma imagem pode ser vista como uma matriz de dados. Ao aplicar o PCA, transformamos essa matriz em um novo espaço onde os eixos (componentes principais) capturam a maior parte da variância dos dados.

Para compressão de imagens, o PCA permite reconstruir a imagem utilizando apenas um subconjunto dos componentes principais. Isso resulta em uma imagem com menos dados, mas que ainda retém as características visuais mais importantes. A qualidade da imagem reconstruída é diretamente proporcional ao número de componentes principais utilizados.

O pipeline do PCA geralmente envolve:
1.  **Centralização dos dados:** Subtrair a média de cada característica.
2.  **Cálculo da matriz de covariância:** Mede a relação entre as diferentes características.
3.  **Cálculo de autovalores e autovetores:** Os autovetores representam as direções dos componentes principais, e os autovalores indicam a magnitude da variância ao longo dessas direções.
4.  **Ordenação:** Autovetores são ordenados pelos seus autovalores correspondentes em ordem decrescente.
5.  **Seleção de componentes:** Escolher os `k` autovetores com os maiores autovalores.
6.  **Projeção:** Projetar os dados originais no novo espaço de menor dimensão.
7.  **Reconstrução (para compressão):** Inverter a projeção para obter uma versão de menor dimensão dos dados originais.
