import openpyxl
import datetime
import line_notify
import os
import sys

# 先切換到當前目錄，才能正常讀取檔案
cwd_dir = os.path.dirname(sys.argv[0])
os.chdir(cwd_dir)

# line訊息內容
msg = ''

# 讀取檔案
wb = openpyxl.load_workbook('./config.xlsx', True)
ws = wb[wb.sheetnames[0]]

# 今日
today = datetime.date.today()
# 逐列檢查
for target in ws:
    content = target[0].value
    if content == '項目':
        continue
    # xlsx讀入是datetime無法加減, 要轉換為date
    target_date = target[1].value.date()

    # 已過日期要加1年
    if target_date.month < today.month:
        target_date = datetime.date(
            today.year+1, target_date.month, target_date.day)
    notify_before_days = target[2].value

    # 距離目標日期剩下天數
    remain_days = (target_date - today).days
    if remain_days == notify_before_days:
        msg += '\n' + content

# 設定line token(建議定義在電腦環境變數內)
line_notify.setToken(os.environ['DATE_TOKEN'])
line_notify.sendMessage(msg)
