from dolgozo import Dolgozo

class Talon:
    def __init__(self):
        self.file_name = 'talonkft.txt'
        self.dolgozok = []
    def open_file(self):
        fp = open(self.file_name, 'r', encoding='utf-8')
        lines = fp.readlines()
        for line in lines:
            line = line.rstrip()
            (nev, telepules, cim, szuletes, fizetes) = line.split(':')
            dolgozo = Dolgozo(nev, telepules, cim, szuletes, fizetes)
            self.dolgozok.append(dolgozo)
        fp.close()
    def kiTataiDolgozok(self):
        for dolgozo in self.dolgozok:
            if dolgozo.telepules == 'Tata':
                print(dolgozo.nev)

    def csengeriFizetesek(self):
        osszeg = 0
        for dolgozo in self.dolgozok:
            if dolgozo.telepules == 'Csenger':
                osszeg = osszeg + int(dolgozo.fizetes)
        print('Csengeri fizetések:', osszeg)
    
talon = Talon()
talon.open_file()
talon.kiTataiDolgozok()
talon.csengeriFizetesek()



