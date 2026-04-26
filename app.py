# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """ 
        Специальный класс, который отвечает за 
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        with open('contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        self.wfile.write(bytes(html_content, 'utf-8'))

if __name__ == "__main__":        

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:

        webServer.serve_forever()
    except KeyboardInterrupt:

        pass


    webServer.server_close()
    print("Server stopped.")