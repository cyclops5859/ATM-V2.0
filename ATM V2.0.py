# Made by Cyclops (Rehan khan).
# visit https://github.com/cyclops5859 for more.
# Install pyttsx3 before running the code.

import time
import pyttsx3
import os

# Speaking function.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

print ("----------------------------------------------------------------------------")
print (" ")
time.sleep(1)
print("Welcome To Cyclops Bank!")
pyttsx3.speak("Welcome To Cyclops Bank!")
print(r"""
    ----------------------------------------------------------------
     _______           _______  _        _______  _______  _______   
    (  ____ \|\     /|(  ____ \( \      (  ___  )(  ____ )(  ____ \  
    | (    \/( \   / )| (    \/| (      | (   ) || (    )|| (    \/  
    | |       \ (_) / | |      | |      | |   | || (____)|| (_____   
    | |        \   /  | |      | |      | |   | ||  _____)(_____  )  
    | |         ) (   | |      | |      | |   | || (            ) |  
    | (____/\   | |   | (____/\| (____/\| (___) || )      /\____) |  
    (_______/   \_/   (_______/(_______/(_______)|/       \_______)

    ----------------------------------------------------------------
                                                                """)
                                                                
#---------------------------------------------------------------------------------------------------------------------------------------

def IsDriveExists(drive):
    return os.path.exists(drive + ':\\')

d = IsDriveExists('d')
e = IsDriveExists('e')
f = IsDriveExists('f')

Trials = 3
UserPin = 5836
sos = 911
sos2 = 6385 
amount = 13420.69

time.sleep (1)
print("1. Please pick your language : English \n2. kripya apani bhasha chunen : Hindi \n3. krpaya apali bhasa nivada : Marathi \n4. Tafadhali chagua lugha yako : Kswahili")
pyttsx3.speak(" Please pick your language : English, Hindi, Marathi or Kswahili")
lang = int(input(">>> : "))

#---------------------------------------------------------------------------------------------------------------------------------------

