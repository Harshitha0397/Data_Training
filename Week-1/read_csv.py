# Enhanced version snippet
import os 
 
def read_csv(file_path):
   if not os.path.exists(file_path): 
        print(f"Error: The file {file_path} does not exist.") 
        return 
    try: 
        with open(file_path, mode='r', newline='') as csvfile: 
            reader = csv.reader(csvfile) 
            header = next(reader, None) 
            if header is None: 
                print("CSV file is empty!") 
                return 
            print("Header:", header) 
            count = 0 
            for row in reader: 
                print("Row:", row) 
                count += 1 
            print(f"Total rows: {count}") 
    except Exception as e: 
        print("Unexpected error:", e)