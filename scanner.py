import socket
import threading
from queue import Queue

# Global variables
q = Queue()
open_ports = []
print_lock = threading.Lock()

def worker(ip):
    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                with print_lock:
                    print(f"Porta {port:<5} aberta")
                    open_ports.append(port)
        q.task_done()

def get_default_ports():
    return [20, 21, 22, 23, 80, 139, 445, 443, 3389, 5800, 5900]

def get_ports_from_user():
    ports_input = input("Digite as portas (separadas por espaço): ")
    try:
        return [int(port) for port in ports_input.split()]
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números separados por espaço.")
        return get_ports_from_user()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def scan_ports(ip, ports, num_threads=100):
    for port in ports:
        q.put(port)
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(ip,), daemon=True)
        thread.start()
    q.join()

def main():
    print("--- python-port-scanner ---")
    try:
        scan_local_input = input("Deseja scanear o Ip local? (Pressione Enter para Sim, 'n' para Nao): ").strip().lower()
        if scan_local_input == 'n':
            ip = input("Digite o IP a ser escaneado: ").strip()
        else:
            ip = get_local_ip()
            print(f"IP local detectado: {ip}")

        use_default_ports = input("Deseja usar portas padrão? (Pressione Enter para Sim, 'n' para Nao): ").strip().lower()
        if use_default_ports == 'n':
            ports = get_ports_from_user()
        else:
            ports = get_default_ports()
            print(f"Usando portas padrão: {ports}")

        print(f"\nIniciando verificação de {len(ports)} portas em {ip}...")
        scan_ports(ip, ports)

        print("\n" + "="*30)
        print("  Verificação Concluída")
        print("="*30)
        if open_ports:
            open_ports.sort()
            print(f"Portas abertas encontradas: {open_ports}")
        else:
            print("Nenhuma porta aberta foi encontrada.")
    except socket.gaierror:
        print(f"\n[!] Erro de Hostname: Não foi possível encontrar o IP para '{ip}'. Verifique o nome.")
    except KeyboardInterrupt:
        print("\n[!] Processo interrompido pelo usuário.")
    except Exception as e:
        print(f"\n[!] Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
