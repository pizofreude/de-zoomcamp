# Introduction to Data Engineering Zoomcamp

## Summary of "Data Engineering Zoomcamp 2024"

1. **Course Overview and Format**  
   - The course includes six modules and two workshops covering topics like workflow orchestration (Kestra), data warehousing (BigQuery), batch processing (Spark), and stream processing (SQL).  
   - Participants can complete the course at their own pace, with resources and videos available for flexible learning.  

2. **Technical Prerequisites**  
   - Basic programming knowledge, familiarity with Python, command line usage (bash), and Docker commands are expected.  
   - Environment setup can be done using GitHub Codespaces or cloud virtual machines.  

3. **Interactive Learning and Support**  
   - Slack is the primary platform for community interaction, announcements, and Q&A.  
   - Comprehensive FAQs and office hours are available to address common concerns and technical issues.  

4. **Modules and Content Highlights**  
   - **Module 1**: Environment setup, using Docker, and transitioning from CSV to Parquet formats.  
   - **Module 2**: Workflow orchestration with Kestra, building pipelines.  
   - **Module 3**: Data warehousing with BigQuery.  
   - **Module 4**: Advanced data transformation with DBT.  
   - **Module 5**: Batch processing with Spark.  
   - **Module 6**: Stream processing using SQL and Kafka.  

5. **Final Project and Certification**  
   - Participants are encouraged to create a final project that demonstrates practical skills, with the option to collaborate with nonprofits.  
   - Completing the project is required for certification.  

6. **Community Contributions and Sponsorship**  
   - The course is free and supported by sponsors like Kestra, dlt, Mage, DBT Hub, and RisingWave. Participants are encouraged to star the course repository on GitHub to help promote it.  

7. **Motivation and Accessibility**  
   - The course was created to provide free, high-quality education for data enthusiasts worldwide, supported by volunteers and industry professionals.  

8. **Challenges and Advice**  
   - Modules can be demanding (e.g., setting up Docker and GCP), but participants are advised to take their time and focus on understanding core concepts.  
   - Past participants found tools like GitHub Codespaces helpful for simplifying setup. Note: Using Windows does requires additional setup especially for Docker.  

9. **Upcoming Events and Resources**  
   - Additional workshops, webinars, and office hours are planned throughout the course.  
   - A curated list of datasets and project ideas is available for participants.  

10. **Career Outlook and Skills Application**  
   - Skills from the course are applicable in various fields, including ML and analytics.  
   - Data engineering remains in demand, and foundational knowledge from the course supports further specialization in tools like AWS, GCP, or Azure.

---
---

# [Introduction](https://www.youtube.com/live/AtRhA-NfS24?si=C0M1oDPeX8KWeggJ) - Self-Study Notes

## Overview

