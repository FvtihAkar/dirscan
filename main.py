import requests as req
import threading
import sys
import time


print("[*] Reading wordlist...")
wordlist = open("wordlist.txt","r").read().split("\n")
slist = open("success.txt","a")
flist = open("fails.txt","a")
try:
    url = sys.argv[1]

except:
    print("Please enter a valid url!!!")
    exit()
    
if not url.startswith("http://") and not url.startswith("https://"):
    print(url)
    print("Please enter a valid url!!!")
    exit()

if not url.endswith("/"):
    url += "/"

def writeSuccess(d: str):
    slist.write(f"{d}\n")
    return
def writeFail(d: str):
    flist.write(f"{d}\n")
    return

i=0
def test():
        global url
        global wordlist
        global i
        global slist,flist
        while i < len(wordlist):
            try:
                res = req.get(url+wordlist[i])
            except:
                exit()

            if res.status_code == 404 or res.status_code == 403:
                print(f"[-] {wordlist[i]}")
                writeFail(wordlist[i])
            else:
                print(f"[+] {wordlist[i]} {res.status_code}")
                writeSuccess(wordlist[i])
            i+=1

        flist.close()
        slist.close()
        exit()
    


print("[*] Scan starting...")
for i in range(10):
    t = threading.Thread(target=test)
    t.start()
    time.sleep(0.1)