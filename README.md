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

## Repository Structure

- **`product.json`**: File generated by the AWS CLI command containing raw API output.
- **`offer_prod_id.py`**: Python script that extracts Product ID and Offer ID and generates an Excel file.
- **`product_offer_ids.xlsx`**: Output Excel file containing the extracted IDs.
- **`requirements.txt`**: List of Python packages required for the scripts.
- **`README.md`**: This documentation file.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.

## License

[Insert your license information here.]
EOF
```

This command will create a file named `README.md` in your current directory with the contents above. You can then commit and push the file to your GitHub repository.
