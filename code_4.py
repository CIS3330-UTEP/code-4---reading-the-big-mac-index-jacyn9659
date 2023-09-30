import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[(df['year'] == year) & (df['iso_a3'] == coountry_code)]
    mean_price = round(float(filtered_df['dollar_price'].mean()),2)

    return mean_price
    
                

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[df['iso_a3'] == country_code]
    mean_price_country = round(float(filtered_df['dollar_price'].mean()),2)

    return mean_price_country 
   

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[df['year'] == year]
    cheapest_big_mac_price = filtered_df.loc[filtered_df['dollar_price'].idxmin()]

    return cheapest_big_mac_price
  

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[df['year'] == year]
    expensive_big_mac_price = filtered_df.loc[filtered_df['dollar_price'].idxmax()]

    return expensive_big_mac_price
    

if __name__ == "__main__":
    country = input("enter country code: ")
    year = int(input(" enter year: "))
    get_big_mac_price_by_year(year, country)
    get_big_mac_price_by_country(country)
    get_the_cheapest_big_mac_price_by_year(year)
    get_the_expensive_big_mac_by_price(year)
    
    
    
