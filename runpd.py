import os
import datetime
import json
import time
import sys
path = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(path)
os.system("clear")
file = path + "/setting.json"
print("程序将在3秒后启动！Programme will start 3 seconds later!")
time.sleep(3)
try:
    fileR=open(file,"r")
except FileNotFoundError:
    fileW=open(file,"w")
    fileW.close()
    fileR=open(file,"r")
settings=fileR.read()
if settings == "":
    settings = {"language":"","password":"null","vms":[]}
    fileW=open(file,"w")
    fileW.write(json.dumps(settings))
else:
    settings=json.loads(settings)
while True:
    os.system("clear")
    if settings["language"] == "":
        settings["language"] = input("选择你的语言（choose your language）C(hinese)/E(nglish):")
        fileW=open(file,"w")
        fileW.write(json.dumps(settings))
        os.system("clear")
    if settings["language"] == "E":
        if settings["password"] == "null":
            settings["password"] = input("you haven't typed in the admin user's password, type it here(we use it to modify the system date to bypass the pd's active verify system to run the vm):")
            fileW=open(file,"w")
            fileW.write(json.dumps(settings))
            os.system("clear")
        os.system('open -a /Applications/Parallels\ Desktop.app')
        if len(settings["vms"]) == 0:
            vm=input("you have no vms recorded, type your vm's name here(please type accurately and don't type in specialchars or chinese words):")
            settings["vms"].append(vm)
            fileW=open(file,"w")
            fileW.write(json.dumps(settings))
            os.system("clear")
        else:
            while True:
                print("vms:")
                tmp = 1
                for i in settings["vms"]:
                    print(str(tmp)+"、"+i)
                    tmp=tmp+1
                vm=input("choose which vm to run(type in the serial number,if you want to add a new one, type in 'new', if you want to delete one, type in 'delete'):")
                if vm == "new":
                   vm=input("type your new vm's name here(please type accurately and don't type in specialchars or chinese words):")
                   settings["vms"].append(vm)
                   fileW=open(file,"w")
                   fileW.write(json.dumps(settings)) 
                   os.system("clear")
                   break
                elif vm == "delete":
                    delete=input("choose which vm to delete(type in the serial number, delete the vm willn't delete the vm files, it's just make the wrong vm name no longer display):")
                    if int(delete) <= len(settings["vms"]) and int(delete) > 0:
                        del settings["vms"][int(delete)-1]
                        fileW=open(file,"w")
                        fileW.write(json.dumps(settings))
                        os.system("clear")
                    else:
                        print("your input is error, please type again!")
                        time.sleep(5)
                        os.system("clear")
                elif int(vm) <= len(settings["vms"]) and int(vm) > 0:
                    vm = settings["vms"][int(vm)-1]
                    os.system("clear")
                    break
                else:
                   print("your input is error, please type again!")
                   time.sleep(5)
                   os.system("clear")
        d=datetime.datetime.now().strftime('%m%d%H%M%Y%S')
        Mon=d[0]+d[1]
        Day=d[2]+d[3]
        Hour=d[4]+d[5]
        Minu=d[6]+d[7]
        Year=d[8]+d[9]+d[10]+d[11]
        Sec=d[12]+d[13]
        os.system('echo %s | sudo -S %s' % (settings["password"], "date 010100002021.00"))
        print("time-")
        os.system('prlctl start "'+ vm +'"')
        s=datetime.datetime.now().strftime('%S')
        Sec=str(int(Sec)+int(s))
        if int(Sec) >= 60:
            Sec = str(int(Sec) - 60)
            Minu = str(int(Minu) + 1)
        if int(Minu) >= 60:
            Minu = str(int(Minu) - 60)
            Hour = str(int(Hour) + 1)
        if int(Hour) == 24:
            Hour = "00"
        if int(Hour) < 10:
            Hour = "0" + Hour
        if int(Minu) < 10:
            Minu = "0" + Minu
        if int(Sec) < 10:
            Sec = "0" + Sec
        os.system('echo %s | sudo -S %s' % (settings["password"], "date " + Mon + Day + Hour + Minu + Year + "." + Sec))
        print("time+")
        print("Notice if the time didn't return to the correct time automaticlly, please turn it back manually in the perfrance settings.")
        time.sleep(15)
        os.system("clear")
    elif settings["language"] == "C":
        if settings["password"] == "null":
            settings["password"] = input("你还没有输入过电脑管理员账户的密码，请输入（只是为了修改系统时间来绕开pd的激活验证系统）:")
            fileW=open(file,"w")
            fileW.write(json.dumps(settings))
            os.system("clear")
        if len(settings["vms"]) == 0:
            vm=input("你还没有虚拟机名字被记录，请输入你的虚拟机名字（请准确地完全输入名称，请尽量不要使用特殊字符或中文字符）:")
            settings["vms"].append(vm)
            fileW=open(file,"w")
            fileW.write(json.dumps(settings))
            os.system("clear")
        else:
            while True:
                print("vms:")
                tmp = 1
                for i in settings["vms"]:
                    print(str(tmp)+"、"+i)
                    tmp=tmp+1
                vm=input("请输入你想要启动的虚拟机（请输入名字前的序号！如果你想要新建一个名字，请输入”new“，如果你想要删除一个名字，请输入“delete”）:")
                if vm == "new":
                   vm=input("输入您的新虚拟机的名字（请尽量不要使用特殊字符或中文字符）:")
                   settings["vms"].append(vm)
                   fileW=open(file,"w")
                   fileW.write(json.dumps(settings)) 
                   os.system("clear")
                   break
                elif vm == "delete":
                    delete=input("输入你想要删除的虚拟机（输入名字前的序号！删除虚拟机并不会删除虚拟机文件，只是让错误的名字不再显示！）:")
                    if int(delete) <= len(settings["vms"]) and int(delete) > 0:
                        del settings["vms"][int(delete)-1]
                        fileW=open(file,"w")
                        fileW.write(json.dumps(settings))
                        os.system("clear")
                    else:
                        print("输入错误，请重新输入！")
                        time.sleep(5)
                        os.system("clear")
                elif int(vm) <= len(settings["vms"]) and int(vm) > 0:
                    vm = settings["vms"][int(vm)-1]
                    os.system("clear")
                    break
                else:
                   print("输入错误，请重新输入！")
                   time.sleep(5)
                   os.system("clear")
        os.system('open -a /Applications/Parallels\ Desktop.app')
        d=datetime.datetime.now().strftime('%m%d%H%M%Y%S')
        Mon=d[0]+d[1]
        Day=d[2]+d[3]
        Hour=d[4]+d[5]
        Minu=d[6]+d[7]
        Year=d[8]+d[9]+d[10]+d[11]
        Sec=d[12]+d[13]
        os.system('echo %s | sudo -S %s' % (settings["password"], "date 010100002021.00"))
        print("将时间更改到过去")
        os.system('open -a /Applications/Parallels\ Desktop.app')
        os.system('prlctl start "'+ vm +'"')
        s=datetime.datetime.now().strftime('%S')
        Sec=str(int(Sec)+int(s))
        if int(Sec) >= 60:
            Sec = str(int(Sec) - 60)
            Minu = str(int(Minu) + 1)
        if int(Minu) >= 60:
            Minu = str(int(Minu) - 60)
            Hour = str(int(Hour) + 1)
        if int(Hour) == 24:
            Hour = "00"
        if int(Hour) < 10:
            Hour = "0" + Hour
        if int(Minu) < 10:
            Minu = "0" + Minu
        if int(Sec) < 10:
            Sec = "0" + Sec
        os.system('echo %s | sudo -S %s' % (settings["password"], "date " + Mon + Day + Hour + Minu + Year + "." + Sec))
        print("将时间恢复到现在")
        print("如果系统时间没有自动恢复到正确的时间，请手动在系统偏好设置中调回。")
        time.sleep(15)
        os.system("clear")
    else:
        print("输入错误，请重新输入！\n your input is error, please type again!")
        time.sleep(5)
        os.system("clear")