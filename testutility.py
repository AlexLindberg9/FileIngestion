
import yaml

def read_config_file(filepath):
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)

def validate_columns(df, table_config): 
    df.columns = df.columns.str.replace(' ', '')
    df_columns = list(df.columns)
    table_config['columns'] = list(map(lambda x: x.replace(' ',''), table_config['columns']))
    
    df_columns.sort()
    table_config['columns'].sort()
    
    if df_columns == table_config['columns']: 
        print('Column name and length validation successful!')
        return 1
    else: 
        print('Column name and length validation failed!')
        mismatch_yaml = list(set(df_columns).difference(table_config['columns']))
        print('These file columns are not in the YAML file:', mismatch_yaml)
        mismatch_file = list(set(table_config['columns']).difference(df_columns))
        print('These YAML columns are not in the file uploaded:', mismatch_file)
        return 0
