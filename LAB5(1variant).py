class Rocket:

    def __init__(self, fuel_level, total_weight,engine_running):      
        self.fuel_level = fuel_level
        self.total_weight = total_weight
        self.engine_running = engine_running

    def spend_fuel(self, count):

        self.total_weight -= count
        self.fuel_level -= count 
        
        if self.fuel_level > 0:         #Топлива достаточно
            self.engine_running = True
            return True

        else:                           #Топлива недостаточно
            self.fuel_level=0
            self.engine_running = False    
            return False   

    def get_fuel_level(self):
        return f'Текущее количество топлива: {self.fuel_level}'
   
    def get_total_weight(self):
        return f'Текущая масса ракеты: {self.total_weight}'

    def get_is_engine_running(self):
        return f'Состояние двигателя(True-работает, False-не работет): {self.engine_running}'    

def Main():
    Test = Rocket(60000, 120000, True)
    k=0

    while (Test.fuel_level) > 0: 
        k+=1
        print(k,'минута')
        Test.spend_fuel(30000)
        print(Test.get_fuel_level())
        print(Test.get_total_weight())
        print(Test.get_is_engine_running())
        if Test.fuel_level == 0:
            print("Хьюстон, у нас большие проблемы...")
        

Main()