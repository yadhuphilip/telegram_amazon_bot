import requests
import time
from bs4 import BeautifulSoup
import flask

a= 60*50

link = "https://www.flipkart.com/hp-15q-core-i5-7th-gen-4-gb-1-tb-hdd-windows-10-home-15q-ds0028tu-laptop/p/itmfbyhahh7ytg4h?pid=COMFBYH9ZF9BBKHE&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_7_6&otracker1=AS_Query_OrganicAutoSuggest_7_6&lid=LSTCOMFBYH9ZF9BBKHEPUXVV8&fm=SEARCH&iid=06759ad7-7567-497c-b102-8c14e2ccae89.COMFBYH9ZF9BBKHE.SEARCH&ppt=sp&ppn=sp&ssid=5dxhue8ops0000001562268705804&qH=ad490de95fff9428"
cur_rice="₹38,990" 
chat_id_char="##"
second_id="##"
api_token="##"
api_link="https://api.telegram.org/bot##"


def send_message(msg):
    new_link1 = api_link+"sendMessage?chat_id={}&text={}".format(chat_id_char,msg)
    new_link2 = api_link+"sendMessage?chat_id={}&text={}".format(second_id,msg)
    requests.get(new_link1)
    requests.get(new_link2)

    
while True:
    req = requests.get(link)
    if req:
        soup = BeautifulSoup(req.content,'html.parser')

        result = soup.find(class_='_3qQ9m1')
        result = result.get_text()
        if result!=cur_rice:
            cur_rice=result
            result = result+" changed"+"\n{}".format(link)
    
        send_message(result)
    else:
        pass


    

    time.sleep(a)






    
