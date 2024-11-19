import singer
import pandas as pd

LOGGER = singer.get_logger()

# Schema definition
schema = {
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'date_utc': {'type': 'string', 'format': 'date-time'},
    }
}

def main():
    url = 'https://api.spacexdata.com/v4/launches'
    df = pd.read_json(url)
    
    # Convert DataFrame to records
    records = df.to_dict(orient='records')

    # Write schema and records to Singer
    singer.write_schema('launches', schema, 'id')
    singer.write_records('launches', records)

if __name__ == '__main__':
    main()
