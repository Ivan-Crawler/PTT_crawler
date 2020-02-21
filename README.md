PTT爬蟲說明文件
=========
<img src="https://i.imgur.com/HYLhkrP.png"/>

目錄
=================
* [使用方式](#使用方式)
    * [程式碼執行方式](#程式碼執行方式)
    * [終端機執行方式](#終端機執行方式)
* [參數說明](#參數說明)
    * [Board_Name](#Board_Name)
    * [start](#start)
    * [page_num](#page_num)
* [檔案說明](#檔案說明)
    * [PTT爬蟲範例.py](#PTT爬蟲範例py)
    * [Ivan_ptt.py](#Ivan_pttpy)
    
 
使用方式
=================

程式碼執行方式
-----------
```
crawl_ptt_page(Board_Name ='版名' , start =開始爬取的頁數 ,page_num= 往回爬幾頁)
```

範例
```
crawl_ptt_page(Board_Name ='Elephants', start =4921 ,page_num= 5)
```

終端機執行方式
-----------
1. 切換到Ivan_ptt.py的檔案路徑下。
```
cd 檔案位置
```
<img src="https://imgur.com/Y9VYwPh.png"/>

2. 啟動Ivan_ptt.py，並按照指示輸入相關資訊，想從第幾頁開始爬可以直接按Enter跳過，就會從最新的文章開始。
```
python Ivan_ptt.py
```
<img src="https://imgur.com/dMk9jjV.png"/>

3.開始自動爬蟲，爬蟲完成後，在Ivan_ptt.py的檔案路徑下就會出現「您爬的版名.csv」檔案.
<img src="https://imgur.com/dMk9jjV.png"/>



參數說明
=================
| 參數名稱      | 型態     | 是否必填     |
| ---------- | :-----------:  | :-----------: |
| Board_Name | 字串str  | Yes |
| start | 字串數字皆可  | No |
| page_num | 數字  | Yes |

#### Board_Name
版名請簪照實體網頁中的版名（如以下圖片範例），必須大小寫相同，否則會搜尋不到。

<img src="https://imgur.com/PD0Gy26.png"/>

#### start
從第幾頁開始爬。此頁數可以從網址中查看，而最新的一頁只會顯示index.html，只要點上一頁，往前推導即可。`若沒有給這個參數，就自動從最新的一頁開始進行爬蟲。`

<img src="https://i.imgur.com/xNUVXR6.png"/>

#### page_num
顧名思義，往回爬幾頁。
 
檔案說明
=================

PTT爬蟲範例.py
-----------
範例使用方式。講述如何使用Ivan_ptt.py檔案。

Ivan_ptt.py
-----------
PTT爬蟲工具主程式。

