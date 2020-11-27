import argparse
import base64
parser = argparse.ArgumentParser()
parser.add_argument("shift", help="shift numberic value", type=int)
parser.add_argument("path", help="name of the file")
args  = parser.parse_args()
shift = args.shift

with open(args.path, mode='rb') as file: # b is important -> binary
    content = file.read()
encoded = (base64.b64encode(content)).decode('utf-8')
print(type(encoded))
#data = base64.b64decode(encoded)

strs = 'abcdefghijklmnopqrstuvwxyz=/'
strs = strs + strs.upper()

charset_size = len(strs)
data = []
for i in encoded:
    if i.strip() and i in strs:
        data.append(strs[(strs.index(i) + shift) % charset_size])
    else:
        data.append(i)
output = ''.join(data)


outputf = 'outbin_'+args.path
myfileo = open(outputf, 'w')
myfileo.write(encoded)
myfileo.close()
