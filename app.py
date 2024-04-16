#import internal and external Libraries
import sys
import glob
import os
import json
import re
import pandas as pd

# create the get column func to create the schema dynamically
def get_column_names(schemas, ds_name, sorting_key='column_position'):
    column_details = schemas[ds_name]
    columns = sorted(column_details, key=lambda col: col[sorting_key])
    return [col['column_name'] for col in columns]

# read the csv data from the file and create dataframe

def read_csv(file, schemas):
    file_path_list = re.split('[/\\\]', file)
    ds_name = file_path_list[-2]
    columns = get_column_names(schemas, ds_name)
    df = pd.read_csv(file, names=columns)
    return df

# Create to_json function which takes the df and convert csv into json
def to_json(df, tgt_base_dir, ds_name, file_name):
    json_file_path = f'{tgt_base_dir}/{ds_name}/{file_name}'
    os.makedirs(f'{tgt_base_dir}/{ds_name}', exist_ok=True)
    df.to_json(
        json_file_path,
        orient='records',
        lines=True
    )
  
def file_converter(src_base_dir,tgt_base_dir,ds_name):

    schemas = json.load(open(f'{src_base_dir}/schemas.json'))
    files = glob.glob(f'{src_base_dir}/{ds_name}/part-*')
    if len(files) == 0:
       raise NameError(f"No Files found for {ds_name}")

    for file in files:
        #print(f'Processing {file}')
        df = read_csv(file, schemas)
        file_name = re.split('[/\\\]', file)[-1]
        to_json(df, tgt_base_dir, ds_name, file_name)

def process_files(ds_names = None):
  src_base_dir = os.environ.get('SRC_BASE_DIR')
  tgt_base_dir = os.environ.get('TGT_BASE_DIR')
  schemas = json.load(open(f'{src_base_dir}/schemas.json'))
  if not ds_names:
    ds_names = schemas.keys()
  for ds_name in ds_names:
    try:
      print(f'Processing {ds_name}')
      file_converter(src_base_dir,tgt_base_dir,ds_name)
    except NameError as ne:
       print(ne)
       print(f"Error processing {ds_name}")
       pass


if __name__ == '__main__':
      if len(sys.argv) == 2:
        ds_name = json.loads(sys.argv[1])
        process_files(ds_name) 
      else:
         process_files()