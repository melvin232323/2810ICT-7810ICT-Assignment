# 2810ICT/7810ICT 2023 Assignment
## Part A - Project Management, and Part B - Statistical Data Analysis and Presentation

The assignment work for this course is a group-based (max 3 people) data analysis project that is split into 2 parts – design and implementation. There are several different datasets in this repository – you will need to choose 1 that your team will work on for both Part A and B. The overall goal for this assignment is to develop a simple data analysis and visualization tool for a dataset. You will need to design and implement this tool, and it must provide a graphical user interface that will handle the analysis and visualization of the data. Each dataset has a number of analysis and visualization tasks that your interface must enable a user to perform. In addition to the listed tasks, you must come up with 1 additional analysis/visualization/insight that your software provides (you will need to come up with an appropriate task based on the dataset you pick). All the assignment work must be hosted on a GitHub repo with access restricted to your group members. This repository should have a track record of regular commits showing the incremental (and group-based) work done on the project. ALL project resources (documents, code, images, and others) should be in the GitHub repo.

Additionally, your private git repo should be shared with the following accounts:
- 2810ICT-7810ICT-Assignment
  
### Part A - Project Management (25%, Due Sunday 3rd September)

#### Submission Requirements
This assignment must be submitted online via L@G under the assessment page. Only 1 submission per group is needed. Your submission should include:
- Project Plan.docx - A project plan document. You should use the provided template.
- Software Design Document.docx - A software design document. You should use the provided template.
- Gantt chart.xlsx - A separate Gantt chart (high-resolution version). You should embed this in your project plan (as an image or other), but also provide the original file.
- git_log.txt - A copy of the Git Log
- Any other documents/supporting files you have created that you think are necessary to include at this stage
  
In Part A, you will need to prepare a project plan that includes a Project Overview, Work-Breakdown Structure, Activity Definition and estimation and a Gantt chart for displaying scheduling & time estimation. This project plan should include sensible estimates for the various tasks required for both Part A and B (including estimates on preparing the project planning documentation). As you complete various components, you should put the actual completion time/dates on your Gantt chart to track how close you were to your estimates. For the subsequent stage of the assignment, you should revise your project plan with any additional details and continue to track your work.

You will then need to prepare a Software Design Document for one of the given data sets and related questions. You should start with a System Vision Statement (this can be included in your design document). You should then produce a formal list of requirements that need to be satisfied, some use cases for your software, a listing of system components and the related software design, and an early user interface design/wireframe (to be implemented in part B). There are templates provided for these documents. Please read the template documents for more hints and guidance.

To start your project, you should clone the following repo which contains the templates. 

https://github.com/2810ICT-7810ICT-Assignment/2810ICT-7810ICT-2023-Assignment

It is important to note that submission of this assignment is a requirement for passing the course. Late submissions will be marked according to Griffith University’s assessment policy. 5% of the overall mark will be deducted for each business day late. After 5 days, no submissions will be accepted.

### Part B – Statistical Data Analysis and Presentation (35%, Due Sunday 8th October)

#### Submission Requirements
This assignment must be submitted online via L@G under the assessment page. Only 1 submission per group is needed. Your submission should include:
- All *.py files containing the data analysis program
- User Manual.docx - (No provided template) briefly explains how to use your software and shows its features, illustrating them by using informative screenshots of your software. 
- Software Testing Report.docx - containing a brief testing plan and unit tests & coverage test results. You should use the provided template.
- Executive Summary.docx - An executive summary covering a 12-month. You should use the provided template.
- Project Plan.docx - An updated project plan document (with Gantt chart embedded)
- Gantt chart.xlsx - An updated separate Gantt chart (high-resolution version)
- Software Design Document.docx - An updated software design document
- git_log.txt - A copy of the Git Log
- Any other documents/supporting files you have created that you think are necessary to include at this stage

For Part B, you will need to implement the software that you designed in Part A. Before you begin writing code, you should come up with a testing plan that will thoroughly test the various components of your system. As you begin your implementation, you can start testing these components as they are finished. You must present the results of your testing in a testing report. You should prepare a brief user manual that explains how to use your software and shows its features. Finally, you should use your software to prepare a report that analyses the data over a 12-month period and presents the results in an executive summary. Your report should present the results from all of your required features for your chosen dataset, and should contain images from your software as well as some analysis and comments about the data.

It is important to note that submission of this assignment is a requirement for passing the course. Late submissions will be marked according to Griffith University’s assessment policy. 5% of the overall mark will be deducted for each business day late. After 5 days, no submissions will be accepted.

### Group Requirements

This assignment should be completed in groups of up to 3 people who should be in the same lab/workshop. You have a three-week window (i.e., Week 1, Week 2 and Week 3) to assemble your group autonomously. If you do not do so within this timeframe, you will be assigned to a group automatically. If you are unable to work in a group or have any specific issues, you should discuss this with your campus convenor. Make sure you include the name and student number of all group members in your submitted documentation. All group members should join the same group on L@G: People -> Group (make sure this is coordinated beforehand).

### Marking

This assignment is worth 60% of your final grade. Except in extraordinary circumstances, all group members will be given the same mark, so it is important that you all contribute and work together to complete the assignment. A full rubric for each part will be made available on the course website. Please note that all submitted assignments will be analyzed by a plagiarism detector that is specifically designed for assignment submissions containing program source code. We will aim to have all assignments marked within 2 weeks of the due date.


## Datasets

There are 4 datasets available for you to do your assignment on. Each dataset has a set of required analysis functions. Remember, in addition to the listed required analysis tools, you must come up with 1 additional analysis task/tool of your own.

### Victoria State Accident DataSet
https://www.kaggle.com/gaurav896/victoria-state-accident-dataset

**Required Features:**
- For a user-selected period, display the information of all accidents that happened in the period.
- For a user-selected period, produce a chart to show the number of accidents in each hour of the day (on average).
- For a user-selected period, retrieve all accidents caused by an accident type that contains a keyword (user entered), e.g. collision, pedestrian.
- Allow the user to analyze the impact of alcohol in accidents – ie: trends over time, accident types involving alcohol, etc.
- One other ‘insight’ or analysis tool of your choice

### Sydney Airbnb Data: 
https://www.kaggle.com/tylerx/sydney-airbnb-open-data

**Required Features:**
- For a user-selected period, report the information of all listings in a specified suburb
- For a user-selected period, produce a chart to show the distribution of prices of properties
- For a user-selected period, retrieve all records that contain a keyword (user entered), e.g. pool, pet.
- Analysing how many customers commented on factors related to cleanliness (multiple key words may be associated with cleanliness – justify your selection). 
- One other ‘insight’ or analysis tool of your choice

### NSW Traffic Penalty Data: 
https://www.kaggle.com/llihan/australia-nsw-traffic-penalty-data-20112017

**Required Features:**
- For a user-selected period, report the information of all penalty cases.
- For a user-selected period, produce a chart to show the distribution of cases in each offense code
- For a user-selected period, retrieve all cases captured by radar or camera based on offense description
- Analysing the cases caused by mobile phone usage - ie: trend over time, offense code, and so on.
- One other ‘insight’ or analysis tool of your choice

### New York Restaurant Inspection results: 
https://www.kaggle.com/datasets/new-york-city/nyc-inspections

**Required Features:**
- For a user-selected period, retrieve relevant inspection details.
- For a user-selected period, plot the distribution of violations over the different suburbs
- For a user-selected period, retrieve all violations that contain a keyword (user entered).
- Analyse the cases related to animals, e.g., rats, mice or others, and their trend over time and distribution over suburbs
- One other ‘insight’ or analysis tool of your choice
