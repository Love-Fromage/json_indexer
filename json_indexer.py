import json
import argparse

parser = argparse.ArgumentParser(
    prog="json_indexer",
    description="This updates the ids automatically in the given json")
parser.add_argument("file_path_json",
                    help="Give the path to the json file to edit.")

args = vars(parser.parse_args())
fj = args["file_path_json"]

#on load le json en ram
with open(fj, "r", encoding="utf-8") as read_it:
    data = json.load(read_it)
    #print IS console.log()
    # print(data)

#on passe a travers le "data" et on change le value de la key "id" pour le index de l'enumaration
#comme dans un array.map javascript
for index, item in enumerate(data):
    item["id"] = index
    if (item["id"] != index):
        print(item["id"], index)

with open(fj, "w", encoding="utf-8") as read_it:
    json.dump(data, indent=4, fp=read_it, ensure_ascii=False)

print("ca marche coco", fj)
# json.dumps()