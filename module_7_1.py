from pprint import pprint

class Product:
    name = ''
    weight = 5.4
    category = ''
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = weight
        self.category =category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def add(self, *products):
        list_p1 = list(products)
        str_read_File = self.get_products()

        self.file = open(self.__file_name,'a')
        for i in list_p1:
            if str(i) in str_read_File:
                print(f'Продукт {str(i)} уже есть в магазине' )
            else:
                self.file.write(str(i)+'\n')
        self.file.close()

    def get_products(self):
        self.file = open(self.__file_name,'r')
        str_read = self.file.read()
        self.file.close()
        return str_read

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1,p2,p3)
print(s1.get_products())


