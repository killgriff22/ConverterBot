defualtexpect="1234567890ZXCVBNM<>?ASDFGHJKL:QWERTYUIOP}[|~!@#$%^&*()_+zxcvbnm,./asdfghjkl;qwertyuiop[]"
#very proud of this very shitty encryption method i wrote like a year ago
import random
class newmethod:
    def encode_string(string,rot,seed):
        strng =""
        if type(seed) == str:
            seed_i=0
            for char in seed:
                seed_i+=ord(char)
            seed=seed_i
            del seed_i
        for i,char in enumerate(string):
            shift = random.randint(0,100)
            nextshift = 0 if i == 0 else random.randint(0,100)
            next=f"{hex(int(shift*rot+nextshift)*seed).split('0x')[1]}​{hex(int(rot+ord(char)+shift)*seed).split('0x')[1]}​{hex(int(nextshift*rot)*seed).split('0x')[1]}​"
            strng += next
        return strng
    def decode_string(string,rot,seed):
        strng = ""
        split = string.split("​")
        lst=[int(split[i],16) for i in range(len(split)-1)]
        split=lst
        del(lst)
        if type(seed) == str:
            seed_i=0
            for char in seed:
                seed_i+=ord(char)
            seed=seed_i
            del seed_i
        for i in range(0,len(split)-1,3):
            _ = int(split[i])
            __ = int(split[i+1])
            ___ = int(split[i+2])
            ___ //= seed
            ___ //= rot
            _ //= seed
            _ -= ___
            _ //= rot
            #_ += seed
            __ //= seed
            __ -= (rot+_)
            #__+=seed*rot
            try:
                strng+=chr(__)
            except:
                print("Failed to decode")
        return strng
class x4x5:
    def generatekey(expect=defualtexpect):
        import random
        codes=[]
        random.seed(expect)
        for char in expect:
            code=""
            for i in range(4):
                code+=random.choice(expect)
            code += char
            codes.append(code)
        key=""
        random.shuffle(codes)
        for code in codes:
            key+=code
        return key
    def decrypt(key,msg):
        keys=[key[i:i+5] for i in range(0, len(key), 5)]
        msg = [msg[i:i+4] for i in range(0, len(msg), 4)]
        decrypted=""
        for partkey in msg:
            for fullkey in keys:
                if partkey in fullkey:
                    decrypted += fullkey[4]
        return decrypted
    def encrypt(key,msg):
        encoded=""
        keys= [key[i:i+5] for i in range(0, len(key), 5)]
        for char in msg:
            for key in keys:
                if key[4] == char:  encoded+=[key[i:i+4] for i in range(0, len(key), 4)][0]
        return encoded
