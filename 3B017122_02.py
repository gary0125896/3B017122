student = {
    'sid' : input("請輸入您的學號："),
    'sname' : input("請輸入您的姓名："),
    'fchina' : float(input("請輸入您的國文成績：")),
    'fmath' : float(input("請輸入您的數學成績：")),
    'finfo' : float(input("請輸入您的電腦成績："))
        }
total = student['fchina']+student['finfo']+student['fmath']
avg = (student['fchina']+student['finfo']+student['fmath'])/3
print(avg)
print("-" * 30)
print(f"{student['sname']}({student['sid']})同學您好：")
print("以下是您的各科成績與分數評定\n")
print(f"國文：{student['fchina']} / 數學：{student['fmath']} / 電腦：{student['finfo']}")
print(f"總分：{total} / 平均：{avg}")
print("-" * 30)
if avg>60:
    print("及格")
else:
    print("不及格")