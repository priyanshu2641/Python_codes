#Javascript Object Notation
import json
data='{"var1":"Priyanshu","var2":"Sneaker game","var3":26}'

parsed=json.loads(data)
print(parsed['var1'])
print(parsed['var2'])
print(parsed['var3'])

#json.dumps makes the python code javascript compatible

a={
    "Priyanshu":"Coder",
    "Intersets":["Cricket","Cosmology","Sneaker"],
    "Date of Birth":"(26,4,2001)"
}
b=json.dumps(a)
print(b)