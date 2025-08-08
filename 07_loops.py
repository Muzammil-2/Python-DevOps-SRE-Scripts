#list of data structure which hold multiple values of 

list_of_cloud = ["aws","azure","gcp","digital ocean","utho","alibaba","oracle"]

#cloud =  "gcp" # variable

print (list_of_cloud)

# add new cloud "salesforce" 
list_of_cloud.append("salesforce")

# add new cloud IBM
list_of_cloud.append("IBM")

print (list_of_cloud)
list_of_cloud.insert(2,"Heroku")

print (list_of_cloud)

print(len(list_of_cloud)) 
# iterrate the cloud list
for cloud in list_of_cloud:
    print (list_of_cloud)
