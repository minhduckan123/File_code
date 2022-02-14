import re
import json


f = open("hw_log.txt", "r")
data = f.readlines()
dict_item = {}


def serialize(string):
    dict_data = {}
    
    result = re.split("\s", string, 5)
    dict_data["Date"] = result[0]
    dict_data["Time"] = result[1]
    dict_data["Pid"] = result[2]
    dict_data["Level"] = result[3]
    dict_data["Component"] = result[4][:len(result[4])-1]
    dict_data["Content"] = result[5].strip()
    
    
    return dict_data


for i in range(len(data)):
    dict_item[i+1] = serialize(data[i])


nf = open("hdfs_log.json", "w", encoding="UTF-8")

json.dump(dict_item, nf, indent=4)

nf.close()

f = open("hdfs_log.json", "r", encoding="UTF-8")
data = json.load(f)
dict_item_null = {}

def deserialize(string):
    dict_id = {}
    result_blk = re.findall("blk", string)
    result_src = re.findall("src", string)
    result_dest = re.findall("dest", string)

    if result_blk and result_dest and result_src:
        list_id = content_data.split()
        dict_id["block_id"] = list_id[-5]
        dict_id["source_ip"] = list_id[-3]
        dict_id["dest_ip"] = list_id[-1]
        
        return dict_id

for i in range(len(data)):
    content_data = data["%s" %(i+1)]["Content"]
    
    dict_item_null["%s" %(i+1)] = deserialize(content_data)
    
dict_item = {key: value for key,value in dict_item_null.items() if value is not None}
    
    
nf = open("hdfs_block_travel.json", "w", encoding="UTF-8")
json.dump(dict_item, nf, indent=4)
