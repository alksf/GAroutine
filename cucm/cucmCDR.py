#!/usr/bin/env python3

import sys
import csv
import time


def date_and_time(time_value):
    return time.strftime("%d.%m.%y %H:%M:%S", time.localtime(float(time_value)))

def convert_duration(secs):
    secs = int(secs)
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

if __name__ == '__main__':

    usage = 'Error, Correct Usage: cucmCDR.py "/path/to/cdrfile" -[cgpn|cdpn|any] 4357'

    if (len(sys.argv) != 4 or (sys.argv[2] not in ['-cgpn','-cdpn','-any'])):
        print(usage)
        sys.exit()

    else:
        infile = open((sys.argv[1]), 'r')
        outfile = open((sys.argv[3])+'.txt', 'w', newline='\n', encoding='utf-8')
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        writer.writerow(['Date/Time', 'Duration', 'Calling Number', 'Called Number', 'Final Called Number'] )

        for row in reader:
            if sys.argv[2] == '-cgpn':
                if row[8] == (sys.argv[3]):
                    writer.writerow([date_and_time(row[47]),convert_duration(row[55]),row[8],row[29],row[30]])
            elif sys.argv[2] == '-cdpn':
                if row[29] == (sys.argv[3]) or row[30] == (sys.argv[3]):
                    writer.writerow([date_and_time(row[47]),convert_duration(row[55]),row[8],row[29],row[30]])
            elif sys.argv[2] == '-any':
                if row[8] == (sys.argv[3]) or row[29] == (sys.argv[3]) or row[30] == (sys.argv[3]):
                    writer.writerow([date_and_time(row[47]),convert_duration(row[55]),row[8],row[29],row[30]])

        print("Finished successfully!")
        infile.close()
        outfile.close()
