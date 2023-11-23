class PIF:
    def __init__(self) -> None:
        self.array = []

    def add(self, token, value):
        self.array.append((token, value))

    def export(self):
        f = open("pif.out", "w")
        
        for (k, v) in self.array:
            f.write(k + " => " + str(v) + "\n")
        
        f.close()
