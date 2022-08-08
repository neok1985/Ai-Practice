# coding: utf-8

#GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

#time 라이브러리 임포트
import time

# 핀 번호 할당 방법은 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 핀 번호 할당
SRV = 12

# 출력 핀으로 설정
GPIO.setup(SRV, GPIO.OUT)

# 주파수 설정
freq = 50.0

# PWM 객체 인스턴스 생성
# 출력 핀: SRV, 주파수: freq
p = GPIO.PWM(SRV, freq)

# PWM 신호 출력 시작
p.start(100)

# 예외 처리
try:
   # 무한 반복
   while 1:
        # for deg in range(2, 13, 1):
        #     p.ChangeDutyCycle( deg  )
        #     time.sleep(1)
        # for deg in range(12, 1, -1):
        #     p.ChangeDutyCycle( deg  )
        #     time.sleep(1)
        for i in range(0, 180):
            dc = 1.0/18.0*i+2
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        for i in range(180, 0, -1):
            dc = 1.0/18.0*i+2
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        

# 키보드 예외 검출
except KeyboardInterrupt:
   # 아무것도 하지 않음
   pass

# PWM 정지
p.stop()

# GPIO 개방
GPIO.cleanup()
