This repository contains scripts and instructions to extract Product and Offer IDs from the AWS Marketplace Catalog API and convert them into a simplified Excel file.

## Overview

When updating the instance type and pricing using the AWS Marketplace Catalog API, you first need to retrieve the Product ID and Offer ID. This repository guides you through the following steps:

1. **Extracting Product and Offer IDs**: Retrieve the IDs using the AWS CLI.
2. **Converting `product.json` to an Excel File**: Use a Python script to generate an Excel file containing only the Product ID and Offer ID.

## Prerequisites

- **AWS CLI**: Installed and configured with appropriate credentials.
- **Python 3.x**: Installed on your system.


## Steps
### 1. Clone the original AWS repository
```bash
git clone https://github.com/aws-samples/aws-marketplace-reference-code/tree/main
```

### 2. Follow the documentation for python
```bash 
cd python
```
Install all the necessary things as mentioned in the documentation. and navigate to the following directory for to add dimenions. 
```bash
cd  /aws-marketplace-reference-code/python/src/catalog_api/products/ami/add_dimension_to_ami_product_and_set_price_in_public_offer
```

### 3. Extracting Product and Offer IDs

Run the following command to extract the Product and Offer IDs from the AWS Marketplace Catalog API. The output is stored in a file named `product.json`.

```bash
aws marketplace-catalog list-entities --catalog AWSMarketplace --entity-type Offer > product.json
```

### 4. Clone the new repository 
```bash 
git clone https://github.com/TamangPemba/aws_product_dimension_price_update.git
cd aws_product_dimension_price_update
```

### 5. Install the necessary python Libraries. 
```bash
pip install -r requirements.txt
```

### 6. Converting product.json to an Excel File

Use the provided Python script `offer_prod_id.py` to convert `product.json` into an Excel file containing only the Product ID and Offer ID. The script performs the following actions:

- Reads `product.json`
- Extracts the Product ID and Offer ID from each entity in the `EntitySummaryList`
- Writes the extracted data to an Excel file named `product_offer_ids.xlsx`

To run the script, execute:

```bash
python3 offer_prod_id.py
```

### 7. Viewing the Excel File from the Command Line

If you prefer to view the Excel file from the command line, you can convert it to CSV format and then use `less` to browse the file:

```bash
xlsx2csv product_offer_ids.xlsx
```
### 8. Create a new file instace_type.txt

Copy the instance type and it's corresponding price 
```bash
r5n.2xlarge	0.55
m6id.4xlarge	1.11
x2idn.16xlarge	4.47
```

### 9. Generating the dimension and RateCard

```bash
python3 update.py
```
You will see output like below, 
```bash 
{
"DetailsDocument": [
{"Key": "r5n.2xlarge","Name": "r5n.2xlarge","Description": "r5n.2xlarge","Unit": "Hrs","Types": ["Metered"]},
{"Key": "m6id.4xlarge","Name": "m6id.4xlarge","Description": "m6id.4xlarge","Unit": "Hrs","Types": ["Metered"]},
{"Key": "x2idn.16xlarge","Name": "x2idn.16xlarge","Description": "x2idn.16xlarge","Unit": "Hrs","Types": ["Metered"]}
],
"RateCard": [
{"DimensionKey": "r5n.2xlarge","Price": "0.55"},
{"DimensionKey": "m6id.4xlarge","Price": "1.11"},
{"DimensionKey": "x2idn.16xlarge","Price": "4.47"}
]
}
```

### 10. Update changeset.json 

Open Changeset.json file and update the DetailsDocument 
```bash
E.g. 
 "DetailsDocument": [
        {"Key": "r5n.2xlarge","Name": "r5n.2xlarge","Description": "r5n.2xlarge","Unit": "Hrs","Types": ["Metered"]},
        {"Key": "m6id.4xlarge","Name": "m6id.4xlarge","Description": "m6id.4xlarge","Unit": "Hrs","Types": ["Metered"]},
        {"Key": "x2idn.16xlarge","Name": "x2idn.16xlarge","Description": "x2idn.16xlarge","Unit": "Hrs","Types": ["Metered"]}
      ]
    },
```
Note: - You have to update everytime or this. This is for to adding new instace type, if instance type is already preset, it will generate a error. 

### 11. Update the RateCard 

Update the RateCard in changeset.json file, while updateing RateCard, add a comma (,) at the previous last RateCard and paste your new RateCard below. You need RateCard of all existing instance types. 

Before 
```bash
{"DimensionKey": "d3en.12xlarge","Price": "3.35"},
{"DimensionKey": "m6i.8xlarge","Price": "2.23"},
{"DimensionKey": "r7iz.12xlarge","Price": "3.35"}
``` 
After 
```bash
{"DimensionKey": "d3en.12xlarge","Price": "3.35"},
{"DimensionKey": "m6i.8xlarge","Price": "2.23"},
{"DimensionKey": "r7iz.12xlarge","Price": "3.35"},
{"DimensionKey": "r5n.2xlarge","Price": "0.55"},
{"DimensionKey": "m6id.4xlarge","Price": "1.11"},
{"DimensionKey": "x2idn.16xlarge","Price": "4.47"}
```
### 12. Updating the dimension and price 

```bash
python3 start_changeset.py
```

