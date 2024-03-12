class Seq():
    def __init__(self, strbases):
        print("New sequence was created")
        self.strbases = strbases
    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)
class Gene(Seq):
    def __init__(self, strbases,  name=""):
        super().__init__(strbases)
        self.name = name
        print("new gene created")

    def __str__(self):
        return self.strbases + '-' + self.name

s1 = Seq("AGACGACGTAT")
s2 = Seq("AGACGAGT")
g = Gene("AACGT", "U5")

print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print(f"Length Seq 1:", s1.len())
print(f"Length Seq 2:", s2.len())
print(f"Gene: {g}")
print(f"Length Gene:", g.len())