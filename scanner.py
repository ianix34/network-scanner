import socket
import ssl

def get_target():
    return input("Enter target: ")
def create_https_connection(target):
    context = ssl.create_default_context()
    sock = socket.create_connection((target, 443))
    secure_sock = context.wrap_socket(sock, server_hostname=target)
    return secure_sock
def send_request(sock, target):
    request = f"GET / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n"
    sock.send(request.encode())
def receive_response(sock):
    response = b""
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response += data
    return response
def main():
    target = get_target()
    try:
        sock = create_https_connection(target)
        print("[+] HTTPS connection established")
        send_request(sock, target)
        response = receive_response(sock)
        print(response.decode(errors="ignore"))
        sock.close()
    except Exception as e:
        print(f"[-] Error: {e}")

if _name_ == "_main_":
    main()
