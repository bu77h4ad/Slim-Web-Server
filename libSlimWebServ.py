#Создание заголовка для отправки браузеру
def CreateHeader(code):
	if code == 404:
		code = b"404 Not Found"
	if code == 200:
		code = b"200 OK"
	header = \
	b"HTTP/1.1 "+ code + b"\r\n" + \
    b"Server: MicroPython-WebServer\r\n"+ \
    b"Content-Type: text/html; charset=UTF-8\r\n"+ \
    b"\r\n"  
	return header

# Функция для обработки запрашиваемой страницы
def findFile(patch = "www\\", file=""):
	indexPages = [        
        "index.html",
        "index.htm",        
        "default.html",
        "default.htm"
    ]
    # Удаляем лишнее из строки
	file = file.strip("b'/")
	# Проверяем есть ли в строке переменные
	if file.find("?") != -1:		
		file = file[:file.find("?")]		

	# Ищет страницу по умолчанию
	if file == "":
		for page in indexPages:	
			try :	
				print (page)			
				f = open ( patch+page, 'rb')
				f.close()
				return page
			except:
				pass
					
	return file

# Обработчик GET запросов
def requestGet (patch ='', file = ''):
	file = findFile(patch, file)
	print ("requestGet(",patch, file,")")
	try:
		f = open( patch+file,'rb')
		a = f.read()
		#print (a)
		f.close()
		return CreateHeader(200), a
	except :
		print("file not found", patch+file)		
		return CreateHeader(404), b"404 not Found"
	