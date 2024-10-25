# University Clustering using SVD and Flask

## Project Overview
This project utilizes Singular Value Decomposition (SVD) to reduce the dimensionality of university data, focusing on clustering and feature extraction. A Flask-based web application enables users to upload new university data and process it through a saved SVD model for dimensionality reduction and visualization.

## Features
#### Data Collection: University data, including 25 U.S. institutions, with 7 key features (e.g., SAT scores, acceptance rates).
#### SVD Dimensionality Reduction: Reduces dataset dimensionality to simplify feature analysis.
#### Flask Web Application: A user-friendly interface for uploading data and viewing SVD-transformed results.

## Technologies Used
#### Python (Pandas, NumPy, Scikit-learn, Matplotlib)
#### Flask (for web interface)
#### Joblib (for model persistence)
#### Excel (for data input/output)

## Project Structure
#### app.py: Flask application code for handling file uploads and SVD transformation.
#### University_Clustering_SVD.ipynb: Jupyter notebook containing data preprocessing, SVD implementation, and visualization.
#### svd_DimRed: Serialized pipeline with imputation, standardization, and SVD transformation.
#### templates: HTML files for web interface rendering.

## Installation
#### Clone this repository.
#### Install the necessary dependencies:
#### code:pip install -r requirements.txt
#### Run the Flask application:
#### code : python app.py

## Usage
#### Open the app in your web browser.
#### Upload an Excel file with university data.
#### View the transformed SVD output.

## Data
#### The dataset includes university information with features such as:

#### SAT: Average SAT scores.
#### Top10: % of top 10 academic rank students.
#### Accept: Acceptance rate.
#### SFRatio: Student-to-faculty ratio.
#### Expenses: Total cost in USD.
#### GradRate: Graduation rate.

## Future Enhancements
#### Add clustering algorithms (e.g., K-Means) to analyze SVD components.
#### Implement interactive plots for a more dynamic UI.

