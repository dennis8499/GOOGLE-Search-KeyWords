# GOOGLE Search KeyWords
 利用GOOGLE的搜尋功能，找尋擁有特定關鍵字的網頁，並找尋有無input label(學校作業)
1. 創立google網址:
	1. 有兩種方式可以去上google搜尋內容，一種是跟正常使用的方法一樣，在搜尋欄內，輸入關鍵字之後開始搜尋，另外一種是在google網址列輸入想要的內容之後案開始，而我是選擇第二種方式來做使用。基本上要讓google搜尋東西時，讓網址欄變成這樣https://www.google.com.tw/search?q=然後再q=之後輸入想要搜尋的內容之後，就可以開始搜尋，假設我要搜尋login.php我就讓網址變成https://www.google.com.tw/search?q=login.php就可以進行搜尋了。
2. 找尋網址名稱跟網址:
	1. 標題在<h3 class "r">
	2. 網址在<cite class "iUH30">
3. 創建好要搜尋的網址後，利用requests來進行訪問，並用BeautifulSoup去搜尋標題與網址，並串成list後寫入到url.txt的文件檔
4. 確認是否有input label
	1. 利用BeautifulSoup來搜尋input label