import machine
import time

# Inisialisasi I2C
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))  # Ganti dengan pin yang sesuai

def scan_i2c_addresses():
    addresses = i2c.scan()
    if addresses:
        print('Perangkat I2C ditemukan pada alamat:')
        for addr in addresses:
            print('Alamat I2C: 0x{:02X}'.format(addr))
    else:
        print('Tidak ada perangkat I2C ditemukan.')

while True:
    scan_i2c_addresses()
    time.sleep(5)  # Delay 5 detik sebelum pemindaian berikutnya
