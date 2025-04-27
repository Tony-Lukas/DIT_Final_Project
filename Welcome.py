from main import MyClass
import time

class Dinosour(MyClass):
    def __init__(self):
        self.logo = self.load_logo()
        self.show_logo()
        print("Welcome to Jurassic Park Research Faculty (J.P.R.F)!")
        print("How can we help you today?")
        time.sleep(1)
        super().__init__('Dinosaurs')

    def load_logo(self):
        with open('logo.txt','r') as f:
            return f.readlines()
    
    def show_logo(self):
        for line in self.logo:
            print(line,end='')


if __name__ == '__main__':
    Dino = Dinosour()
    Dino.run()
    Dino.show_logo()
    print("Thank you")
