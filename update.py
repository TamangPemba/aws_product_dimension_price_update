import json

input_file = "instance_type.txt"   # e.g., lines like: m3.xlarge    0.27
output_file = "result.json"         

dimensions = []
ratecard = []

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            print(f"Skipping invalid line: {line}")
            continue
        instance_type, price = parts[0], parts[1]
        dimensions.append({
            "Key": instance_type,
            "Name": instance_type,
            "Description": instance_type,
            "Unit": "Hrs",
            "Types": ["Metered"]
        })
        ratecard.append({
            "DimensionKey": instance_type,
            "Price": price
        })

result = {
    "DetailsDocument": dimensions,
    "RateCard": ratecard
}

def custom_format(data):
    """Return a string of JSON with custom formatting for arrays."""
    output = "{\n"
    first_key = True
    for key, value in data.items():
        if not first_key:
            output += ",\n"
        first_key = False
        output += f'"{key}": '
        if isinstance(value, list):
            output += "[\n"
            output += ",\n".join("{}".format(json.dumps(item, separators=(',', ': '))) for item in value)
            output += "\n]"
        else:
            output += json.dumps(value, separators=(',', ': '))
    output += "\n}"
    return output

formatted_json = custom_format(result)

with open(output_file, "w") as outfile:
    outfile.write(formatted_json)

print(f"Generated custom formatted changeset file: {output_file}")

