#!/usr/bin/env python3

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import argparse
import pandas as pd

def read_excel_data(file_path, n=None):
    # Read data from the Excel file
    df = pd.read_excel(file_path, engine='openpyxl')

    # If the --scrape flag is used, return the first n rows
    if n is not None:
        df = df.head(n)

    return df

def main():

    install("pandas")
    install("openpyxl")
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Scrape data from an Excel file.')
    parser.add_argument('--scrape', type=int, help='Scrape the first N entries of the dataset')
    parser.add_argument('--save', type=str, help='Save the scraped dataset to the specified file path')

    args = parser.parse_args()

    # Read data from the Excel file
    file_path = 'pems_0416i10.xlsx'
    scraped_data = read_excel_data(file_path, n=args.scrape)

    # If the --save flag is used, save the data to the specified file
    if args.save:
        scraped_data.to_csv(args.save, index=False)
        print(f'Data saved to {args.save}')
    else:
        # Print the scraped data to standard output
        print(scraped_data)

if __name__ == '__main__':
    main()
