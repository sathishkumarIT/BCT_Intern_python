#hashMap
d = {}
d["name"] = "Sathish"
d["age"] = 25
d["city"] = "Chennai"
print(d)
print(d["name"]) 
print(d.get("age"))
print(d.get("city", "Not Found"))   
print(d.get("country", "Not Found"))
d["age"] = 26
print(d)
del d["city"]
print(d)

#looping through hashMap
for key in d:
    print(key, ":", d[key])

for key, value in d.items():
    print(key, ":", value)

