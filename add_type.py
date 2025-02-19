import sys

with open("add_type.txt", "r") as infile:
    instance_types = [line.strip() for line in infile if line.strip()]

instance_list = ",".join(f'"{t}"' for t in instance_types)

snippet = f'"DetailsDocument": {{"InstanceTypes": [{instance_list}]}}}},'

with open("type.json", "w") as outfile:
    outfile.write(snippet)

