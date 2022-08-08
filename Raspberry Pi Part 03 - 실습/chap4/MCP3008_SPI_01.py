#-*-coding:utf-8-*-
# git clone git://github.com/doceme/py-spidev
# cd py-spidev
# sudo python3 setup.py install


# 필요한 라이브러리를 불러옵니다.
import spidev
import time

# 딜레이 시간 (센서 측정 간격)
delay=0.5

# MCP3008 채널중 센서에 연결한 채널 설정
ldr_channel=0

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

while True:
	# readadc 함수로 ldr_channel의 SPI 데이터를 읽어 저장
	pot_value = readadc(ldr_channel)
	print("--------------------------------------")
	print("POT Value : %d" % pot_value)
	time.sleep(delay)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	