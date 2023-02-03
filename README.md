# Motor Current Signature Analysis to detect Anomalies
 A machine Learning model to detect anomalies in a dataset consisting real time current readings of a 3-phase AC motor (3.2 hp).
 
## Importance of  Motor Current Signature Analysis
Motor current signature analysis is a technique that helps in determining the induction motor’s operating condition without disturbing production. In other words, it senses an electrical signal that has current components and identifies the faults in the initial stage. Therefore, it plays a pivotal role in preventing damage and diagnosing motor failure.

## Approach taken to solve this problem:
* The dataset having current readings are in 6 files. So combine it into a single source.
* <b>Data Analysis</b> and <b>Data Visualizations</b> to understand the pattern and distribution of data
* Necessary data pre-processing steps to make the data ready for modeling
* As there are no target labels, this is an <b>Unsupervised machine learning</b> problem.
* Fit the data to <b>KMeans Clustering </b>algorithm and split the data into 2 clusters.
* The cluster value can be stored as a target column and now our problem becomes a <b>Classification type</b>.
* Now, use the whole dataset along with target column to train and build a classification model (<b>Random Forest Classifier</b>)
* Model is saved to a pickle file so that it can be imported and reused with any values.

## The steps involved in this task:
1. Loading the tools
2. Loading the dataset
3. Exploratory Data Analysis (EDA)
4. Feature scaling
5. Model Building- KMeans Clustering algorithm
6. Data clustered into anomaly or not and exported to "predicted.csv" file
7. Classification Model (Random Forest Classifier) to predict class (Anomaly or not) for future data
8. Test model by giving sample test data 
9. Model Evaluation
10. Save the model to a pickle file
