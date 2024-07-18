# etl/extract.
import pandas as pd 
import yaml
# Load configuration from config.yml
with open("config.yml", "r") as config_file:
        config = yaml.safe_load(config_file)
        print(config)
 
        # Extract data
        #data = extract_data(config['input_file_path'])
       # logging.info("Data extraction successful....")
#input_file_path = "data/raw_store_transactions.csv"
#data = pd.read_csv(config)
#print(data.head(2))

#def extract_data(input_file_path):
    #try:
        #data = pd.read_csv(input_file_path)
        #return data
    #except Exception as e:
        #raise Exception(f"Error while extracting dataset: {str(e)}")




