#Создание заголовка для отправки браузеру
def CreateHeader(code, filename = '.html' ):
	mimeTypes = {
        ".txt"   : b"text/plain",
        ".htm"   : b"text/html",
        ".html"  : b"text/html",
        ".css"   : b"text/css",
        ".csv"   : b"text/csv",
        ".js"    : b"application/javascript",
        ".xml"   : b"application/xml",
        ".xhtml" : b"application/xhtml+xml",
        ".json"  : b"application/json",
        ".zip"   : b"application/zip",
        ".pdf"   : b"application/pdf",
        ".jpg"   : b"image/jpeg",
        ".jpeg"  : b"image/jpeg",
        ".png"   : b"image/png",
        ".gif"   : b"image/gif",
        ".svg"   : b"image/svg+xml",
        ".ico"   : b"image/x-icon"
    }
	filename = filename.lower()
	for ext in mimeTypes :
		if filename.endswith(ext) :
			type = mimeTypes[ext]
	if code == 404:
		code = b"404 Not Found"
	if code == 200:
		code = b"200 OK"
	header = \
	b"HTTP/1.1 "+ code + b"\r\n" + \
    b"Server: Slim-Web-Server\r\n"+ \
    b"Content-Type: "+ type + b"; charset=UTF-8\r\n"+ \
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
def requestGet (patch ='', link = ''):
	varHtmlDict = {}
	# Удаляем лишнее из строки
	link = link.strip("b'/")
	
	# Проверяем есть ли в строке переменные
	if link.find("?") != -1:		
		file = 	link[:link.find("?")]
		file = 	findFile(patch, file)
		varHtml = 	link[link.find("?"):].split("&")		
		#	Создаем словарь для переменных посланных GET запросом
		for i in range(0,len(varHtml)):			
			varHtml[i] = varHtml[i].strip("?&")		
			if 	varHtml[i].find("=") == -1:
				continue
			varHtmlDict[varHtml[i].split("=")[0]] = varHtml[i].split("=")[1]
	else :
		file = findFile(patch, link)
	print ("requestGet(",patch, file,")")
	try:
		f = open( patch+file,'rb')
		bodyHtml = f.read()		
		f.close()
		return CreateHeader(200, file), bodyHtml, varHtmlDict
	except :
		print("link not found", patch+link)		
		return CreateHeader(404), b"404 not Found", varHtmlDict
	