from miniciti.bilding import Bilding

class ColorBilding(Bilding):

    def __init__(self, color="bli"):
        self.color = color

    def isBli(self):
        return self.color == "bli"
