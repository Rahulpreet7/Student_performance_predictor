## End to End machine learning project
Approach for the project <br />
<br />
**Data Ingestion** :
In Data Ingestion phase the data is first read as csv. <br />
Then the data is split into training and testing and saved as csv file. <br />
**Data Transformation** :
In this phase a ColumnTransformer Pipeline is created. <br />
for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data. <br />
for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler. <br />
This preprocessor is saved as pickle file. <br />
**Model Training** :
In this phase base model is tested . The best model found is found. <br />
After this hyperparameter tuning is performed. <br />
This model is saved as pickle file. <br />
**Prediction Pipeline** :
This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python. <br />
**Flask App creation** :
Flask app is created with User Interface to predict the student's performance on a math test inside a Web Application. <br />
**Deployment** :
The application will be deployed on AWS or Azure using either CI/CD pipelines or Github Actions.
