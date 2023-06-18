class dad:
    Sport="Tennis"
    Height=5.7
    Weight=80

class son(dad):
    Sport="Football"
    Height= 5.8

class grandson(son):
    Sport="Cricket"

Neil= dad()
Nitin= son()
Mukesh= grandson()

print(Mukesh.Sport)
print(Mukesh.Height)
print(Mukesh.Weight)
print(Nitin.Weight)