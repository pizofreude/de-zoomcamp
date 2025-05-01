# Peer Review 1: [Data-engineering-professional-certificate](https://github.com/elgrassa/Data-engineering-professional-certificate/tree/main)

## Evaluation Process

The criteria for evaluation are following the recommended DTCS rubric: [Course Project Objective](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/projects) and [DTC Project Evaluation Criteria 2025 Full](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/project.md).

### Contents of interest:

- `.dbt` Directory: Indicates the use of dbt for transformations.
- `README.md`: Contains project details and description.
- `dbt_project.yml`: Configuration file for dbt.
- Directories like models, kestra: Related to workflow orchestration and data transformations via dbt Cloud.
- Data files and images: May support dashboards or ingestion pipelines.

### Action:

- Review `README.md` for problem description.
- Investigate workflow orchestration tools in the kestra directory.
- Check `dbt_project.yml` and models for dbt usage.
- Project testing and evaluation.

## Evaluation Summary:

**Repository:** [Data-engineering-professional-certificate](https://github.com/elgrassa/Data-engineering-professional-certificate/tree/main) 

**1. Problem Description:**

The problem is described clearly in the README file. The project focuses on analyzing Poland's real estate market through a static dashboard.

Score: 2 points

**2. Cloud:**

The project uses dbt Cloud and BigQuery for data processing, and some parts of the pipeline utilize cloud technologies. Although there's no mentioned of IaC tools, the project demonstrates cloud usage via dbt Cloud, BigQuery and Streamlit.

Score: 2 points

**3. Data Ingestion: Batch / Workflow Orchestration:**

Kestra is used for orchestration, handling multiple CSV files and automating the ETL process. Since the dataset itself is not being updated regularly, the focus is more on the ETL process rather than end-to-end batch data ingestion into a data lake that is triggered by any/external events.

Score: 2 points

**4. Data Ingestion: Stream:**

No mention of streaming systems like Kafka or Pulsar in the README since this project is batch-oriented.

Score: 0 points

**5. Data Warehouse:**

Data is transformed and optimized in BigQuery. Partitioning and clustering are not explicitly mentioned, but transformations are done via DBT.

Score: 2 points

**6. Transformations (dbt, Spark, etc.):**

Transformations are implemented using dbt Cloud.

Score: 4 points

**7. Dashboard:**

A [Streamlit dashboard](https://polish-flats-ps.streamlit.app/) is developed with multiple visualizations and interactive features.

Score: 4 points

**8. Reproducibility:**

Detailed instructions are provided in the README file, including requirements and setup instructions for Docker and DBT.

Score: 4 points

### Final Score: 20 points

## Review comments

### 1. **Problem Description**  

The problem is well-articulated in the README file of the `Data-engineering-professional-certificate` repo. The project focuses on analyzing Poland's real estate market using a Streamlit dashboard. The scope and objectives are clear, with a focus on price fluctuations and market behaviors across several cities.  
**Comment:** Great job describing the problem and connecting it to the project's goals. The clarity makes it easy to understand the purpose.

### 2. **Cloud**

The project effectively utilizes Cloud DBT and BigQuery for data processing, demonstrating a strong integration of cloud technologies. The README explains these tools' roles and provides instructions for setting up BigQuery with DBT Cloud.
**Comment:** Excellent use of cloud technologies. Consider adding IaC tools for provisioning cloud resources e.g. you can ingest the Kaggle dataset to BigQuery using Terraform provisioned infrastructure.

### 3. **Data Ingestion: Batch / Workflow Orchestration**

Kestra is employed for orchestrating workflows, automating the ETL process from CSV ingestion to loading into PostgreSQL and BigQuery. This demonstrates a comprehensive and end-to-end pipeline.  
**Comment:** Well done on implementing workflow orchestration. Adding examples or screenshots of Kestra Flows/DAGs could further illustrate your orchestration.

### 4. **Data Warehouse**

BigQuery is used for storing and querying data, with DBT transformations applied. However, there is no explicit mention of partitioning or clustering for optimization.  
**Comment:** Great use of BigQuery and DBT. Including explanations on how data partitioning or clustering optimizes queries could strengthen this aspect.

### 5. **Transformations (DBT, Spark, etc.)**

DBT is used extensively for data transformations, with clearly defined steps in the `dbt_project.yml` file and models directory. The README also highlights its utility in cleaning and structuring data.  
**Comment:** Excellent use of DBT for transformations. This ensures modular and reusable SQL models. Jinja SQL FTW!

### 6. **Dashboard**

The Streamlit dashboard is implemented with multiple interactive visualizations, including charts comparing city-level rental and sales trends. The app is live and accessible.  
**Comment:** Fantastic job on the dashboard. The interactive features and visualization add great value to the project. The static nature of the dashboard is okay for now considering the project scope and the future plans that involve a more dynamic dashboard.

### 7. **Reproducibility**

The README provides clear and detailed instructions for setting up the project locally, including Docker Compose commands and DBT setup steps.  
**Comment:** Excellent work on writing thorough instructions. This ensures others can easily reproduce your results.

---

### **Summary of Feedback:**

This submission demonstrates a commendable effort in solving the problem of analyzing Poland's real estate market. The project leverages Cloud DBT, BigQuery, and Streamlit effectively, showcasing a strong understanding of modern data engineering tools and practices. Kestra is used for batch workflow orchestration, and dbt Cloud facilitates modular and reusable transformations. The interactive Streamlit dashboard is well-implemented, providing clear visual insights into the data albeit its static nature.

While the project excels in batch processing, cloud integration, and reproducibility, there are areas for improvement:
1. Incorporating Infrastructure as Code (IaC) tools, such as Terraform, to automate cloud resource provisioning.
2. Enhancing the data warehouse by explicitly using partitioning and clustering for query optimization.
3. Adding examples or screenshots of Kestra Flows/DAGs to better illustrate the orchestration process.
4. Exploring streaming capabilities to expand the project's scope for real-time data processing. This is especially relevant for real-time housing data processing that commonly involves regular fluctuations.

Overall, this project achieves a solid foundation in data engineering with room for further enhancements. Future updates and improvements, such as a more dynamic dashboard and advanced optimizations, would make this project even more impactful.

## Learning In Public

**1. "[Peer Review 1: Analyzing Poland's Real Estate Market (Part 1)](https://dev.to/pizofreude/peer-review-1-analyzing-polands-real-estate-market-part-1-2c6d)"**

This post focus on the problem description, data ingestion (batch), workflow orchestration with Kestra, and cloud setup with BigQuery and dbt Cloud.

**2. "[Peer Review 1: Poland's Real Estate Market Dashboards and Insights with Streamlit (Part 2)](https://dev.to/pizofreude/peer-review-1-polands-real-estate-market-dashboards-and-insights-with-streamlit-part-2-5eah)"**

This post dive deeper into the implementation of the Streamlit dashboard, data transformations with dbt, visualization techniques, and future plans for the project.
