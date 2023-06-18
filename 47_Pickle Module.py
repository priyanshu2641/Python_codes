# It is used to preserve any object- Eg.-List,Tuple,Set
import pickle
sneakers=["Nike","jordan","Adidas","Reebok","Puma","New Balance"]
# file="bestsneakersbrand.pkl"
# fileobj=open(file,"wb")
# pickle.dump(sneakers,fileobj)
# fileobj.close()

file="bestsneakersbrand.pkl"
fileobj=open(file,"rb")
a=pickle.load(fileobj)
print(a)