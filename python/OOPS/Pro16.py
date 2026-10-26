from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def roi(self):
        pass

class HDFC(RBI):
    def roi(self):
        return 7.5

class SBI(RBI):
    def roi(self):
        return 9.5 

hdfc = HDFC()
sbi = SBI()

print(hdfc.roi())
print(sbi.roi())