# # PackageLoader - для загрузки шаблонов из пакета
# # DictLoader - для загрузки шаблонов из словоря
# # FunctionLoader - для загрузки на основе функции
# # PrefixLoader - загрузчик, использующий словарь для построения подкаталогов
# # ChoiceLoader - загрузчик содержащий список других загрузчиков (если один не сработаетб выбирается следующий)
# # ModuleLoader - загрузчик для скомпилированных шаблонов
#
# from jinja2 import Environment, FileSystemLoader
#
# subs = ["Информатика", "Физика", "Англиский", "Математика"]
#
# file_loder = FileSystemLoader('templates')
# env = Environment(loader=file_loder)
#
# tm = env.get_template('about.html')
# msg = tm.render(list_table=subs)
#
# print(msg)


import socket

def start_my_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 2022))
        server.listen(4)

        while True:
            print('working...')
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            content = load_page_from_get_request(data)

            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Работа завершена')

def load_page_from_get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    print(path)
    response = ''
    try:
        with open("views"+path, "rb") as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + "Прошу прощения, страницы нет").encode('utf-8')



if name == "main":
    start_my_server()
