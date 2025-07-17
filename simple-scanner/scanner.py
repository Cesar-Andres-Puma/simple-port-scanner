import socket, platform

def verificar_porta(ip,porta):
    try:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.settimeout(1)
         resultado = s.connect_ex((ip, porta))
         s.close()

         if resultado == 0:
             print(f"porta{porta} aberta em {ip}")
         else:
             print(f"porta {porta} fechada em {ip}")

    except Exception as e:
               print(f"Error: {e}")

def main():
    so = platform.system()
    print(f"sistema operacional detectado: {so}")
    
    ip = input("Digite o IP: ").strip()
    porta_str = input("Digite a porta (ou portas separadas por virgulas): ").strip()

    portas = []
    if "," in porta_str:
               portas = [int(p.strip()) for p in porta_str.split(",")]
    else:
               portas= [int(porta_str)]

    for porta in portas:
     verificar_porta(ip,porta)

if __name__ == "__main__":
     main() 

