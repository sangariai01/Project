class grandparents:
    def __init__(self,grandpaname,grandmaname,familyname):
        self.gfn=grandpaname
        self.gmn=grandmaname
        self.fn=familyname 
        
    def welcome(self):
        print(self.gfn,self.gmn,self.fn)
        
x=grandparents("Marudhu","Mano","KVM")
x.welcome()

class fam(grandparents):
    def __init__(self, grandpaname, grandmaname, familyname,fathername,mothername):
        self.ftn=fathername
        self.mtn=mothername
        super().__init__(grandpaname, grandmaname, familyname)
        
    def greetings(self):
        print("Hi all..!","I am",self.gfn,"and my wife",self.gmn,"Welcome you all to my",self.fn," family.I introduce my son Mr",self.ftn,"and his wife Mrs",self.mtn)
        
x=fam("Marudhu","Mano","KVM","Sam","Lathu")
x.greetings()
     
class famtree(fam):
    def __init__(self, grandpaname, grandmaname, familyname,fathername,mothername,sonname,daughtername):
        self.sn=sonname
        self.dn=daughtername
        super().__init__(grandpaname, grandmaname, familyname,fathername,mothername)
        
    def intro(self):
        print("Hi all..!","I am",self.gfn,"and my wife",self.gmn,"Welcome you all to my",self.fn," family.I introduce my son Mr",self.ftn,"and his wife Mrs",self.mtn,"and my grandchildrens are Mr.",self.sn,"and Ms.",self.dn)
        
x=famtree("Marudhu","Mano","KVM","Sam","Lathu","San","Mahe")
x.intro()

       