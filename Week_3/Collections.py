#List allows duplicate
#Modification is allowd
#allow different data types

List = [1 ,2,3 ,4 ,"Sathish"]
print(List)
List.append("sk")
print(List)
List.insert(0 , "Msk")
print(List)
List[1] = "MSK"
print(List)

#index 
print(List[-1])

# delete
List.remove("Msk")
print(List)
List.pop(3)
print(List)

#Length
print(len(List))
print(List[0:3])
print(List.reverse())

#tuple
#tuple allows duplicate
#Modification is not allowd
#allow different data types

Tuple = (1 ,2,3 ,4 ,"Sathish")
print(Tuple)

Li = list(Tuple)
Li.append("sk")

tuple2 = tuple(Li)
print(tuple2)

#set
#Set does not allow duplicate
#Modification is allowd
#allow different data types
Set = {1 ,2,3 ,4 ,"Sathish"}
print(Set)
Set.add("sk")
print(Set)
Set.remove("Sathish")
Set.discard("Sathish")
print(Set)
Set.pop()
print(Set)
Set.update(["sk1" , "sk2"])
print(Set)

#Dictionary
#Dictionary does not allow duplicate keys   
#Modification is allowd
#allow different data types
Dict = {"Name":"Sathish" , "Age":25 , "City":"Tuticorin"}
print(Dict)
Dict["Age"] = 21
print(Dict)
Dict["Country"] = "India"
print(Dict)
Dict.pop("City")
print(Dict)
del Dict["Country"]         
print(Dict)
