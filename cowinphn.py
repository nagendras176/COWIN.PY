import requests as req
import time as time
import datetime as date
import asyncio
from sys import argv
from playsound import playsound


def num_cor(num):
    if num<10:
        return "0"+str(num)
    return str(num)

def strdate(datestr):
    return str(datestr.day)+"-"+num_cor(datestr.month)+"-"+str(datestr.year)

def day_on(j):
    return strdate(date.date.today()+date.timedelta(days=j))
def twenty_days():
    return list(map(day_on,list(range(0,20))))
       


def is_etn_available_on_date(datedata,pincode):
    params={'pincode':pincode,'date':datedata}
    header={'User-Agent':'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Mobile Safari/537.36'}
    res=req.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin',params=params,headers=header)
                              
    for i in res.json()['centers']:
      min_age_limit=i['sessions'][0]['min_age_limit']
      available=i['sessions'][0]["available_capacity"]
      print(str(available)+" vaccines is available for agelimit of "+str(min_age_limit))
      if(min_age_limit>18 and available>0):
            del(res)
            return True
      return False

      
def check_iterate():
    for pincode in argv[1:]:
      print("BEGINING OF PINCODE: "+pincode)
      for i in twenty_days() :
          print("date"+i)
          bool=is_etn_available_on_date(i,pincode)
          if(bool==True):
            print("*******************************************************************************")
            print("VACCINE IS AVAILABLE ON ::"+i+" PINCODE :"+pincode)
            print("********************************************************************************")
           # os.system('play-audio Avg.mp3') 
            playsound("./Avg.mp3")
          else:
            print("Not available on :"+i)
      
      
         

def main():
   while(True):
     check_iterate()
     time.sleep(310)
     
main()
