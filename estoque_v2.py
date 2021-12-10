import pandas as pd

class Product:

    name: str
    quantity: int
    id: int

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.id = None

    def register_id(self, id):
        self.id = id

    def change_quantity(self, quantity):
        new_quantity = self.quantity + quantity
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print('Error')

    def __str__(self):
        return f'(id:{self.id}) {self.name}: {self.quantity} un.'\

    def __repr__(self):
        return f'Product{self.name.title().replace(" ", "")}'

class Inventory:

    Product: object

    def __init__(self):
        self.inventory = []
        self.names = set()
        self.last_id = 1

    def load_inventory(self, inventory):
        # create a way to load an pre made inventory from a table or somenthing of the sort
        # need to get last id ro something like used ids
        pass

    def register_product(self, name, quantity=0):
        if name not in self.names:
            product = Product(name, quantity)
            product.register_id(self.last_id)
            self.inventory.append(product)
            self.names.add(name)
            self.last_id += 1
        else:
            for product in self.inventory:
                if product.name == name:
                    print(f'Find {product.name}')
                    product.change_quantity(quantity)

    def __str__(self):
        output_string = 'List of products: \n' + '-' * 15 + '\n'
        for product in self.inventory:
            output_string  += f'{product} \n'
        output_string  += '-' * 15
        return output_string 

    def __repr__(self):
        return f'{self.inventory}'

    def to_lists(self):
        list_name = [product.name for product in self.inventory]
        list_quantity = [product.quantity for product in self.inventory]
        list_id = [product.id for product in self.inventory]
        return list_name, list_quantity, list_id

if __name__ == '__main__':
    # here creates and inventory for products
    e = Inventory()
    # registering products and adding quantity in pre existing ones
    e.register_product('Modern Desk')
    e.register_product('Modern Desk', 1)
    e.register_product('Laptop', 10)
    e.register_product('Keyboard', 6)
    # print a list of the inventory with id, name, quantity
    print(e)
    # repr de class + name of de product obj
    print([e])
    # transforming the atributes of the object store in lists
    name, qtd, id = e.to_lists()
    # transforming (manually) the lists in a Pandas DataFrame
    df = pd.DataFrame({'id': id, 'name': name, 'quantity': qtd})
    # printing Pandas DataFrame
    print(df)