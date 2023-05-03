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


import matplotlib.pyplot as plt
import seaborn as sns

def create_visualization(df):
    lane_columns = [col for col in df.columns if col.startswith('Lane') and col.endswith('Speed')]
    lane_speed_averages = df[lane_columns].mean()

    plt.figure(figsize=(8, 6))
    sns.barplot(x=lane_speed_averages.index, y=lane_speed_averages.values)
    plt.xlabel('Lane Number')
    plt.ylabel('Average Speed')
    plt.title('Average Speed by Lane')
    plt.savefig('average_speed_by_lane.png')
    print('Visualization saved as average_speed_by_lane.png')



def main():

    install("pandas")
    install("openpyxl")
    install("matplotlib")
    install("seaborn")
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Scrape data from an Excel file.')
    parser.add_argument('--scrape', type=int, help='Scrape the first N entries of the dataset')
    parser.add_argument('--save', type=str, help='Save the scraped dataset to the specified file path')
    parser.add_argument('--viz', action='store_true', help='Create a visualization of the average speed by lane')
    args = parser.parse_args()

    # Read data from the Excel file
    file_path = 'pems_0416i10.xlsx'
    scraped_data = read_excel_data(file_path, n=args.scrape)

    # If the --viz flag is used, create the visualization
    if args.viz:
        create_visualization(scraped_data)

    # If the --save flag is used, save the data to the specified file
    if args.save:
        scraped_data.to_csv(args.save, index=False)
        print(f'Data saved to {args.save}')
    else:
        # Print the scraped data to standard output
        print(scraped_data)

if __name__ == '__main__':
    main()
