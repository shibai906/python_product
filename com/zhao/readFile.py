# -*- coding=utf-8 -*-
import time

def printlog(filePath, pos):
    print("执行了")
    print(pos)
    while True:
        fd = open(filePath)
        if pos != 0:
            fd.seek(pos, 0)
        while True:
            line = fd.readline()
            if line.strip():
                print(line.strip())
            pos = pos + len(line)
            if not line.strip():
                break
        time.sleep(3)
        fd.close()

def main():
    pos = 0
    filePath = '/home/java-tron/hulin/syslog-monitor/codelab/tron.log'
    printlog(filePath, pos)


#    except KeyboardInterrupt:
#      notifier.stop()
#      break

if __name__ == "__main__":
    main()
