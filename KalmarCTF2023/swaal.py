# ref: https://github.com/Daste745/kalmarctf-2023/blob/master/swaal/analyze.py#L17
import json

with open("swaal.json") as f:
    packets = json.load(f)

letters: dict[int, str] = {}
column = 0
for packet in packets:
    data = packet["_source"]["layers"]["data"]["data.data"]
    value = int(data, base=16)

    if value == 0:
        if column not in letters:
            letters[column] = " "
    elif value == 10:  # LF
        column = 0
        continue
    else:
        letters[column] = chr(value)

    column += 1

print("".join(letters.values()))