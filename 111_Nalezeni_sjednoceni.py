#111: Dány dvě posloupnosti čísel, nalezení jejich sjednocení
#Vít Šrámek, 3. ročník, B-SGG
#ZS 2022/2023
#Úvod do programování (MZ370P19)


#trida pro nahrani a vypsani cisel
class Processor():

    #pripravi promenne pro vstupni soubory a cisla
    file = ""   
    numbers = []

    def __init__(self, file):
        self.file = file
        self.numbers = []
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
    def storeValues(self, file, sorted_numbers):
        try:
            with open(file, 'w') as outfile:
                try:
                    for i in sorted_numbers:
                        outfile.write(i + "\n")                    
                except Exception as ch:
                    print("Stala se chyba ", ch, "oprav ji a zkus to znova")
        except Exception as ch:
                print("Při vypisovani dat se stala chyba ", ch, "oprav ji a začni znovu")
        else:
            pass

#trida pro serazeni cisel
class Merger():
    #pripravi promenne 
    sorted_number = []

    def __init__(self,value1, value2):
        pointer1 = 0 
        pointer2 = 0 
        len1 = len(value1)
        len2 = len(value2)         
        len_total = len1 + len2    

        #seradi cisla  a odstrani duplicitu
        for i in range(len_total):
            #vypise prebyvajici cisla z druheho souboru
            if (pointer1 == len1 - 1):
                for j in range(len2 - pointer2):
                    if (value2[pointer2 + j]) not in self.sorted_number:
                        if int(value2[pointer2 + j])< int(value1[pointer1]):                        
                            self.sorted_number.append(value2[pointer2 + j])
                        elif int(value2[pointer2 + j])> int(value1[pointer1]):
                            self.sorted_number.append(value1[pointer1])
                            for i in range(len2-pointer2-j):
                                if (value2[pointer2 + j]) not in self.sorted_number:                       
                                    self.sorted_number.append(value2[pointer2 + j+i])
                print("End at value1")
                break
            #vypise prebyvajici cisla z prvniho souboru
            elif (pointer2 == len2 - 1):
                for j in range(len1 - pointer1):   
                    if (value1[pointer1 + j]) not in self.sorted_number:
                        if int(value1[pointer1 + j]) < int(value2[pointer2]):
                            self.sorted_number.append(value1[pointer1 + j])
                        elif int(value1[pointer1 + j]) > int(value2[pointer2]):
                            self.sorted_number.append(value2[pointer2])
                            for i in range(len1-pointer1-j):
                                if (value1[pointer1 + j]) not in self.sorted_number:                       
                                    self.sorted_number.append(value1[pointer1 + j+i])
                print("End at value2")
                break     
            #postupne seradi cisla podle velikosti a zapise je
            if (int(value1[pointer1]) > int(value2[pointer2])) and (int(value2[pointer2])) not in self.sorted_number:
                self.sorted_number.append(value2[pointer2])
                pointer2 = pointer2 + 1
            elif (int(value1[pointer1]) < int(value2[pointer2])) and (int(value1[pointer1])) not in self.sorted_number:
                self.sorted_number.append(value1[pointer1]) 
                pointer1 = pointer1 + 1
            elif (int(value1[pointer1]) == int(value2[pointer2])) and (int(value1[pointer1])) not in self.sorted_number: 
                self.sorted_number.append(value1[pointer1])
                pointer1 = pointer1 + 1
                pointer2 = pointer2 + 1
                i = i + 1 

    def getNumbers(self):
        return self.sorted_number


#provede operace s testovacimi soubory
proc = Processor("vstup2.txt")
values_to_process = proc.getNumbers()
print("Extracted numbers 1: " + str(values_to_process))

proc2 = Processor("vstup3.txt")
values_to_process2 = proc2.getNumbers()
print("Extracted numbers 2: " + str(values_to_process2))

merger = Merger(values_to_process, values_to_process2)
sorted_numbers = merger.getNumbers()
print("Results: " + str(sorted_numbers))

#vypise vysledky a skonci
proc.storeValues("vystup2.txt", sorted_numbers)
quit()