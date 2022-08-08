#-*-coding:utf-8-*-

# 필요한 라이브러리를 불러옵니다.
import spidev
import time

# 딜레이 시간 (센서 측정 간격)
delay=0.5

# MCP3008 채널설정
sw_channel = 0
vrx_channel = 1
vry_channel = 2

# SPI 인스턴스 spi 생성
spi=spidev.SpiDev()

# SPI 통신 시작하기
spi.open(0, 0)

# SPI 통신 속도 설정
spi.max_speed_hz=100000


# 0 ~ 7 까지 8개의 채널에서 SPI 데이터를 읽어서 반환
def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

# 무한루프
while True:
	vrx_pos = readadc(vrx_channel)  # X, Y 축 포지션값
	vry_pos = readadc(vry_channel)
	sw_val = readadc(sw_channel)    # 스위치 입력
	print("X : {} Y : {} SW : {}".format(vrx_pos, vry_pos, sw_val)) # 출력
	time.sleep(delay)  # delay 시간만큼 기다림
