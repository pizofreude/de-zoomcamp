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

## Introduction - Self-Study Notes

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
  - The NYC Taxi and Limousine Commission dataset was used as an example.

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
