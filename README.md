# -END-TO-END-DATA-SCIENCE-PROJECT

COMPANY: CODTECH IT SOLUTIONS

NAME: K RAJESH

INTERN ID: CTO4DG2597

DOMAIN:DATA SCIENCE

MENTOR:NEELA SANTHOSH

im happy to complete this task and be a part in codetech , coming to this task i have faced many issues during completion like first i did in  colab but later i found that it cannot have terminal , in this task i have used python as my core programming language thoughout this project , Pandas For data loading and preprocessing task,Scikit-learn (sklearn)  For building the machine learning pipeline, including preprocessing and model training,Random Forest Classifier – The machine learning algorithm used for classification.
Pickle To serialize and save the trained model.
FastAPI  A modern Python web framework used to build the REST API.
Uvicorn  ASGI server used to run the FastAPI app.
Swagger UI Auto-generated API documentation that helped test and visualize the endpoints.
** Project Overview:**
This project focuses on building a complete machine learning pipeline to predict the survival of passengers aboard the Titanic based on features such as age, gender, class, and fare. After training the model, I deployed it using FastAPI, so users can interact with the model in real-time through an API endpoint.
The overall flow:
Load Titanic dataset from a remote source.
Clean and preprocess the data.
Train a Random Forest classifier.
Save the model using pickle.
Create an API using FastAPI to make real-time predictions.
Test and validate using Swagger UI.
im listing some challenges faced during the task :
Like every real-world project, this one came with a fair share of challenges:

Library Errors & Environment Setup:
Initially, I ran into issues with installing dependencies like tensorflow, pandas, and scikit-learn due to Python version conflicts. I learned the importance of using compatible versions and managing virtual environments for smooth installations.

Module Import Errors:
When I tried to run the API using Uvicorn, I kept getting ModuleNotFoundError because I had accidentally named both my folder and Python file as titanic_project, which confused Python. Renaming the file to api.py resolved the issue.

Data Preprocessing Bugs:
Handling categorical data like 'Sex' and ensuring all transformations were applied consistently across training and prediction pipelines took time to debug.

Understanding ASGI and FastAPI Structure:
Unlike Flask, FastAPI is async-based and follows stricter structure. Learning how to define models using Pydantic and link everything using decorators was initially confusing but became easier with practice.

 What I Learned:
This task was extremely beneficial in making me more confident with end-to-end machine learning deployment. Specifically, I learned:

How to clean and preprocess real-world datasets.

How to build scalable ML pipelines using Pipeline and ColumnTransformer.

How to save and load models using pickle. this was new to me but i learned during this project

How to expose ML models as REST APIs using FastAPI.

The importance of API testing and documentation using Swagger UI.

It wasn’t just about writing ML code — it was about productizing it for real-time use.

This project simulates a real-world business scenario. Predictive models like this can be applied to:

Customer churn prediction (similar data structure).

Loan approval systems in fintech.

Medical diagnosis tools (survival prediction, risk assessment).

Insurance claims and fraud detection.

Embedded decision-making tools in web or mobile apps.

By exposing the model as an API, it can be integrated into any front-end or enterprise application. For example, a travel company could integrate this model into their CRM to estimate passenger risk for certain scenarios.

This task wasn't just a coding exercise — it was a complete simulation of how machine learning models are deployed in production. It taught me to think like a developer and an engineer, not just a data scientist. By completing this project, I now have a solid understanding of how data-driven products are built from scratch and delivered to users through APIs.

I'm proud to say this project has boosted my technical confidence, and I now feel more prepared to handle full-stack data science problems in real-world settings.

<img width="1846" height="865" alt="Image" src="https://github.com/user-attachments/assets/2f762fb5-5c83-486c-b65e-cde414977c36" />
<img width="1830" height="863" alt="Image" src="https://github.com/user-attachments/assets/20e75849-6024-4e29-8015-11415bb8c7d8" />
<img width="1888" height="966" alt="Image" src="https://github.com/user-attachments/assets/47f32ded-7f89-4bb2-ad03-02d582d65822" />
<img width="921" height="940" alt="Image" src="https://github.com/user-attachments/assets/969d4245-ca9e-4781-bbb2-bc736e426856" />
<img width="863" height="288" alt="Image" src="https://github.com/user-attachments/assets/93c66386-7f0e-4f36-8d12-9d47d7703a5f" />











