# AWS Marketplace Product and Offer ID Extraction

This repository contains scripts and instructions to extract Product and Offer IDs from the AWS Marketplace Catalog API and convert them into a simplified Excel file.

## Overview

When updating the instance type and pricing using the AWS Marketplace Catalog API, you first need to retrieve the Product ID and Offer ID. This repository guides you through the following steps:

1. **Extracting Product and Offer IDs:** Retrieve the IDs using the AWS CLI.
2. **Converting `product.json` to an Excel File:** Use a Python script to generate an Excel file containing only the Product ID and Offer ID.

## Prerequisites

- **AWS CLI:** Installed and configured with the appropriate credentials.
- **Python 3.x:** Installed on your system.

## Steps

### 1. Clone the Original AWS Repository

Clone the AWS Marketplace reference code repository:

```bash
git clone https://github.com/aws-samples/aws-marketplace-reference-code.git
```
Below is the revised section with the added documentation links:

### 2. Follow the Documentation for Python

Change directory to the Python section:

```bash
cd aws-marketplace-reference-code/python
```

Install all necessary dependencies as mentioned in the [Python Documentation](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/python). Then navigate to the following directory to add dimensions:

```bash
cd src/catalog_api/products/ami/add_dimension_to_ami_product_and_set_price_in_public_offer
```

For more details on working with single AMI products, please refer to the [AWS Marketplace API Documentation](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-single-ami-products.html).


### 3. Clone the New Repository

Clone your new repository:

```bash
git clone https://github.com/TamangPemba/aws_product_dimension_price_update.git
cd aws_product_dimension_price_update
```

### 4. Install the Necessary Python Libraries

Install the required Python packages using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```
### 5. Extracting Product and Offer IDs

Run the following command to extract the Product and Offer IDs from the AWS Marketplace Catalog API. The output is stored in a file named `product.json`.

```bash
aws marketplace-catalog list-entities --catalog AWSMarketplace --entity-type Offer > product.json
```

### 6. Converting `product.json` to an Excel File

Use the provided Python script `offer_prod_id.py` to convert `product.json` into an Excel file that contains only the Product ID and Offer ID. The script performs the following actions:

- Reads `product.json`.
- Extracts the Product ID and Offer ID from each entity in the `EntitySummaryList`.
- Writes the extracted data to an Excel file named `product_offer_ids.xlsx`.

To run the script, execute:

```bash
python3 offer_prod_id.py
```

### 7. Viewing the Excel File from the Command Line

```bash
xlsx2csv product_offer_ids.xlsx
```

### 8. Create a New File for Instance Types

Create a file named `instance_type.txt` and copy the instance types along with their corresponding prices into it. This will used for to add new dimensions.
For example:

```
r5n.2xlarge    0.55
m6id.4xlarge   1.11
x2idn.16xlarge 4.47
```

---

### 9. Update the File `add_type.txt`

Paste the instance types that you want to add into `add_type.txt`. For example:

```bash
m3.xlarge
c6a.large
c6a.16xlarge
c6id.8xlarge
m5dn.2xlarge
c7i.48xlarge
hs1.8xlarge
m6in.12xlarge
```

Then, execute the `add_type.py` script:

```bash
python3 add_type.py
```

This will generate a new file called `type.json`. Copy the contents of that file and update the `changeset.json` file accordingly. For example:

```bash
"DetailsDocument": {"InstanceTypes": ["m3.xlarge", "c6a.large", "c6a.16xlarge", "c6id.8xlarge", "m5dn.2xlarge", "c7i.48xlarge", "hs1.8xlarge", "m6in.12xlarge"]},
```

### 10. Generating the Dimension and RateCard

Run the following command to generate the dimension and RateCard JSON using the `update.py` script:

```bash
python3 update.py
```

You should see output similar to:

```json
{
  "DetailsDocument": [
    {"Key": "r5n.2xlarge", "Name": "r5n.2xlarge", "Description": "r5n.2xlarge", "Unit": "Hrs", "Types": ["Metered"]},
    {"Key": "m6id.4xlarge", "Name": "m6id.4xlarge", "Description": "m6id.4xlarge", "Unit": "Hrs", "Types": ["Metered"]},
    {"Key": "x2idn.16xlarge", "Name": "x2idn.16xlarge", "Description": "x2idn.16xlarge", "Unit": "Hrs", "Types": ["Metered"]}
  ],
  "RateCard": [
    {"DimensionKey": "r5n.2xlarge", "Price": "0.55"},
    {"DimensionKey": "m6id.4xlarge", "Price": "1.11"},
    {"DimensionKey": "x2idn.16xlarge", "Price": "4.47"}
  ]
}
```

### 11. Updating `changeset.json` for Dimensions

Open the `changeset.json` file and update the `DetailsDocument` section with the new dimensions. For example:

```json
"DetailsDocument": [
  {"Key": "r5n.2xlarge", "Name": "r5n.2xlarge", "Description": "r5n.2xlarge", "Unit": "Hrs", "Types": ["Metered"]},
  {"Key": "m6id.4xlarge", "Name": "m6id.4xlarge", "Description": "m6id.4xlarge", "Unit": "Hrs", "Types": ["Metered"]},
  {"Key": "x2idn.16xlarge", "Name": "x2idn.16xlarge", "Description": "x2idn.16xlarge", "Unit": "Hrs", "Types": ["Metered"]}
]
```

**Note:** You must update this each time you add a new instance type. If an instance type is already present, the script will generate an error.

### 12. Updating the RateCard

Update the `RateCard` section in `changeset.json`. When updating the RateCard, add a comma (`,`) after the previous last entry and paste your new RateCard entries below. You must include RateCards for all existing instance types.

**Before:**

```json
{"DimensionKey": "d3en.12xlarge", "Price": "3.35"},
{"DimensionKey": "m6i.8xlarge", "Price": "2.23"},
{"DimensionKey": "r7iz.12xlarge", "Price": "3.35"}
```

**After:**

```json
{"DimensionKey": "d3en.12xlarge", "Price": "3.35"},
{"DimensionKey": "m6i.8xlarge", "Price": "2.23"},
{"DimensionKey": "r7iz.12xlarge", "Price": "3.35"},
{"DimensionKey": "r5n.2xlarge", "Price": "0.55"},
{"DimensionKey": "m6id.4xlarge", "Price": "1.11"},
{"DimensionKey": "x2idn.16xlarge", "Price": "4.47"}
```

### 12. Updating the Dimension and Price

Finally, update the dimensions and pricing by running the following command:

```bash
python3 start_changeset.py
```

---
Thank You
---

