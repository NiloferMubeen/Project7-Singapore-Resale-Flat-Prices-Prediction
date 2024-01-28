# Introduction
This report presents the process of designing a regression model to predict fair prices for the resale of public housing flats in Singapore based on historical data obtained between 2015 and 2024.
# Data Preprocessing
1. The dataset doesn not include any null values. But duplicates were found and dropped
2. The remaining lease column had values in the form of years and months(63 years and 7 months). This column was completely converted into months.
3. The columns like flat model, flat type, block, town, street name have high correlation with the resale price. Hence these columns were encoded using the sklearn.preprocessing.LabelEncoder.
# Splitting Data For Train, Test & Validation
The data is first split with 33% allocated for held-out training data that will be used to evaluate the final model’s performance after model selection.As the dataset is large, it is not necessary to do k-fold cross validation, and the rest of the data can just be split 70:30 again for training data and test data that is used to evaluate model performance during training.
# Libraries Used
1. sklearn
2. streamlit
3. pandas
4. numpy
5. matplotlib
6. seaborn
# Regression Algorithms tried:
1. Ridge Regression
2. Extra Trees Regressor
3. Decision Tree Regressor
4. Random Forest Regressor
5. XG Boost Regressor
# Model Selection
After careful evaluation and trying different regression Algorithms, the performances of all models were compared. The Extra trees, Random Forest and Decision tree models performed well. But the MSE 
was considerably reduced by the Random Forest model . Hence Random Forest Regressor was chosen as the Ideal model in this use case.
