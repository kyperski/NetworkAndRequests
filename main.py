import socket
import requests
def main():
    print("выберите мод - 1: Открытые порты 2: Таймаут")
    x=input()
    if x=="1":
        # Определяем порты для проверки
        ports = [80, 81, 8000, 8080, 443, 554, 37777, 7000]
    
        ip=input()

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"✓ Порт {port} открыт")
            sock.close()
    elif x=="2":
        try:
            response = requests.get(input(), timeout=5)
        except requests.exceptions.Timeout:
            print("Слишком долго брад")

# Запускаем функцию
if __name__ == "__main__":
    main()