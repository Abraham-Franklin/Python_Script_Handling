import os

name = input("Enter name you wish to name the file: ").strip()
file_name = f"./{name}"
if os.path.exists(file_name):
    print("File name already exists!!!")
else:
    fs = open(file_name, 'x')
    print("file_name created successfully")
    
    f = open(file_name, 'a')
    note = input("""Enter text: \n \t""")
    f.write(note)
    f.close()
    
    fx = open(file_name, "r")
    print(fx.read())
    fx.close()
