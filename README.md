# Calculadora Básica em Python

Este projeto implementa uma calculadora simples em Python que permite ao usuário escolher uma operação matemática básica (adição, subtração, multiplicação ou divisão) e realizar cálculos com dois números fornecidos.

## Funcionalidades

- O usuário pode selecionar uma das seguintes operações:
  - Adição (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`)

- Após selecionar a operação, o usuário insere dois números.
- O cálculo é feito e o resultado é exibido na tela.

## Como funciona

### 1. Escolha da Operação
Ao iniciar o programa, o usuário será apresentado a um menu com quatro opções:
- `1` para adição
- `2` para subtração
- `3` para multiplicação
- `4` para divisão

O usuário deve inserir o número correspondente à operação desejada.

### 2. Entrada dos Números
Depois de escolher a operação, o usuário deverá fornecer dois números:
- O **primeiro número**
- O **segundo número**

Ambos os números podem ser inteiros ou decimais (ponto flutuante).

### 3. Cálculo e Exibição do Resultado
Dependendo da operação escolhida, o programa realizará um dos seguintes cálculos:
- **Adição**: Soma os dois números.
- **Subtração**: Subtrai o segundo número do primeiro.
- **Multiplicação**: Multiplica os dois números.
- **Divisão**: Divide o primeiro número pelo segundo, exceto se o segundo número for zero. Caso contrário, o programa exibirá uma mensagem de erro de divisão por zero.

### 4. Tratamento de Erros
Se o usuário escolher uma operação inválida (não `1`, `2`, `3` ou `4`), o programa exibe uma mensagem de erro e pede para escolher uma operação válida.

Se o usuário tentar dividir por zero, o programa exibirá um aviso informando que a divisão por zero não é permitida.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o código fornecido no arquivo `calculadora.py`.
3. No terminal, navegue até o diretório onde o arquivo está salvo.
4. Execute o programa com o comando:
   ```bash
   python calculadora.py
