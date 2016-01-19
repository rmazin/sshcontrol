import os, pprint, pwd, crypt

input_list = ['1. Grant Access', '2. Revoke Access'] #List of choices (activate or revoke)
toggle = input("Select an option: " + ' '.join(input_list) + "\n") #choose from list

#print toggle

if (toggle == 1): #if activate access is chosen
    tg = "Grant Access"
    print "You have chosen to ", tg
    #newUser = raw_input("Enter a new username to create and grant access to!")
    newUser = 'deploy'
    newPass = raw_input("Enter a password for your new user!")
    try:
        pwd.getpwnam(newUser) # check if user exists
        print pwd.getpwnam(newUser)
    except KeyError:
        print('User deploy does not exist.')
        print "\n creating user: " + newUser
        encPass = crypt.crypt(newPass,"22") #encrypt password
        os.system("useradd -p "+encPass+" deploy") #create user

    os.system("ssh-keygen -f " + newUser) #create key
    os.system("mv " + newUser + "* ~/.ssh/authorized_keys") #move key to authorized_keys
    print newUser + " has been created and given SSH access!"
else:
    tg = "Revoke Access"
    print "You have chosen to ", tg
    #revokeUser = raw_input("Please enter the username you want to revoke access from!")
    revokeUser = 'deploy'
    os.system("mv ~/.ssh/authorized_keys/" + revokeUser + "* /tmp") #move key from authorized_keys to revoke access
    print "Access for " + revokeUser + " has been revoked!"