### Course Duration and Structure
- **Duration**: 6 modules plus 2 workshops.
- **Format**: Weekly modules covering key data engineering topics.
- **Interactivity**: Q&A sessions, [Slack](https://datatalks.club/slack.html) discussions, and [GitHub](https://github.com/DataTalksClub/data-engineering-zoomcamp) contributions.

### Key Resources
- **Slack**: Main platform for discussions.
- **GitHub Repository**: Contains all course materials.
- **Telegram Channel**: For announcements and updates.
- **Environment Setup**: Use GitHub Codespaces or cloud virtual machines for ease of starting up as compared to local installations with some hurdles especially when using Windows. Linux FTW! OpenSUSE Tumbleweed 😉

---

## Key Topics and Modules

### Week 1: Environment Setup and Basics
- **Key Tools**: Docker, Terraform, GitHub Codespaces.
- **Focus**: Preparing the environment for the course.
- **Skills Required**: Basic command-line knowledge, Docker commands, Python basics.

### Week 2: Workflow Orchestration
- **Tool**: Kestra (orchestration tool).
- **Content**:
  - Simplify scripts created in Week 1.
  - Convert CSV files to Parquet format and upload to Google Cloud Storage.
- **Notes**:
  - The [NYC Taxi and Limousine Commission](https://github.com/DataTalksClub/nyc-tlc-data) dataset was used as an example.

### Week 3: Data Warehousing
- **Tool**: Google BigQuery.
- **Focus**: Storing and querying large datasets.

### Week 4: DBT (Data Build Tool)
- **Content**:
  - Transform data for analysis.
  - Build visualizations and dashboards.

### Week 5: Batch Processing
- **Tool**: Apache Spark.
- **Focus**:
  - Batch processing similar to DBT.
  - Provides finer control over data pipelines.

### Week 6: Streaming and Real-Time Data Processing
- **Tools**: Kafka, RisingWave (open-source SQL streaming tool).
- **Focus**:
  - Stream processing using SQL.
  - Introduction to stream-based architectures.

---

## Workshops
1. **Workflow Orchestration**:
   - Practical session to consolidate Week 2 content.
2. **Streaming Data with SQL**:
   - Hands-on workshop focusing on real-time data pipelines.

---

## Final Project
- **Objective**: Create a comprehensive data engineering project. This is the course requirement for graduation with certificate.
- **Guidelines**:
  - Use any tools and concepts covered in the course.
  - Option to partner with nonprofits or work independently.
  - Focus on practical, real-world data use cases.
- **Submission**:
  - Homework files available in the GitHub cohort repository.
  - Submit projects via a new automated platform (replacing Google Forms): [Course Management Platform](https://courses.datatalks.club/de-zoomcamp-2025/). Note: If Sign up using GitHub Auth failed (e.g. Server Error 500), user is adviced to use Slack Auth or GAuth instead. This is a known bug and still work-in-progress.

---

## Expectations and Requirements
- **Prerequisites**:
  - Familiarity with Python and basic programming concepts.
  - Command-line proficiency.
- **Time Commitment**: Flexible; follow your own pace.
- **Certificates**: Awarded upon successful completion of the final project. Homework submission counts toward internal ranking system as motivational instrument for participants.

---

## Additional Tips
- **GitHub Contributions**:
  - Star the course repository to help it trend.
  - Solve some ticket on Github issues as open-source contributions.
  - Engage with the community by sharing insights or asking questions.
- **Slack**:
  - Check the [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?tab=t.0#heading=h.edeyusfgl4b7) document before posting queries.
  - Use relevant channels to interact with peers, or directly ask @ZoomcampQABot in the #course-data-engineering channel before reaching out to instructors as final resort.
- **Environment**:
  - Codespaces offers a simple setup with pre-installed tools like Docker and Python.
  - Cloud virtual machines provide flexibility for advanced setups.

---

## Career Insights and Recommendations
- **Job Outlook**:
  - Despite tech layoffs, demand for data engineers remains strong.
  - Skills in platforms like GCP, AWS, and Azure are valuable.
- **Certifications**:
  - Beneficial, especially for early-career professionals and consultants.
- **Applications**:
  - Data engineering techniques are foundational for ML and analytics roles.

---

## Why This Course is Free
- **Motivation**: Sharing knowledge with the community.
- **Support**: Funded by sponsors like Kestra, dlt, Mage, DTHub, and RisingWave.
- **Community Contribution**:
  - Participants can support the course by sharing it, contributing feedback, or donating through training budgets towards [DataTalksClub](https://github.com/DataTalksClub).

---

## Miscellaneous Notes
- Consider [**Learning in Public**](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/learning-in-public.md) to stay motivate with extra points for ranking.
- **Office Hours**: Scheduled for specific topics like Kestra and project guidance.
- **FAQ Document**: Comprehensive guide available for common queries.
- **Past Student Contributions**:
  - Many alumni have shared tools and insights to improve the course.
- **Data Architect Path**:
  - Consider learning about Kimball methodologies.

---

By following this structured approach, we can maximize our learning experience in the Data Engineering Zoomcamp 2025 Cohort.

Good luck everyone!

---
---


# Docker + Postgres

## 🎥 [Introduction to Docker](https://youtu.be/EYNwNlOrpr0?si=we50KI-9J_3oYEhw)

## Study Notes: DE Zoomcamp 1.2.1 - Introduction to Docker

### Overview

- **Topic:** Introduction to Docker and its importance for data engineers.
- **Purpose:** Learn the basics of Docker, including its use cases, advantages, and practical setup for data engineering tasks such as running databases and pipelines.

---

### Key Concepts

1. **What is Docker?**
    - A platform for delivering software in isolated environments called **containers**.
    - Containers ensure **isolation** and portability, making it easier to run applications without interfering with the host system or other containers.
2. **Why Docker for Data Engineers?**
    - **Reproducibility:** Ensures consistent environments across different systems.
    - **Local experiments and testing:** Quickly set up and run tools like PostgreSQL without installing them on the host system.
    - **Integration tests (CI/CD):** Simulate real-world scenarios by connecting components like data pipelines and databases in isolated environments.
    - **Cloud readiness:** Docker images can be deployed to cloud environments (e.g., Kubernetes, AWS Batch) for scalable execution.

---

### Practical Examples and Workflow

1. **Docker for Running PostgreSQL**
    - A PostgreSQL database can run inside a container, eliminating the need to install it on the host system.
    - Multiple containers can run different database instances without conflicts.
    - Tools like **pgAdmin** can also run in containers for database management and SQL query execution.
        
        ![1-container.png](/course_notes/images/01-docker-terraform/1.2.1/1-container.png)
        
2. **Data Pipelines in Docker**
    - Example pipeline: A Python script that processes data from a CSV file, performs transformations using **pandas**, and outputs results to PostgreSQL.
    - Dependencies (Python version, libraries) are included in the container to ensure consistency.
        
        ![2-pipeline.png](/course_notes/images/01-docker-terraform/1.2.1/2-pipeline.png)
        
3. **Isolation and Reproducibility**
    - Containers can be reset to their original state after each use.
    - Docker images can be shared, ensuring the same environment is used regardless of the platform.
        
        ![3-reproducibility.png](/course_notes/images/01-docker-terraform/1.2.1/3-reproducibility.png)
        

---

### Key Docker Commands and Concepts

1. **Basic Commands**
    - `docker run [image-name]`: Runs a container based on the specified image.
    - `docker build -t [tag-name] .`: Builds a Docker image from a Dockerfile.
    - `docker exec -it [container-id] bash`: Access the container's terminal.
    - `docker stop [container-id]`: Stops a running container.
2. **Images and Containers**
    - **Image:** A template containing instructions to create a container.
    - **Container:** A running instance of an image.
3. **Dockerfile**
    - A file containing instructions to build a custom Docker image.
    - Common commands in Dockerfile:
        - `FROM [base-image]`: Specifies the base image (e.g., `python:3.9`).
        - `RUN [command]`: Executes commands (e.g., `RUN pip install pandas`).
        - `ENTRYPOINT`: Defines the default command executed when a container starts.
        - `WORKDIR`: Sets the working directory inside the container.

---

### Practical Demonstrations

1. **Running a Container**
    - Run a test image: `docker run hello-world`.
    - Run an Ubuntu image interactively: `docker run -it ubuntu bash`. `it` means interactive.
2. **Installing Python Dependencies in a Container**
    - Start a Python container: `docker run -it python:3.9 bash`.
    - Install pandas: `pip install pandas`. To install python library in a docker container, use this command: `docker run -it --entrypoint=bash python: 3.9` which will run the entry point inside bash to run pip install command.
    - Run Python commands within the container.
    - Note: Changes made in the container (e.g., installed packages) are lost after the container stops.
3. **Creating a Custom Docker Image**
    - Example Dockerfile for a data pipeline:
        
        ```docker
        FROM python:3.9
        RUN pip install pandas
        WORKDIR /app
        COPY pipeline.py /app/
        ENTRYPOINT ["python", "pipeline.py"]
        
        ```
        
    - Build the image from a Dockerfile: `docker build -t pipeline-image .`
        - `-t` = tag
        - `pipeline-image` = tag name
        - `.` = build the docker image in current directory
        - In the Docker command `docker build -t test:pandas .`, the colon `:` is used to tag the image being built. Specifically:
            - `test` is the name of the image.
            - `pandas` is the tag for that image.
        
        Tags are useful to differentiate between versions or variations of the same image. So, in this case, `test:pandas` might indicate a specific version of the `test` image that includes pandas (a Python library for data manipulation and analysis).
        
        The `.` at the end specifies the current directory as the build context, meaning Docker will use the contents of the current directory to build the image.
        
    - Run the container: `docker run pipeline-image`.
        - `docker run -it test:pandas 2025-01-27` let us runs the image at specified date.
        - `docker run -it test:pandas 2025-01-27 param1 param2` let us runs the image at specified date with various parameters.
4. **Parameterizing the Pipeline**
    - Pass arguments to the script using command-line parameters.
    - Example: `docker run pipeline-image arg1 arg2`.
    - Access parameters in Python using `sys.argv`.

---

### Advantages of Docker

1. **Portability:** Run the same container in local, cloud, or CI/CD environments.
2. **Consistency:** Eliminates the "works on my machine" problem.
3. **Isolation:** Prevents interference between different applications or services.
4. **Scalability:** Easily deploy containers in distributed systems like Kubernetes.

---

### Recommendations for Beginners

1. **Tools for Development:**
    - Use **Visual Studio Code** or similar editors for editing files.
    - On Windows, use **Git Bash** or **Windows Subsystem for Linux (WSL)** for a Linux-like terminal experience.
2. **Learning Resources:**
    - Experiment with basic Docker commands.
    - Practice building and running custom images.
    - Explore Docker Hub for prebuilt images.
    - Look into CI/CD tools like GitHub Actions for automation.

---

### Next Steps

- Apply Docker to run PostgreSQL and practice SQL.
- Build and test data pipelines using Docker containers.
- Explore deploying containers to cloud platforms for scalable execution.

---
---

# [🎥 Ingesting NY Taxi Data to Postgres](https://youtu.be/2JM-ziJt0WI?si=mbJhHB7ZjDj5sQ2-)

## Study Notes: DE Zoomcamp 1.2.2 - Ingesting NY Taxi Data to Postgres
### **Introduction and Context**

- The [video](https://youtu.be/2JM-ziJt0WI?si=mbJhHB7ZjDj5sQ2-) builds upon the previous lesson 1.2.1 where Docker was introduced, focusing on how it can be used for data engineering tasks.
- The goal of this session is to set up a PostgreSQL database using Docker, ingest data into it, and practice SQL queries.
- The NY Taxi dataset will be used throughout the course to learn SQL and data ingestion techniques.

---

### **Key Concepts Covered**
### **1. Running PostgreSQL in Docker**

- **Docker Image**: Official PostgreSQL Docker image (version 13) is used.
- **Configuration**: Includes setting environment variables for the database:
    - User: `root`
    - Password: `root`
    - Database: `ny_taxi`
        
        ```bash
        docker run -it \
          -e POSTGRES_USER="root" \
          -e POSTGRES_PASSWORD="root" \
          -e POSTGRES_DB="ny_taxi" \
          -v c:/workspace/de-zoomcamp/1_intro_to_data_engineering/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
          -p 5433:5432 \
          postgres:13
        ```
        
- **Commands for Configuration**:
    - Use `e` flags to set environment variables.
    - Use `v` flag to map a folder on the host machine to the container for persistent storage. `path-to-host-folder:path-to-container-folder`
    - Use `p` flag to map ports (5432 for PostgreSQL). If you happen to install Postgres on your local machine, make sure to use other port number for your Docker Postgresql to avoid conflict such as:
    **`PGCLI -connection failed: FATAL: password authentication failed for user "root"`**

### **2. Persisting Data with Docker**

- **Mounting Volumes**:
    - A folder (e.g., `ny_taxi_postgres_data`) is mapped to store database files.
    - Ensures that data remains available even if the Docker container is restarted.
- **Windows-Specific Note**: Windows paths require absolute paths with specific formatting (e.g., `C:\path\to\folder`).

### **3. Accessing PostgreSQL Database**

- **Using pgcli**:
    - A Python-based command-line client for PostgreSQL.
    - Installed using `pip install pgcli`.
    - Connection command format: `pgcli -h localhost -p 5432 -u root -d ny_taxi`.
    If you installed Postgres on your local machine, then consider mapping other port to your local machine to run Docker Postgres successfully. E.g.:
    `pgcli -h localhost -p 5433 -u root -d ny_taxi`
    - Allows running SQL queries directly from the terminal, e.g.:
        - `\dt` = list tables
        - `\db` = list tablespaces
        - `SELECT COUNT(1) FROM yellow_taxi_data;` = count data rows available

### **4. Exploring the NY Taxi Dataset**

- **Dataset Overview**:
    - Contains taxi trip records (yellow and green taxis) from NYC.
    - Fields include pickup/dropoff times, passenger count, distance, fare, tips, etc.
    - [Data dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf) is available for detailed field descriptions.
- **Downloading the Dataset**:
    - Use `wget` or manual download to get the CSV files:
        - yellow_tripdata_2021-01.csv
        - [taxi_zone_lookup.csv](https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv) 
        e.g. `wget https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv`
    - For performance, process only a subset of rows (e.g., first 100 rows).

### **5. Preparing the Dataset with Pandas**

- **Environment Setup**:
    - Use Jupyter Notebook for interactive data exploration.
    - Libraries used: `pandas` and `sqlalchemy`.
- **Initial Data Exploration**:
    - Read the dataset using `pandas.read_csv()`.
    - Examine the first few rows and basic statistics.
- **Data Schema Definition**:
    - Create an SQL table schema based on the dataset structure.
    - Example schema:
        
        ```sql
        CREATE TABLE yellow_taxi_data (
            vendor_id INTEGER,
            pickup_datetime TIMESTAMP,
            dropoff_datetime TIMESTAMP,
            passenger_count INTEGER,
            trip_distance FLOAT,
            fare_amount DECIMAL,
            tip_amount DECIMAL,
            total_amount DECIMAL
        );
        
        ```
        
    - Data Definition Language: `print(pd.io.sql.get_schema(df, name='yellow_taxi_data'))`:
        
        ```sql
        CREATE TABLE yellow_taxi_data (
        	"VendorID" BIGINT, 
        	tpep_pickup_datetime TIMESTAMP WITHOUT TIME ZONE, 
        	tpep_dropoff_datetime TIMESTAMP WITHOUT TIME ZONE, 
        	passenger_count BIGINT, 
        	trip_distance FLOAT(53), 
        	"RatecodeID" BIGINT, 
        	store_and_fwd_flag TEXT, 
        	"PULocationID" BIGINT, 
        	"DOLocationID" BIGINT, 
        	payment_type BIGINT, 
        	fare_amount FLOAT(53), 
        	extra FLOAT(53), 
        	mta_tax FLOAT(53), 
        	tip_amount FLOAT(53), 
        	tolls_amount FLOAT(53), 
        	improvement_surcharge FLOAT(53), 
        	total_amount FLOAT(53), 
        	congestion_surcharge FLOAT(53)
        )
        ```
        
    - Data ingestion in batch due to large number of dataset:
        - shift+tab = open help for function in jupyter notebook

### **6. Ingesting Data into PostgreSQL**

- **Chunk Processing**:
    - To handle large datasets efficiently, read and insert data in chunks (e.g., 100,000 rows per chunk).
    - Use Pandas’ `to_sql` method to insert data into PostgreSQL.
- **Connection Setup**:
    - Use `sqlalchemy` to create a database engine.
    - Connection string format: `postgresql://<user>:<password>@<host>:<port>/<database>`.
- **Ingestion Workflow**:
    - Generate the SQL schema.
    - Create the table in PostgreSQL.
    - Insert data chunk by chunk.
    - Verify the data using SQL queries (e.g., `SELECT COUNT(*) FROM yellow_taxi_data;`).

---

### **Practical Tips and Insights**

1. **Setting Up Docker**:
    - Use `docker run` commands with appropriate flags to configure and run containers.
    - Troubleshoot port conflicts using `docker ps` and `docker stop` commands.
2. **Optimizing Data Handling**:
    - For large datasets, avoid loading everything into memory at once; use iterators.
    - Save subsets of data for quicker initial exploration.
3. **Windows-Specific Adjustments**:
    - Pay attention to path formats and ensure compatibility with Docker.
4. **SQL Best Practices**:
    - Define appropriate data types (e.g., `DECIMAL` for monetary values).
    - Use indexes for faster querying when working with large datasets (covered in later lessons).
5. **Debugging and Verification**:
    - Always test connections and data integrity after setup.
    - Use simple queries like `SELECT 1;` to verify database readiness.

---

### **Next Steps in the Course**

- Learn about Docker Compose to manage multiple Docker containers.
- Use Airflow for orchestrating data pipelines.
- Perform advanced SQL queries and integrate with BigQuery for analytics.

---
---
