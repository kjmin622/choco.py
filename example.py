import time
from timer import *

# 실사용에서는 time은 import하지 않음 (여기서는 예시를 위해 사용)
# 설명 주석 아래 코드블럭만 읽으면 됨

CONDITION = True
SOLUTION = ""
FRAME = 60

# 2초 타이머 생성
timer_2second = Timer(2)

while True:

    # 특정 조건이 충족되면 timer 작동
    if(CONDITION):
        timer_2second.start()
    
    # ...

    # timer가 작동중이고, 설정된 시간이 끝났으면 솔루션 실행
    if( timer_2second.is_done()):
        SOLUTION;print("timeover")

    
    time.sleep(1/FRAME)