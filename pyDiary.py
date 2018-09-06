import pickle #to read binary files.
import re #to validate password.
import datetime #to attach date and time to diary entries.
import os #to remove file upon account deletion.
from Tkinter import *
import tkMessageBox as tmb #to give info and warnings for certain actions.
class Account(object):
    '''Class to create new user account'''
    q1_list = ('What was your favorite place to visit as a child?',\
                  'Who is your favorite actor, musician, or artist?',\
                  'What is the name of your pet?',\
                  'In what city were you born?',\
                  'What high school did you attend?')
    q2_list = ('What is the name of your first school?',\
                  'What is your favorite movie?',\
                  'What is your mother\'s maiden name?',\
                  'What street did you grow up on?',\
                  'What was the make of your first car?')
    info = ('Please enter your full name.\n\n Use up and down arrow keys to select.\n Age can only be between 16-80 years.\n\n\n\n\n\n\
           The security questions are required in case you forget\nyour login details and need to recover your account.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
           Your password should be 8-16 characters long\nand contain atleast one small and capital alphabet,\n one number and one symbol.')          
    def __init__(self, name, age, gender,q1,ans1,q2,ans2, username, password):
        self.name = name
        self.age = age
        self.gender = gender
        self.username, self.password = username, password
        self.recovery = {self.q1_list[q1]: ans1, self.q2_list[q2]:ans2} #{question 1: answer 1,question 2: answer 2}
        self.diary = [] #[(date,entry),....]
        self.saveToFiles()
    def saveToFiles(self):
        accountsFile()
        accntFile = file(self.username+'.dat','wb')
        accounts[self.username] = self.password
        pickle.dump(accounts,accntsFile)
        pickle.dump(self.__dict__,accntFile)
        accntFile.close()
        accntsFile.close()
class AccountGUI(Account):
    '''Class to create and manage account.
        methods:
           -create_account():to create new account
              -create_widgets()
              -place_widgets()
              -checkData()
              -confirm()
           -open_account():to open existing account
              -create_widgets()
              -place_widgets()
           -Write_new():to write new entry
              -save()
              -discard()
              -create_widgets()
              -place_widgets()
           -Read_old():to read an old entry
              -read()
              -delete()
              -go_back()
              -create_widgets()
              -place_widgets()
           -acc_sett():to access account settings
              -change()
                 -create_widgets()
                 -place_widgets()
                 -checkData()
                 -confirm()
              -delAcc()
              -go_back()
              -create_widgets()
              -place_widgets()
           -recover_account():to recover account
              -confirm()
                 -check()
                 -create_widgets()
                 -place_widgets()
              -create_widgets()
              -place_widgets()'''
    def __init__(self):
       defaultScreen()
    def create_account(self):
        def create_widgets():
            self.txt_lbl = Label(screen, text = 'Please fill out the following details', \
                       font = ('Comic Sans MS',10), bg='black',fg='white',width = 60, \
                       height = 1)
            self.infoLbl = Label(screen, text = Account.info, width = 50)
            self.nameLbl = Label(screen, text = 'Full Name:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.ageLbl = Label(screen, text = 'Age:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.genderLbl = Label(screen, text = 'Gender:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.q1Lbl = Label(screen, text = 'Question 1:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.Ans1Lbl = Label(screen, text = 'Answer 1:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.q2Lbl = Label(screen, text = 'Question 2:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.Ans2Lbl = Label(screen, text = 'Answer 2:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.usernameLbl = Label(screen, text = 'Username:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.passwordLbl = Label(screen, text = 'Password:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.nameEntry = Entry(screen, width = 70)
            self.ageSelect = Listbox(screen, width = 70, height = 1)
            for i in range(16,81):
                self.ageSelect.insert('end',i)
            self.genderSelect = Listbox(screen, width = 70, height = 3)
            self.genderSelect.insert('end','male')
            self.genderSelect.insert('end','female')
            self.genderSelect.insert('end','others')
            self.q1Select = Listbox(screen, width = 70, height = 5)
            for i in range(len(Account.q1_list)):
                self.q1Select.insert('end',Account.q1_list[i])
            self.q1AnsEntry = Entry(screen, width = 70)
            self.q2Select = Listbox(screen, width = 70, height = 5)
            for i in range(len(Account.q2_list)):
                self.q2Select.insert('end',Account.q2_list[i])
            self.q2AnsEntry = Entry(screen, width = 70)
            self.usernameEntry = Entry(screen, width = 70)
            self.passwordEntry = Entry(screen, width = 70, show = '*') 
            self.q1Lbl = Label(screen, text = 'Question 1:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.q2Lbl = Label(screen, text = 'Question 2:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.confirmBtn = Button(screen, text = 'CONFIRM', command = confirm)
            self.cnclBtn = Button(screen, text = 'CANCEL', command = cancel)
        def place_widgets():
            self.txt_lbl.pack(fill = 'x', pady = 7)
            self.infoLbl.place(x = 900, y = 125)
            self.nameLbl.place(x = 150, y = 125)
            self.nameEntry.place(x = 300, y = 125)
            self.ageLbl.place(x = 150,y = 165)
            self.ageSelect.place(x = 300,y = 165)
            self.genderLbl.place(x = 150, y = 205)
            self.genderSelect.place(x =300, y = 205)
            self.q1Lbl.place(x = 150, y = 265)
            self.q1Select.place(x = 300, y = 265)
            self.Ans1Lbl.place(x = 150, y = 345)
            self.q1AnsEntry.place(x = 300, y = 355)
            self.q2Lbl.place(x = 150, y = 395)
            self.q2Select.place(x = 300, y = 395)
            self.Ans2Lbl.place(x = 150, y = 475)
            self.q2AnsEntry.place(x = 300, y = 485)
            self.usernameLbl.place(x = 150, y = 525)
            self.usernameEntry.place(x = 300, y = 525)
            self.passwordLbl.place(x = 150, y = 565)
            self.passwordEntry.place(x = 300, y = 565)
            self.confirmBtn.place(x = 450, y = 605)
            self.cnclBtn.place(x = 550, y = 605)
        def checkData(name, ans1, ans2, username, password):
            check = 0
            passwordCheck = re.match('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!%^&*.@#$]).{8,16}', password)
            if not passwordCheck:
                check = 1
            accountsFile()
            for usernames in accounts:
                if username == usernames or username == '':
                    check = 2
            accntsFile.close()
            for value in [name, ans1, ans2]:
                if value == '':
                    check = 3
            return check
        def confirm():
            name = self.nameEntry.get()
            age = self.ageSelect.get('active')
            gender = self.genderSelect.get('active')
            q1 = Account.q1_list.index(self.q1Select.get('active'))
            ans1 = self.q1AnsEntry.get()
            q2 = Account.q2_list.index(self.q2Select.get('active'))
            ans2 = self.q2AnsEntry.get()
            username = self.usernameEntry.get()
            password = self.passwordEntry.get()
            check = checkData(name, ans1, ans2, username, password)
            if check == 0:
                acc = Account(name, age, gender, q1, ans1, q2, ans2, username, password)
                self.open_account(username)
                self.username = username
            else:
                if check == 1:
                    tmb.showerror('Invalid Details','Invalid Password')
                if check == 2:
                    tmb.showerror('Invalid Details','Username Already Exists')
                if check == 3:
                    tmb.showerror('Invalid Details','Required Details Missing ')
        create_widgets()
        place_widgets()
    def open_account(self, username):
        self.username = username
        def create_widgets():
            self.newDiaryBtn = Button(screen, text = 'Write new diary',\
                                 font = ('Comic Sans MS',20), bg='white',command = self.Write_new)
            self.oldDiaryBtn = Button(screen, text = 'Read old diary',\
                                 font = ('Comic Sans MS',20), bg='white',command = self.Read_old)
            self.settBtn = Button(screen, text = 'Account Settings',\
                                  font = ('Comic Sans MS',20), bg='white',\
                                  command = self.acc_sett)
            self.loutBtn = Button(screen, text = 'Log Out', font = ('Comic Sans MS',20), bg='white',\
                                  command = sign_in)
        def place_widgets():
            self.newDiaryBtn.pack(fill = 'x', pady = 5)
            self.oldDiaryBtn.pack(fill = 'x', pady = 5)
            self.settBtn.pack(fill = 'x', pady = 5)
            self.loutBtn.pack(fill = 'x', pady = 5)
        screen.destroy()
        defaultScreen()
        create_widgets()
        place_widgets()
    def Write_new(self):
        def save():
            with open(self.username+'.dat','rb+') as fo:
                entry = self.diaryText.get("1.0",'end-1c')
                if entry == '':
                    tmb.showerror('Invalid Entry', 'Entry can not be empty')
                else:
                    date = str(datetime.datetime.now())
                    details = pickle.load(fo)
                    details['diary']+=[(date, entry)]
                    fo.seek(0)
                    pickle.dump(details,fo)
                    self.open_account(self.username)
        def discard():
            entry = self.diaryText.get("1.0",'end-1c')
            if entry == '':
                self.open_account(self.username)
            else:
                choice = tmb.askyesno('Discard', 'Are you sure you want to discard the entry')
                if choice == True:
                    self.open_account(self.username)
        def create_widgets():
            date = str(datetime.datetime.now())
            self.dateLbl = Label(screen, text = 'Today\'s date & time: %s'%(date), font = \
                                 ('Comic Sans MS',15), bg='black',fg='white')
            self.diaryLbl = Label(screen, text = 'Diary Entry:', font = \
                                 ('Comic Sans MS',15), bg='black',fg='white')
            self.diaryText = Text(screen, width = 70, height = 10)
            self.saveBtn = Button(screen, text = 'SAVE', command = save)
            self.discardBtn = Button(screen, text = 'DISCARD', command = discard)
        def place_widgets():
            self.dateLbl.place(x = 300, y = 125)
            self.diaryLbl.place(x = 300, y = 165)
            self.diaryText.place(x = 430, y = 165)
            self.saveBtn.place(x = 450, y = 355)
            self.discardBtn.place(x = 550, y = 355)
        screen.destroy()
        defaultScreen()
        create_widgets()
        place_widgets()
    def Read_old(self):
        with open(self.username+'.dat','rb') as fo:
            self.diary = pickle.load(fo)['diary']
        def read():
            entry = self.diarySelect.get('active')
            if entry == '':
                tmb.showerror('Empty','No entry in diary')
            else:
                tmb.showinfo(entry[0], entry[1])
        def delete():
            entry = self.diarySelect.get('active')
            if entry == '':
                tmb.showerror('Empty','No entry in diary')
            else:
                choice = tmb.askyesno('Delete', 'Are you sure you want to delete entry of %s?'%entry[0])
                if choice == True:
                    with open(self.username+'.dat', 'rb+') as fo:
                        details = pickle.load(fo)
                        index = details['diary'].index(entry)
                        details['diary'].remove(entry)
                        fo.seek(0)
                        pickle.dump(details, fo)
                        self.diarySelect.delete(index, index)
        def go_back():
            self.open_account(self.username)
        def create_widgets():
            self.diaryLbl = Label(screen, text = 'Diary Entries:', font = \
                                 ('Comic Sans MS',15), bg='black',fg='white')
            self.diarySelect = Listbox(screen, width = 70, height = 10)
            for i in self.diary:
                self.diarySelect.insert('end',i)
            self.readBtn = Button(screen, text = 'Read', command = read)
            self.delBtn = Button(screen, text = 'Delete', command = delete)
            self.backBtn = Button(screen, text = 'Go back', command = go_back)
        def place_widgets():
            self.diaryLbl.place(x = 150, y = 165)
            self.diarySelect.place(x = 300, y = 165)
            self.readBtn.place(x = 450, y = 355)
            self.delBtn.place(x = 550, y = 355)
            self.backBtn.place(x = 650, y = 355)
        screen.destroy()
        defaultScreen()
        create_widgets()
        place_widgets()
    def acc_sett(self):
        def change():
            temp = self.username
            with open(self.username+'.dat','rb') as fo:
                self.diary = pickle.load(fo)['diary']
            def create_widgets():
                self.options = Listbox(screen, width = 10, height = 5)
                for option in ['Name', 'Age', 'Gender', 'Security questions and answers',\
                               'username','password']:
                    self.options.insert('end',option)
                self.txt_lbl = Label(screen, text = 'Please fill out the following details', \
                           font = ('Comic Sans MS',10), bg='black',fg='white',width = 60, \
                           height = 1)
                self.infoLbl = Label(screen, text = Account.info, width = 50)
                self.nameLbl = Label(screen, text = 'Full Name:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.ageLbl = Label(screen, text = 'Age:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.genderLbl = Label(screen, text = 'Gender:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.q1Lbl = Label(screen, text = 'Question 1:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.Ans1Lbl = Label(screen, text = 'Answer 1:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.q2Lbl = Label(screen, text = 'Question 2:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.Ans2Lbl = Label(screen, text = 'Answer 2:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.usernameLbl = Label(screen, text = 'Username:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.passwordLbl = Label(screen, text = 'Password:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.nameEntry = Entry(screen, width = 70)
                self.ageSelect = Listbox(screen, width = 70, height = 1)
                for i in range(16,81):
                    self.ageSelect.insert('end',i)
                self.genderSelect = Listbox(screen, width = 70, height = 3)
                self.genderSelect.insert('end','male')
                self.genderSelect.insert('end','female')
                self.genderSelect.insert('end','others')
                self.q1Select = Listbox(screen, width = 70, height = 5)
                for i in range(len(Account.q1_list)):
                    self.q1Select.insert('end',Account.q1_list[i])
                self.q1AnsEntry = Entry(screen, width = 70)
                self.q2Select = Listbox(screen, width = 70, height = 5)
                for i in range(len(Account.q2_list)):
                    self.q2Select.insert('end',Account.q2_list[i])
                self.q2AnsEntry = Entry(screen, width = 70)
                self.usernameEntry = Entry(screen, width = 70)
                self.passwordEntry = Entry(screen, width = 70, show = '*') 
                self.q1Lbl = Label(screen, text = 'Question 1:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.q2Lbl = Label(screen, text = 'Question 2:', font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 10)
                self.confirmBtn = Button(screen, text = 'CONFIRM', command = confirm)
                self.cnclBtn = Button(screen, text = 'CANCEL', command = go_back)
            def place_widgets():
                self.txt_lbl.pack(fill = 'x', pady = 7)
                self.infoLbl.place(x = 900, y = 125)
                self.nameLbl.place(x = 150, y = 125)
                self.nameEntry.place(x = 300, y = 125)
                self.ageLbl.place(x = 150,y = 165)
                self.ageSelect.place(x = 300,y = 165)
                self.genderLbl.place(x = 150, y = 205)
                self.genderSelect.place(x =300, y = 205)
                self.q1Lbl.place(x = 150, y = 265)
                self.q1Select.place(x = 300, y = 265)
                self.Ans1Lbl.place(x = 150, y = 345)
                self.q1AnsEntry.place(x = 300, y = 355)
                self.q2Lbl.place(x = 150, y = 395)
                self.q2Select.place(x = 300, y = 395)
                self.Ans2Lbl.place(x = 150, y = 475)
                self.q2AnsEntry.place(x = 300, y = 485)
                self.usernameLbl.place(x = 150, y = 525)
                self.usernameEntry.place(x = 300, y = 525)
                self.passwordLbl.place(x = 150, y = 565)
                self.passwordEntry.place(x = 300, y = 565)
                self.confirmBtn.place(x = 450, y = 605)
                self.cnclBtn.place(x = 550, y = 605)
            def checkData(name, ans1, ans2, username, password):
                check = 0
                passwordCheck = re.match('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!%^&*.@#$]).{8,16}', password)
                if not passwordCheck:
                    check = 1
                accountsFile()
                for usernames in accounts:
                    if username == usernames and not username == temp or username == '':
                        check = 2
                accntsFile.close()
                for value in [name, ans1, ans2]:
                    if value == '':
                        check = 3
                return check
            def confirm():
                name = self.nameEntry.get()
                age = self.ageSelect.get('active')
                gender = self.genderSelect.get('active')
                q1 = Account.q1_list.index(self.q1Select.get('active'))
                ans1 = self.q1AnsEntry.get()
                q2 = Account.q2_list.index(self.q2Select.get('active'))
                ans2 = self.q2AnsEntry.get()
                username = self.usernameEntry.get()
                password = self.passwordEntry.get()
                check = checkData(name, ans1, ans2, username, password)
                if check == 0:
                    if username != temp:
                        os.remove(temp+'.dat')
                        accountsFile()
                        accounts.pop(temp)
                        accntsFile.seek(0)
                        pickle.dump(accounts,accntsFile)
                        accntsFile.close()
                    acc = Account(name, age, gender, q1, ans1, q2, ans2, username, password)
                    with open(username+'.dat','rb+') as fo:
                        details = pickle.load(fo)
                        details['diary'] = self.diary
                        fo.seek(0)
                        pickle.dump(details,fo)
                    self.open_account(username)
                    self.username = username
                else:
                    if check == 1:
                        tmb.showerror('Invalid Details','Invalid Password')
                    if check == 2:
                        tmb.showerror('Invalid Details','Username Already Exists')
                    if check == 3:
                        tmb.showerror('Invalid Details','Required Details Missing ')
            screen.destroy()
            defaultScreen()
            create_widgets()
            place_widgets()
        def delAcc():
            choice = tmb.askyesno('Delete Account', 'Are you sure you want to delete your account?')
            if choice == True:
                os.remove(self.username+'.dat')
                accountsFile()
                accounts.pop(self.username)
                pickle.dump(accounts, accntsFile)
                accntsFile.close()
                sign_in()
        def go_back():
            choice = tmb.askyesno('Return', 'Are you sure you want to go back?')
            if choice == True:
                self.open_account(self.username)
        def create_widgets():
            self.changeBtn = Button(screen, command = change, text = 'Change Account Details',font = ('Comic Sans MS',20), bg='white')
            self.delAccBtn = Button(screen,command = delAcc, text = 'Delete Account',font = ('Comic Sans MS',20), bg='white')
            self.backBtn = Button(screen, command = go_back,text = 'Go back',font = ('Comic Sans MS',20), bg='white')
        def place_widgets():
            self.changeBtn.pack(fill = 'x', pady = 5)
            self.delAccBtn.pack(fill = 'x', pady = 5)
            self.backBtn.pack(fill = 'x', pady = 5)
        screen.destroy()
        defaultScreen()
        create_widgets()
        place_widgets()
    def recover_account(self):
        def confirm():
            accountsFile()
            username = self.usernameEntry.get()
            if accounts.has_key(username):
                with open(username+'.dat','rb') as fo:
                    details = pickle.load(fo)
                self.password = details['password']
                rec = details['recovery']
                rec = rec.items()
                self.q1 = rec[0][0]
                self.a1 = rec[0][1]
                self.q2 = rec[1][0]
                self.a2 = rec[1][1]
                def check():
                    a1 = self.a1Entry.get()
                    a2 = self.a2Entry.get()
                    if a1 == self.a1 and a2 == self.a2:
                        tmb.showinfo('Password Recovered','Your password is \'%s\''%self.password)
                        sign_in()
                    else:
                        tmb.showerror('Incorrect Answer','The answers are incorrect, please try again')
                def create_widgets():
                    self.q1Lbl = Label(screen, text = 'Question 1:%s'%self.q1, font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 70)
                    self.q2Lbl = Label(screen, text = 'Question 2:%s'%self.q2, font = ('Comic Sans MS',15), \
                                  bg='black',fg='white', width  = 70)
                    self.a1Entry = Entry(screen, width = 70)
                    self.a2Entry = Entry(screen, width = 70)
                    self.confirmBtn = Button(screen, text = 'confirm', command = check)
                    self.cnclBtn = Button(screen, text = 'cancel', command = cancel)
                def place_widgets():
                    self.q1Lbl.place(x = 300, y = 125)
                    self.a1Entry.place(x = 300, y = 165)
                    self.q2Lbl.place(x = 300, y = 205)
                    self.a2Entry.place(x = 300, y = 245)
                    self.confirmBtn.place(x = 300, y = 305)
                    self.cnclBtn.place(x = 430, y = 305)
                screen.destroy()
                defaultScreen()
                create_widgets()
                place_widgets()
            else:
                tmb.showerror('Invalid Username','Username does not exist')
        def create_widgets():
            self.usernameLbl = Label(screen, text = 'Username:', font = ('Comic Sans MS',15), \
                              bg='black',fg='white', width  = 10)
            self.usernameEntry = Entry(screen, width = 70)
            self.confirmBtn = Button(screen, text = 'CONFIRM', command = confirm)
            self.cnclBtn = Button(screen, text = 'CANCEL', command = cancel)
        def place_widgets():
            self.usernameLbl.place(x = 300, y = 125)
            self.usernameEntry.place(x = 430, y = 125)
            self.confirmBtn.place(x = 450, y = 185)
            self.cnclBtn.place(x = 550, y = 185)
        create_widgets()
        place_widgets()
def cancel():
    '''Function to cancel earlier choice'''
    choice = tmb.askyesno('Cancel','Are you sure you want to cancel?')
    if choice == True:
        screen.destroy()
        main()  
def createAccount():
    '''Funtion to create and manage account'''
    screen.destroy()
    acc = AccountGUI()
    acc.create_account() 
def sign_in():
    '''Function to access existing account'''
    def confirm():
        username = usernameEntry.get()
        password = passwordEntry.get()
        accountsFile()
        if (username not in accounts) or accounts[username] != password:
                tmb.showerror('Invalid Details', 'Username or Password is incorrect')
                accntsFile.close()
        else:
            screen.destroy()
            acc = AccountGUI()
            acc.open_account(username)
    screen.destroy()
    defaultScreen()
    usernameLbl = Label(screen, text = 'Username:', font = ('Comic Sans MS',20), \
                      bg='black',fg='white', width = 10)
    passwordLbl = Label(screen, text = 'Password:', font = ('Comic Sans MS',20), \
                      bg='black',fg='white', width = 10)
    usernameEntry = Entry(screen, width = 70)
    passwordEntry = Entry(screen, width = 70, show = '*')
    confirmBtn = Button(screen, text = 'CONFIRM',font = ('Comic Sans MS',15), command = confirm, width = 9)
    cnclBtn = Button(screen, text = 'CANCEL', font = ('Comic Sans MS',15), command = cancel, width = 8)
    usernameLbl.place(x = 300, y = 125)
    usernameEntry.place(x = 480, y = 135)
    passwordLbl.place(x = 300, y = 185)
    passwordEntry.place(x = 480, y = 195)
    confirmBtn.place(x = 420, y = 245)
    cnclBtn.place(x = 570, y =245)
def recoverAccount():
    '''Function to recover account'''
    screen.destroy()
    acc = AccountGUI()
    acc.recover_account()
def defaultScreen():
    '''Function to create default screen'''
    global screen
    screen = Tk()
    w,h = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.geometry('%dx%d+0+0'%(w,h))
    screen.title('pyDiary')
    title = Label(screen, text = 'pyDiary', font = ('Comic Sans MS',45), bg='blue',\
               fg='green',width = 60, height = 1)
    title.pack()
def accountsFile():
    '''Function to manage account using binary file'''
    global accntsFile, accounts
    accntsFile = file('accounts.dat','rb+')
    accounts = pickle.load(accntsFile)
    accntsFile.seek(0)
def about():
    '''Function to state what the program is about'''
    with open('about.txt','r') as fo:
        abt = fo.read()
        tmb.showinfo('About',abt)
def main():
    accountsFile()
    defaultScreen()
    txt_lbl = Label(screen, text = 'Please choose one of the following options', \
           font = ('Comic Sans MS',10), bg='black',fg='white',width = 60, \
           height = 1)
    crtAccBtn = Button(screen, text = 'Create Account', font = ('Comic Sans MS',20), \
                bg='white', command = createAccount)
    signInBtn = Button(screen, text = 'Sign In', font = ('Comic Sans MS',20), bg='white', \
                command = sign_in)
    rcvrAccBtn = Button(screen, text = 'Recover Account', font = ('Comic Sans MS',20), \
                bg='white', command = recoverAccount)
    abtBtn = Button(screen, text = 'About', font = ('Comic Sans MS',20), \
                bg='white', command = about)
    exitBtn = Button(screen, text = 'Exit', font = ('Comic Sans MS',20), bg='white', \
                command = screen.destroy)
    txt_lbl.pack(fill = 'x', pady = 5)
    crtAccBtn.pack(fill = 'x',pady = 5)
    signInBtn.pack(fill = 'x',pady = 5)
    rcvrAccBtn.pack(fill = 'x',pady = 5)
    abtBtn.pack(fill = 'x',pady = 5)
    exitBtn.pack(fill = 'x',pady = 5)
    screen.mainloop()
main()
