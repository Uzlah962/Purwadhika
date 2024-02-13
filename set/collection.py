setMovie1 = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk' }
setMovie2 = { 'The Avengers', 'Hulk' }

checkDisjoint = setMovie1.isdisjoint(setMovie2)
checkSubset = setMovie2.issubset(setMovie1)
checkSuperset = setMovie1.issuperset(setMovie2)

print(checkDisjoint) # False
print(checkSubset) # True
print(checkSuperset) # True