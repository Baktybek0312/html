
import socket

def start_my_server():

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 2008))
        server.listen()
        while True:
            print("Working...")
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            content = load_page_from_get_requests(data)

            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Работа завершена")


def load_page_from_get_requests(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; ' \
           'charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html;' \
               'charset=utf-8\r\n\r\n'

    path = request_data.split('')[1]
    print(path)
    response = ''
    try:
        with open("views" + path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response

    except FileNotFoundError:
        return (HDRS_404 + "Прошу прощения, страницы нет").encode('utf-8')


start_my_server()


