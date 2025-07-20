import socket
import platform
import threading
from queue import Queue

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

def main():
   os_name = platform.system()
   print(f"sistema operacional detectado: {os_name}")
   ip = input("Digite o endereco de IP ou hostname: ").strip()
   use_default =input("Deseja usar as portas padrão? (s/n): ").strip().lower() == 's'
   ports = get_default_ports() if use_default else get_ports_from_user()

   for port in ports:
       q.put(port)

   for _ in range(50):
       thread = threading.Thread(target=worker, args=(ip,), daemon=True)
       thread.start()
   
   q.join()

   print("\n" + "="*30)
   print("  Verificação Concluída")
   print("="*30)
   if open_ports:
       open_ports.sort()
       print(f"Portas abertas encontradas: {open_ports}")
   else:
        print("Nenhuma porta aberta foi encontrada.")

if __name__ == "__main__":
    main()
