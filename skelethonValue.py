import requests,json,time,sys,random,os,argparse,datetime
import colorama, hashlib, binascii
import traceback, random
from colorama import Fore, Back, Style
from random import randint
from datetime import datetime as dtime
colorama.init(autoreset=True)

rcfontcolor = Style.NORMAL+Fore.MAGENTA
rccolor = Style.BRIGHT+Back.WHITE+Fore.BLACK
hijau = Style.BRIGHT+Fore.GREEN
res = Style.RESET_ALL
abu2 = Style.BRIGHT+Fore.WHITE
ungu = Style.BRIGHT+Fore.MAGENTA
hijau2 = Style.NORMAL+Fore.GREEN
red2 = Style.BRIGHT+Fore.RED
red = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
#warna tambahan
blue = "\033[1;36m"
blue2 = "\033[1;36m"
mag = "\033[1;35m"
kun = "\033[1;33m"
bg_mg = '\x1b[1;35;100m'
bg_blu = '\x1b[1;34;100m'
bg_kun = '\x1b[1;33;100m'
bg_ab = '\x1b[1;36;100m'
bg_ab2 = '\x1b[1;36;100m'
bg_rd = '\x1b[1;3;41m'
bg_ij = '\x1b[0;30;42m'
bg_end = '\x1b[0m'
version_sc = "1.7"
with open('config.json', 'r') as myfile:
      data=myfile.read()
obj = json.loads(data)
c = requests.session()
url = "https://www.999doge.com/api/web.aspx"
ua = {
 "Origin": "file://",
 "user-agent": obj["User-Agent"],
 "Content-type": "application/x-www-form-urlencoded",
 "Accept": "*/*",
 "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
 "X-Requested-With": "com.reland.relandicebot"
}
os.system('cls' if os.name=='nt' else 'clear')
try:
   r = c.get("https://pastebin.com/raw/aNHuMLzQ", headers={"user-agent": obj["User-Agent"]})
   db = json.loads(r.text)["database"]
   versi = db["version"]
   tipe_script = db["tipe script"].upper()
except:
    print(red+"Database error, Please try again later!")
    sys.exit()
banner = """\033[1;36m                                                                      
             88              88          88  88                       
     .d8888b.88  .dP .d8888b.88.d8888b.d8888P88d888b..d8888b.88d888b. 
     Y8ooooo.88888"  88ooood88888ooood8  88  88'  `8888'  `8888'  `88 
      8888  `8b.88.  ...8888.  ...  88  88    8888.  .8888    88 
     `88888P'dP   `YP`88888P'dP`88888P'  dP  dP    dP`88888P'dP    dP                                                                    
     \033[1;34m≠=============================#ViP#=================================≠"""
print(banner)

if version_sc == versi:
   pass
else:
    print(kuning + "Old Version, Please update version!")
    print(hijau+"Update Version: V"+versi)
    sys.exit()

def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;30m#\033[1;32mRelogin in \033[1;0m{:2d} \033[1;32mseconds".format(remaining))
       sys.stdout.flush()
       time.sleep(1)
    sys.stdout.write("                                             ")

def verif(db):
    if db["tipe script"] == "premium":
            stuser = 0
            for usersc in db["user premium"]:
                if usersc.lower() == obj["Account"]["Username"].lower():
                    stuser = 0
                    break
            if stuser == 1:
                print(hijau+"Hallo, "+obj["Account"]["Username"])
                print(yellow + "Silahkan lakukan aktivasi akun!")
                print(yellow + "contact tele: "+ hijau +"@junsnack")
                sys.exit()
            else:
                print(hijau+"  Selamat Datang, "+obj["Account"]["Username"]+" Terimakasih Atas Donasinya")
                print(kuning+"    Selamat Bermain dan Ingat!! WD lah saat profit!!")
    else:
        print(hijau + "Welcome to 999dicebot Trial Version!")
        print("\033[1;34m≠==================================================≠")

def cekerjump(data):
    datanew = ['test']
    for x in data:
        if x["Toggle"].lower() == "on":
            datanew.append(x)
    datanew.pop(0)
    return datanew

