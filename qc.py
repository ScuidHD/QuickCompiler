#   ==========================
#   I Copyright ScuidHD 2021 I 
#   ==========================

import os

file = input("> ")
fend = file.split(".")

if fend[-1] == "cpp" or fend[-1] == "cc" or fend[-1] == "cxx": #add your own extensions for c++ here

    os.system("g++ -o " + fend[0] + ".exe" + " " + file) #gcc needs to be installed, currently no support for linker options or include options

elif fend[-1] == "c": #add your own extensions for c here

    os.system("gcc -o " + fend[0] + ".exe" + " " + file) #gcc needs to be installed, currently no support for linker options or include options

elif fend[-1] == "py": #add your own extensions for python here
    pyver = input("Python Ver: ")
    if pyver == "2":
        os.system("python " + file) #my own python path command, you may need to change it
    elif pyver == "3":
        os.system("py3 " + file) # my own python 3 path command, you may need to change it
    else:
        print("Error F_31: Not a valid Python version!")

#add your own filetypes here
        
else:
    print("Error F_01: Filetype not supported!")
    
#                                             Error format: Error F_00: info
#                                                                 ^ ^^  ^
#   where the error happened (F = filetype processing etc. -------| ||  |
#   Language (0 = N.A, 1 = C++, 2 = c, 3 = python ------------------||  |
#   Error type (locally for language, each error has its own number) |  |
#   Some additional info on the error ----------------------------------|
