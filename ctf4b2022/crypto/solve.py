from operator import ne
from random import shuffle

FLAG = b"ctf4b{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"
id = b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chal = b"ctf4b{weeerttyuuuooooooaaaashxnnnTTYYDFHHCCN,,??}"
chas = b"ctf4b{weeerttyuuuooooooaaaashxnnnTTYYDFHHCCN,,X?}"
chal_ori = ['w', 'e', 'e', 'e', 'r', 't', 't', 'y', 'u', 'u', 'u', 'o', 'o', 'o', 'o', 'o', 'o', 'a', 'a', 'a', 'a', 's', 'h', 'x', 'n', 'n', 'n', 'T', 'T', 'Y', 'Y', 'D', 'F', 'H', 'H', 'C', 'C', 'N', ',', ',', '?', '?']
origin_ci = [12147, 20481, 7073, 10408, 26615, 19066, 19363, 10852, 11705, 17445, 3028, 10640, 10623, 13243, 5789, 17436, 12348, 10818, 15891, 2818, 13690, 11671, 6410, 16649, 15905, 22240, 7096, 9801, 6090, 9624, 16660, 18531, 22533, 24381, 14909, 17705, 16389, 21346, 19626, 29977, 23452, 14895, 17452, 17733, 22235, 24687, 15649, 21941, 11472]

def challenge(flag, ch):
    cipher = []
    origin = []
    for i in range(len(flag)):
        f = flag[i]
        c = (f + i)**2 + i
        cipher.append(c)
        for j in range(len(origin_ci)):
            if c == origin_ci[j]:
                origin.append(chr(f))
                break
    if(len(origin) != 7):
        print(ch.decode('utf-8'), end="")
        return True
    return False


for i in range(len(id)):
  for c in chal_ori:
    prefix = id[:i]
    suffix = id[i+1:]
    flag = b"ctf4b{" + prefix + c.encode() + suffix + b"}"
    # print(flag)
    result = challenge(flag, c.encode())
    if(result):
      break
print("")


