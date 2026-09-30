#Dictionary =  a collection of {key:value} pairs ordered and changeable. No duplicates.



capitals = 	{"india" :"New Delhi",
		"USA":"Washiton D.C",
		"China":"Beijin",
		"Russia": "Moscow"}

#print(dir(capitals))
#print(capital.get("india"))


#if capitals.get("russia"):
#	print("The Capitals exists")
#else:
#	print("The capital does't exist")	

#capitals.update({"Germany":"Berlin"})
#capitals.pop("China")
#captials.popitem()
#cpatials.clear()

#print(capitals)



#keys = capitals.keys()
#for key in capitals.keys():
	#print(keys)

#values = capitals.values()
#for value in capitals.values():
#	print(value)

items=capitals.items()
for key,value in capitals.items():
	print(f"{key}:{value}")