import json
import pandas as pd

json_file_path = 'product.json'

def extract_product_and_offer_ids(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    extracted_data = []

    for entity in data['EntitySummaryList']:
        product_id = entity['OfferSummary']['ProductId']
        offer_id = entity['EntityId']

        extracted_data.append({
            'ProductId': product_id,
            'OfferId': offer_id
        })

    return extracted_data

def save_to_excel(extracted_data, file_path):
    df = pd.DataFrame(extracted_data)

    # Save to Excel file
    df.to_excel(file_path, index=False)
    print(f"Data saved to {file_path}")

def main():
    extracted_data = extract_product_and_offer_ids(json_file_path)

    excel_file_path = 'product_offer_ids.xlsx'

    save_to_excel(extracted_data, excel_file_path)

if __name__ == "__main__":
    main()


