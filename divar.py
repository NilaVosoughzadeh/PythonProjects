print("WELCOME")
print("1-Admin Log In")
print("2-Users")

while True:
    item = input("Choose Item: ")

    #ورود ادمین
    if item == "1":
        username = input("Enter Username:")
        password = input("Enter Password:")
        if username == "admin" and password == "1394":
            print("Admin Pannel: ")
            command = input(">>")
            if command.lower() == "turn off":
                break
        else:
            print("Invalid username or password!")
    
    elif item == "2":
        command = input("What do you want? (Enter [register / login ] & Name & Pass) ").split()
        cmd = command[0]

        if cmd == "register":
            user = command[1]
            password = command[2]
            # خواندن فایل دیتابیس و جداسازی نام های کاربری
            file = open("users.txt","r")
            data = file.read().split()
            file.close()
            usernames = []

            for i in data:
                info = i.split("-")
                usernames.append(info[0])

             #بررسی ثبت نام   
            if user in usernames:
                print("This Username has already taken!")
            else:
                fileUser = open("users.txt","a")
                fileUser.write(f"{user}-{password}\n")
                fileUser.close()
                print("registered successfully!")

        elif cmd == "login":
            username = command[1]
            password = command[2]
            fileLog = open("users.txt","r")
            data = fileLog.read().split()
            fileLog.close()
            users = {}

            for i in data:
                user = i.split("-")
                users[user[0]] = user[1]
            
            if username in users and password == users[username]:
                print(f"{username} Panel:")

                print("1) add_advertise")
                print("2) rem_advertise")
                print("3) list_my_advertise")

                service = input(">> ")

                usersTitle = {}

                #افزودن آگهی
                if service == "1":
                    title = input("Enter title here: ")
                    
                    fileUsers = open("users.txt","r")
                    dataUsers = fileUsers.read().split()
                    fileUsers.close()

                    #بررسی ثبت نام
                    if username not in users:
                        print("invalid username!!!")

                    else:
                        fileAdd = open("advertise.txt" , "r")
                        dataAdd = fileAdd.read().split()
                        fileAdd.close()

                        titles = []

                        #بررسی آگهی
                        for i in dataAdd:
                            titleInfo = i.split("-")
                            titles.append(titleInfo[0])

                        #بررسی تایتل
                        if title in titles:
                            print("invalid title")

                        #ثبت آگهی
                        else:
                                fileUser = open("advertise.txt","a")
                                fileUser.write(f"{username}-{title}\n")
                                fileUser.close()
                                print("posted successfully!")


                #حذف آگهی
                elif service=="2":
                    titleRem=input("Enter the title you want to delete: ").lower()

                    fileUsers = open("users.txt","r")
                    dataUsers = fileUsers.read().splitlines()
                    fileUsers.close()

                    #بررسی ثبت نام
                    if username not in users:
                        print("invalid username!!!")

                    else:
                        filerem = open("advertise.txt" , "r")
                        dataRem = filerem.read().splitlines()
                        filerem.close()

                        found = False
                        remaining_ads = []

                        for line in dataRem:
                            if "-" in line:
                                user , title = line.split("-")
                                user = user.strip().lower()
                                title = title.strip().lower()

                                if user == username.lower() and title == titleRem:
                                    found = True
                                else:
                                    remaining_ads.append(f"{user}-{title}")

                        if found:
                            fileRemove = open("advertise.txt" , "w")
                            for ad in remaining_ads:
                                fileRemove.write(ad + "\n")
                            fileRemove.close()

                            print("removed successfully!")

                        else:
                            print("Access denied!")


                #نمایش آگهی های منتشر شده
                elif service=="3":
                    fileUsers = open("users.txt","r")
                    dataUsers = fileUsers.read().split()
                    fileUsers.close()

                    #بررسی ثبت نام
                    if username not in users:
                        print("invalid username!!!")
                    else:
                        fileUsers = open("advertise.txt","r")
                        dataUsers = fileUsers.read().split()
                        fileUsers.close()
                        
                        for i in dataUsers:
                            list=i.split("-")
                            print(list)

            else:
                print("invalid username")