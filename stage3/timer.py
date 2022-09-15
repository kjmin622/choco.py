import time

class Timer:
    """
    time 라이브러리를 기반으로 작성된 타이머 클래스
    
    매개변수로 time(초)을 넣어 생성
    start를 통해 타이머 작동하고, is_done을 통해 타이머가 끝났는지 확인
    타이머가 작동하고 있다면 is_run()은 True를 반환
    start()로는 작동중인 타이머는 초기화할 수 없으나 force_start()를 통해 재작동 가능
    set_time((float)time)으로 타이머 시간을 변경 가능
    클래스의 속성은 모두 private임

    Attributes:
        private float _time: 타이머 시간
        private float _now_time: 타이머 현재 시간
        private float _run (bool): 타이머 작동 여부
    Args:
        time (float): 타이머 시간(초)
    """
    def __init__(self,time):
        self._time = time
        self._now_time = None
        self._run = False
    
    def start(self):
        if(not self._run):
            self._run = True
            self._now_time = time.time()

    def force_start(self):
        self._run = True
        self._now_time = time.time()

    def set_time(self, time):
        self._time = time

    def is_run(self):
        return self._run
    
    def is_done(self):
        if(self._run):
            if(time.time() - self._now_time >= self._time):
                self._run = False
                return True
            else:
                return False
        else:
            return False