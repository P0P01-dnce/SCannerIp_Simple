from scapy.all import *

def scanner(ip , port):
    pket = IP(dst=ip) / TCP(dport = port , flags="S")
    resp = sr1(pket, timeout=1,verbose=0)
    if resp and resp.haslayer(TCP) and resp.getlayer(TCP).flags == 0x12:
        return True
    return False
def ingreso():
        ip_capture = input("[Enter ip]>")
        for p in range(20,1025):
            if scanner(ip_capture,p):
                print("----------------------------------------------------\n")
                print(f"|[+]Puerto {p} abierto para la direccion {ip_capture} |")
                print("------------------------------------------------------")
                break
if __name__ == "__main__":
    try:
        while True:
            print("[1]------------Escaneo de Puertos\n")
            print("[2]-------------Salir\n")
            opcion = int(input("Ingresa la opcion:"))
            if opcion == 1:
                ingreso()
            elif opcion == 2:
                print("Saliendo....")
                break
    except ValueError:
        print("Ingresa un dato correcto......")