if lang == 1:
    print ("You have chosen : English")
    pyttsx3.speak ("You have chosen : English")

    while Trials != 0:
        print ("Detecting key card! please wait...")
        pyttsx3.speak("Detecting key card! please wait...")
        time.sleep(1)

        if d or e or f == True:
            print ("Keycard detected!") 
            pyttsx3.speak("Keycard detected!")            
            print ("Please Enter Your 4 digit Pin : ")
            pyttsx3.speak ("Please Enter Your 4 digit Pin")
            Pin = int(input(">>> : "))

            if Pin == sos or Pin == sos2:
                print (">>> The local athority has been notified, plz continue with the transaction. <<<")
                print('LOGIN SUCCESFULL')
                pyttsx3.speak('LOGIN SUCCESFULL')
                pass
            
            elif Pin != UserPin:
                Trials -= 1
                print ("Incorrect account number or pin! you have ", Trials, "Trials Left")
                pyttsx3.speak("Incorrect account number or pin!")

            else:
                print('LOGIN SUCCESFUL')
                pyttsx3.speak('LOGIN SUCCESFUL')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
                print('Please select your Account: \n 1. Current Account \n 2. Saving Account \n:-')
                pyttsx3.speak('Please select your Account: Current Account or Saving Account')
                x = eval(input(">>> : "))

                if x == 1:
                    print('SELECT FROM FOLLOWING OPTIONS: \n 1. Balance Inquiry \n 2. Withdraw \n 3. Change PIN  \n 4. Quit \n:-')
                    pyttsx3.speak('SELECT FROM FOLLOWING OPTIONS: Balance Inquiry, Withdraw, Change PIN or Quit ')
                    response = int(input('>>> : '))
                    
                    valid_responses = ['1', '2', '3', '4']
                    response = response

                    if response == 1:
                        print('YOU HAVE ', amount,'USD IN YOUR ACCOUNT.')
                        pyttsx3.speak('YOU HAVE following amount IN YOUR ACCOUNT.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                    
                    elif response == 2:
                        print('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW.')
                        pyttsx3.speak('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW.')
                        cash_out = int(input(''))
                        
                        if cash_out > amount:
                            print ("YOU HAVE INSUFFICIENT BALANCE")
                            pyttsx3.speak('YOU HAVE INSUFFICIENT BALANCE')

                        else:
                            amount = amount - cash_out
                            print('YOUR NEW BALANCE IS: ', amount, 'USD')
                            pyttsx3.speak('YOUR NEW BALANCE IS')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    elif response == 3:
                        print('ENTER A NEW PIN')
                        pyttsx3.speak('ENTER A NEW PIN')
                        new_pin = int(input('>>> : '))

                        print('CONFIRM NEW PIN')
                        pyttsx3.speak('CONFIRM NEW PIN')
                        new_ppin = int(input('>>> : '))

                        if new_ppin != new_pin:
                            print('PIN MISMATCH')
                            pyttsx3.speak('PIN MISMATCH')

                        else:
                            UserPinn = new_pin
                            print('NEW PIN SAVED')
                            pyttsx3.speak('NEW PIN SAVED')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    elif response == 4:
                        exit()

                    else:
                        print('RESPONSE NOT VALID')
                        pyttsx3.speak('RESPONSE NOT VALID')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif x == 2:
                    amount = 42013.69

                    print('SELECT FROM FOLLOWING OPTIONS: \n 1. Balance Inquiry \n 2. Withdraw \n 3. Change PIN  \n 4. Quit \n:-')
                    pyttsx3.speak('SELECT FROM FOLLOWING OPTIONS: Balance Inquiry, Withdraw, Change PIN or Quit ')
                    response = int(input('>>> : '))

                    valid_responses = ['1', '2', '3', '4']
                    response = response

                    if response == 1:
                        print('YOU HAVE ', amount,'USD IN YOUR ACCOUNT.')
                        pyttsx3.speak('YOU HAVE following amount IN YOUR ACCOUNT.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                    
                    elif response == 2:
                        print('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW.')
                        pyttsx3.speak('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW.')
                        cash_out = int(input('>>> : '))

                        if cash_out > amount:
                            print ("YOU HAVE INSUFFICIENT BALANCE")
                            pyttsx3.speak('YOU HAVE INSUFFICIENT BALANCE')

                        else:
                            amount = amount - cash_out
                            print('YOUR NEW BALANCE IS: ', amount, 'USD')
                            pyttsx3.speak('YOUR NEW BALANCE IS')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    elif response == 3:
                        print('ENTER A NEW PIN')
                        pyttsx3.speak('ENTER A NEW PIN')
                        new_pin = int(input('>>> : '))

                        print('CONFIRM NEW PIN')
                        pyttsx3.speak('CONFIRM NEW PIN')
                        new_ppin = int(input('>>> : '))

                        if new_ppin != new_pin:
                            print('PIN MISMATCH')
                            pyttsx3.speak('PIN MISMATCH')

                        else:
                            UserPinn = new_pin
                            print('NEW PIN SAVED')
                            pyttsx3.speak('NEW PIN SAVED')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    elif response == 4:
                        exit()

                else:
                    print('RESPONSE NOT VALID')
                    pyttsx3.speak('RESPONSE NOT VALID')

        else:
            print ("Failed to detect keycard")
            pyttsx3.speak("Failed to detect keycard")
            exit()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif lang == 2:
        amount2 = 1011852.69
        pyttsx3.speak ("Aapne chuna hai : Hindi")

        while Trials != 0:
            print ("kunji card ka pata lagaane! kripya pratiksha karo...")
            pyttsx3.speak("kunji card ka pata lagaane! kripya pratiksha karo...")
            time.sleep(1)

            if d == True:
                print ("cicard ka pata chala!") 
                pyttsx3.speak("cicard ka pata chala!")

                print ("Kripya apna 4 ankon ka pin dalen")
                pyttsx3.speak ("Kripya apna 4 ankon ka pin dalen")
                Pin = int(input(">>> : "))

                if Pin == sos or Pin == sos2:
                    print (">>> sthaniya authority ko adhisuchit kiya gaya hai, kripya lenden jari rakhen <<<")
                    print('LOGIN SAFAL HUA')
                    pyttsx3.speak('LOGIN SAFAL HUA')
                    pass

                elif Pin != UserPin:
                    Trials -= 1
                    print ("Galat khata sankhya ya pin! aapke paas ", Trials, "moke hai")
                    pyttsx3.speak("Galat khata sankhya ya pin!")

                else:
                    print('LOGIN SAFAL HUA!')
                    pyttsx3.speak('LOGIN SAFAL HUA!')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                print('Kripya apna khata chunen: \n 1. Chalu khata \n 2. Bachat khata \n:-')
                pyttsx3.speak('Kripya apna khata chunen: Chalu khata ya Bachat khata')
                x = eval(input(">>> : "))

                if x == 1:
                    print('Nimnalikhit vikalpon mein se chayan karen: \n 1. Balance janch \n 2. Paise nikale \n 3. Pin badalen  \n 4. Bahar nikalen \n:- ')
                    pyttsx3.speak('Nimnalikhit vikalpon mein se chayan karen : Balance janch, Paise nikale, Pin badalen, Bahar nikalen')
                    response = int(input('>>> : '))

                    valid_responses = ['1', '2', '3', '4']
                    response = response

                    if response == 1:
                        print('Aapke paas ', amount2,'Rupees hai..')
                        pyttsx3.speak('Aapke paas itne rashi hai.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                    
                    elif response == 2:
                        print('Jitne rashi aap nikalna chahte hai, yaha darj kare:-.')
                        pyttsx3.speak('Jitne rashi aap nikalna chahte hai, yaha darj kare.')
                        cash_out = int(input('>>> : '))

                        if cash_out > amount2:
                            print ("aapke paas kam rashi hai")
                            pyttsx3.speak('aapke paas kam rashi hai')

                        else:
                            amount2 = amount2 - cash_out
                            print('Aapka naya rashi hai: ', amount2, 'Rupees')
                            pyttsx3.speak('Aapka naya rashi hai')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    elif response == 3:
                        print('Ek naya pin darj karen:-')
                        pyttsx3.speak('Ek naya pin darj karen')
                        new_pin = int(input(' '))

                        print('Naya pin wapas darj karen:-')
                        pyttsx3.speak('Naya pin wapas darj karen')
                        new_ppin = int(input('>>> : '))

                        if new_ppin != new_pin:
                            print('Galat pin')
                            pyttsx3.speak('Galat pin')

                        else:
                            UserPinn = new_pin
                            print('Aapka naya pin save ho gaya hai')
                            pyttsx3.speak('Aapka naya pin save ho gaya hai')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    elif response == 4:
                        exit()

                    else:
                        print('Gatat javab!')
                        pyttsx3.speak('Gatat javab!')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif x == 2:
                    amount3 = 201852.69

                    print('Nimnalikhit vikalpon mein se chayan karen: \n 1. Balance janch \n 2. Paise nikale \n 3. Pin badalen  \n 4. Bahar nikalen \n:- ')
                    pyttsx3.speak('Nimnalikhit vikalpon mein se chayan karen : Balance janch, Paise nikale, Pin badalen, Bahar nikalen')
                    response = int(input('>>> : '))

                    valid_responses = ['1', '2', '3', '4']
                    response = response

                    if response == 1:
                        print('Aapke paas ', amount3,'Rupees hai..')
                        pyttsx3.speak('Aapke paas itne rashi hai.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                    
                    elif response == 2:
                        print('Jitne rashi aap nikalna chahte hai, yaha darj kare:-.')
                        pyttsx3.speak('Jitne rashi aap nikalna chahte hai, yaha darj kare.')
                        cash_out = int(input('>>> : '))

                        if cash_out > amount3:
                            print ("aapke paas kam rashi hai")
                            pyttsx3.speak('aapke paas kam rashi hai')

                        else:
                            amount = amount - cash_out
                            print('Aapka naya rashi hai: ', amount3, 'Rupees')
                            pyttsx3.speak('Aapka naya rashi hai')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    elif response == 3:
                        print('Ek naya pin darj karen:-')
                        pyttsx3.speak('Ek naya pin darj karen')
                        new_pin = int(input('>>> : '))

                        print('Naya pin wapas darj karen:-')
                        pyttsx3.speak('Naya pin wapas darj karen')
                        new_ppin = int(input('>>> : '))

                        if new_ppin != new_pin:
                            print('Galat pin')
                            pyttsx3.speak('Galat pin')

                        else:
                            UserPinn = new_pin
                            print('Aapka naya pin save ho gaya hai')
                            pyttsx3.speak('Aapka naya pin save ho gaya hai')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    elif response == 4:
                        exit()

                else:
                    print('Gatat javab!')
                    pyttsx3.speak('Gatat javab!')

            else:
                print ("cicard ka pata lagaane mein wiffle")
                pyttsx3.speak("cicard ka pata lagaane mein wiffle")
                exit ()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif lang == 3:
    amount2 = 1011852.69
    print ("Too nivadali ahes : Marathi")
    pyttsx3.speak ("Too nivadali ahes : Marathi")

    while Trials != 0:
        print ("key card shodhane! krpaya thamba...")
        pyttsx3.speak("key card shodhane! krpaya thamba...")
        time.sleep(1)

        if d == True:
            print ("keycard sapadale!") 
            pyttsx3.speak("keycard sapadale!")
            
            print ("krpaya apali 4 anki pin pravist kara:-")
            pyttsx3.speak ("krpaya apali 4 anki pin pravist kara")
            Pin = int(input(" "))

            if Pin == sos or Pin == sos2:
                print (">>> sthanik athori suchit kelley gayley aahe, krpaya vyavahar chalu theva. <<<")
                print('LOGIN SUCCESFULL')
                pyttsx3.speak('LOGIN SUCCESFULL')
                pass

            elif Pin != UserPin:
                Trials -= 1
                print ("chukicha account number kinva pin! tujhyaakade aahe ", Trials, "chachanya shillak ahet")
                pyttsx3.speak("chukicha account number kinva pin!")

            else:
                print('LOGIN SUCCESFUL')
                pyttsx3.speak('LOGIN SUCCESFUL')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            print('krpaya apale khate nivada: \n 1. chalu khate \n 2. Bachat khate \n:-')
            pyttsx3.speak('krpaya apale khate nivada: chalu khate ya Bachat khate')
            x = eval(input(">>> : "))

            if x == 1:
                print('khalil paryayanivada: \n 1. Balance Inquiry \n 2. Withdraw \n 3. pin badla  \n 4. sodun jane \n:- ')
                pyttsx3.speak('khalil paryayanivada: Balance Inquiry, Withdraw, pin badla, sodun jane ')
                response = int(input('>>> : '))

                valid_responses = ['1', '2', '3', '4']
                response = response

                if response == 1:
                    print('apalya khatyat khalil rakkam aahe', amount2,'Rupees.')
                    pyttsx3.speak('apalya khatyat khalil rakkam aahe.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                
                elif response == 2:
                    print('tumhala maghar ghyayachi asel ti rakkam pravist kara:-.')
                    pyttsx3.speak('tumhala maghar ghyayachi asel ti rakkam pravist kara.')
                    cash_out = int(input('>>> : '))

                    if cash_out > amount2:
                        print ("tumachyakade apura samtol aahe")
                        pyttsx3.speak('tumachyakade apura samtol aahe')

                    else:
                        amount = amount2 - cash_out
                        print('tumacha navin samtol aahe: ', amount2, 'Rupees')
                        pyttsx3.speak('tumacha navin samtol aahe')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif response == 3:
                    print('navin pin pravist kara:-')
                    pyttsx3.speak('navin pin pravist kara')
                    new_pin = int(input('>>> : '))

                    print('navin pinachi pusti kara:-')
                    pyttsx3.speak('navin pinachi pusti kara')
                    new_ppin = int(input('>>> : '))

                    if new_ppin != new_pin:
                        print('pin bemel')
                        pyttsx3.speak('pin bemel')

                    else:
                        UserPinn = new_pin
                        print('navin pin save kelley')
                        pyttsx3.speak('navin pin save kelley')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif response == 4:
                    exit()

                else:
                    print('pratisad vaidh nahi')
                    pyttsx3.speak('pratisad vaidh nahi')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            elif x == 2:
                amount3 = 201852.69

                print('khalil paryayanivada: \n 1. Balance Inquiry \n 2. Withdraw \n 3. pin badla  \n 4. sodun jane \n:- ')
                pyttsx3.speak('khalil paryayanivada: Balance Inquiry, Withdraw, pin badla, sodun jane ')
                response = int(input('>>> : '))

                valid_responses = ['1', '2', '3', '4']
                response = response

                if response == 1:
                    print('apalya khatyat khalil rakkam aahe', amount3,'Rupees.')
                    pyttsx3.speak('apalya khatyat khalil rakkam aahe.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                
                elif response == 2:
                    print('tumhala maghar ghyayachi asel ti rakkam pravist kara:-.')
                    pyttsx3.speak('tumhala maghar ghyayachi asel ti rakkam pravist kara.')
                    cash_out = int(input('>>> : '))

                    if cash_out > amount:
                        print ("tumachyakade apura samtol aahe")
                        pyttsx3.speak('tumachyakade apura samtol aahe')

                    else:
                        amount = amount3 - cash_out
                        print('tumacha navin samtol aahe: ', amount3, 'Rupees')
                        pyttsx3.speak('tumacha navin samtol aahe')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif response == 3:
                    print('navin pin pravist kara:-')
                    pyttsx3.speak('navin pin pravist kara')
                    new_pin = int(input('>>> : '))

                    print('navin pinachi pusti kara:-')
                    pyttsx3.speak('navin pinachi pusti kara')
                    new_ppin = int(input('>>> : '))

                    if new_ppin != new_pin:
                        print('pin bemel')
                        pyttsx3.speak('pin bemel')

                    else:
                        UserPinn = new_pin
                        print('navin pin save kelley')
                        pyttsx3.speak('navin pin save kelley')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif response == 4:
                    exit()

            else:
                print('pratisad vaidh nahi')
                pyttsx3.speak('pratisad vaidh nahi')
    
        else:
            print ("keycard shodhanyat apayashi")
            pyttsx3.speak("keycard shodhanyat apayashi")
            exit()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif lang == 4:
    amount4 = 30948111.69
    
    print ("Umechagua : Kswahili")
    pyttsx3.speak ("YUmechagua Kswahili")

    while Trials != 0:
        print ("Kugundua kadi muhimu! Tafadhali subiri...")
        pyttsx3.speak("Kugundua kadi muhimu! Tafadhali subiri...")
        time.sleep(1)

        if d == True:
            print ("Kadi ya kiungo cha kati imegunduliwa!") 
            pyttsx3.speak("Kadi ya kiungo cha kati imegunduliwa!")

            print ("Tafadhali Ingiza Pini yako ya tarakimu 4:-")
            pyttsx3.speak ("Tafadhali Ingiza Pini yako ya tarakimu 4")
            Pin = int(input(">>> : "))

            if Pin == sos or Pin == sos2:
                print (">>> Eneo la tukio limearifiwa, tafadhali endelea na shughuli. <<<")
                print('KUINGIA SUCCESFUL')
                pyttsx3.speak('KUINGIA SUCCESFUL')
                pass

            elif Pin != UserPin:
                Trials -= 1
                print ("Nambari ya akaunti isiyo sahihi au pini! Una ", Trials, "Majaribio Yaliyoachwa")
                pyttsx3.speak("Nambari ya akaunti isiyo sahihi au pini!")

            else:
                print('KUINGIA SUCCESFUL')
                pyttsx3.speak('KUINGIA SUCCESFUL')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            print('Tafadhali teua Akaunti yako: \n 1. Akaunti ya sasa \n 2. Kuhifadhi Akaunti \n:-')
            pyttsx3.speak('Tafadhali teua Akaunti yako: Akaunti ya sasa, Kuhifadhi Akaunti')
            x = eval(input(">>> : "))

            if x == 1:
                print('TEUA KUTOKA KWA MACHAGUO YAFUATAYO: \n 1. Sawazisha Uchunguzi \n 2. Kuondoa \n 3. Badilisha PIN  \n 4. Aga \n:- ')
                pyttsx3.speak('TEUA KUTOKA KWA MACHAGUO YAFUATAYO: Sawazisha Uchunguzi, Kuondoa, Badilisha PIN, Aga ')
                response = int(input('>>> : '))

                valid_responses = ['1', '2', '3', '4']
                response = response

                if response == 1:
                    print('UNA ', amount4,'TZS KWENYE AKAUNTI YAKO..')
                    pyttsx3.speak('Una kiasi kinachofuata kwenye akaunti yako.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                
                elif response == 2:
                    print('INGIZA KIASI AMBACHO UNGEPENDA KUONDOA:-')
                    pyttsx3.speak('INGIZA KIASI AMBACHO UNGEPENDA KUONDOA')
                    cash_out = int(input('>>> : '))

                    if cash_out > amount4:
                        print ("HUNA UWIANO WA KUTOSHA")
                        pyttsx3.speak('HUNA UWIANO WA KUTOSHA')

                    else:
                        amount = amount4 - cash_out
                        print('USAWA WAKO MPYA NI: ', amount4, 'TZS')
                        pyttsx3.speak('USAWA WAKO MPYA NI')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif response == 3:
                    print('INGIZA PIN MPYA:-')
                    pyttsx3.speak('INGIZA PIN MPYA:-')
                    new_pin = int(input('>>> : '))

                    print('THIBITISHA PIN MPYA:-')
                    pyttsx3.speak('THIBITISHA PIN MPYA')
                    new_ppin = int(input('>>> : '))

                    if new_ppin != new_pin:
                        print('PIN KUTOLINGANA')
                        pyttsx3.speak('PIN KUTOLINGANA')

                    else:
                        UserPinn = new_pin
                        print('PIN MPYA IMEHIFADHIWA')
                        pyttsx3.speak('PIN MPYA IMEHIFADHIWA')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif response == 4:
                    exit()

                else:
                    print('JIBU SIO HALALI')
                    pyttsx3.speak('JIBU SIO HALALI')
                    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            elif x == 2:
                amount5 = 28956420.69
                print('TEUA KUTOKA KWA MACHAGUO YAFUATAYO: \n 1. Sawazisha Uchunguzi \n 2. Kuondoa \n 3. Badilisha PIN  \n 4. Aga \n:- ')
                pyttsx3.speak('TEUA KUTOKA KWA MACHAGUO YAFUATAYO: Sawazisha Uchunguzi, Kuondoa, Badilisha PIN, Aga ')
                response = int(input('>>> : '))

                valid_responses = ['1', '2', '3', '4']
                response = response

                if response == 1:
                    print('UNA ', amount5,'TZS KWENYE AKAUNTI YAKO..')
                    pyttsx3.speak('Una kiasi kinachofuata kwenye akaunti yako.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                
                elif response == 2:
                    print('INGIZA KIASI AMBACHO UNGEPENDA KUONDOA:-')
                    pyttsx3.speak('INGIZA KIASI AMBACHO UNGEPENDA KUONDOA')
                    cash_out = int(input('>>> : '))

                    if cash_out > amount5:
                        print ("HUNA UWIANO WA KUTOSHA")
                        pyttsx3.speak('HUNA UWIANO WA KUTOSHA')

                    else:
                        amount = amount5 - cash_out
                        print('USAWA WAKO MPYA NI: ', amount5, 'TZS')
                        pyttsx3.speak('USAWA WAKO MPYA NI')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif response == 3:
                    print('INGIZA PIN MPYA:-')
                    pyttsx3.speak('INGIZA PIN MPYA:-')
                    new_pin = int(input('>>> : '))

                    print('THIBITISHA PIN MPYA:-')
                    pyttsx3.speak('THIBITISHA PIN MPYA')
                    new_ppin = int(input('>>> : '))

                    if new_ppin != new_pin:
                        print('PIN KUTOLINGANA')
                        pyttsx3.speak('PIN KUTOLINGANA')

                    else:
                        UserPinn = new_pin
                        print('PIN MPYA IMEHIFADHIWA')
                        pyttsx3.speak('PIN MPYA IMEHIFADHIWA')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif response == 4:
                    exit()

            else:
                print('JIBU SIO HALALI')
                pyttsx3.speak('JIBU SIO HALALI')

        else:
            print ("Imeshindwa kugundua kadi ya kiungoa")
            pyttsx3.speak("Imeshindwa kugundua kadi ya kiungoa")
