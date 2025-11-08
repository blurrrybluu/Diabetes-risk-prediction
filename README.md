AI-Powered Web App using PySpark, scikit-learn & Streamlit



Live App  
[https://your-link-here.streamlit.app](https://your-link-here.streamlit.app) *(updated after deployment)*


Features  
- Predicts diabetes risk in real-time  
- Uses Glucose, BMI, Age, Pregnancies+ BMI Category 
- 85% AUC with Random Forest  
- Feature importance+ clinical explanations  
- Mobile-friendly web interface  



 Dataset  
[Pima Indians Diabetes (UCI)](https://www.kaggle.com/uciml/pima-indians-diabetes-database)  
- 768 female patients  
- 8 clinical features + binary outcome  



Tech Stack  
| Layer 			                  | Tool                   				|
|------------------------------	|------------------------------ |
| Data 				                  | PySpark, Pandas	             	|
| Model 			                  | scikit-learn (Random Forest)  |
| Deployment 		              	| Streamlit, Streamlit Cloud    |  
| Versioning 			              | GitHub 		                   	|

Model Performance
AUC: 0.85
Top Predictor: Glucose (28%)
Pregnancies: 5th most important (9%)


How to Run Locally  
```bash
pip install streamlit scikit-learn pandas joblib
streamlit run app.py


