# 抓取網頁原始碼 (HTML)
import urllib.request as req
import requests
def getData(url):
    # 建立 Requests 物件, 附加  Headers 的資訊
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("gbk")

    # 解析原始碼
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")   # 建立 BeautifulSoap 物件
    images = root.find_all("img")   # 搜尋所有 img 標籤

    # 設定儲存資料夾
    import os
    folder_path = './photo/'
    if os.path.exists(folder_path) == False:   # 判斷資料夾是否已經存在
        os.makedirs(folder_path)   # 建立資料夾
    os.chdir('photo')   # 移動工作目錄至 images 資料夾
    
    # 下載圖片至資料夾中
    import time
    for index,item in enumerate(images):
        if item:		
            html = requests.get(item.get("src"))   # get函式獲取圖片連結地址，requests傳送訪問請求
            img_name = str(index + 1) + ".jpg"

            with open(img_name, 'wb') as file:   # 以byte形式將圖片資料寫入
                file.write(html.content)
                file.flush()
            file.close()   # 關閉檔案
            print('第%d張圖片下載完成' % (index+1))
            index = index +1
            time.sleep(1)   # 自定義延時
    print('抓取完成')

    # 抓取下一頁連結
    nextlink = root.find("a", string = "下一页")   # 找到 a 中含有 "下一頁" 的標籤
    return nextlink["href"]   # 獲取 "下一頁" 標籤的連結

# 主程序: 抓取頁面圖片
pageURL = "http://www.jituwang.com/sucai/chunji-7541327.html"
count = 0
while count < 5:
    pageURL = "http://www.jituwang.com" + getData(pageURL)
    count += 1













