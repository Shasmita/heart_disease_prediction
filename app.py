import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

heart_disease_model = pickle.load(open('saved_model/heart_disease_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction Project',
                          
                          ['Home',
                           'Heart Disease Prediction',
                           'Data Information'],
                          icons=['person','heart','activity'],
                          default_index=0)
    
    
# Home Page
if (selected == 'Home'):
    
    # page title
    st.title('Heart Disease Prediction Project')
    
    

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        CHOICES = {1: "Male", 2: "Female"}

        def format_func(option):
            return CHOICES[option]

        sex = st.selectbox("Gender", options=list(CHOICES.keys()), format_func=format_func)   
        
    with col3:
        CHOICES = {0: "Asymptomatic", 1: "Non-anginal pain", 2: "Atypical Angina", 3: "Typical Angina"}

        def format_func(option):
            return CHOICES[option]

        cp = st.selectbox("Chest pain Type", options=list(CHOICES.keys()), format_func=format_func)
        
    with col1:

        CHOICES = {0: "Nothing to Note", 1: "ST-T Wave abnormality", 2: "Left Ventricular Hypertrophy"}

        def format_func(option):
            return CHOICES[option]

        restecg = st.selectbox("Resting Electrocardiographic results", options=list(CHOICES.keys()), format_func=format_func)
        
    with col2:

        CHOICES = {0: "FBS < 120 mg/dl", 1: "FBS > 120 mg/dl"}

        def format_func(option):
            return CHOICES[option]

        fbs = st.selectbox("Fasting Blood Sugar", options=list(CHOICES.keys()), format_func=format_func)
        
    with col3:

        CHOICES = {0: "Yes", 1: "No"}

        def format_func(option):
            return CHOICES[option]

        exang = st.selectbox("Exercise Induced Angina", options=list(CHOICES.keys()), format_func=format_func)
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', '(0.0 - 6.0)')
        
    with col2:

        CHOICES = {0: "Normal", 1: "Fixed defect", 2: "Reversable defect"}

        def format_func(option):
            return CHOICES[option]

        thal = st.selectbox("Thalium Stress result", options=list(CHOICES.keys()), format_func=format_func)
        
        
    with col3:

        ca_ls = [0, 1, 2, 3, 4]
        ca = st.selectbox('Major vessels colored by flourosopy', ca_ls)

    with col1:
        trestbps = st.slider('Resting Blood Pressure', 0, 220, 120)
        
    with col2:
        chol = st.slider('Serum Cholestoral in mg/dl', 0, 600, 150)
        
    with col3:
        thalach = st.slider('Maximum Heart Rate Achieved', 0, 250, 100)
        
        

    CHOICES = {0: "Unslopping: Better heart rate with exercise", 1: "Flatsloping: Minimal change", 2: "Downslopings: Signs of unhealthy heart"}

    def format_func(option):
            return CHOICES[option]

    slope = st.selectbox("Slope of the peak exercise ST segment", options=list(CHOICES.keys()), format_func=format_func)
        
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Data Information Page
if (selected == "Data Information"):
    
    # page title
    st.title("Data Information")

    st.text('Age: age of the patient [years]')
    st.text('Sex: sex of the patient [M: Male, F: Female]')
    st.text('ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]')
    st.text('RestingBP: resting blood pressure [mm Hg]')
    st.text('Cholesterol: serum cholesterol [mm/dl]')
    st.text('FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]')
    st.text('RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV, LVH: showing probable or definite left ventricular hypertrophy by Estes criteria]')
    st.text('MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]')
    st.text('ExerciseAngina: exercise-induced angina [Y: Yes, N: No]')
    st.text('Oldpeak: oldpeak = ST [Numeric value measured in depression]')
    st.text('ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]')
    st.text(' HeartDisease: output class [1: heart disease, 0: Normal]''')
    
    
    


