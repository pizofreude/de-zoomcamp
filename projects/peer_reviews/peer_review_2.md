# Peer Review 2: [TfL Station Footfall Data Analysis Pipeline](https://github.com/hbg108/tfl-data-visualization/tree/main)

## Evaluation Process

The criteria for evaluation are following the recommended DTCS rubric: [Course Project Objective](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/projects) and [DTC Project Evaluation Criteria 2025 Full](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/project.md).

### Contents of interest:

- **`.dbt` Directory**:  
  - Contains `dbt_project.yml` (project config, materialization set to table, standard dbt structure).
  - `models/` subdirectory includes:
    - `station_footfall_daily.sql`: the main transformation model.
    - `schema.yml`: dbt schema file for model/table testing and documentation.
- **`README.md`**:  
  - Comprehensive project description, setup steps, pipeline overview, and infrastructure instructions.
- **`dbt_project.yml`**:  
  - Defines dbt structure, model materialization, and directory organization.
- **Kestra Directory**:  
  - Contains workflow orchestration similar to Will's demonstration in [Kestra lesson](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration).
- **Data files and images**:  
  - Images (such as dashboard screenshots) and references to data sources for pipeline input and dashboard support.


### Action

- **Review `README.md` for Problem Description**  
  - The README thoroughly outlines the motivation, architecture (GCP, BigQuery, dbt, Kestra), and step-by-step deployment, demonstrating both clarity and completeness.
- **Investigate Workflow Orchestration (Kestra)**  
  - The Kestra directory is referenced for YAML flow definitions handling ingestion, transformation, and scheduling. README provides detailed orchestration logic and manual override options.
- **Check `dbt_project.yml` and Models**  
  - The `dbt_project.yml` configures a typical dbt project with best practices (directory structure, table materialization).
  - The `models/` directory includes at least one transformation SQL model and a schema file, indicating dbt's role in daily data aggregation and data warehouse management.
- **Project Testing and Evaluation**  
  - Based on visible files, the project follows data engineering best practices.  
  - Direct evidence of automated tests or CI/CD is not present, and same goes for dbt-level testing/documentation.



## Evaluation Summary:

