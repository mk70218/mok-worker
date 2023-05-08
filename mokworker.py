import time

def start_focus_timer(minutes):
    seconds = minutes * 60
    print("专注计时开始，共计", minutes, "分钟")
    for i in range(seconds, 0, -1):
        time.sleep(1)
        mins, secs = divmod(i, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
    print("专注计时结束，恭喜完成本次专注！")

# 调用函数开始专注，30 表示时长为 30 分钟
start_focus_timer(30)
