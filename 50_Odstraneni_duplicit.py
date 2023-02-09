#50: Odstranění duplicitních prvků z posloupnosti a sdělení jejich počtu
#Vít Šrámek, 3. ročník, B-SGG
#ZS 2022/2023
#Úvod do programování (MZ370P19)


#trida pro nahrani cisel
class Char():
    #pripravi promenne
    value = int
    occurences = 1
    processed = 0

    #vybere pouze cisla
    def __init__(self, value):
        if value.isnumeric():
            self.value = value

    #vytvori objekty
    def __repr__(self):
        text = 'Number: ' + str(self.value) + ', Occurences: ' + str(self.occurences) + '\n' 
        return text
    
    #spocita pocet vyskytu cisla
    def increment(self):
        self.occurences = self.occurences + 1

    #def setProcessed(self):
    #    processed = 1

    #def getProcessed(self): #tohle asi muzu dat pryc
    #    return self.processed

    #vypise hodnotu cisla
    def getValue(self):
        return self.value

#trida pro operace s cisli    
class Numbers():

    #pripravi promenne pro operace
    numbers_array = []
    original_value = ""
    data_without_duplicits = []
    duplicities = 0

    #vypise neduplicitni cisla
    def __init__(self, data):
        self.original_value = data
        counter = 0
        for i in data:            
            val = Char(i)            
            in_list = 0
            if counter == 0:
                self.data_without_duplicits.append(val)
            else:    
                for j in self.data_without_duplicits:
                    if i == j.value:
                        j.increment()
                        in_list = 1
                        self.duplicities += 1
                if in_list == 0:                    
                    self.data_without_duplicits.append(val)
            counter += 1


    #seradi cisla podle numericke hodnoty
    def sort(self):
        sorted_list = []
        self.sorted_list = sorted(self.data_without_duplicits, key=lambda v: int(v.getValue()))
        print("Sorted data: " + "\n" + str(self.sorted_list))
        return self.sorted_list    

    #vypise pocet duplcit
    def getDuplicities(self):
        print("Number of duplicities: " + str(self.duplicities))
        return self.duplicities

#trida pro nahrani a vypsani cisel
class Processor():

    #pripravi promenne pro vstupni soubory a cisla
    file = ""   
    numbers = []

    def __init__(self, file):
        self.file = file
        # nacte vstupni soubor, pripadne nahlasi chybu
        try:
            with open (self.file, 'r') as infile:
                try:
                    data = infile.read()
                except Exception as ch:
                        print("Při načítání dat se stala chyba: ", ch, "oprav ji a začni znovu")
                try:
                    data=data.replace("\n", ",")
                    data_split = data.split(",")
                    infile.close()
                except Exception as ch:
                    print("Při převodu dat se stala chyba: ", ch, "oprav ji a začni znovu")
        except FileNotFoundError as ch:
                print("Chyba při načítání souboru, soubor nenalezen. Nahraj ho a začni znovu")
        except Exception as ch:
                print("Při otevírání dat se stala chyba ", ch, "oprav ji a začni znovu")
        else:
            pass

        #vezme pouze ciselne udaje
        for i in data_split:
            if i.isnumeric():
                self.numbers.append(i)

    def getNumbers(self):
        return self.numbers
    
    #ulozi vysledne hodnoty    
    def storeValues(self, file, sorted_numbers, duplicities):
        try:
            with open(file, 'w') as outfile:
                try:
                    for i in sorted_numbers:
                        outfile.write(str(i.value)+"\n")
                except Exception as ch:
                    print("Stala se chyba ", ch, "oprav ji a zkus to znova")
        except FileNotFoundError as ch:
                print("Chyba při otevirani souboru, soubor nenalezen. Nahraj ho a začni znovu")
        except Exception as ch:
                print("Při vypisovani dat se stala chyba ", ch, "oprav ji a začni znovu")
        else:
            pass

#provede operace s testovacimi soubory
proc = Processor("vstup.txt")
values_to_process = []
values_to_process = proc.getNumbers()
print("Extracted numbers: " + str(values_to_process))

numbers = Numbers(values_to_process)
sorted_numbers = numbers.sort()
duplicities = numbers.getDuplicities()

#vypise vysledky a skonci
proc.storeValues("vystup1.txt", sorted_numbers, duplicities)
quit()