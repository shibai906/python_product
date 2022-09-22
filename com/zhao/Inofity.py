#-*- coding=utf-8 -*-
import os
from datetime import datetime
import pyinotify
import logging
import json
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import threading

client = InfluxDBClient(url="http://3.129.224.33:8086", token="5up3r-S3cr3t-auth-t0k3n", org="influxdata-org")
write_api = client.write_api(write_options=SYNCHRONOUS)


def getTime(line):
    try:
        hourTime = line.split(" INFO  ")[0].split(".")[0]
        dayTime = datetime.now().strftime('%Y-%m-%d')
        time = dayTime + " " + hourTime
        return datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    except:
        return datetime.utcnow()


def printlog(filePath, pos):
    #  global pos
    try:
        fd = open(filePath)
        if pos != 0:
            fd.seek(pos, 0)
        while True:
            line = fd.readline()
            if line.strip():
                strings = line.strip()
                #        print(strings)
                if strings.__contains__('--GRAFANA_INFO--'):
                    print(strings)
                    logContent = strings.split('--GRAFANA_INFO--')[1]
                    logContent = logContent.replace('"{', '{')
                    logContent = logContent.replace('}",', '},')
                    logContent = logContent.replace('\\"', '"')
                    #          print(logContent)
                    jsonLogContent = json.loads(logContent)
                    p = Point("content")
                    if ('value' in jsonLogContent):
                        p.field('value', jsonLogContent['value'])
                    else:
                        p.field('value', 1.0)
                    for key in jsonLogContent:
                        print(key + ":" + str(jsonLogContent[key]))
                        p = p.tag(key, jsonLogContent[key])
                    time = getTime(line)
                    print(time)
                    #          p.field('value', 1.0)
                    p = p.time(time, WritePrecision.NS)
                    #          print(p)
                    write_api.write('sysLog', 'influxdata-org', p)
            pos = pos + len(line)
            if not line.strip():
                break
        fd.close()
    except e:
        print(str(e))

class MyEventHandler(pyinotify.ProcessEvent):
  def __init__(self, filePath, pos):
    self.filePath = filePath
    self.pos = pos
  def process_IN_MODIFY(self,event):
    try:
      print('modifyed')
      self.pos = printlog(self.filePath,self.pos)
    except e:
      print(str(e))

def threadPrintlog(filePath):
  pos = 0
#  print(filePath)
  pos = printlog(filePath, pos)
  wm = pyinotify.WatchManager()
  wm.add_watch(filePath, pyinotify.ALL_EVENTS, rec=True)
  eh = MyEventHandler(filePath, pos)
  notifier = pyinotify.Notifier(wm,eh)
  notifier.loop()

def main():
  for i, j, k in os.walk(r'/data/sunio-route/'):
    for g in k:
      filePath = os.path.join(i, g)
      if filePath.__contains__('/tron.log'):
#        print(filePath)
#        threadPrintlog(filePath)
        thread = threading.Thread(target=threadPrintlog, args=(filePath,))
        thread.start()

if __name__ == "__main__":
  main()
                                                                                                                                                                                                                            98,6          Bot
