# print('RS232_485')
import minimalmodbus
import time

c = minimalmodbus.Instrument(port='com9', slaveaddress=1)
c.serial.baudrate = 9600
c.serial.bytesize = 7
c.serial.parity = 'E'
c.serial.stopbits = 1
c.serial.timeout = 1
c.mode = minimalmodbus.MODE_ASCII
# c.mode=minimalmodbus.MODE_RTU
c.clear_buffers_before_each_transaction = True
c.close_port_after_each_call = True
start_time=time.time()

'''
# 單一bit寫入
c.write_bit(
    registeraddress=int('800', 16),
    value=1,
    functioncode=5
)
'''
'''
# 單一bit讀取
TmpX = c.read_bit(
    registeraddress=int('800', 16),
    functioncode=2
)
print(TmpX)
'''
'''
# 多點寫入
TmpArray = []
for index in range(0, 31):
    if index % 2 == 0:
        TmpArray.append(0)
    else:
        TmpArray.append(0)
c.write_bits(
    registeraddress=int('800', 16),
    values=TmpArray
)
'''
'''
# 多點讀取
TmpX = c.read_bits(
    registeraddress=int('800', 16),
    number_of_bits=31,
    functioncode=2
)
print(TmpX)
'''
'''
while True:
    for n in range(0,31):
        if n %2 == 0:
            c.write_bit(
                registeraddress=int('800', 16),
                value=0,
                functioncode=5
            )
        else:
            c.write_bit(
                registeraddress=int('800', 16),
                value=1,
                functioncode=5
            )
'''
'''
#設定變數值寫入
Tmp2=16706
c.write_register(
    registeraddress=int('17D0',16),
    value=Tmp2,
    number_of_decimals=0,#放大10的幾次方
    signed=True,#有號無號設定
    functioncode=6
)
'''
'''
#設定變數值讀取
Tmp=c.read_register(
    registeraddress=int('17D0',16),
    number_of_decimals=0,#縮小10的幾次方
    signed=True,#有號無號設定
)
print(Tmp)
'''
'''
TmpArray = []
while True:
    for index in range(1,4):
        if index % 3 != 1:
            TmpArray.append(1)
            TmpArray.append(0)
            TmpArray.append(0)
        elif index %3 != 2:
            TmpArray.append(0)
            TmpArray.append(1)
            TmpArray.append(0)
        else:
            TmpArray.append(0)
            TmpArray.append(0)
            TmpArray.append(1)
    c.write_bits(
        registeraddress=int('0500', 16),
        values=TmpArray
    )
'''
'''

for n in ['&','~','&~']:
    Tmp2=int(n.encode('utf-8').hex(),16)#文字變成16進制,再轉成10進制
    print(Tmp2)
'''
c.write_string(
    registeraddress=int('17D0',16),
    textstring='AB',
    number_of_registers=1
)

Tmp=c.read_string(
    registeraddress=int('17D0',16),
    number_of_registers=1,
    functioncode=3
)
print(Tmp)