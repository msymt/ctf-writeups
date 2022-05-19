import glob
import subprocess

f_dict = {}
files = glob.glob("./Logs/*")
for file in files:
  dir = file[:-4] + "xml"
  f = open(dir, "w")
  print(dir)
  subprocess.run(["python3", "./python-evtx/scripts/evtx_dump.py", file], stdout=f)
