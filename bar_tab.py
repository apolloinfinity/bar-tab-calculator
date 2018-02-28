class Tab:

    #Class level attribute. Every time a new tab is created, these will remain the same
    menu = {
        'wine': 5,
        'beer': 3, 
        'soft_drink': 2,
        'chicken': 10,
        'beef': 15,
        'veggie': 12, 
        'desert': 6
    }

    def __init__(self):
        self.total = 0
        self.items = []
    
    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item] # Gets dict and its key. Key is the price and is what gets added.

    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20} ${self.menu[item]}') # 20 inside the string format gives the final result 20 spaces from it

        print(f'{"Total":20} ${total:.2f}')