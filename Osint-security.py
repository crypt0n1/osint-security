import imaplib
import email
import re
import os
import webbrowser
from os import system
from time import sleep
from colorama import Fore
import sys
import requests
import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import timezone
import json


BLACK = '\033[30m'

RED = '\033[31m'

GREEN = '\033[32m'

YELLOW = '\033[33m'

BLUE = '\033[34m'

MAGENTA = '\033[35m'

CYAN = '\033[36m'

WHITE = '\033[37m'

RESET = '\033[38m'

os.system("clear")

def osint():
    print(RED + """ ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓  ██████ ▓█████  ▄████▄   █    ██  ██▀███   ██▓▄▄▄█████▓▓██   ██▓
▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█   ██  ▓██▒▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒
▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░░ ▓██▄   ▒███   ▒▓█    ▄ ▓██  ▒██░▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░  ▒██ ██░
▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░   ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▓▓█  ░██░▒██▀▀█▄  ░██░░ ▓██▓ ░   ░ ▐██▓░
░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ ▒██████▒▒░▒████▒▒ ▓███▀ ░▒▒█████▓ ░██▓ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▓    ▒ ░░      ██▒▒▒ 
  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒   ░░▒░ ░ ░   ░▒ ░ ▒░ ▒ ░    ░     ▓██ ░▒░ 
░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      ░  ░  ░     ░   ░         ░░░ ░ ░   ░░   ░  ▒ ░  ░       ▒ ▒ ░░  
    ░ ░        ░   ░           ░                ░     ░  ░░ ░         ░        ░      ░            ░ ░     
                                                          ░                                        ░ ░     
""")
    print(YELLOW + "\033[33m-------------------------------------------------")
    print(YELLOW + "Autor  :   Crpt0n1c")
    print(YELLOW + "-------------------------------------------------")
    print(YELLOW + "Youtube   :   Crypt0n1c py")
    print(YELLOW + "---------------------------------------------")
    print(YELLOW + "Telegram @crypt0n1c000")
    print(YELLOW + "-------------------------------------------------")

    print(YELLOW + "1) ip tracker")
    sleep(1)
    print(YELLOW + "2) num info")
    sleep(1)
    print(YELLOW + "3) phishing")
    sleep(1)
    print(YELLOW + "4) IP logger")
    sleep(1)
    print(YELLOW + "5) search name(SOLO FUNCIONA PARA GENTE DE MEXICO)")
    sleep(1)
    print(YELLOW + "6) mail checker")
    sleep(1)
    print(YELLOW + "7) EXIT ")
    sleep(1)
    os = input(YELLOW + "opcion > ")
    if os == "1":
        print(RED + """ ██▓ ██▓███     ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██▒▓██░  ██▒   ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒   ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒ ░  ░     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░▓  ▒▓▒░ ░  ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░▒ ░            ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ░░░            ░        ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
 ░                          ░           ░  ░░ ░      ░  ░      ░  ░   ░     
                                            ░                               
""")
        ip = input(YELLOW + "ip > ")

        url = f'http://ip-api.com/{ip}'

        
        jiji = requests.get(url)
        
        informacion = jiji.text
        
        print(informacion)
        
        retu = input("presione enter para volver")
        
        if retu == " ":
        
            system("clear")
        
        return osint()
    
    elif os == "2":
        print(RED + """ ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████      ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░   ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
          ░  ░  ░    ░ ░           ░    ░  ░         ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                                        ░                                                        
""")
        mobileNo = input("Enter phone number with Country code: ")

        mobileNo = phonenumbers.parse(mobileNo)

        #conseguir el timezone de  un phonenumber
        print(timezone.time_zones_for_number(mobileNo))

        #consiguiendo carrier de un phone number
        print(carrier.name_for_number(mobileNo, "en"))

        #Consiguiendo informacion de la region
        print(geocoder.description_for_number(mobileNo, "en"))

        #Validando numero de telefono
        print("Valid phone number :", phonenumbers.is_valid_number(mobileNo))
        
        #Checking possibility of a number
        print("Checking possibility of Number :", phonenumbers.is_possible_number(mobileNo))

        retu2 = input("Presione enter para volver al menu principal \n\n\n")

        if retu2 == " ":
            system("clear")
        return osint()
    elif os == "3":
        print("Esta opcion no esta disponible actualmente!")
        
        retu3 = input("Presione enter para volver al menu")

        if retu3 == " ":
            system("clear")
        return osint()
    elif os == "4":
        """Es un acortador tienes que poner un link para acortarlo con grabify y consuir la ip de la persona"""

        webbrowser.open_new_tab("https://grabify.link/")

        retu4 = input("Presione enter para salir")

        if retu4 == " ":
            system("clear")
        return osint()

    elif os == "5":
            webbrowser.open_new_tab("https://www.gob.mx/curp/")

            retu5 = input("Presione enter para salir")

            if retu5 == " ":

                system("clear")
            
            return osint()
        
    elif os == "6":
        
        print(RED + """

 ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ██▓ ███▄    █   █████▒▒█████  
▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
░      ░     ░   ▒    ▒ ░  ░ ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
       ░         ░  ░ ░      ░  ░    ░           ░            ░ ░  
                                                                   

""")
        user_input = str(input("Enter email: "))
        
        print("Your original mail is: {}".format(user_input))
        
        user_name = user_input[:user_input.index("@")]
        
        domain_name = user_input[user_input.index("@") + 1 :]
        
        print("Domain info: ")
        
        print("Your username is: {}  |   Your mail provider is: {} ".format(user_name, domain_name))
        
        print("para mas informacion del correo espere unos segundos")
        
        sleep(7)
        
        webbrowser.open_new_tab("https://whatismyipaddress.com/trace-email")
    
        retu6 = input("Presione enter para salir")


    if retu6 == " ":

        system("clear")

    return osint()

osint()