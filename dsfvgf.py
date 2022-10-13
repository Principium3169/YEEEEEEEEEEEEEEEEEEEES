class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight
    def __str__(self):
        return str(self.number) + " " + str(self.model) + " " + str(self.weight)
    def receiveCall(self, caller):
        
phone1 = Phone(1, 2, 3)
phone2 = Phone(4, 5, 6)
phone3 = Phone(7, 8, 9)
print(phone1, phone2, phone3)