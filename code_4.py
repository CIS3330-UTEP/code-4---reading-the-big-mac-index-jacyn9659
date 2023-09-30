import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[(df['date'] == year) & (df['iso_a3'] == country_code)]
    mean_price = round(float(filtered_df['dollar_price'].mean()),2)

    return mean_price
    
                

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[df['iso_a3'] == country_code]
    mean_price_country = round(float(filtered_df['dollar_price'].mean()),2)

    return mean_price_country 
   

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[df['date'] == year]
    cheapest_big_mac_price = filtered_df.loc[filtered_df['dollar_price'].idxmin()]

    return cheapest_big_mac_price
  

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[df['date'] == year]
    expensive_big_mac_price = filtered_df.loc[filtered_df['dollar_price'].idxmax()]

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
    
    
    
    
