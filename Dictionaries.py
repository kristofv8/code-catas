my_dict = {"key1":"value1", "key2":"value2"}
print(my_dict)
print(my_dict["key1"])
prices_lookup = {"apples":2.99, "oranges":1.99, "milk": 5.50}
print(prices_lookup["apples"])
d = {"k1":123, "k2":[0,1,2,3], "k3":{"insidekey":100}}
print(d["k1"]), print(d["k2"]), print(d["k3"] ["insidekey"])
print(d["k2"] [3])
d = {"key1":["a","b","c","d"]}
print(d)
mylist = d["key1"]
print(mylist)
letter = mylist[2]
print(letter)
print(letter.upper())
print(d)
print(d["key1"])
print(d ["key1"] [2].upper())
d = {'key1':100, "key2":200}
d["key3"] = 300
d["key2"] = "new value"
print(d.keys())
print(d.values())
print(d.items())