from pyModbusTCP.client import ModbusClient
import time



c = ModbusClient(
    host='192.168.1.5',
    port=502,
    auto_open=True,
    unit_id=1,
    timeout=1,
    debug=False
)
'''
# 寫入單筆Bit
# ------------------------------
s = c.write_single_coil(
    bit_addr=int('500', 16),
    bit_value=False
)
print(s)
'''
'''
# 寫入多筆Bits
# ------------------------------
bits_value=[True, False, True]
s = c.write_multiple_coils(
    bits_addr=int('500', 16),
    bits_value=bits_value
)
print(s)
'''

#讀出多筆Bit
#------------------------------
s = c.read_coils(
    bit_addr=int('500', 16),
    bit_nb=5#抓幾筆資料
)
print(s)

'''
# 寫入單筆數值
# ------------------------------
s = c.write_single_register(
    reg_addr=int('17D0', 16),
    reg_value=18489#輸入變數值
)
print(s)
'''
'''
OriginalArray = [
    'AB', 'CD', 'EF', 'GH', 'IJ',
    'KL', 'MN', 'OP', 'QR', 'ST',
    'UV', 'WX', 'YZ', 'ab', 'cd',
    'ef', 'gh', 'ij', 'kl', 'mn',
    'op', 'qr', 'st', 'uv', 'wx',
    'yz', '01', '23', '45', '67',
    '89', '~@', '#$', '%^', '&*',
    '()', '_+', '<>', '?/', 'CE'
]
TmpArray = []
MaxIndex = len(OriginalArray)

for index1, value1 in enumerate(OriginalArray):
    Tmp2 = int(value1.encode('utf-8').hex(), 16)
    TmpArray.append(Tmp2)
s = c.write_multiple_registers(
    regs_addr=int('17D0', 16),
    regs_value=TmpArray
)
'''

start_time = time.time()
TmpArray = []
for n in range(0, 99):#0,100=100筆
    TmpArray.append(42)
print(TmpArray)
s = c.write_multiple_registers(
    regs_addr=int('17D0', 16),
    regs_value=TmpArray
)
End_time = time.time()
print('End-Start',End_time-start_time)
'''
s = c.read_holding_registers(
    reg_addr=int('17D0', 16),
    reg_nb=100
)

TmpArray = []
for index, value in enumerate(s):
    if value != 0:
        Tmp1 = hex(value)[2:]
        TmpArray.append(bytes.fromhex(Tmp1).decode('utf-8'))
    else:
        TmpArray.append(value)
print(TmpArray)
'''