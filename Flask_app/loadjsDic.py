import json
try:
    with open("./16_image.json", "r") as file:
       dic_string = json.load(file)
       print(dic_string[0]["HostConfig"]["ReadonlyPaths"])
       count = len(dic_string)
       print("Number of indexes:", count)
       print("Available indexes:", list(range(count)))
       
#  # Number of indexes (items) in the list
# count = len(dic_string)
# print("Number of indexes:", count)

# # List available index numbers
# print("Available indexes:", list(range(count)))
       
except TypeError:
    print("list indices must be integers or slices, not str")
