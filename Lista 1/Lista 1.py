import random

class Vector:

    def __init__(self, size=3):  # inicjator
        self.size = size
        self.elements = []
        
    def generate_random(self): # ta metoda nadaje losowe wartości elementom wektora
        self.elements = []
        for i in range(self.size):
            a = random.randint(-100,100)
            self.elements.append(a)
            i+=1
       
    def load_from_list(self,list): # ta metoda przypisuje podaną listę jako wartości elementów wektora
        if len(list) != self.size:
            return "rozmiar wektora i liczba elementów w liście są różne"
        self.elements = list
    
    def __add__(self, other): # definicja dodawania dla klasy
        if self.size != other.size:
            return "ValueError"
        wynik = []
        for i in range(len(self.elements)):
            a = self.elements[i] + other.elements[i]
            wynik.append(a)
            i+=1
        return wynik

    def __sub__(self, other):  # definicja odejmowania dla klasy
        if self.size != other.size:
            return "ValueError"
        wynik = []
        for i in range(len(self.elements)):
            a = self.elements[i] - other.elements[i]
            wynik.append(a)
            i+=1
        return wynik

    def __mul__(self, other): # definicja mnożenia dla klasy
        if isinstance(other, int) == True:
            for i in range(len(self.elements)):
                self.elements[i] = self.elements[i] * other
            return self.elements
        else:
            for i in range(len(other.elements)):
                other.elements[i] = other.elements[i] * self.size
            return other.elements
        
    def len(self): # ta metoda liczy długość wektora
        a=0
        for i in range(self.size):
            a+=(self.elements[i])**2
            i+=1
        return (a**(1/2))
        
    def sum(self): # ta metoda sumuje wszystkie elementy wektora
        a=0
        for i in range(self.size):
            a+=self.elements[i]
        return a

    def dot_product(self, other): # metoda służąca do mnożenia skalarnego
        if self.size != other.size:
            return "ValueError"
        wynik=0
        for i in range(self.size):
            wynik+=self.elements[i]*other.elements[i]
        return wynik
        
    def __str__(self): #reprezentacja tekstowa wektora
        return f"{self.elements}"

    def __getitem__(self, index): # operator [] pozwalający na dostęp do konkretnych elementów wektora
        return self.elements[index]

    def __contains__(self, item): # operator in sprawdzający przynależność elementu do wektora
        return item in self.elements

p = Vector(4)
r = Vector(4)

p.generate_random()
r.load_from_list([1,2,3,4])
print(f"wektor p {p}")
print(f"wektor r {r}")
print(f"dodawanie {p+r}")
print(f"odejmowanie {p-r}")
print(f"mnożenie p*2 {p*2}")
print(f"długość wektora p {p.len()}")
print(f"suma elementów p {p.sum()}")
print(f"mnożenie wektorowe {p.dot_product(r)}")
print(f"trzeci element wektora p {p[2]}")
print(f"sprawdzenie czy 3 należy do p {3 in p}")

# raise, 
# def __rmul__(self,other):
