# # x = int(input("Enter your name: "))
# a = [1,2,3,4,5,6,"Kritharth",10.2]
# print(a)
# a.pop(2);
# print(a)

class Animal:
    breed:str
    limbs:int
    
    def __init__(self,breed,limbs) -> None:
        self.breed = breed
        self.limbs = limbs
    
    def set_age(self):
        age = 5
        print(age)
        
    


dog = Animal("german shephard",4)
cat =Animal("persian",4)
print(dog.breed)
print(cat.breed)
