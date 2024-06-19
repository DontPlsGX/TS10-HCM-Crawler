import requests
import csv
from multiprocessing import cpu_count, Process


year = 2024

def crawl(start, stop, name):
    file = open(name, 'w', encoding = 'utf-8')
    file.write('"SBD","Họ Tên","Toán","Văn","Ngoại Ngữ","Chuyên","Tổng điểm","Tổng điểm chuyên"' + "\n")
    file.close()
    file = open(name, 'a', encoding = 'utf-8')
    session = requests.Session()
    session.headers.update({"Origin": "https://tuoitre.vn"}) 
    for x in range(start, stop+1):
        try: 
            scraping_url = "https://s6.tuoitre.vn/api/diem-thi-lop-10.htm?keywords=" \
                + str(x) + "&year=" + str(year) +"&sitename=tuoitre.vn"
            response = session.get(scraping_url)
            info = response.json()['data'][0]
        except: 
            pass
        else: 
            diem = (info['id'],info['HO_TEN'],info['TOAN'],info['VAN'], info['NGOAI_NGU'],info['CHUYEN'],sum((info['TOAN'], info['VAN'], info['NGOAI_NGU'])),sum((info['TOAN'], info['VAN'], info['NGOAI_NGU'], info['CHUYEN']*2 if info['CHUYEN'] > 0 else 0)),)
            diemthi = ",".join(['"' + str(i) + '"' for i in diem])
            file.write(diemthi + "\n")
    file.close()

if __name__ == "__main__":
    crawl(9001,9438,'ketqua5.csv')
    # files = [f'ketqua{i}.csv' for i in range(1,5)] 
    # p1 = Process(target=crawl,args=(90000,115501,files[0]))
    # p2 = Process(target=crawl,args=(115502,141003,files[1]))
    # p3 = Process(target=crawl,args=(141004, 166505,files[2]))
    # p4 = Process(target=crawl,args=(166506,192007,files[3]))

    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()

    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()