**Repository:** [TfL Station Footfall Data Analysis Pipeline](https://github.com/hbg108/tfl-data-visualization/tree/main) 

**1. Problem Description:**

The README contains a clear and complete problem description:

Describes the business context—analyzing passenger flow at TfL stations using Oyster card tap counts.
Explains the value: optimizing station management, understanding congestion, and supporting data-driven decisions.
Specifies the data source and project goals.

Score: 2 points

**2. Cloud:**

The project is developed for Google Cloud Platform (GCP).
Infrastructure as Code (IaC) is used via Terraform (terraform/ directory with main.tf, variables.tf).
Resources provisioned include a GCS bucket and BigQuery dataset, as explicitly detailed in the README.

Score: 4 points

**3. Data Ingestion: Batch / Workflow Orchestration:**

Workflow orchestration is implemented end-to-end via Kestra.
The pipeline includes multiple steps: download -> upload to bucket -> load to BigQuery -> consolidate tables.
The Kestra flows automate ingestion for multiple years and schedule weekly updates.

Score: 4 points

**4. Data Ingestion: Stream:**

No streaming technology (Kafka, Pulsar, etc.) is present or described.
The project is batch-oriented, as is appropriate for the source data.

Score: 0 points

**5. Data Warehouse:**

BigQuery is used as the data warehouse.
Tables are partitioned (by travel date) for efficient querying and cost optimization, as described in the README.
There is an explanation of partitioning and its purpose.

Score: 4 points

**6. Transformations (dbt, Spark, etc.):**

Transformations are implemented using dbt (dbt/ directory, dbt_project.yml, SQL models).
dbt is used for aggregation and modeling, with automated triggering via orchestration.

Score: 4 points

**7. Dashboard:**

The [Looker Studio dashboard](https://lookerstudio.google.com/reporting/33cf406c-c312-4a59-bebd-5d8bf62e0ca6/page/BSfHF) (linked and screenshotted in the repo) includes at least 2 tiles: a time series chart and a station ranking table.
Filtering and interactivity are supported.

Score: 4 points

**8. Reproducibility:**

Step-by-step, clear instructions are provided for setup, credentials, infrastructure, orchestration, and running transformations.
The code is modular and instructions cover both local and cloud setup.
The project is easy to run if you have GCP credentials and follows best practices.

Score: 4 points

### Final Score: 26 points

## Review comments

### 1. **Problem Description**  

The problem is well-described in the README of the `tfl-data-visualization` project. The project focuses on analyzing passenger flow patterns at London Tube and TfL Rail stations using Oyster card tap counts. The business context, data source, and objectives—supporting station management, congestion analysis, and data-driven infrastructure decisions—are clearly articulated.  
**Comment:** Excellent articulation of the problem and its real-world significance. The clarity helps the reader quickly understand the project’s goals and value.

### 2. **Cloud**

The project is developed for Google Cloud Platform (GCP), using BigQuery as the data warehouse and Google Cloud Storage for raw data. Infrastructure as Code (IaC) is implemented via Terraform, automating the provisioning of cloud resources.  
**Comment:** Outstanding use of cloud technologies and automation. Leveraging Terraform for GCP infra shows strong cloud engineering practice.

### 3. **Data Ingestion: Batch / Workflow Orchestration**

Kestra is used for workflow orchestration, automating the end-to-end batch pipeline from data download to ingestion and transformation. Multiple Kestra flows are defined for ingestion, consolidation, and scheduled updates, providing a robust and modular DAG.  
**Comment:** Great job with fully automated workflow orchestration. Consider including visual examples or screenshots of Kestra flows to further clarify the orchestration structure.

### 4. **Data Warehouse**

BigQuery is used as the data warehouse, and the ingestion pipeline creates both external and native tables. Data is consolidated and partitioned by travel date, optimizing for query performance and cost. The rationale for partitioning is explained in the documentation.  
**Comment:** Excellent use of partitioning and cloud-native DWH features. Detailing clustering strategies (if any) could further enhance this section.

### 5. **Transformations (DBT, Spark, etc.)**

Transformations are implemented using dbt, with modular models and schema documentation. dbt is triggered automatically via Kestra orchestration, ensuring up-to-date aggregate tables for analytics and visualization.  
**Comment:** Very strong use of dbt for transformations and documentation. The modular structure and automation are well executed.

### 6. **Dashboard**

A Looker Studio dashboard is provided with at least two interactive tiles: a time series chart and a station ranking table. The dashboard is filterable by multiple dimensions (date, station, tap type, etc.) and is accessible online.  
**Comment:** Excellent dashboard implementation with multiple insights and interactive filtering. The visuals effectively communicate the analyzed data.

### 7. **Reproducibility**

The README offers detailed, step-by-step instructions for setup, credentials, GCP provisioning, Kestra orchestration, and dbt usage. The process is clear and should be easy for others to reproduce, assuming access to required GCP resources.  
**Comment:** Great job on ensuring reproducibility. The thorough instructions are a strong point for this submission.

---

### **Summary of Feedback:**

This submission demonstrates a high level of competence in building a modern data engineering pipeline for analyzing London’s TfL station footfall data. The project leverages GCP, Terraform, Kestra, BigQuery, and dbt, showcasing a strong grasp of current tools and best practices. The batch pipeline is fully automated and modular, and the dashboard provides actionable insights.

Strengths include:
- Clear problem statement and business relevance.
- Cloud-native architecture with IaC and automated orchestration.
- Robust data warehouse design with partitioning.
- Modular, testable transformations via dbt.
- Interactive and insightful dashboard.
- Excellent documentation and reproducibility.

Areas for improvement:
1. Add explicit data validation tests (dbt tests, pipeline checks) and consider integrating CI/CD for automated testing and deployment.
2. Expand on monitoring and alerting for the production pipeline (e.g., notifications on failure).
3. Include screenshots or diagrams of Kestra flows for better orchestration visibility.
4. Explore streaming data ingestion if the data source ever supports real-time feeds, to expand the project’s scope.
5. Further detail clustering strategies or additional warehouse optimization practices if applicable.

**Overall:**  
This project is an exemplary demonstration of cloud data engineering, with solid end-to-end automation, clarity, and scalability. Addressing the above enhancement areas would make it even more production-ready and demonstrate further depth in operational excellence.

## Learning In Public

**1. "[Peer Review 2: TfL Station Footfall Data Analysis Pipeline (Part 1)](https://dev.to/pizofreude/peer-review-2-tfl-station-footfall-data-analysis-pipeline-part-1-4909)"**

This post covers foundational elements, setting context and reviewing the project up to the orchestration stage.

**2. "[Peer Review 2: Data Warehousing, Transformation, and Reproducibility in tfl-data-visualization (Part 2)](https://dev.to/pizofreude/peer-review-2-data-warehousing-transformation-and-reproducibility-in-tfl-data-visualization-22pp)"**

This post dive deeper into the remainder of the pipeline, focusing on advanced analytics, visualization, and practical reproducibility—concluding with overall feedback and recommendations.
