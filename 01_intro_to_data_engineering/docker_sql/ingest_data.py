# #!/usr/bin/env python
# # coding: utf-8
# import argparse
# from time import time
# import pandas as pd
# from sqlalchemy import create_engine
# import os
# import gzip
# import shutil


# # define the main function
# def main(params):
#     user = params.user
#     password = params.password
#     host = params.host
#     port = params.port
#     db = params.db
#     table_name = params.table_name
#     url = params.url
#     csv_name = 'output.csv'

#     # download the csv
#     os.system(f"wget {url} -O {csv_name}")

#     # decompress the csv.gz
#     with gzip.open(yellow_tripdata_2021-01.csv.gz, 'rb') as f_in:
#         with open(csv_name, 'wb') as f_out:
#             shutil.copyfileobj(f_in, f_out)

#     engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

#     # read data in chunks
#     df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)


#     df = next(df_iter)


#     df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
#     df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


#     # create table's header
#     df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')


#     # ingestion iteration
#     while True:
#         try:
#             t_start = time()
        
#             df = next(df_iter)
        
#             df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
#             df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            
#             df.to_sql(name=table_name, con=engine, if_exists='append')
        
#             t_end = time()
        
#             print('inserted another chunk, took %.3f second' % (t_end - t_start))
#         except:
#             print('Data ingestion completed.')
#             break


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

#     # user, password, host, port, database name, table name, url of the csv
#     parser.add_argument('--user', help='username for postgres database')
#     parser.add_argument('--password', help='password for postgres database')
#     parser.add_argument('--host', help='host for postgres database')
#     parser.add_argument('--port', help='port for postgres database')
#     parser.add_argument('--db', help='database name for postgres database')
#     parser.add_argument('--table_name', help='table name for postgres database')
#     parser.add_argument('--url', help='url of the csv file')

#     args = parser.parse_args()

#     main(args)



#!/usr/bin/env python
# coding: utf-8
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine
import os
import gzip
import shutil

# define the main function
def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_gz_name = 'output.csv.gz'
    csv_name = 'output.csv'

    # download the csv.gz
    os.system(f"wget {url} -O {csv_gz_name}")

    # decompress the csv.gz
    with gzip.open(csv_gz_name, 'rb') as f_in:
        with open(csv_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # read data in chunks
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # create table's header
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # ingestion iteration
    while True:
        try:
            t_start = time()

            df = next(df_iter)

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))
        except StopIteration:
            print('Data ingestion completed.')
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    # user, password, host, port, database name, table name, url of the csv
    parser.add_argument('--user', help='username for postgres database')
    parser.add_argument('--password', help='password for postgres database')
    parser.add_argument('--host', help='host for postgres database')
    parser.add_argument('--port', help='port for postgres database')
    parser.add_argument('--db', help='database name for postgres database')
    parser.add_argument('--table_name', help='table name for postgres database')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)
