import pickle
def createAccounts():
    '''Function to create a binary file containing empty dictionary to be used in 'pyDiary.py' program'''
    accntsFile = file('accounts.dat','wb')
    accounts = {} #{username:password}
    pickle.dump(accounts,accntsFile)
    accntsFile.close()
createAccounts()

