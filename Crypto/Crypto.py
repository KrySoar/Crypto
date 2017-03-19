from functions import *
import conf

close = False
isFirst = False #TRUE BY DEFAULT
os.system("color C")
while close != True:
    if isFirst:
        mode = input("#type help to list the commands available#\n>")
        isFirst = False
        conf.cls()
    else:
        mode = input(">")
        conf.cls()
        
    if mode == "help":
        with open("help/help.txt","r") as myhelp:
            print(myhelp.read())

    elif mode == "conf":
    	arg = input("Argument>")
    	conf.cls()
    	conf.conf(arg)
    elif mode == "base64":
        mode = input("base64>mode>")
        conf.cls()
        if mode == "encode":
            encodeB64()
        elif mode == "decode":
            decodeB64()
        else:
            print("#type help for help#")
    elif mode == "md5" or mode == "sha" or mode == "sha1" or mode == "sha224" or mode == "sha256" or mode == "sha384" or mode == "sha512" or mode == "md4" or mode == "whirlpool":
        encrypting(mode)
    elif mode == "hash":
        hashlist = {"md5","sha","sha1","sha224","sha256","sha384","sha512","md4","whirlpool"}
        print(hashlist)
    elif mode == "quit":
        exit()
    else:
        print("#type help to list the commands available#\nUnknown Command :{mode} \n".format(mode=mode)) 

