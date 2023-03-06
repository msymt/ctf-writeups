# ref. # ref: https://github.com/Daste745/kalmarctf-2023/blob/master/cards/analyze.py
import json

with open("cards.json") as f:
    packets = json.load(f)

collect_packets: list[tuple[str, str]] = []
last_cwd = "0"
for packet in packets:
    layers = packet["_source"]["layers"]

    if "ftp" in layers:
      cwd = layers["ftp.current-working-directory"]
      last_cwd = cwd

    if "data" in layers:
      data = layers["data"]["data.data"]
      collect_packets.append((data, last_cwd))

# CWDでソート
collect_packets.sort(key = lambda x: x[1])

for packet, cwd in collect_packets:
  value = int(packet, base=16) # hex string -> int
  print(chr(value), end="")
print()

"""
"ftp": {
          "ftp.request": "0",
          "ftp.response": "1",
          "250 Directory successfully changed.\\r\\n": {
            "ftp.response.code": "250",
            "ftp.response.arg": "Directory successfully changed."
          }
        },
        "ftp.current-working-directory": "374"
      }
"""
