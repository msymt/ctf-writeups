import glob

f_dict = {}
files = glob.glob("./out/*")
for file in files:
  f = open(file, "r")
  read_data = f.read()
  f_dict[file] = read_data
  f.close()

dict_no_dup = dict()
result = dict()
for key, val in f_dict.items():
    dict_no_dup[val] = key

for key, val in dict_no_dup.items():
    result[val] = key

print(result)
