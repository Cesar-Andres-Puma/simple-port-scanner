import socket
import platform

def check_ports(ip, ports):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            status = "aberta" if result == 0 else "fechada"
            print(f"Porta {port} {status} em {ip}")

def get_default_ports():
    return [20, 21, 22, 23, 80, 139, 445, 443, 3389, 5800, 5900]

def get_ports_from_user():
    ports_input = input("Digite as portas (separadas por espaço): ")
    try:
        return [int(port) for port in ports_input.split()]
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números separados por espaço.")
        return get_ports_from_user()

def main():
    os_name = platform.system()
    print(f"Sistema operacional detectado: {os_name}")
    ip = input("Digite o IP: ").strip()
    use_default = input("Deseja verificar portas padrão? (s/n): ").strip().lower() == 's'
    ports = get_default_ports() if use_default else get_ports_from_user()
    print(f"Verificando portas: {ports}")
    try:
        check_ports(ip, ports)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
