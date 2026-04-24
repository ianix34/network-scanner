import socket
import ssl 
target=input("ENTER TARGET:")
port=443
context=ssl.create_default_context()
with socket.create_connection((target, port)) as sock:
    with context.wrap_socket(sock, server_hostname=target) as ssock:
        print("[+] HTTPS connection established")
        request=f"GET /HTTP/1.1\r\nHost:{target}\r\n\r\n"
        ssock.send(request.encode())
        response=ssock.recv(1024)
        print(response.decode(errors="ignore"))
