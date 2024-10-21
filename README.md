# Blogging-Platform
![image](https://github.com/Pro-Lan/Blogging-Platform/blob/main/%E9%A6%96%E9%A0%81.png)
## 安裝套件
```python
pip install -r requirements.txt
```
## 執行
```python
python manage.py runserver
```

## 系統功能:

### (一)文章:

1. 列出文章
2. 寫文章(支援Markdown語法)
3. 自動分頁
4. 瀏覽數(作者瀏覽不會增加)
5. 最熱門、最新文章排序
6. 搜索文章
7. 目錄(For Markdown)
8. 文章分類
9. 文章標題圖
10. 顯示評論

### (二)用戶:

1. 登入
2. 登出
3. 註冊
4. 刪除
5. 用戶個人信息(頭像、簡介等)
6. 發表評論(需登入才能使用)
7. 發布文章
8. 刪除文章(只有作者本人才能使用)
9. 修改文章(只有作者本人才能使用)

### (三)未來可新增的功能

1.收藏文章

2.通知作者

3.第三方登入

4.RWD

## 系統設計:

### (一)網站架構:
![image](https://github.com/Pro-Lan/Blogging-Platform/blob/main/%E7%B6%B2%E7%AB%99%E6%9E%B6%E6%A7%8B.png)
### (二)資料庫設計:
![image](https://github.com/Pro-Lan/Blogging-Platform/blob/main/%E8%B3%87%E6%96%99%E5%BA%AB%E8%A8%AD%E8%A8%88.png)
### 外鍵關係:

1. 一個文章分類，可以對應到多篇文章
2. 一篇文章可以有多個評論
3. 一個使用者可以發表多篇文章
4. 一個使用者可以發表多個評論
5. 每個 **`User`** 對象都對應到一個唯一的**`Profile`**  (one to one)

