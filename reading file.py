name = raw_input('filename:')
import pickle
fo=open(name+'.dat','rb+')
a=pickle.load(fo)
print a
    
