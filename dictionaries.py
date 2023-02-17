#profile = {}
#profile["username"]="Bena"
#profile["age"]=12
#profile["email"]="benasucks@gmail.com"


#print (profile)
profile={}

def sign_up():
    username= input("Enter username")
    email=input("Enter email")
    password=input("Enter password")
    
    profile["username"]=username
    profile["email"]=email
    profile["password"]=password
sign_up()

def getprofile():
    print(profile)
getprofile()

def changeusername():
    newusername=input("Enter new username")
    profile["username"]= newusername
changeusername()
getprofile()