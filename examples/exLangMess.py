curdir= ""
fname = curdir + "verification/" + "langMess.json"
with open(fname, 'r', encoding='utf-8') as file_object:
    messDict = json.load(file_object)
print(messDict["noCPCond"])
