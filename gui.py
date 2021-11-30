#FINAL FINAL INTERFACE
#importing modules/packages
import tkinter as tk
import keygen as kg
import encryptdecrypt as ed

from tkinter import tix


class user:
    def __init__(self,name,colour,pd):
        self.name=name
        self.colour=colour
        self.pd=pd
        self.kpu=None
        self.kpr=None
        self.newkeypair()
        

    def userhomepg(self):
        
        def checkpq():
            '''check validity of p and q for key generation and
                and perform operations accordingly'''
            
            pu,qu=e1.get(),e2.get() #get values from entry box
            f=open('primenos.txt') #get prime numbers
            content=f.read().split() #list containing primes
            
            if pu==qu=='use random':
                self.newkeypair()
                l4['text']=str(self.kpu)
                l5['text']=str(self.kpr)
            elif pu in content and qu in content and int(pu)*int(qu)>127 and pu!=qu:
                self.newkeypair(pu,qu)
                l4['text']=str(self.kpu)
                l5['text']=str(self.kpr)
                
            else:
                #creating an error window
                err=tk.Toplevel(nw)
                err.title('ERROR')
                err.geometry('250x70')
                err_label=tk.Label(err,text='INVALID INPUT\np and q must be 2 primes\np*q>127\np cannot be equal to q')
                err_label.pack()
                #tk.Message(nw,text='Invalid p and q values. Try again.')

        #creating window definitions
        nw = tix.Toplevel(root)
        nw.state('zoomed')
        nw.title(self.name)
        nw.configure(bg=self.colour)
        nw.geometry('500x400')

        def createbal(widget,msg):
            b=tix.Balloon(nw)
            b.bind_widget(widget,balloonmsg=msg)

        def helpbtn():
            hel=tk.Toplevel(nw)
            hel.title('HELP')
            hel_label=tk.Label(hel,text='''Welcome to your homepage !
Your default key pair has been generated and displayed 

Here's what you can do :

'Keys Available' - Displays the keys available to you

'ENTER P AND Q' - To create new key pair 
Enter unique prime numbers p and q into entry box
or use the randomly generated primes simply by 
clicking the 'CREATE NEW KEY' button

'Write' - To write text message and encrypt using selected key

'Read' - To decrypt using selected key and read text message''')
            hel_label.pack()

        #on clicking help window will open which gives instructions on usage
        help1=tk.Button(nw, text = 'HELP BUTTON\n    (?)',bg='orange',command=helpbtn)
        help1.place(x=980,y=50)
            
        #labels to display keypairs of self
        l1=tk.Label(nw,bg='red',text='YOUR KEY PAIR',font='20')

        l2=tk.Label(nw,bg='green',fg='white',text='Public Key')
        createbal(l2,'Key available to all users')
        
        l3=tk.Label(nw,bg='green',fg='white',text='Private Key')
        createbal(l3,'Key available to only you')
        
        l4=tk.Label(nw,text=str(self.kpu))#user's public key
        l5=tk.Label(nw,text=str(self.kpr))#user's private key

        l1.pack(padx=10)
        l2.place(x=620,y=80)
        l3.place(x=850,y=80)
        l4.place(x=620,y=110)
        l5.place(x=850,y=110)

        #for keys available to user
        keys=['Pr '+self.name+str(self.kpr),'Pu '+userA.name+str(userA.kpu),'Pu '+userB.name+str(userB.kpu),'Pu '+userC.name+str(userC.kpu)]
        variable = tk.StringVar(nw)
        variable.set('Keys Available') # default value
        dropd=tk.OptionMenu(nw,variable,*keys)
        createbal(dropd,'See the keys available to you')
        dropd.pack(pady=10)

        #user enters key
        la=tk.Label(nw,bg='blue',fg='white',text='ENTER P AND Q')
        e1=tk.Entry(nw)
        e1.insert(tk.END,'use random') #default val
        createbal(e1,'Or enter your own prime numbers')
        e2=tk.Entry(nw)
        e2.insert(tk.END,'use random') #default val
        createbal(e2,'Or enter your own prime numbers')
        extralab=tk.Label(nw,bg=self.colour)
        extralab.pack(pady=25)
        la.pack(pady=10)
        e1.pack(pady=5)
        e2.pack(pady=5)
        
        create=tk.Button(nw, text = 'Create new key',bg='pink',command=checkpq)#on clicking button new key gets generated with either random values or user defined values
        createbal(create,'click to create')
        create.pack(pady=10)

        #to write message to someone
        button4 = tk.Button(nw, text = 'WRITE', width = 25,command = self.write)#opens new page where user can write a message
        button4.place(x=680,y=350)
        createbal(button4,'write a message')

        #to read message from someone
        button5 = tk.Button(nw, text = 'READ', width = 25,command = self.read)#opens a page where user can read a message
        button5.place(x=680, y=400)
        createbal(button5,'read a message ')

        #go to previous window
        bexit=tk.Button(nw,text='HOME',fg='white',bg='black',command=nw.destroy)#redirects to login page
        bexit.pack(padx=100,pady=150)
        
    def newkeypair(self,p=0,q=0):
        ''' creates new key pair and assigns to self'''
        e,d,n=kg.main(int(p),int(q))
        self.kpu,self.kpr = (e,n),(d,n)#key pairs for user
        
    def write(self):
        #opening file object
        
        #passw
        nw = tk.Toplevel(root)
        nw.state('zoomed')
        nw.configure(bg=self.colour)

        #dropdown
        l=[self.kpr,userA.kpu,userB.kpu,userC.kpu]
        keys=['Pr '+self.name+str(l[0]),'Pu '+userA.name+str(l[1]),'Pu '+userB.name+str(l[2]),'Pu '+userC.name+str(l[3])]
        variable = tk.StringVar(nw)
        variable.set('Send message using') # default value
        dropd=tk.OptionMenu(nw,variable,*keys)#opens a drop down box showing available keys to the user
        dropd.pack(pady=10)

        #text
        text=tk.Text(nw,height=20,width=50)
        text.pack()

        def getinfo():
            f=open('textmessage.txt','w+')
            msg=text.get('1.0','end')
            k=l[keys.index(variable.get())]  #k==> key
            file_con=ed.encrypt(msg,k)#message gets encrypted
            f.write(str(file_con))#encrypted message gets stored in a file
            f.close()

        #close file
        close_button=tk.Button(nw,text='finish',bg='pink',command=getinfo)
        close_button.pack(pady=20)
        
        #go to previous window
        bexit=tk.Button(nw,text='USER PAGE', fg='white', bg='dark green',command=nw.destroy)
        bexit.pack(padx=100,pady=100)
        
    def read(self):
        
        #window def
        nw = tk.Toplevel(root)
        nw.state('zoomed')
        nw.configure(bg=self.colour)
        button1 = tk.Button(nw, text = 'Public key for '+self.name, width = 25, bg='orange')
        button1.pack(pady=10)

        #opening file object
        la=tk.Label(nw)

        #dropdown
        l=[self.kpr,userA.kpu,userB.kpu,userC.kpu]
        keys=['Pr '+self.name+str(l[0]),'Pu '+userA.name+str(l[1]),'Pu '+userB.name+str(l[2]),'Pu '+userC.name+str(l[3])]
        variable = tk.StringVar(nw)
        variable.set(keys[0]) # default value
        dropd=tk.OptionMenu(nw,variable,*keys)
        dropd.pack(pady=10)


        def decndis():
            f=open('textmessage.txt','r')
            k=l[keys.index(variable.get())]  #k==> key
            file_con=f.read()
            msg=ed.decrypt(file_con[1:-1].split(','),k)
            la['text']=msg#the decrypted message is displayed 
            la.place(x=600,y=150)
            f.close()

        #decrypt button
        close_button=tk.Button(nw,text='Decrypt and Display',bg='pink',command=decndis)
        close_button.pack(pady=10)

        #go to previous window
        bexit=tk.Button(nw,text='USER PAGE',fg='white',bg='dark green',command=nw.destroy)
        bexit.pack(padx=100,pady=100)
        