def indodax(coin):
    
    try:
        if coin == "DOGE" or coin == "doge" or coin == "Doge":
            pair = "doge_idr"
        elif coin == "LTC" or coin == "ltc" or coin == "Ltc":
            pair = "ltc_idr"
        else:
            pair = "eth_idr"
            
        url = 'https://indodax.com/api/' + str(pair) + '/ticker'

        indx = requests.get(url)
        jsindx = json.loads(indx.text)
        pricepair = int(jsindx["ticker"]["last"])
    except:
        if coin == "DOGE" or coin == "doge" or coin == "Doge":
            coinpair = "doge"
        elif coin == "LTC" or coin == "ltc" or coin == "Ltc":
            coinpair = "ltc"
        else:
            coinpair = "eth"
            
        url = "https://beducode-price.herokuapp.com/price/" + str(coinpair)

        price = c.get(url)
        data = json.loads(price.text)
        pricepair = data["last"]

    return pricepair

# FORMAT VALUE TO IDR

def rupiah_format(angka):
    return 'Rp ' + '{:0,.2f}'.format(angka)

def konvert(persen, taruhan):
    global high
    global low
    if taruhan.lower() == "low" or taruhan.lower() == "lo":
        low = 0;
        high = int(int(float(persen) * 10000) - 1)
    else:
        low = int(1000000 - int(float(persen) * 10000))
        high = 999999

