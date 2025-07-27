class Writer:
    def __init__(self, name):
        self.name = name

    def write(self):
        print(f"{self.name} is writing an article.")

class Blogger(Writer):
    def __init__(self, name, platform):
        self.platform = platform

    def write(self):
        print(f"Posting to {self.platform}...")
        write()

w = Writer("Grace")
w.write()

b = Blogger("Dan", "Medium")
b.write()
