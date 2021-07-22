myfile = open("D:\\development_codes\\python_learning\\file_operations\\newfile.txt", "r+")

myfile.truncate()  #truncate comandasi ile faylda ne varsa temiz silirsen

myfile.truncate(10)  #bununla ise 10cu xarakterden sonra ne varsa silinir
