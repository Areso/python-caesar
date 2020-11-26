import argparse
parser = argparse.ArgumentParser()
parser.add_argument("shift", help="shift numberic value", type=int)
parser.add_argument("source", help="source for decoding: file, input, batch, batchf")
parser.add_argument("-p", "--path", help="name of the file")
parser.add_argument("-b", "--batch", help="batch string to encode")
parser.add_argument("-bf", "--batchf", help="batch string to encode. out to file")
parser.add_argument("-i", "--input", help="interactive input")
args  = parser.parse_args()
shift = args.shift

if args.path:
    myfiler = open(args.path, 'r')
    content = myfiler.read()
    myfiler.close()
if args.batch:
    content = args.batch
if args.batchf:
    content = args.batchf
if args.input:
    content = input('Input string: ')

strs = 'abcdefghijklmnopqrstuvwxyz'
strs = strs + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
strs = strs + ' ' + strs.upper()

charset_size = len(strs)
data = []
for i in content:
    if i.strip() and i in strs:
        data.append(strs[(strs.index(i) + shift) % charset_size])
    else:
        data.append(i)
output = ''.join(data)

if (args.batch or args.input):
    print(output)

if args.batchf:
    myfileo = open('enc_res.txt', 'w')
    myfileo.write(output)
    myfileo.close()

if args.path:
    outputf = 'out_'+args.path
    myfileo = open(outputf, 'w')
    myfileo.write(output)
    myfileo.close()
