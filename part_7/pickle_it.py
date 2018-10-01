import pickle, shelve
print("Conserver")
variety = ["tomatoo", "pickles", "apples"]
shape = ["all", "parts", "shrinks"]
brand = ["Glavprodukt", "Chumak", "Hainse"]
f =open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()
print("'Unzipping'")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print  (brand)
print("\nShelve module")
s = shelve.open("pickles2.dat")
s["variety"]  = ["tomatoo", "pickles", "apples"]
s["shape"] = ["all", "parts", "shrinks"]
s["brand"] = ["Glavprodukt", "Chumak", "Hainse"]
print("Extract")
print("TM- ", s["brand"])
print("forms- ", s["shape"])
print("variety- ", s["variety"])
s.close()
