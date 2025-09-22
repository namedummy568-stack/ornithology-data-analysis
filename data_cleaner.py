# Python script to clean bird migration data
import pandas as pd

def clean_migration_data(file_path):
    """
    Reads a CSV file, cleans the bird migration data, and saves it to a new CSV.
    """
    try:
        df = pd.read_csv(file_path)

        # Convert 'MigrationDate' to datetime objects
        df['MigrationDate'] = pd.to_datetime(df['MigrationDate'])

        # Drop rows with any missing values
        df.dropna(inplace=True)

        # Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # Ensure LocationLat is within -90 and 90, and LocationLon is within -180 and 180
        df = df[(df['LocationLat'] >= -90) & (df['LocationLat'] <= 90)]
        df = df[(df['LocationLon'] >= -180) & (df['LocationLon'] <= 180)]

        # Example of a more complex cleaning rule: standardize DeviceModel names
        df['DeviceModel'] = df['DeviceModel'].replace({
            'GPS-V2.1': 'GPS-Model-A',
            'GPS-V3.0': 'GPS-Model-B',
            'GPS-V2.5': 'GPS-Model-A' # Assuming V2.5 is similar to V2.1
        })

        output_file_path = file_path.replace('.csv', '_cleaned.csv')
        df.to_csv(output_file_path, index=False)
        print(f"Cleaned data saved to {output_file_path}")
        return df
    except Exception as e:
        print(f"An error occurred during data cleaning: {e}")
        return None

if __name__ == "__main__":
    # Assuming the script is run from the root of the repository
    clean_migration_data('migration_data.csv')
