import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[(df['date'].str[:4] == str(year)) & (df['iso_a3'] == country_code.upper())]
    mean_price = round(float(filtered_df['dollar_price'].mean()),2)

    return mean_price
    
                

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    country_df = df[df['iso_a3'] == country_code.upper()]
    mean_price_country = round(float(country_df['dollar_price'].mean()),2)

    return mean_price_country 
   

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_Year = df.query(query)
    min_df = df_Year['dollar_price'].idxmin()
    min_mac = df.loc[min_df]
    cheapest_big_mac_price = (f"{min_mac['name']}({min_mac['iso_a3']}): ${round(min_mac['dollar_price'],2)}")
    
    return cheapest_big_mac_price
  
def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_Year = df.query(query)
    max_df = df_Year['dollar_price'].idxmax()
    max_mac = df.loc[max_df]
    expensive_big_mac_price = (f"{max_mac['name']}({max_mac['iso_a3']}): ${round(max_mac['dollar_price'],2)}")
 
    return expensive_big_mac_price
    

if __name__ == "__main__":
    country = input("enter country code: ")
    year = int(input(" enter year: "))
    mean_price_year = get_big_mac_price_by_year(year, country)
    mean_price_country = get_big_mac_price_by_country(country)
    cheapest_price = get_the_cheapest_big_mac_price_by_year(year)
    most_expensive_price = get_the_most_expensive_big_mac_price_by_year(year)
    print(f"Mean Big Mac price in {country} in {year}: ${mean_price_year}")
    print(f"Mean Big Mac price in {country}: ${mean_price_country}")
    print(f"The cheapest Big Mac in {year}: {cheapest_price['name']}({cheapest_price['iso_a3']}): ${round(cheapest_price['dollar_price'], 2)}")
    print(f"The most expensive Big Mac in {year}: {most_expensive_price['name']}({most_expensive_price['iso_a3']}): ${round(most_expensive_price['dollar_price'], 2)}")
    
    
    
    