def rev(num):
    if (len(num) < 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        gg = num.rstrip('0')
        km  = int(8) - (len(gg))
        a = '0' * km
        result = ("0."+gg+abu2+a+res)
    if (len(num) == 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        gg = num.rstrip('0')
        km  = int(8) - (len(gg))
        a = '0' * km
        result = ("0."+gg+abu2+a+res)
    else:
        len_num = len(num)
        end = num[-8:]
        first = num[:len_num-8]
        gg = end.rstrip('0')
        km  = int(8) - (len(gg))
        a = '0' * km
        result = (first+"."+gg+abu2+a+res)
    return (result)

def hitung(bal, bet, iflose):
  print("\033[1;34m=============== Calculator Betting =================")
  print(hijau+"Balance"+abu2+": "+res+bal+hijau+"\nBase Bet"+abu2+": "+res+bet+hijau+"\nIf Lose"+abu2+": "+res+iflose+"\n")
  balance = int(float(bal)*(10 ** 8))
  balance = int(balance)
  basebet = int(float(bet)*(10 ** 8))
  balance -= int(basebet)
  balance = int(balance)
  prof = 0
  no = 1
  while True:
      prof += basebet
      prof = int(prof)
      print(ungu+"["+res+str(no)+ungu+"] "+res+str(rev(str(basebet))) +red2+ " Lose -"+str(rev(str(prof)))+res+ " Balance " +blue2+ str(rev(str(balance))))
      if (balance <= basebet):
          sys.exit()
      basebet *= float(iflose)
      basebet = int(basebet)
      balance -= int(basebet)
      balance = int(balance)
      no += 1

def cektime(stime, etime):
    ctime = etime - stime
    restime = datetime.timedelta(seconds=ctime)
    return str(restime).split(".")[0]

def resultbet(win,bet):
    if 1 <= win:
        cek = hijau2+" "+str(bet)
    else:
        cek = red2+"-"+str(bet)
    return (cek)

def cekhilo(win,hilo):
    if hilo.lower() == "lo" or hilo.lower() == "low":
        hilo = "L"
    if hilo.lower() == "hi":
        hilo = "H"
    if 1 <= win:
        cek = bg_ij+" "+str(hilo)
    else:
        cek = bg_rd+" "+str(hilo)
    return (cek)

def register(user,sandi):
    data = {
        "a": "CreateAccount",
        "Key": "7cad3bf8b2ad41f39e94dea3986d5d8f"
    }
    r1 = c.post(url,headers=ua,data=data)
    sesi = json.loads(r1.text)["SessionCookie"]
    data = {
        "a": "CreateUser",
        "s": sesi,
        "Username": user,
        "Password": sandi
    }
    r1 = c.post(url,headers=ua,data=data)
    jsn = json.loads(r1.text)
    try:
        if jsn['success'] == 1:
            print(hijau + "Register success!")
    except:
        print(red + "Username Already Exists!")

def login(username, password):
    if obj["Account"]["2FA"].lower() == "on":
        otp = input("Input Google Autenticator (2FA): ")
    else:
        otp = ""
    r = c.get(url,headers=ua,data={"a": "Login","Key": "8b4993006b434c2a859b9c5660655974","Username": username,"Password": password,"Totp": otp})
    js = json.loads(r.text)
    try:
        if js['LoginInvalid'] == 1:
            print (red+"Failed to login, cek username and password!")
            sys.exit()
    except KeyError:
        verif(db)
        return (js)

def deposite():
    data = {
        "a": "GetDepositAddress",
        "s": js["SessionCookie"],
        "Currency": obj["Currency"].lower(),
    }
    r1 = c.post(url,headers=ua,data=data)
    jsn = json.loads(r1.text)["Address"]
    return (jsn)

def withdraw(amount, wallet, js):
    if obj["Account"]["2FA"].lower() == "on":
        otp = input("Input Google Autenticator (2FA): ")
    else:
        otp = ""
    wd = {
        "a": "Withdraw",
        "s": js["SessionCookie"],
        "Amount": int(float(amount)*(10 ** 8)),
        "Address": wallet,
        "Totp": otp,
        "Currency": obj["Currency"].lower()
    }
    r1 = c.post(url,headers=ua,data=wd)
    return (json.loads(r1.text))

def history(jenis):
    data = {
        "a": jenis,
        "s": js["SessionCookie"],
        "Token": ""
    }
    r1 = c.post(url,headers=ua,data=data)
    return (json.loads(r1.text))

def dice():
   js = login(obj["Account"]["Username"], obj["Account"]["Password"])
   if str(getbetset).lower() == "auto":
       if 2 <= len(obj["Config"]):
           print(red + "          Auto Change Betset: "+hijau+"Switch ON")
           autobetset = "on"
           nobetset = 0
           setbetset = obj["Config"][nobetset]
       else:
           print(yellow + "Note: You must have more than 1 betset to activate this feature!")
           print(yellow + "Auto Change Betset: "+red+"Switch OFF")
           autobetset = "off"
           nobetset = 0
           setbetset = obj["Config"][0]
   else:
       autobetset = "off"
       try:
           nobetset = int(getbetset)
           setbetset = obj["Config"][nobetset]
       except:
           print(red+"Bet Set Not Found!")
           sys.exit()
   data = {
      "a": "GetBalance",
      "s": js["SessionCookie"],
      "Currency": obj["Currency"].lower(),
      "ProtocolVersion": "2"
   }
   r1 = c.post(url,headers=ua,data=data)
   jsn = json.loads(r1.text)
   startbal = jsn["Balance"]
   print(hijau+"\n          Balance Awal Anda :",res+str((float(int(startbal))/(10 ** 8))))
   print("            ↪️ \033[1;36mStart Bet Set ["+res+setbetset["Name Bet Set"]+"\033[1;36m]")
   basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
   menit = int(dtime.now().strftime('%M')) + int(obj["Auto Change Betset"]["Interval"])
   cc = float(setbetset["Chance"])
   hilo = "hi"
   cseed = 0
   ised = red + "OFF"
   stseed = 0
   lose = 0
   win = 0
   ls = 0
   ws = 0
   ls_ci = 0
   ls_bet = 0
   wn_bet = 0
   wn_res = 0
   ls_res = 0
   res_profit = 0
   prof_betset = 0
   prof = 0
   ls_hilo = 0
   ls_cbet = 0
   wn_cbet = 0
   wn_hilo = 0
   hilo_bet = 0
   roll = 1
   roll_jump = 1
   cjump = 0
   m_ranbet = 0
   switchbet = 0
   spin = 0
   awaltime = time.time()
   
   try:
       while True:
       	#Auto Change Betset(CLEAR)
           if autobetset == "on":
               if (int(obj["Auto Change Betset"]["Interval"])) !=0:
                   waktu = dtime.now().strftime('%M')
                   if int(waktu) > int(menit-1):
                       menit = int(dtime.now().strftime('%M')) + int(obj["Auto Change Betset"]["Interval"])
                       if len(obj["Config"]) == int(nobetset)+1:
                           nobetset = 0
                       else:
                           nobetset +=1
                       setbetset = obj["Config"][nobetset]
                       switchbet = 1 
                       if obj["Auto Change Betset"]["Reset to Base Bet"].lower() == "on":
                           basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
                       sys.stdout.write("\r                                                        \r")
                       print("         🔄 \033[1;36mChange Bet Set ["+res+setbetset["Name Bet Set"]+"\033[1;36m]")
               if int(float(obj["Auto Change Betset"]["If Profit"])*(10 ** 8)) != 0:
                   try:
                       prof_betset += int(jsn["PayOut"]) - int(initbase)
                       prof_betset = int(prof_betset)
                   except KeyError:
                       prof_betset = 0
                   if int(float(obj["Auto Change Betset"]["If Profit"])*(10 ** 8)) <= prof_betset:
                       if len(obj["Config"]) == int(nobetset)+1:
                           nobetset = 0
                       else:
                           nobetset +=1
                       setbetset = obj["Config"][nobetset]
                       prof_betset = 0
                       switchbet = 1
                       if obj["Auto Change Betset"]["Reset to Base Bet"].lower() == "on":
                           basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
                       sys.stdout.write("\r                                                        \r")
                       print("         🔄 \033[1;36mChange Bet Set ["+res+setbetset["Name Bet Set"]+"\033[1;36m]")
               if int(obj["Auto Change Betset"]["If Lose Streak"]) != 0:
                   if int(obj["Auto Change Betset"]["If Lose Streak"]) <= ls_cbet:
                       if len(obj["Config"]) == int(nobetset)+1:
                           nobetset = 0
                       else:
                           nobetset +=1
                       setbetset = obj["Config"][nobetset]
                       ls_cbet = 0
                       switchbet = 1
                       if obj["Auto Change Betset"]["Reset to Base Bet"].lower() == "on":
                           basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
                       sys.stdout.write("\r                                                        \r")
                       print("         🔄 \033[1;36mChange Bet Set ["+res+setbetset["Name Bet Set"]+"\033[1;36m]")
               if int(obj["Auto Change Betset"]["If Win Streak"]) != 0:
                   if int(obj["Auto Change Betset"]["If Win Streak"]) <= wn_cbet:
                       if len(obj["Config"]) == int(nobetset)+1:
                           nobetset = 0
                       else:
                           nobetset +=1
                       setbetset = obj["Config"][nobetset]
                       wn_cbet = 0
                       switchbet = 1
                       if obj["Auto Change Betset"]["Reset to Base Bet"].lower() == "on":
                           basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
                       sys.stdout.write("\r                                                        \r")
                       print("         🔄 \033[1;36mChange Bet Set ["+res+setbetset["Name Bet Set"]+"\033[1;36m]")
           #Random Chance(CLEAR)
           if setbetset["Random Chance"]["Toggle"].lower() == "on":
               if int(float(setbetset["Random Chance"]["If Base Bet"])*(10 ** 8)) != 0:
                   if int(float(setbetset["Random Chance"]["If Base Bet"])*(10 ** 8)) <= basebet:
                       cc = round(random.uniform(float(setbetset["Random Chance"]["Min"]),float(setbetset["Random Chance"]["Max"])),2)
                       rcc = "on"
                   else:
                       if int(setbetset["Random Chance"]["Reset Chance"]) !=0:
                           rcc = "off"
                           cc = float(setbetset["Chance"])
                       else:
                           rcc = "off"
               else:
                   rcc = "on"
                   cc = round(random.uniform(float(setbetset["Random Chance"]["Min"]),float(setbetset["Random Chance"]["Max"])),2)
               konvert(cc,str(hilo))
           else:
               rcc = "off"
               cc = float(setbetset["Chance"])
               konvert(cc,str(hilo))
           data = {
               "a": "PlaceBet",
              "s": js["SessionCookie"],
              "PayIn": basebet,
              "Low": low,
              "High": high,
              "ClientSeed": cseed,
              "Currency": obj["Currency"].lower(),
              "ProtocolVersion": "2"
           }
           r1 = c.post(url,headers=ua,data=data)
           jsn = json.loads(r1.text)
           initbase = basebet
           hilo_bet +=1
           #filters hasil beting
           if int(jsn["PayOut"]) != 0:
               win +=1
               lose = 0
               ls_ci = 0
               ls_bet = 0
               wn_bet +=1
               wn_res +=1
               ls_res = 0
               ls_cbet = 0
               wn_cbet +=1 
           else:
               win = 0
               lose +=1
               ls_ci +=1
               ls_bet +=1
               wn_bet = 0
               wn_res = 0
               ls_res +=1
               ls_cbet +=1
               wn_cbet = 0
           #analisa lose streak & win streak
           if win > ws:
               ws += 1
           if lose > ls:
               ls += 1
           prof = jsn["StartingBalance"]+int(jsn["PayOut"])-int(basebet)-startbal
           if 0 <= int(prof):
               tprof = prof
           else:
               tprof = str(prof).replace("-", "")
           finalbal = int(jsn["StartingBalance"]) + int(jsn["PayOut"]) - int(basebet)
           marketidx = indodax(obj["Currency"].lower())
           lastprice = marketidx
           finalbal2 = float(int(finalbal))/(100000000)
           finalbal3 = float(int(tprof))/(100000000)
           wd2 = rupiah_format(lastprice * finalbal3)
           wd = rupiah_format(lastprice * finalbal2)
           if prof > 0:
               
               if rcc == "on":
                   print (cekhilo(win, hilo)+" "+'\x1b[0m'+"|"+resultbet(win,str(rev(str(basebet))))+"|","|"+"Profit",hijau2+str(str(wd2))+"|","|"+"Balance",kun+str(rev(str(finalbal)))+"|"+blue2+"Total"+": "+ str(str(wd)))
               else:
                   print (cekhilo(win, hilo)+" "+'\x1b[0m'+"|"+resultbet(win,str(rev(str(basebet))))+"|","|"+"Profit",hijau2+str(str(wd2))+"|","|"+"Balance",kun+str(rev(str(finalbal)))+"|"+blue2+"Total" +": "+ str(str(wd)))
           else:
    
               if rcc == "on":
                   print (cekhilo(win, hilo)+" "+'\x1b[0m'+"|"+resultbet(win,str(rev(str(basebet))))+"|","|"+" Lose",red2+"-"+str(str(wd2))+"|","|"+"Balance",kun+str(rev(str(finalbal)))+"|"+blue2+"Total"+ ": "+ str(str(wd)))
               else:
                   print (cekhilo(win, hilo)+" "+'\x1b[0m'+"|"+resultbet(win,str(rev(str(basebet))))+"|","|"+" Lose",red2+"-"+str(str(wd2))+"|","|"+"Balance",kun+str(rev(str(finalbal)))+"|"+blue2+"Total"+ ": "+ str(str(wd)))
           presentase = round(int(prof) / int(startbal)*100,3)
           if presentase <= 0:
               presentase_pr = bg_rd+" Profit "+str(presentase)+"%"+bg_end
           if presentase >= 0:
               presentase_pr = bg_ij+" Profit "+str(presentase)+"%"+bg_end
           if rcc == "on":
               sys.stdout.write(bg_ab2+" "+cektime(awaltime, time.time())+" "+bg_end+" "+bg_ij+"W"+str(ws)+" "+bg_end+" "+bg_rd+"L"+str(ls)+" "+bg_end+" "+bg_ab2+" R: "+str(roll)+" "+bg_end+" "+presentase_pr+bg_end+" "+rccolor +rcfontcolor+"Harga koin : "+str(rupiah_format(marketidx))+bg_end+" "+"\r")
           else:
               sys.stdout.write(bg_ab2+" "+cektime(awaltime, time.time())+" "+bg_end+" "+bg_ij+"W"+str(ws)+" "+bg_end+" "+bg_rd+"L"+str(ls)+" "+bg_end+" "+bg_ab2+" "+str(float(cc))+" "+bg_end+" "+presentase_pr+bg_end+" "+rccolor + rcfontcolor+"Harga koin : "+str(rupiah_format(marketidx))+bg_end+" "+"\r")
           #ON / OFF Client Seed(CLEAR)
           if obj["Client Seed"]["Toggle"].lower() == "on":
               if obj["Client Seed"]["If Random Chance"].lower() == "on":
                   if rcc == "on":
                       if 1 <= stseed:
                           ised = red + "OFF"
                           cseed = 0
                           stseed = 0
                       else:
                           ised = hijau + "ON"
                           cseed = randint(0,999999)
                           stseed +=1
                   else:
                       stseed = 0
                       ised = red + "OFF"
                       cseed = 0
               if int(float(obj["Client Seed"]["If Base Bet"])*(10 ** 8)) != 0:
               	if int(float(obj["Client Seed"]["If Base Bet"])*(10 ** 8)) <= basebet:
               	    if 1 <= stseed:
                           ised = red + "OFF"
                           cseed = 0
                           stseed = 0
               	    else:
                           ised = hijau + "ON"
                           cseed = randint(0,999999)
                           stseed +=1
               	else:
                       stseed = 0
                       ised = red + "OFF"
                       cseed = 0
           else:
               stseed = 0
               ised = red + "OFF"
               cseed = 0
           #mode jump if lose
           datjump = cekerjump(setbetset["Jump If Lose"])
           if 1 <= len(datjump):
               if switchbet == 1:
                   roll_jump = 1
                   switchbet = 0
               if roll_jump == 1:
                   try:
                       bacajump = datjump[int(cjump)]
                   except IndexError:
                       m_ranbet = 1
                       cjump = 0
                       bacajump = datjump[int(cjump)]
               if setbetset["Repeat Jump If Lose"].lower() == "on":
                   if int(float(setbetset["Base Bet"])*(10 ** 8)) == basebet:
                       roll_jump = 1
                       cjump = 0
                       m_ranbet = 0
               if m_ranbet == 1:
                   if int(float(setbetset["Base Bet"])*(10 ** 8)) == basebet:
                       roll_jump = 1
                       cjump = 0
                       m_ranbet = 0
               else:
                   if int(bacajump["Number Of Bets"]) <= roll_jump:
                       roll_jump = 1
                       if len(datjump) == int(cjump)+1:
                           cjump = 0
                           m_ranbet = 1
                       else:
                           m_ranbet = 0
                           cjump +=1
                   else:
                       roll_jump +=1
               try:
                   bacajump = datjump[int(cjump)]
               except IndexError:
                   m_ranbet = 1
                   cjump = 0
                   bacajump = datjump[int(cjump)]
               if m_ranbet == 0:
                   basebet = int(float(setbetset["Base Bet"])*(10 ** 8)) * float(bacajump["If Lose"])
                   basebet = int(basebet)
               else:
                   basebet *= float(setbetset["If Lose"])
                   basebet = int(basebet)
           else:
               #perkalian base bet if lose(CLEAR)
               if float(setbetset["If Lose"]) != 0:
                   if ls_bet != 0:
                       basebet *= float(setbetset["If Lose"])
                       basebet = int(basebet)
                       ls_bet = 0
          #perkalian base bet if win(CLEAR)
           if float(setbetset["If Win"]) != 0:
               if wn_bet !=0:
                  basebet *= float((setbetset["If Win"]))
                  basebet = int(basebet)
                  wn_bet = 0
           #variable riset jika sampai maximal bet(CLEAR)
           if int(float(setbetset["Max Bet"])*(10 ** 8)) != 0:
               if int(float(setbetset["Max Bet"])*(10 ** 8)) <= basebet:
                   basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
           #variable reset if win streak(CLEAR)
           if int(setbetset["Reset If Win Streak"]) != 0:
               if int(setbetset["Reset If Win Streak"]) <= wn_res:
                   basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
                   wn_res = 0
           #variable reset if lose streak(CLEAR)
           if int(setbetset["Reset If Lose Streak"]) != 0:
               if int(setbetset["Reset If Lose Streak"]) <= ls_res:
                   basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
                   ls_res = 0
           #variable reset if profit (CLEAR)
           if int(float(setbetset["Reset If Profit"])*(10 ** 8)) != 0:
               res_profit += int(jsn["PayOut"]) - int(initbase)
               res_profit = int(res_profit)
               if int(float(setbetset["Reset If Profit"])*(10 ** 8)) <= res_profit:
                 basebet = int(float(setbetset["Base Bet"])*(10 ** 8))
                 res_profit = 0
           #Stop If Base Bet > Final Balance
           if int(basebet) > int(finalbal):
               print ("\n" + '\x1b[0;30;100m'+" "*18+"NO MORE BALANCE"+" "*18+'\x1b[0m')
               sys.exit()
           #Analisa HI/LOW bet
           if setbetset["Bet"]["Hi / Low"]["Toggle"].lower() == "on":
               if setbetset["Bet"]["Hi / Low"]["Random"].lower() == "on":
                   hilo = random.choice(["hi","low"])
               else:
                   if win !=0:
                       wn_hilo += 1
                       ls_hilo = 0
                   else:
                       ls_hilo += 1
                       wn_hilo = 0
                   if int(setbetset["Bet"]["Hi / Low"]["If Bets"]) !=0:
                       if int(setbetset["Bet"]["Hi / Low"]["If Bets"]) <= hilo_bet: 
                           if hilo.lower() == "hi":
                               hilo = "lo"
                           else:
                               hilo = "hi"
                           hilo_bet = 0
                   if int(setbetset["Bet"]["Hi / Low"]["If Win Streak"]) !=0:
                       if int(setbetset["Bet"]["Hi / Low"]["If Win Streak"]) <= wn_hilo:
                           wn_hilo = 0
                           if hilo.lower() == "hi":
                               hilo = "lo"
                           else:
                               hilo = "hi"
                   if int(setbetset["Bet"]["Hi / Low"]["If Lose Streak"]) !=0:
                       if int(setbetset["Bet"]["Hi / Low"]["If Lose Streak"]) <= ls_hilo:
                           ls_hilo = 0;
                           if hilo.lower() == "hi":
                               hilo = "lo"
                           else:
                               hilo = "hi"
           else:
               hilo = setbetset["Bet"]["Bet"]
           #Stop If Target Profit(CLEAR)
           if int(float(obj["Target Profit"]["Target Profit"])*(10 ** 8)) != 0:
               if int(float(obj["Target Profit"]["Target Profit"])*(10 ** 8)) <= prof:
                   if obj["Target Profit"]["Relogin If Target Profit"]["Toggle"].lower() == "on":
                       tunggu(int(obj["Target Profit"]["Relogin If Target Profit"]["Interval"]))
                       os.system('cls' if os.name=='nt' else 'clear')
                       print(banner)
                       prof = 0
                       startbal = finalbal
                   else:
                       print (hijau+"\nYay.! \nProfit Mencapai Target.....!\n"+hijau+"Profit "+res+str(rev(str(prof))))
                       sys.exit()
           #Stop If Target Balance(CLEAR)
           if int(float(obj["Target Balance"])*(10 ** 8)) != 0:
               if int(float(obj["Target Balance"])*(10 ** 8)) <= finalbal:
                   print (hijau+"\nYay.! \nBalance Mencapai Target.....!\n"+hijau+"Balance "+res+str(rev(str(finalbal))))
                   sys.exit()
           #Stop If Target Lose(CLEAR)
           if int(float(obj["Target Lose"])*(10 ** 8)) != 0:
               if int(str(prof).find('-')) == 0:
                   targetlose = int(str(prof).replace("-", ""))
               else:
                   targetlose = 0
               if int(float(obj["Target Lose"])*(10 ** 8)) <= targetlose:
                   print (red2+"\nLose Target....!")
                   sys.exit()
            #Fitur Cut Lose
           if obj["Cut Lose"].lower() == "on":
               if int(str(prof).find('-')) == 0:
                   cutlose = int(str(prof).replace("-", ""))
               else:
                   cutlose = 0
               if round(int(startbal)/2) <= int(cutlose+basebet):
                   print(yellow+"Cutlose Bet"+abu2+": "+res+str(rev(str(basebet))),yellow+"If You Lose Betting: "+red+"-"+str(rev(str(basebet+cutlose))))
                   pilih = input(yellow+"Continue betting (y/n) => "+res)
                   if pilih.lower() == "y":
                       pass
                   else:
                       sys.exit()
           if obj["Auto Wd"]["Toggle"].lower() == "on":
               if int(float(obj["Auto Wd"]["If Balance"])*(10 ** 8)) <= finalbal:
                   wd = withdraw(obj["Auto Wd"]["Amount"], obj["Auto Wd"]["Wallet Address"], js)
                   sys.stdout.write("\r                                                    \r")
                   print ("Withdraw "+str(rev(str(wd["Pending"]))) + " " + str(obj["Currency"]).upper())
                   finalbal = int(finalbal) - int(float(obj["Auto Wd"]["Amount"])*(10 ** 8))
                   startbal = int(finalbal)
                   prof = 0
           roll +=1
           time.sleep(float(setbetset["Interval"]) / 1000)
   except KeyError:
        print ('\x1b[0;30;100m'+" "*12+"INSUFFICIENT BALANCE!"+" "*18+'\x1b[0m')
        sys.exit()
   except KeyboardInterrupt:
        print ('\x1b[0;30;100m'+" "*12+"BETTING STOPED!"+" "*18+'\x1b[0m')
        sys.exit()
#    except:
#        traceback.print_exc() print error

try:
    if int(sys.argv[1].find('-c')) == 0:
        parser = argparse.ArgumentParser(description='999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risk')
        parser.add_argument(
            '-c','--betset',
            default=0,
            help='Enter Your Betset Number (default: 0)'
        )
        getbetset = parser.parse_args().betset
        dice()
    elif int(sys.argv[1].find('-a')) == 0:
        print(hijau + "Your Key: "+res+getdeviceid())
        print(yellow + "Silahkan lakukan aktivasi device!\nUntuk mengaktifkan difitur multiakun!")
        print(yellow + "contact tele: "+ hijau +"@junsnack")
        sys.exit()
    elif int(sys.argv[1].find('-r')) == 0:
        register(sys.argv[2],sys.argv[3])
    elif int(sys.argv[1].find('-kal')) == 0:
        hitung(sys.argv[2],sys.argv[3],sys.argv[4])
    elif int(sys.argv[1].find('-d')) == 0:
        try:
           if str(sys.argv[2]).lower() == "history":
                js = login(obj["Account"]["Username"], obj["Account"]["Password"])
                his = history("GetDeposits")
                print("\033[1;34m=================="+blue+" History Deposite \033[1;34m================")
                for dat_depo in his['Deposits']:
                    print(blue+"Wallet"+red+": "+res+dat_depo["Address"])
                    print(blue+"Amount"+red+": "+res+str(rev(str(dat_depo["Value"]))))
                    print(blue+"Transaction Hash"+red+": "+res+dat_depo['TransactionHash'])
                    print(blue+"Date"+red+": "+res+dat_depo['Date'])
                    print(blue+"Currency"+red+": "+res+dat_depo['Currency'].upper())
                    print("\033[1;34m=====================================================")
           else:
               print(hijau + "History Withdrawal" +abu2 + ": " + res + str(sys.argv[0]) + " -w history")
               sys.exit()
        except IndexError:
            js = login(obj["Account"]["Username"], obj["Account"]["Password"])
            getaddress = deposite()
            print(hijau + "Wallet Deposite" + abu2 + ": " + res + str(getaddress) + hijau + "\nNote" + abu2 + ": " + res + "Send " + str(obj["Currency"]).upper() + " Only!")
            sys.exit()
    elif int(sys.argv[1].find('-w')) == 0:
        if str(sys.argv[2]).lower() == "history":
            js = login(obj["Account"]["Username"], obj["Account"]["Password"])
            his = history("GetWithdrawals")
            print("\033[1;34m==============="+blue+" Histrory Withdrawal "+hijau+"=================")
            for dat_wd in his['Withdrawals']:
                print(blue+"Wallet"+red+": "+res+dat_wd["Address"])
                print(blue+"Amount"+red+": "+res+str(rev(str(dat_wd["Value"]))))
                print(blue+"Fee"+red+": "+res+str(rev(str(dat_wd["Fee"]))))
                print(blue+"Transaction Hash"+red+": "+res+dat_wd['TransactionHash'])
                print(blue+"Requested"+red+": "+res+dat_wd['Requested'])
                print(blue+"Completed"+red+": "+res+dat_wd['Completed'])
                print(blue+"Currency"+red+": "+res+dat_wd['Currency'].upper())
                print("\033[1;34m=====================================================")
            sys.exit()
        try:
            js = login(obj["Account"]["Username"], obj["Account"]["Password"])
            wd = withdraw(sys.argv[2],sys.argv[3],js)
            print (hijau+"Withdrawal request is sent!")
            print (hijau+"Amount"+abu2+": "+str(rev(str(wd["Pending"]))) + " " + str(obj["Currency"]).upper())
            print (hijau+"Wallet"+abu2+": "+str(sys.argv[3]))
            print (hijau+"Status"+abu2+": "+yellow+"Pending")
        except IndexError:
            print(hijau + "Withdraw" +abu2 + ": " + res + str(sys.argv[0]) + " -w amount wallet")
            sys.exit()
    elif int(sys.argv[1].find('-help')) == 0:
        print(hijau + "Help:")
        print(hijau + "Create Account" +abu2 + ": " + res + str(sys.argv[0]) + " -r username password")
        print(hijau + "Auto Change Betset" +abu2 + ": " + res + str(sys.argv[0]) + " -c auto")
        print(hijau + "Betting" +abu2 + ": " + res + str(sys.argv[0]) + " -c nobetset")
        print(hijau + "Deposite" +abu2 + ": " + res + str(sys.argv[0]) + " -d")
        print(hijau + "Withdraw" +abu2 + ": " + res + str(sys.argv[0]) + " -w amount wallet")
        print(hijau + "Calculator Bet" +abu2 + ": " + res + str(sys.argv[0]) + " -kal balance basebet iflose")
        print(hijau + "History Deposite" +abu2 + ": " + res + str(sys.argv[0]) + " -d history")
        print(hijau + "History Withdrawal" +abu2 + ": " + res + str(sys.argv[0]) + " -w history")
        sys.exit()
    else:
        print(hijau + "Help" +abu2 + ": " + res + "python " + str(sys.argv[0]) + " -help")
        sys.exit()
except IndexError:
    getbetset = 0
    dice()
