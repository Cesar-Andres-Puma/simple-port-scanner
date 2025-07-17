Esse é apenas um pequeno projeto que tive como base do curso Desec, apenas para fins educacionais.

# Simple Port Scanner

Um scanner de portas simples em Python, para verificar se portas estão abertas ou fechadas em um IP informado. Ideal para fins educacionais e testes básicos em redes locais.

---

## Funcionalidades

- Suporte a múltiplas portas (digitadas separadas por vírgula)
- Detecta se a porta está aberta ou fechada usando conexão TCP
- Tempo de timeout configurado para 1 segundo
- Exibe o sistema operacional detectado no início

---

## Requisitos

- Python 3.x
- Sistema operacional Linux, Windows ou macOS

---

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Cesar-Andres-Puma/simple-port-scanner.git
   cd simple-port-scanner

2. Execute o script:

python scanner.py

3. Exemplo de uso:

Digite o IP: 192.168.0.1
Digite a porta (ou portas separadas por vírgulas): 22,80,443
Porta 22 aberta em 192.168.0.1
Porta 80 fechada em 192.168.0.1
Porta 443 aberta em 192.168.0.1
