class inputUpper:
    
    def inputString(self):
        str1=''
        self.str1 = input('Enter String: ')
        
    def printString(self):
        print(self.str1.upper())
        
str1 = inputUpper()
str1.inputString()
str1.printString()