from pathlib import Path
import pandas as pd


# Project directories
DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def inspect_dataset(file_path):
    """Inspect the structure and quality of a CSV dataset."""

    print("\n" + "=" * 70)
    print(f"DATASET: {file_path.name}")
    print("=" * 70)

    # World Bank CSV files contain 4 metadata rows before the table
    if file_path.name.startswith("API_"):
        df = pd.read_csv(file_path, skiprows=4)
    else:
        df = pd.read_csv(file_path)

    
    print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")

   
    print("\nColumns:")
    for column in df.columns:
        print(f"- {column}")

    
    print("\nData types:")
    print(df.dtypes)


    print("\nFirst 5 rows:")
    print(df.head().to_string())

    
    print("\nMissing values:")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("No missing values.")
    else:
        for column, count in missing.items():
            percentage = (count / len(df)) * 100
            print(f"- {column}: {count} ({percentage:.1f}%)")

   
    empty_columns = [
        column for column in df.columns
        if df[column].isnull().all()
    ]

    print("\nCompletely empty columns:")

    if empty_columns:
        for column in empty_columns:
            print(f"- {column}")
    else:
        print("None")

   
    print(f"\nDuplicate rows: {df.duplicated().sum()}")

   
    date_columns = [
        column
        for column in df.columns
        if "date" in column.lower() or "time" in column.lower()
    ]

    print("\nPossible date/time columns:")

    if date_columns:
        for column in date_columns:
            print(f"- {column}")

            converted_dates = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            valid_dates = converted_dates.dropna()

            if not valid_dates.empty:
                print(
                    f"  Date range: "
                    f"{valid_dates.min().date()} to "
                    f"{valid_dates.max().date()}"
                )
    else:
        print("None")

    
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    print("\nNumeric columns:")

    if numeric_columns:
        print(", ".join(numeric_columns))
    else:
        print("None")

    print()


def main():
    """Inspect all CSV files inside the data directory."""

    csv_files = sorted(DATA_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in the data directory.")
        return

    print(f"Found {len(csv_files)} CSV file(s).")

    for file_path in csv_files:
        try:
            inspect_dataset(file_path)

        except Exception as error:
            print(f"\nERROR inspecting {file_path.name}:")
            print(error)


if __name__ == "__main__":
    main()