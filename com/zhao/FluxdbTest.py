import json
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "5up3r-S3cr3t-auth-t0k3n"
org = "influxdata-org"
bucket = "syslog"

client = InfluxDBClient(url="http://3.129.224.33:8086", token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
delete_api = client.delete_api()


def delete():
    delete_api.delete('drop measurement content', bucket='syslog')

def pri():
  #   tables = query_api.query("""from(bucket: "syslog")
  # |> range(start: -48h)
  # |> set(key: "_value", value: "1.0")
  # |> filter(fn: (r) => r._measurement == "content")
  # |> filter(fn: (r) => r["logName"] != "SwapSyncEventChaserTask.executeTask blockTime!" and r["logName"] != "SwapSnapshotEventChaserTask.executeTask blockTime!")
  # |> group(columns: ["logName"])
  # |> sum()""")
    tables = query_api.query('from(bucket: "syslog") |> range(start: -1h)')
    for table in tables:
        print(table)
        for row in table.records:
            print(row.values)
            # break


def ins():
    point = Point("mem") \
        .tag("host", "host1") \
        .tag("您好", 123232432342) \
        .tag("value", 100000) \
        .field("value", 1.0) \
        .time(datetime.utcnow(), WritePrecision.NS)
    res = write_api.write('syslog', 'influxdata-org', point)
    print(res)


def getTime(line):
    try:
        hourTime = line.split(" INFO  ")[0].split(".")[0]
        dayTime = datetime.now().strftime('%Y-%m-%d')
        time = dayTime + " " + hourTime
        return datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    except:
        return datetime.now()


# def test():
#     str = '00:18:53.981 INFO  [http-nio-10090-exec-5] [o.t.d.s.LogClient](LogClient.java:32) --GRAFANA_INFO--{"product":"router","logName":"request-scan-volumeAll","logContent":"{\"exchangeAddress0\":\"\",\"exchangeAddress1\":\"\"}","requestId":"f7db924a-4ded-41c6-9b6d-5d3137aa11b9"}'
#     logContent = str.split('--GRAFANA_INFO--')[1]
#     logContent = logContent.replace('"{', '{')
#     logContent = logContent.replace('}",', '},')
#     logContent = logContent.replace('\\"', '"')
#     jsonLogContent = json.loads(logContent)
#     p = Point("content")
#     for key in jsonLogContent:
#         #            print(key + ":" + str(jsonLogContent[key]))
#         p = p.tag(key, jsonLogContent[key])
#     time = getTime(str)
#     print(time)
#     if ('value' in jsonLogContent):
#         p.field('value', jsonLogContent['value'])
#     else:
#         p.field('value', 0.0)
#
#     p = p.time(time, WritePrecision.NS)
#     #          print(p)
#     write_api.write('syslog', 'influxdata-org', p)


if __name__ == '__main__':
    pri()