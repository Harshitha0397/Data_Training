# read_csv.py
import csv 
 
def read_csv(file_path): 
    try: 
        with open(file_path, mode='r', newline='') as csvfile: 
            reader = csv.reader(csvfile) 
            # Read header 
            header = next(reader) 
            print("Header:", header) 
            # Iterate over rows 
            row_count = 0 
            for row in reader: 
                print("Row:", row) 
                row_count += 1 
            print(f"Total rows (excluding header): {row_count}") 
    except FileNotFoundError: 
        print(f"Error: File not found - {file_path}") 
    except Exception as e: 
        print("Error while reading CSV:", str(e)) 
 
if __name__ == "__main__": 
    read_csv("sample_data.csv")