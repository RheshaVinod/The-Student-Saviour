def webBlock():

    import time
    from datetime import datetime as dt

#Path to the host file, redirect to local host, list of websits to block
    host_path = "C:\Windows\System32\drivers\etc"
    redirect = "127.0.0.1"
    website_list = ["www.netflix.com","www.facebook.com","www.youtube.com","www.instagram.com"]
    sh = int(input("enter the start time for your study hour(in hour)"))
    eh =int(input("enter the end time for your study hour(in hour)"))
#Condition
    while True:
    #Check for the current time
        if dt(dt.now().year,dt.now().month,dt.now().day,sh) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,eh):
            print("Study hours")
            file = open(host_path,"r+")
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        else:
            print("fun time!!!")
            file = open(host_path,'r+')
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        time.sleep(2)
