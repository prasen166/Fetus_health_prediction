import streamlit as st
import pickle


with open('fetus_health_88.pkl', 'rb') as f:
    model = pickle.load(f)


def map_to_category(prediction):
    if prediction == 0:
        return "Normal"
    elif prediction == 1:
        return "Suspect"
    elif prediction == 2:
        return "Pathological"
    else:
        return "Unknown"


def make_prediction(baseline, accelerations, fetal_movement, uterine_contractions,
                    light_decelerations, severe_decelerations, prolongued_decelerations,
                    abnormal_short_term_variability, mean_value_of_short_term_variability,
                    percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability,
                    histogram_width, histogram_min, histogram_max, histogram_number_of_peaks,
                    histogram_number_of_zeroes, histogram_mode, histogram_mean, histogram_median,
                    histogram_variance, histogram_tendency):
    
    
    data = [[baseline, accelerations, fetal_movement, uterine_contractions,
             light_decelerations, severe_decelerations, prolongued_decelerations,
             abnormal_short_term_variability, mean_value_of_short_term_variability,
             percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability,
             histogram_width, histogram_min, histogram_max, histogram_number_of_peaks,
             histogram_number_of_zeroes, histogram_mode, histogram_mean, histogram_median,
             histogram_variance, histogram_tendency]]
    
    
    prediction = model.predict(data)
    

    category = map_to_category(prediction[0])
    
    return category


def main():
    st.title('Fetal Health Prediction')
    st.write('Enter the required parameters to predict fetal health:')
    

    baseline = st.number_input('Baseline Value', step=0.1)  
    accelerations = st.number_input('Accelerations', step=0.1)
    fetal_movement = st.number_input('Fetal Movement', step=0.1)
    uterine_contractions = st.number_input('Uterine Contractions', step=0.1)
    light_decelerations = st.number_input('Light Decelerations', step=0.1)
    severe_decelerations = st.number_input('Severe Decelerations', step=0.1)
    prolongued_decelerations = st.number_input('Prolongued Decelerations', step=0.1)
    abnormal_short_term_variability = st.number_input('Abnormal Short Term Variability', step=0.1)
    mean_value_of_short_term_variability = st.number_input('Mean Value of Short Term Variability', step=0.1)
    percentage_of_time_with_abnormal_long_term_variability = st.number_input('Percentage of Time with Abnormal Long Term Variability', step=0.1)
    mean_value_of_long_term_variability = st.number_input('Mean Value of Long Term Variability', step=0.1)
    histogram_width = st.number_input('Histogram Width', step=0.1)
    histogram_min = st.number_input('Histogram Min', step=0.1)
    histogram_max = st.number_input('Histogram Max', step=0.1)
    histogram_number_of_peaks = st.number_input('Histogram Number of Peaks', step=0.1)
    histogram_number_of_zeroes = st.number_input('Histogram Number of Zeroes', step=0.1)
    histogram_mode = st.number_input('Histogram Mode', step=0.1)
    histogram_mean = st.number_input('Histogram Mean', step=0.1)
    histogram_median = st.number_input('Histogram Median', step=0.1)
    histogram_variance = st.number_input('Histogram Variance', step=0.1)
    histogram_tendency = st.number_input('Histogram Tendency', step=0.1)
    
    
    if st.button('Predict'):
        prediction_result = make_prediction(baseline, accelerations, fetal_movement, uterine_contractions,
                                           light_decelerations, severe_decelerations, prolongued_decelerations,
                                           abnormal_short_term_variability, mean_value_of_short_term_variability,
                                           percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability,
                                           histogram_width, histogram_min, histogram_max, histogram_number_of_peaks,
                                           histogram_number_of_zeroes, histogram_mode, histogram_mean, histogram_median,
                                           histogram_variance, histogram_tendency)
        st.write(f'Prediction Result: {prediction_result}')

if __name__ == '__main__':
    main()
