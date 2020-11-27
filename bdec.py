import argparse
import base64
parser = argparse.ArgumentParser()
parser.add_argument("shift", help="shift numberic value", type=int)
parser.add_argument("path", help="name of the file")
args  = parser.parse_args()
shift = args.shift

with open(args.path, mode='r') as file:
    content = file.read()
encoded = content

strs = 'abcdefghijklmnopqrstuvwxyz=/'
strs = strs + strs.upper()

charset_size = len(strs)
data = ''

for i in content:
    if i.strip() and i in strs:
        if strs.index(i) >=shift:
            orig = strs.index(i) - shift
        else:
            orig = strs.index(i) + charset_size - shift
        data = data + strs[orig]
    else:
        data = data + i
output = data

encoded = output.encode('utf-8')
decoded = base64.b64decode(content)


outputf = 'outbindec_'+args.path
myfileo = open(outputf, 'wb')
myfileo.write(decoded)
myfileo.close()
