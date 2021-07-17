with open("python.txt", "w") as f: #using the with-as solution, the files gets closed automatically, without needing the close() method
    f.write("Hello Python!\n")