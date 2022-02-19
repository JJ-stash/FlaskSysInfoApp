import pwd

def getUsers():
    user_list = []

    for p in pwd.getpwall():
        user_list.append(p[0])
        
    return user_list