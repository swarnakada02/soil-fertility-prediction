# Soil-Fertility-Prediction-Using-Machine-Learning

## CONTENTS OF THIS FILE
1. [Purpose of the project](#purpose-of-the-project)
2. [Dataset Introduction](#dataset-introduction)
3. [Software files](#software-files)
4. [Project files](#project-files)
5. [Important Links](#important-links)
6. [Project Execution Steps](#project-execution-steps)

### 1. Purpose of the Project
***
The proposed system aims to predict the soil fertility for better yield production or vegetation cover.To be precise and accurate in predicting fertility, the project analyses the nutrient contents present in the soil.With this, we can reduce the human effort in the industrial sector where they predict the quality of the soil.
We have taken soil dataset and preprocessed it and implemented various models on preprocessed data for to find the better accurate model. The models that are implemented are:
* Linear Model
* Support Vector Regression (Linear)
* Support Vector Regression(RBF)
* Support Vector Regression (Poly)
* Decision Tree Regression
* Random Forest Regression

### 2. Dataset Introduction
***
This dataset contains the various elements found in the soil, for instance, organic matter, various nitrogen compounds, potassium, sodium, sulphates, boron, etc, It also contains various soil properties like pH. The target of this data is set to predict the vegetation cover which is the percent vegetative cover. The higher the vegetation cover higher is the fertility of the soil for crops.
Vegatation cover is calcuated in percentage from 1 to 100, so, it becomes the regresion task. To achive the results various regression methods are applied and performance of each model is analysed.

	1.Sample
	2.DIR.
	3.INT/EXT
	4.Sub-Sample #
	5.Date
	6.Time
	7.Latitude
	8.Longitude
	9.Slope
	10.Aspect
	11.%Veg.Cover
	12.NO3-N(ppm)
	13.NH4-N(ppm)
	14.P Bicar(ppm)
	15.K Acet(ppm)
	16.S04-S(ppm)
	17.B(ppm)
	18.Organic Matter %
	19.pH
	20.Zn(ppm)
	21.Cu(ppm)
	22.Fe(ppm)
	23.Ca(meq/100g)
	24.Mg(meq/100g)
	25.Na(meq/100g)

### 3. Software files
***
In this project we need NumPy,pandas,sikit-learn,Google Collaboratory and flask.We need to install NumPy,pandas,sikit-learn and flask in your system before starting up with the project.We can use the Google Collaboratory directly through the browser without any installation.

### 4. Project files
***
The project files are:
* Soil_Fertility_Prediction.ipynb
* project.py
* ProjectHomePage.html
* Results.html
* dataset.txt
* soil_data.xlsx
* preprocessed_data.csv

### 5. Important links
***
The below links are used for finding installation commands.
* NumPy - https://numpy.org/install/
* Pandas - https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
* scikit-learn- https://scikit-learn.org/stable/install.html
* Flask - https://flask.palletsprojects.com/en/2.0.x/installation/
* Google Collaboratory - https://research.google.com/colaboratory/

### 6. Project Execution Steps
***
   1. Create a folder and place dataset.txt,project.py files in it.
   2. Create a folder with name templates in the folder where we placed dataset.txt,project files.
   3. Place the ProjectHomePage.html file in templates folder.
   4. Select project.py file--> Right click on project.py file --> select open with --> click Python.
   5. Python terminal will be opened and a url will be displayed .
   6. Copy and paste that url "http://127.0.0.1:5000/" in your browser and press enter the webpage will be opened.
   7. Enter the 14 nutrient values in the webpage and click on predict button.
   8. The result will be displayed in the webpage.
