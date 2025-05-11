#library access system
class member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
class Studentmember(member):
    def __init__(self,name,member_id):
        super().__init__(name,member_id)
        self.borrowedbooks=[]
    def borrowedbooks(self,book):
        self.borrowedbooks.append(book)
    def return_book(self,book):
        if book in self.borrowedbooks:
            self.borrowedbooks.remove(book)
    def display(self):
        print(f"{self.name} has been borrowed")

student1=Studentmember("rahul",123)
student1.display()

#drone fleet management
class Device:
    def __init__(self,device):
        self.device=device
class flyer:
    def fly(self):
        print('flying')
class drone(Device,flyer):
    def __init__(self,device,):
        Device.__init__(self,device)
    def capture_image(self):
        print("capturing images")
device1=drone("123")
device1.fly()
device1.capture_image() 

#online learning platform
class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayinfo(self):
        print(f"user name is {self.name}\nuser email id is {self.email}")

class instructer(user):
    def __init__(self, name, email, expertise):
        super().__init__(name, email)
        self.expertise = expertise

    def upload_content(self):
        print(f"{self.name} is uploading content in {self.expertise}")

    def displayinfo(self):
        super().displayinfo()
        print(f"role: Instructer\nExpertise: {self.expertise}")

class coursecreator(user):
    def __init__(self, name, email, tools):
        super().__init__(name, email)
        self.tools = tools

    def createcourse(self):
        print(f"{self.name} is creating course completely\n")

    def displayinfo(self):
        super().displayinfo()
        print(f"role is course creator\nTool used is: {self.tools}")


instructer1 = instructer("rames", "ramesh@email.com", "physics")
instructer1.displayinfo()
instructer1.upload_content()

creater1 = coursecreator("suresh", "suresh@email.com", "google classroom")
creater1.displayinfo()
creater1.createcourse()

#smart home appliance
class appliance:
    def status(self):
        print("generic appliance status")
class fan(appliance):
    def status(self):
        print("fan is on at speed 4")

class light(appliance):
    def status(self):
        print("light is off")
        
class AC(appliance):
    def status(self):
        print("AC is coolin at 17 degrees")

f1=fan()
l1=light()
a1=AC()      
device=[f1,l1,a1]
for devise in device:
    devise.status()

#geometry toolkit
class shaplecalculate:
    def area(self,a,b=None):
        if b is None:
            return 3.14*a*a
        else:
            return a*b
calc=shaplecalculate()
print("circle area=",calc.area(4))
print("rectangle area=",calc.area(3,4))
