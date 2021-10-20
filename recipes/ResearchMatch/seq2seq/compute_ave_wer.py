import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output_folder", type=str)
args = parser.parse_args()

all_ins = 0
all_del = 0
all_sub = 0
total = 0
for i in range(1, 5):
    chunk = f"chunk{i}"
    f = open(args.output_folder+"/"+chunk+'/4568/wer.txt', 'r')
    res = f.readlines()[11]
    print(res)
    # %WER 36.84 [ 140 / 380, 16 ins, 8 del, 116 sub ]
    # 0    1     2 3   4 5    6  7    8 9    10  11  12
    eles = res.split()
    all_ins += int(eles[6])
    all_del += int(eles[8])
    all_sub += int(eles[10])
    total += int(eles[5][:-1])
all_errors = all_ins + all_del + all_sub
WER = all_errors / total * 100
print(f"%WER {WER:.1f} [ {all_errors} / {total}, {all_ins} ins, {all_del} del, {all_sub} sub ]")