def open_txt():
    #pass
    text_file = open('Test.txt','r')
    content=text_file.read()
    text.insert(END,content)
    text_file.close()

#user object definitions
userA=user('Alice','light green','a123')
userB=user('Bob','light blue','b123')
userC=user('Oscar','yellow','o123')
user_pd={'Alice':userA,'Bob':userB,'Oscar':userC}

def checklog():
    try:
        if user_pd[e1.get()].pd==e2.get():
            l5.pack_forget() # <=====
            user_pd[e1.get()].userhomepg()#directs to user's page
    except KeyError:
        l5['text']='Invalid username/password'
        l5.pack()

#ROOT WINDOW

root=tix.Tk()
root.title('RSA Encryptor-Decryptor')
root.state('zoomed')
root.configure(bg='pink')
root.geometry('500x400')
l1=tk.Label(text='WELCOME TO RSA ENCRYPTOR-DECRYPTOR',fg='purple',font='20',bg='pink')
l1.pack(pady=10)
l2=tk.Label(text='Please Enter Login Details',fg='green',font='20',bg='pink')
l2.pack(pady=10)
l3=tk.Label(text='Username : ',fg='purple',font='20',bg='pink')
l3.pack()
e1=tk.Entry()
e1.pack(pady=10)
l4=tk.Label(text='Password : ',fg='purple',font='20',bg='pink')
l4.pack()
e2=tk.Entry(show='*')
e2.pack(pady=10)
l5=tk.Label(fg='purple',font='20',bg='pink')

b1=tk.Button(root,text='Log In', width=25,command = checklog)#checks the user and password are matching or not
b1.pack(pady=10)

'''#user buttons
button1=tk.Button(root,text=userA.name,bg=userA.colour, width=25,command = userA.userhomepg)
button1.pack(pady=10)
button2=tk.Button(root,text=userB.name,bg=userB.colour, width=25,command = userB.userhomepg)
button2.pack(pady=10)
button3=tk.Button(root,text=userC.name,bg=userC.colour, width=25,command = userC.userhomepg)
button3.pack(pady=10)
'''
#exit button
bexit=tk.Button(root,text='EXIT',fg='white',bg='black',command=root.destroy)#closes the program
bexit.pack(padx=80,pady=80)

root.mainloop()
