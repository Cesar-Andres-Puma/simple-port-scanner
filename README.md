# Scanner de Portas Rápido com Threads em Python

Um scanner de portas TCP concorrente e eficiente, construído em Python, ideal para verificações rápidas de rede. Este projeto evoluiu de um scanner sequencial simples para uma ferramenta multithread robusta e com uma interface de usuário aprimorada.

## 🚀 Principais Funcionalidades

-   **Verificação Rápida e Concorrente:** Utiliza múltiplas threads para escanear dezenas de portas simultaneamente, tornando a verificação muito mais rápida que os métodos sequenciais.
-   **Captura de Banners (Banner Grabbing):** Tenta identificar o serviço e a versão que está rodando na porta aberta, fornecendo mais contexto sobre o alvo.
-   **Scan de IP Local Automático:** Detecta automaticamente o IP da sua máquina para facilitar verificações na sua própria rede.
-   **Interface de Usuário Ágil:** Permite o uso da tecla `Enter` para selecionar as opções padrão, agilizando o processo.
-   **Relatório Final Limpo:** Exibe uma lista clara e ordenada apenas com as portas que foram encontradas abertas ao final da verificação.
-   **Listas de Portas Flexíveis:** Oferece uma lista padrão com as portas mais comuns ou permite que o usuário insira uma lista personalizada.
-   **Tratamento de Erros Inteligente:** Fornece mensagens de erro claras para situações como hostnames inválidos ou interrupção pelo usuário (`Ctrl+C`).

---

## ⚙️ Requisitos

-   Python 3.x
-   Conexão de rede ativa.

---

## 📦 Instalação e Uso

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Cesar-Andres-Puma/simple-port-scanner.git](https://github.com/Cesar-Andres-Puma/simple-port-scanner.git)
    cd simple-port-scanner
    ```

2.  **Execute o script:**
    ```bash
    python3 scanner.py
    ```

3.  **Siga as instruções na tela.** O script é interativo e irá guiá-lo.

    **Exemplo de interação:**
    ```
    $ python3 scanner.py
    --- Python Port Scanner ---
    Deseja escanear o IP local? (Pressione Enter para Sim, 'n' para Não): n
    Digite o IP ou hostname para escanear: scanme.nmap.org
    Deseja verificar as portas padrão? (Pressione Enter para Sim, 'n' para Não): 

    Iniciando verificação de 23 portas em scanme.nmap.org...
    ```

---

## 📊 Exemplo de Saída

A saída mostra as portas abertas em tempo real e, ao final, apresenta um resumo limpo com os banners capturados.

## ⚠️ Aviso Ético

Este script foi desenvolvido para fins educacionais e de estudo. Utilize-o apenas em redes e sistemas para os quais você tenha **permissão explícita**. Realizar varreduras de portas em sistemas de terceiros sem autorização é uma atividade antiética e pode ser ilegal.
