# 當從 GitHub 刪除資料後，記的要 Pull 回 Local，不然會造成 push rejected

# 創建虛擬環境: windows 和 MAC 不同
# 1. conda 指令, 會說明這些指令能做什麼
# 2. conda create -n XXX_venv(虛擬環境的名稱) python=3.6(指定 python 版本, 根據自己 pyhton 版本去定義)
# 3. conda info -e  檢視虛擬開發環境
# 4. activate XXX_venv(虛擬環境的名稱) 進入虛擬開發環境
# 5. deactivate XXX_venv(虛擬環境的名稱) 離開虛擬開發環境

# django-admin.exe startproject XXX(檔案名稱)        建立 django 的專案
# python manage.py runserver     啟動開發 server
# ----------------------------------------------------------------------------------------------------------
# 5.
# 常用快捷鍵，例如復制當前行、刪除當前行、批量注釋、縮進、查找和替換。
# 常用快捷鍵的查詢和配置：Keymap
# Ctrl + D：復制當前行或 Ctrl + C -> Ctrl + V
# Ctrl + X：刪除當前行
# Shift + Enter：快速換行
# Ctrl + / ：快速注釋（選中多行后可以批量注釋）
# Tab：縮進當前行（選中多行后可以批量縮進）
# Shift + Tab：取消縮進（選中多行后可以批量取消縮進）
# Ctrl + F：查找
# Ctrl + H：替換

# 6.
# Pycharm安裝插件，例如Markdown
# support、數據庫支持插件等。
# Plugins -> Browse
# repositories -> 搜索‘markdown
# support’ -> install
# 右上角View有三個選項可選，一般我們都用中間那個左側編寫，右側實時預覽

# 7.
# Git配置
# 需要本地安裝好Git
# Version
# Control ->  Git
# 配置了Git等版本控制系統之后，可以很方便的diff查看文件的不用

# 8.
# 常用操作指南。例如復制文件路徑、在文件管理器中打開、快速定位、查看模塊結構視圖、tab批量換space、TODO的使用、Debug的使用。
# 復制文件路徑：左側文件列表右鍵選中的文件  -> Copy Path
# 在文件管理器中打開：右鍵選中的文件  -> 往下找到Show In Explorer
#
# 快速定位：按住Ctrl + 鼠標左鍵點擊 ，點擊在源文件中展開類，函數，方法等的定義
# 查看結構：IDE左側邊欄Structure
# 查看當前項目的結構
# tab批量換space：Edit  ->  Convert Indents

# TODO的使用： #TODO要記錄的事情
# Debug設置斷點，直接點擊行號與代碼之間的空白處即可設置斷點
# Tab頁上右鍵 -> Move
# Right（Down），把當前Tab頁移到窗口右邊（下邊），方便對比
# 文件中右鍵 -> Local
# History能夠查看文件修改前后的對比
#
# IDE右下角能看到一些有用的信息，光標當前在第幾行的第幾個字符、當前回車換行、當前編碼類型、當前Git分支
# IDE右側邊欄  ->  Database

# 9.
# 去掉煩人的波浪線
# 單獨一行的注釋：  # +1空格+注釋內容
# 代碼后跟著的注釋：2
# 空格 +  # +1空格+注釋內容
# 保持良好的統一的編程風格是十分重要的。
# Google上面有很多關于各種語言的編程規范指導，Python也有自己的一些編程規范，
# PyCharm也會按一定的規范（比如PEP8）來檢查編輯器中的代碼。
# 這里的編程風格有代碼編寫格式層面的也有代碼邏輯組織層面的。
# https: // github.com / iwhgao / zh - google - styleguide / blob / master / google - python - styleguide / python_language_rules.rst
# https: // github.com / iwhgao / zh - google - styleguide / blob / master / google - python - styleguide / python_style_rules.rst
#
# 黃色波浪色不合規范
# 綠色波浪線符合規范

# 10.
# SSH
# Terminal： Default
# encoding: UTF8
# Settings   ->   Tools   ->   SSH
# Terminal    ->   最后一行Default
# encoding: 選擇UTF - 8

