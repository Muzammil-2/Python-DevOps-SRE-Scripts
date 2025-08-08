# production packages missing
dev_environment = {"jenkins","java","Sonarqube","Docker","Kubectl","aws"}
production_environment = {"jenkins","java","Sonarqube","Docker","Kubectl"}

missing_pks_prod = dev_environment - production_environment

print (missing_pks_prod)

for tool in dev_environment[0]:
    print(dev_environment)