import pandas as pd
import requests

# Function to download the dataset
def download_dataset(url, file_name):
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Dataset downloaded successfully as {file_name}")
    else:
        print(f"Failed to download dataset. Status code: {response.status_code}")

# Function to perform data transformations and fix errors
def transform_and_fix_errors(input_file, output_file):
    # Read the dataset into a DataFrame
    df = pd.read_csv(input_file , encoding='latin-1', header=7, on_bad_lines='skip')

    # Perform your data transformations and error fixes here
    # Example: Fixing missing values
    df.fillna(value=0, inplace=True)

    # Save the transformed dataset
    df.to_csv(output_file, index=False)
    print(f"Transformed dataset saved as {output_file}")

# Function to perform data cleaning
def clean_dataset(input_file, output_file):
    # Read the dataset into a DataFrame
    df = pd.read_csv(input_file)

    # Perform data cleaning operations
    # Example: Drop duplicates
    df.drop_duplicates(inplace=True)

    # Save the cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"Cleaned dataset saved as {output_file}")

if __name__ == "__main__":
    # URLs of the datasets to download
    dataset_url1 = "https://www.landesdatenbank.nrw.de/ldbnrwws/downloader/00/tables/23111-01d_00.csv"
    dataset_url2 = "https://www.landesdatenbank.nrw.de/ldbnrwws/downloader/00/tables/23112-04i_00.csv"

    # Local file names
    downloaded_file1 = "downloaded_dataset1.csv"
    downloaded_file2 = "downloaded_dataset2.csv"
    transformed_file1 = "transformed_dataset1.csv"
    transformed_file2 = "transformed_dataset2.csv"
    cleaned_file1 = "cleaned_dataset1.csv"
    cleaned_file2 = "cleaned_dataset2.csv"

    # Step 1: Download the datasets
    download_dataset(dataset_url1, downloaded_file1)
    download_dataset(dataset_url2, downloaded_file2)

    # Step 2: Transform the datasets and fix errors
    transform_and_fix_errors(downloaded_file1, transformed_file1)
    transform_and_fix_errors(downloaded_file2, transformed_file2)

    # Step 3: Clean the datasets
    clean_dataset(transformed_file1, cleaned_file1)
    clean_dataset(transformed_file2, cleaned_file2)
