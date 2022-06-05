from operator import ne
from random import shuffle

FLAG = b"ctf4b{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"
chal = b"ctf4b{weeerttyuuuooooooaaaashxnnnTTYYDFHHCCN,,??}"
chas = b"ctf4b{weeerttyuuuooooooaaaashxnnnTTYYDFHHCCN,,X?}"

seed = []
# FLAG = b"ctf4b{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}"
# FLAG = b"ctf4b{1234567890qwertyuiopasdfghjklzxcvbnm QWERTY}"
# FLAG = b"ctf4b{1234567890qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM{}_.,!@#$%^&*()_+-=[]{}|;':<>?/~`}"
# data = "1234567890qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM{}_.,!@#$%^&*()_+-=[]{}|;':<>?/~`"
chal_ori = ['w', 'e', 'e', 'e', 'r', 't', 't', 'y', 'u', 'u', 'u', 'o', 'o', 'o', 'o', 'o', 'o', 'a', 'a', 'a', 'a', 's', 'h', 'x', 'n', 'n', 'n', 'T', 'T', 'Y', 'Y', 'D', 'F', 'H', 'H', 'C', 'C', 'N', ',', ',', '?', '?']

origin_ci = [12147, 20481, 7073, 10408, 26615, 19066, 19363, 10852, 11705, 17445, 3028, 10640, 10623, 13243, 5789, 17436, 12348, 10818, 15891, 2818, 13690, 11671, 6410, 16649, 15905, 22240, 7096, 9801, 6090, 9624, 16660, 18531, 22533, 24381, 14909, 17705, 16389, 21346, 19626, 29977, 23452, 14895, 17452, 17733, 22235, 24687, 15649, 21941, 11472]

def solve(flag):
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
        print(origin[6:-1]) # ctf4{...} -> ...
        seed.extend(origin[6:-1])
        # print(len(origin[6:-1]))
    # shuffle(cipher)
    # print("cipher =", cipher)

def challenge():
    cipher = []
    origin = []
    for i in range(len(chal)):
        f = chal[i]
        c = (f + i)**2 + i
        cipher.append(c)
        for j in range(len(origin_ci)):
            if c == origin_ci[j]:
                dec = chr(f)
                origin.append(chr(f))
                print(f, chr(f), j)
                break
    # shuffle(cipher)
    print("cipher =", cipher)



if __name__ == "__main__":
    # cnt = 0
    # data = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_.,!@#$%^&*()_+-=[]{}|;':<>?/~`"
    # for c in data:
    #     full = c * 42
    #     flag = b"ctf4b{" + full.encode() + b"}"
    #     # print(flag)
    #     solve(flag)
    # print(seed)
    # print(''.join(seed))
    challenge()