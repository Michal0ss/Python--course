# set = collection which is  unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dishes.update(utensils)
#dinnertable = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

#for x in dinnertable:
#    print(x)