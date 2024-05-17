import pandas as pd
import json


#Read json file

print("Loading case.json file...") 
with open('data/raw/case.json', 'r') as file:
    data = json.load(file)

def curatedOfferOptions(data):
    """
    This function extracts curated offer events

    Args:
        data (dict): a dictionary of data extracted from json file

    Returns:
        DataFrame: A DataFrame of details of curated offer events

    """
    curated_offer_options = []

    for item in data:
        if "CurationProvider" in item["payload"]:
            payload = json.loads(item["payload"])

            for curation_provider in payload:
                for option in curation_provider['options']:
                    row = { 'OfferId' : curation_provider['offerId'],
                          'DealerId' : curation_provider['dealerId'],
                          'UniqueOptionId' : option['uniqueOptionId'],
                          'OptionId' : option['optionId'],
                          'IsMobileDealer' : option['isMobileDealer'],
                          'IsOpen' : option['isOpen'],
                          'ETA' : option['eta'],
                          'ChamaScore' : option['chamaScore'],
                          'ProductBrand' : option['productBrand'],
                          'IsWinner' : option['isWinner'],
                          'MinimumPrice' : option['minimumPrice'],
                          'MaximumPrice' : option['maximumPrice'],
                          'DynamicPrice' : option['dynamicPrice'],
                          'FinalPrice' : option['finalPrice'],
                          #return value if present
                          'DefeatPrimaryReason': (option.get('defeatPrimaryReason', "")),
                          'DefeatReasons': ', '.join(option.get('defeatReasons', [])),
                          'EnqueuedTimeSP' : pd.Timestamp(item['EnqueuedTimeUtc']).tz_convert('America/Sao_Paulo').strftime('%d/%m/%Y')
                          }
                    curated_offer_options.append(row)
    return pd.DataFrame(curated_offer_options)

def dynamicPriceOption():
    pass

def dynamicPriceRange():
    pass

def main():
    pass

if __name__ == "__main__":
    main()