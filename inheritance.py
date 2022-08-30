class students:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = f'{self.fname}{self.lname}@gmail.com'
        
    def fullName(self):
        return f'\nFirstName: {self.fname}\nLastName: {self.lname}\nAge: {self.age}\nEmail: {self.email}\nRank: {self.rank}'
    
class teachers(students):
    count = 0
    def __init__(self, fname, lname, age, rank):
        super().__init__(fname, lname, age)
        self.rank = rank
        teachers.count += 1
        
T1 = teachers('Katlong', 'Mark', 39, 9)
T2 = teachers('Sam', 'John', 42, 12)

print('List of teachers are: ', teachers.count)
print(T1.fullName())
print(T1.fullName())