class TagCloud:

    # definise konstruktor i u njemu inicijalizjujemo tag atribut u prazan diksneri , biram diksneri jer omogucava da se brzo dobije broj taga

    def __init__(self):
        self.__tags = {}

# metod add koji uzima tag i proverava imamo li taj tag u diksneriju i ako ga nema setovacemo njegovu
# vrednost na jedan u suprotnom inkrementujemo ga za jedan, i da bude sve malim slovima
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __itter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("pythOn")
cloud.add("pyThon")
cloud.add("python")

# ako se ispred imena atributa stavi __ dupli underskor  postaje private umesto public ali su i dalje dostupni, nije kao u javi
print(cloud.__tags)

cloud["python"] = 10
len(cloud)

print(cloud.__tags["PYTHON"])

print(cloud.__dict__)
