from sys import getsizeof

# za razliku od lista ne cujavu podatke u memoriji vec henerisu nove u svakoj iteraciji a ponasaju se kao liste, moze se iterirati

values = (x*2 for x in range(100000))
for x in values:
    print(x)

# za 100 : gen: 208, za 10000 gen: 208-dakle cak i ako ima puno vise objekata velicina je ista, za liste bi se znacajno razlikovala
print("gen:", getsizeof(values))

# ako bi koristili list komprehensions: za 100 je list: 920 , za 100000 list: 800984
values = [x*2 for x in range(100000)]
print("list:", getsizeof(values))

# u situacijama kada koristimo velike kolicine podataka ili infinit stream of data bolje je koritiri generator
