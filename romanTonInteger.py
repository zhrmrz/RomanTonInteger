class Sol:
    def __init__(self,rom_num):
        self.rom_num=rom_num
    def convertor(self):
        s=str(self.rom_num)
        couples={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        singles={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        integer=0
        while(i<len(s)):
            if(i<len(s)-2 and s[i:i+2] in couples):
                integer+=couples[s[i:i+2]]
            else:
                integer+=singles[s[i]]
            i+=1
        return integer
if __name__ == '__main__':
    rom_num=input("Enter a roman number to be converted to integer : ")
    p1=Sol(rom_num)
    print(p1.convertor())
