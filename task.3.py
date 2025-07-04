# contact book 
contacts = {}
# 3 contacts
contacts("ali")=" 01123456779"
contacts("oney")= "01012345678"
contacts("essam")= "01213456789"
#print all names 
print("names in contacts book")
for name in contacts:
    print(name)
#search by name 
name = input (" enter name to find phone :")
if name in contacts:
    print("phone number:" , contacts(name))
else:
    print ("not found.")