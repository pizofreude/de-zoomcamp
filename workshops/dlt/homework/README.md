# **Workshop "Data Ingestion with dlt": Homework**


---

## **Dataset & API**

We’ll use **NYC Taxi data** via the same custom API from the workshop:

🔹 **Base API URL:**  
```
https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api
```
🔹 **Data format:** Paginated JSON (1,000 records per page).  
🔹 **API Pagination:** Stop when an empty page is returned.  

## **Question 1: dlt Version**

1. **Install dlt**:


```python
 !pip install dlt[duckdb]
```

    Collecting dlt[duckdb]
      Downloading dlt-1.6.1-py3-none-any.whl.metadata (11 kB)
    Requirement already satisfied: PyYAML>=5.4.1 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (6.0.2)
    Requirement already satisfied: click>=7.1 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (8.1.8)
    Requirement already satisfied: duckdb>=0.9 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (1.1.3)
    Requirement already satisfied: fsspec>=2022.4.0 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (2024.10.0)
    Requirement already satisfied: gitpython>=3.1.29 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (3.1.44)
    Collecting giturlparse>=0.10.0 (from dlt[duckdb])
      Downloading giturlparse-0.12.0-py2.py3-none-any.whl.metadata (4.5 kB)
    Collecting hexbytes>=0.2.2 (from dlt[duckdb])
      Downloading hexbytes-1.3.0-py3-none-any.whl.metadata (3.3 kB)
    Requirement already satisfied: humanize>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (4.11.0)
    Collecting jsonpath-ng>=1.5.3 (from dlt[duckdb])
      Downloading jsonpath_ng-1.7.0-py3-none-any.whl.metadata (18 kB)
    Collecting makefun>=1.15.0 (from dlt[duckdb])
      Downloading makefun-1.15.6-py2.py3-none-any.whl.metadata (3.2 kB)
    Requirement already satisfied: orjson!=3.10.1,!=3.9.11,!=3.9.12,!=3.9.13,!=3.9.14,<4,>=3.6.7 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (3.10.15)
    Requirement already satisfied: packaging>=21.1 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (24.2)
    Collecting pathvalidate>=2.5.2 (from dlt[duckdb])
      Downloading pathvalidate-3.2.3-py3-none-any.whl.metadata (12 kB)
    Collecting pendulum>=2.1.2 (from dlt[duckdb])
      Downloading pendulum-3.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.9 kB)
    Requirement already satisfied: pluggy>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (1.5.0)
    Requirement already satisfied: pytz>=2022.6 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (2025.1)
    Requirement already satisfied: requests>=2.26.0 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (2.32.3)
    Requirement already satisfied: requirements-parser>=0.5.0 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (0.9.0)
    Collecting rich-argparse<2.0.0,>=1.6.0 (from dlt[duckdb])
      Downloading rich_argparse-1.7.0-py3-none-any.whl.metadata (14 kB)
    Collecting semver>=3.0.0 (from dlt[duckdb])
      Downloading semver-3.0.4-py3-none-any.whl.metadata (6.8 kB)
    Requirement already satisfied: setuptools>=65.6.0 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (75.1.0)
    Collecting simplejson>=3.17.5 (from dlt[duckdb])
      Downloading simplejson-3.20.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.2 kB)
    Requirement already satisfied: tenacity>=8.0.2 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (9.0.0)
    Collecting tomlkit>=0.11.3 (from dlt[duckdb])
      Downloading tomlkit-0.13.2-py3-none-any.whl.metadata (2.7 kB)
    Requirement already satisfied: typing-extensions>=4.8.0 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (4.12.2)
    Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.11/dist-packages (from dlt[duckdb]) (2025.1)
    Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython>=3.1.29->dlt[duckdb]) (4.0.12)
    Requirement already satisfied: ply in /usr/local/lib/python3.11/dist-packages (from jsonpath-ng>=1.5.3->dlt[duckdb]) (3.11)
    Requirement already satisfied: python-dateutil>=2.6 in /usr/local/lib/python3.11/dist-packages (from pendulum>=2.1.2->dlt[duckdb]) (2.8.2)
    Collecting time-machine>=2.6.0 (from pendulum>=2.1.2->dlt[duckdb])
      Downloading time_machine-2.16.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (21 kB)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests>=2.26.0->dlt[duckdb]) (3.4.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests>=2.26.0->dlt[duckdb]) (3.10)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests>=2.26.0->dlt[duckdb]) (2.3.0)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests>=2.26.0->dlt[duckdb]) (2025.1.31)
    Requirement already satisfied: types-setuptools>=69.1.0 in /usr/local/lib/python3.11/dist-packages (from requirements-parser>=0.5.0->dlt[duckdb]) (75.8.0.20250210)
    Requirement already satisfied: rich>=11.0.0 in /usr/local/lib/python3.11/dist-packages (from rich-argparse<2.0.0,>=1.6.0->dlt[duckdb]) (13.9.4)
    Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython>=3.1.29->dlt[duckdb]) (5.0.2)
    Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.6->pendulum>=2.1.2->dlt[duckdb]) (1.17.0)
    Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=11.0.0->rich-argparse<2.0.0,>=1.6.0->dlt[duckdb]) (3.0.0)
    Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=11.0.0->rich-argparse<2.0.0,>=1.6.0->dlt[duckdb]) (2.18.0)
    Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=11.0.0->rich-argparse<2.0.0,>=1.6.0->dlt[duckdb]) (0.1.2)
    Downloading giturlparse-0.12.0-py2.py3-none-any.whl (15 kB)
    Downloading hexbytes-1.3.0-py3-none-any.whl (4.9 kB)
    Downloading jsonpath_ng-1.7.0-py3-none-any.whl (30 kB)
    Downloading makefun-1.15.6-py2.py3-none-any.whl (22 kB)
    Downloading pathvalidate-3.2.3-py3-none-any.whl (24 kB)
    Downloading pendulum-3.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (384 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m384.9/384.9 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading rich_argparse-1.7.0-py3-none-any.whl (25 kB)
    Downloading semver-3.0.4-py3-none-any.whl (17 kB)
    Downloading simplejson-3.20.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (144 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m144.8/144.8 kB[0m [31m12.6 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading tomlkit-0.13.2-py3-none-any.whl (37 kB)
    Downloading dlt-1.6.1-py3-none-any.whl (884 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m884.3/884.3 kB[0m [31m28.5 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading time_machine-2.16.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (32 kB)
    Installing collected packages: makefun, tomlkit, simplejson, semver, pathvalidate, jsonpath-ng, hexbytes, giturlparse, time-machine, rich-argparse, pendulum, dlt
    Successfully installed dlt-1.6.1 giturlparse-0.12.0 hexbytes-1.3.0 jsonpath-ng-1.7.0 makefun-1.15.6 pathvalidate-3.2.3 pendulum-3.0.0 rich-argparse-1.7.0 semver-3.0.4 simplejson-3.20.1 time-machine-2.16.0 tomlkit-0.13.2
    

> Or choose a different bracket—`bigquery`, `redshift`, etc.—if you prefer another primary destination. For this assignment, we’ll still do a quick test with DuckDB.

2. **Check** the version:



```python
!dlt --version
```

    [39mdlt 1.6.1[0m
    

or:


```python
import dlt
print("dlt version:", dlt.__version__)
```

    dlt version: 1.6.1
    



**Answer**:  
- Provide the **version** you see in the output.

> dlt 1.6.1

## **Question 2: Define & Run the Pipeline (NYC Taxi API)**

Use dlt to extract all pages of data from the API.

Steps:

1️⃣ Use the `@dlt.resource` decorator to define the API source.

2️⃣ Implement automatic pagination using dlt's built-in REST client.

3️⃣ Load the extracted data into DuckDB for querying.




```python
import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import PageNumberPaginator


# your code is here:
# Define the API resource for NYC taxi data
@dlt.resource(name="ny_taxi")   # <--- The name of the resource (will be used as the table name)
def ny_taxi():
    client = RESTClient(
        base_url="https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api",
        paginator=PageNumberPaginator(
            base_page=1,
            total_path=None
        )
    )

    for page in client.paginate("data_engineering_zoomcamp_api"):    # <--- API endpoint for retrieving taxi ride data
        yield page   # <--- yield data to manage memory

pipeline = dlt.pipeline(
    pipeline_name="ny_taxi_pipeline",
    destination="duckdb",
    dataset_name="ny_taxi_data"
)
```

Load the data into DuckDB to test:







```python
load_info = pipeline.run(ny_taxi)
print(load_info)
```

    Pipeline ny_taxi_pipeline load step completed in 2.12 seconds
    1 load package(s) were loaded to destination duckdb and into dataset ny_taxi_data
    The duckdb destination used duckdb:////content/ny_taxi_pipeline.duckdb location to store data
    Load package 1739804847.1155753 is LOADED and contains no failed jobs
    

Start a connection to your database using native `duckdb` connection and look what tables were generated:


```python
import duckdb
from google.colab import data_table
data_table.enable_dataframe_formatter()

# A database '<pipeline_name>.duckdb' was created in working directory so just connect to it

# Connect to the DuckDB database
conn = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")

# Set search path to the dataset
conn.sql(f"SET search_path = '{pipeline.dataset_name}'")

# Describe the dataset
conn.sql("DESCRIBE").df()
```





  <div id="df-7697be99-15f5-45e1-b793-ef78b3c71da7" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>database</th>
      <th>schema</th>
      <th>name</th>
      <th>column_names</th>
      <th>column_types</th>
      <th>temporary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ny_taxi_pipeline</td>
      <td>ny_taxi_data</td>
      <td>_dlt_loads</td>
      <td>[load_id, schema_name, status, inserted_at, sc...</td>
      <td>[VARCHAR, VARCHAR, BIGINT, TIMESTAMP WITH TIME...</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ny_taxi_pipeline</td>
      <td>ny_taxi_data</td>
      <td>_dlt_pipeline_state</td>
      <td>[version, engine_version, pipeline_name, state...</td>
      <td>[BIGINT, BIGINT, VARCHAR, VARCHAR, TIMESTAMP W...</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ny_taxi_pipeline</td>
      <td>ny_taxi_data</td>
      <td>_dlt_version</td>
      <td>[version, engine_version, inserted_at, schema_...</td>
      <td>[BIGINT, BIGINT, TIMESTAMP WITH TIME ZONE, VAR...</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ny_taxi_pipeline</td>
      <td>ny_taxi_data</td>
      <td>ny_taxi</td>
      <td>[end_lat, end_lon, fare_amt, passenger_count, ...</td>
      <td>[DOUBLE, DOUBLE, DOUBLE, BIGINT, VARCHAR, DOUB...</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-7697be99-15f5-45e1-b793-ef78b3c71da7')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-7697be99-15f5-45e1-b793-ef78b3c71da7 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-7697be99-15f5-45e1-b793-ef78b3c71da7');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


<div id="df-57a28b3c-a6fa-4335-ba6e-823fa4dbd7b6">
  <button class="colab-df-quickchart" onclick="quickchart('df-57a28b3c-a6fa-4335-ba6e-823fa4dbd7b6')"
            title="Suggest charts"
            style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
  </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

  <script>
    async function quickchart(key) {
      const quickchartButtonEl =
        document.querySelector('#' + key + ' button');
      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
      quickchartButtonEl.classList.add('colab-df-spinner');
      try {
        const charts = await google.colab.kernel.invokeFunction(
            'suggestCharts', [key], {});
      } catch (error) {
        console.error('Error during call to suggestCharts:', error);
      }
      quickchartButtonEl.classList.remove('colab-df-spinner');
      quickchartButtonEl.classList.add('colab-df-quickchart-complete');
    }
    (() => {
      let quickchartButtonEl =
        document.querySelector('#df-57a28b3c-a6fa-4335-ba6e-823fa4dbd7b6 button');
      quickchartButtonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';
    })();
  </script>
</div>

    </div>
  </div>




**Answer:**
* How many tables were created?

> 4 tables were created (3 of those were system tables)

## **Question 3: Explore the loaded data**

Inspect the table `ride`:



```python
df = pipeline.dataset(dataset_type="default").ny_taxi.df()
df
```





  <div id="df-42881aee-213a-4d6c-8dab-9cf744baf258" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>end_lat</th>
      <th>end_lon</th>
      <th>fare_amt</th>
      <th>passenger_count</th>
      <th>payment_type</th>
      <th>start_lat</th>
      <th>start_lon</th>
      <th>tip_amt</th>
      <th>tolls_amt</th>
      <th>total_amt</th>
      <th>trip_distance</th>
      <th>trip_dropoff_date_time</th>
      <th>trip_pickup_date_time</th>
      <th>surcharge</th>
      <th>vendor_name</th>
      <th>_dlt_load_id</th>
      <th>_dlt_id</th>
      <th>store_and_forward</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40.742963</td>
      <td>-73.980072</td>
      <td>45.0</td>
      <td>1</td>
      <td>Credit</td>
      <td>40.641525</td>
      <td>-73.787442</td>
      <td>9.0</td>
      <td>4.15</td>
      <td>58.15</td>
      <td>17.52</td>
      <td>2009-06-14 23:48:00+00:00</td>
      <td>2009-06-14 23:23:00+00:00</td>
      <td>0.0</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>YuocFGK8bzyDYg</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40.740187</td>
      <td>-74.005698</td>
      <td>6.5</td>
      <td>1</td>
      <td>Credit</td>
      <td>40.722065</td>
      <td>-74.009767</td>
      <td>1.0</td>
      <td>0.00</td>
      <td>8.50</td>
      <td>1.56</td>
      <td>2009-06-18 17:43:00+00:00</td>
      <td>2009-06-18 17:35:00+00:00</td>
      <td>1.0</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>YckW5kCkISNY7Q</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40.718043</td>
      <td>-74.004745</td>
      <td>12.5</td>
      <td>5</td>
      <td>Credit</td>
      <td>40.761945</td>
      <td>-73.983038</td>
      <td>2.0</td>
      <td>0.00</td>
      <td>15.50</td>
      <td>3.37</td>
      <td>2009-06-10 18:27:00+00:00</td>
      <td>2009-06-10 18:08:00+00:00</td>
      <td>1.0</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>gYwlhNz3yZXYiA</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40.739637</td>
      <td>-73.985233</td>
      <td>4.9</td>
      <td>1</td>
      <td>CASH</td>
      <td>40.749802</td>
      <td>-73.992247</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>5.40</td>
      <td>1.11</td>
      <td>2009-06-14 23:58:00+00:00</td>
      <td>2009-06-14 23:54:00+00:00</td>
      <td>0.5</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>iDzm4oAlckCrQQ</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40.730032</td>
      <td>-73.852693</td>
      <td>25.7</td>
      <td>1</td>
      <td>CASH</td>
      <td>40.776825</td>
      <td>-73.949233</td>
      <td>0.0</td>
      <td>4.15</td>
      <td>29.85</td>
      <td>11.09</td>
      <td>2009-06-13 13:23:00+00:00</td>
      <td>2009-06-13 13:01:00+00:00</td>
      <td>0.0</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>ncYSAN65YqWbxw</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9995</th>
      <td>40.783522</td>
      <td>-73.970690</td>
      <td>5.7</td>
      <td>1</td>
      <td>CASH</td>
      <td>40.778560</td>
      <td>-73.953660</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>5.70</td>
      <td>1.16</td>
      <td>2009-06-19 11:28:00+00:00</td>
      <td>2009-06-19 11:22:00+00:00</td>
      <td>0.0</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>jQsgb9HPhg6lgQ</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9996</th>
      <td>40.777200</td>
      <td>-73.964197</td>
      <td>4.1</td>
      <td>1</td>
      <td>CASH</td>
      <td>40.779800</td>
      <td>-73.974297</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>4.10</td>
      <td>0.89</td>
      <td>2009-06-17 07:43:00+00:00</td>
      <td>2009-06-17 07:41:00+00:00</td>
      <td>0.0</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>W4B9oPHNrIrr6w</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9997</th>
      <td>40.780172</td>
      <td>-73.957617</td>
      <td>6.1</td>
      <td>1</td>
      <td>CASH</td>
      <td>40.788388</td>
      <td>-73.976758</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>6.10</td>
      <td>1.30</td>
      <td>2009-06-19 11:46:00+00:00</td>
      <td>2009-06-19 11:39:00+00:00</td>
      <td>0.0</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>Bz2da3WnzFFhOQ</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9998</th>
      <td>40.777342</td>
      <td>-73.957242</td>
      <td>5.7</td>
      <td>1</td>
      <td>CASH</td>
      <td>40.773828</td>
      <td>-73.956690</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>6.20</td>
      <td>0.97</td>
      <td>2009-06-17 04:19:00+00:00</td>
      <td>2009-06-17 04:13:00+00:00</td>
      <td>0.5</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>2FfjtlJtvm2weA</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9999</th>
      <td>40.757122</td>
      <td>-73.986293</td>
      <td>6.5</td>
      <td>1</td>
      <td>Credit</td>
      <td>40.756313</td>
      <td>-73.972948</td>
      <td>2.0</td>
      <td>0.00</td>
      <td>8.50</td>
      <td>0.92</td>
      <td>2009-06-17 08:34:00+00:00</td>
      <td>2009-06-17 08:24:00+00:00</td>
      <td>0.0</td>
      <td>VTS</td>
      <td>1739804847.1155753</td>
      <td>UCzCcWz0UU27ZA</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>10000 rows × 18 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-42881aee-213a-4d6c-8dab-9cf744baf258')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-42881aee-213a-4d6c-8dab-9cf744baf258 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-42881aee-213a-4d6c-8dab-9cf744baf258');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


<div id="df-5d9b4366-7fd4-4d6a-a7fe-83e78511edb3">
  <button class="colab-df-quickchart" onclick="quickchart('df-5d9b4366-7fd4-4d6a-a7fe-83e78511edb3')"
            title="Suggest charts"
            style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
  </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

  <script>
    async function quickchart(key) {
      const quickchartButtonEl =
        document.querySelector('#' + key + ' button');
      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
      quickchartButtonEl.classList.add('colab-df-spinner');
      try {
        const charts = await google.colab.kernel.invokeFunction(
            'suggestCharts', [key], {});
      } catch (error) {
        console.error('Error during call to suggestCharts:', error);
      }
      quickchartButtonEl.classList.remove('colab-df-spinner');
      quickchartButtonEl.classList.add('colab-df-quickchart-complete');
    }
    (() => {
      let quickchartButtonEl =
        document.querySelector('#df-5d9b4366-7fd4-4d6a-a7fe-83e78511edb3 button');
      quickchartButtonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';
    })();
  </script>
</div>

  <div id="id_60078d1a-fdff-4f50-bd04-54cdeeb6e151">
    <style>
      .colab-df-generate {
        background-color: #E8F0FE;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        fill: #1967D2;
        height: 32px;
        padding: 0 0 0 0;
        width: 32px;
      }

      .colab-df-generate:hover {
        background-color: #E2EBFA;
        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
        fill: #174EA6;
      }

      [theme=dark] .colab-df-generate {
        background-color: #3B4455;
        fill: #D2E3FC;
      }

      [theme=dark] .colab-df-generate:hover {
        background-color: #434B5C;
        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
        fill: #FFFFFF;
      }
    </style>
    <button class="colab-df-generate" onclick="generateWithVariable('df')"
            title="Generate code using this dataframe."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z"/>
  </svg>
    </button>
    <script>
      (() => {
      const buttonEl =
        document.querySelector('#id_60078d1a-fdff-4f50-bd04-54cdeeb6e151 button.colab-df-generate');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      buttonEl.onclick = () => {
        google.colab.notebook.generateWithVariable('df');
      }
      })();
    </script>
  </div>

    </div>
  </div>




**Answer:**
* What is the total number of records extracted?

> 10000 records is extracted.

## **Question 4: Trip Duration Analysis**

Run the SQL query below to:

* Calculate the average trip duration in minutes.


```python
with pipeline.sql_client() as client:
    res = client.execute_sql(
            """
            SELECT
            AVG(date_diff('minute', trip_pickup_date_time, trip_dropoff_date_time))
            FROM ny_taxi;
            """
        )
    # Prints column values of the first row
    print(res)
```

    [(12.3049,)]
    

**Answer:**
* What is the average trip duration?

> The average trip duration is 12.3049 minutes.

## **Submitting the solutions**

* Form for submitting: TBA




## **Solution**

We will publish the solution here after deadline.
