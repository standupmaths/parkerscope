import serial
import time
import csv
from datetime import datetime

now = datetime.now()

folder = "/Users/mattparker/Dropbox/python/Solareclipse_2023/DATA/"
time_index = str(int(now.timestamp()))
filename_raw = folder + "parkerscope_rawdata-" + time_index + ".csv"
filename_fancy = folder + "parkerscope_fancydata-" + time_index + ".csv"

def lux_convert(hout):
    power_index = int(hout[2:6])
    sig_figs = int(hout[6:])
    # power values from "Light Meter CEM DT-1309 Data Acquisition with LabVIEW" paper
    # need to remove a bunch of weird data when the device is changing scales
    if power_index in [80, 180, 188, 288] and int(hout[6:7]) <= 3:
        powers = {180: 0.1, 80: 1, 288: 10, 188: 100}
        pow = powers[power_index]
    else:
        return "E"
    return sig_figs * pow


def main():
    
    with serial.Serial() as s:
        s.baudrate = 9600
        s.port = "/dev/tty.usbserial-0001"
    
        s.open()

        # for some reason device gives the same result three times, so we discard two out of three results
        track = 0

        while(True):
            s.write(b'*IDN?')
            out = s.read(5)
            hout = out.hex()
            if track == 0:
                print(hout)
                fancy_hout = lux_convert(hout)
                print(fancy_hout)

                now = datetime.now()
                # safety store the data
                dis_data = [now.timestamp(), hout]
                with open(filename_raw, 'a') as csvfile:  
                    csvwriter = csv.writer(csvfile) 
                    csvwriter.writerow(dis_data)
                # fancy up the data
                if fancy_hout != "E":
                    nowish= datetime.now().strftime('%H:%M:%S.%f')
                    print(nowish)
                    fancy_data = [nowish, fancy_hout]
                    with open(filename_fancy, 'a') as csvfile:  
                        csvwriter = csv.writer(csvfile) 
                        csvwriter.writerow(fancy_data)
                # any gui fun will go here

            time.sleep(3)
            track = (track + 1)%3


if __name__ == '__main__':
    main()