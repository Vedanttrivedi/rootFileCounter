import os
dirs = ['C:/Users/RedLine Compuer/Desktop',"E:/"]
exts  = ['txt','html','py','cpp','c','css','js','java','php','dll','jpg','JPG','png','mkv','mp4','mp3','pdf','xls','docx','o','pub','ppt']
counts = []

for i in range(len(exts)):
    counts.append(0)

paths = []
def clean(paths):
        new_paths = []
        for i in paths:
                n1 = ""
                for j in i:
                        if j=="\\":
                                n1+='/'
                        else:
                                n1+=j
                new_paths.append(n1)
        return new_paths

for i in dirs:
        os.chdir(i)
        for dirpath in os.walk(os.getcwd()):
                paths.append(dirpath)
perpath = []
for i in paths:
        perpath.append(i[0])

new_path = clean(perpath)
counter = 0

for k in range(len(exts)):
    for i in new_path:
        os.chdir(i)
        d = 0
        for j in os.listdir():
            if j.endswith(exts[k]):
                counts[k]+=1

for k in range(len(counts)):
    t = k
    for j in range(k+1,len(counts)):
        if counts[t] > counts[j]:
            t = j
    try:
        v = counts[k]
        counts[k] = counts[t]
        counts[t] = v
        c = exts[k]
        exts[k] = exts[t]
        exts[t]  =c
    except Exception as e:
        print(e)

t = 0
for i  in dirs:
    print(i)
    for j in range(22):
        t+=1
for i in range(len(exts)):
	print(exts[i]+"\t:\t"+str(counts[i]))
print(t)
#cur.execute(r)
input('press!')
