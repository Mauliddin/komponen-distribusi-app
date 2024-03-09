import csv

class Read():
    @staticmethod
    def read_data():
        file_csv = "data/komponen.csv"
        with open(file_csv) as file:
            csv_reader = csv.reader(file, delimiter=";")
            data = list(csv_reader)
        
        ids = [row[0] for row in data]
        komponen = [row[1] for row in data]
        aug_image = [row[2] for row in data]
        
        return ids, komponen, aug_image
