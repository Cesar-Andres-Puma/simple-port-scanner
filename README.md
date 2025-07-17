# Simple Port Scanner

Um scanner de portas simples em Python que verifica se portas estão abertas ou fechadas em um IP informado.

---

## Funcionalidades

- Verifica múltiplas portas TCP de um host
- Opção para escanear portas padrão comuns
- Permite entrada personalizada de portas pelo usuário
- Detecta o sistema operacional onde o script está rodando
- Timeout de conexão configurado para 1 segundo

---

## Requisitos

- Python 3.x
- Conexão de rede para testar portas remotas

---

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/Cesar-Andres-Puma/simple-port-scanner.git
cd simple-port-scanner

2.Execute o script

- python scanner.py

3. Siga as instruções na tela:

- Informe o Ip alvo
- Escolha se quer usar as portas padrão ou digitar suas próprias portas (separadas por espaço)

4.Sistema operacional detectado: Linux
- Digite o IP: 192.168.0.1
- Deseja verificar portas padrão? (s/n): s
- Verificando portas: [20, 21, 22, 23, 80, 139, 445, 443, 3389, 5800, 5900]
- Porta 20 fechada em 192.168.0.1
- Porta 21 fechada em 192.168.0.1
- Porta 22 aberta em 192.168.0.1

#Aviso
- Este script é para fins educacionais e deve ser usado apenas em redes e dispositivos autorizado
