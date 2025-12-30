import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load models
@st.cache_resource
def load_models():
    try:
        model = pickle.load(open('amazon_books_model.pkl', 'rb'))
        main_genre_encoder = pickle.load(open('main_genre_encoder.pkl', 'rb'))
        sub_genre_encoder = pickle.load(open('sub_genre_encoder.pkl', 'rb'))
        return model, main_genre_encoder, sub_genre_encoder
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None, None

def main():
    st.title("📚 Amazon Bestseller Predictor")
    st.markdown("Predict whether a book will become an Amazon bestseller")
    
    # Load models
    model, main_genre_encoder, sub_genre_encoder = load_models()
    
    if model is None:
        st.error("Failed to load models. Please ensure all .pkl files are present.")
        return
    
    # Sidebar for input
    st.sidebar.header("Book Information")
    
    # Get available genres from encoders (both are LabelEncoders)
    try:
        if hasattr(main_genre_encoder, 'classes_'):
            main_genres = main_genre_encoder.classes_.tolist()
        else:
            main_genres = ['Literature & Fiction']  # Default fallback
    except:
        main_genres = ['Literature & Fiction']  # Default fallback
    
    try:
        if hasattr(sub_genre_encoder, 'classes_'):
            sub_genres = sub_genre_encoder.classes_.tolist()
        else:
            sub_genres = ['Romance']  # Default fallback
    except:
        sub_genres = ['Romance']  # Default fallback
    
    # Input fields in the order expected by the model: Price, Rating, No. of People rated, Main Genre, Sub Genre
    price = st.sidebar.number_input("Price ($)", min_value=0.0, value=9.99, step=0.01)
    rating = st.sidebar.slider("Average Rating", 0.0, 5.0, 4.0, 0.1)
    num_reviews = st.sidebar.number_input("Number of People Rated", min_value=0, value=100, step=10)
    main_genre = st.sidebar.selectbox("Main Genre", main_genres)
    sub_genre = st.sidebar.selectbox("Sub Genre", sub_genres)
    
    # Encode genres
    try:
        main_genre_encoded = main_genre_encoder.transform([main_genre])[0]
    except:
        main_genre_encoded = 0
    
    try:
        sub_genre_encoded = sub_genre_encoder.transform([sub_genre])[0]
    except:
        sub_genre_encoded = 0
    
    # Prepare features in the exact order expected by the model: Price, Rating, No. of People rated, Main Genre, Sub Genre
    features = np.array([[price, rating, num_reviews, main_genre_encoded, sub_genre_encoded]])
    
    # Make prediction
    if st.sidebar.button("Predict Bestseller Status"):
        try:
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0]
            
            st.success("### Prediction Complete!")
            
            if hasattr(model, 'classes_'):
                class_names = model.classes_
            else:
                class_names = ['Not Bestseller', 'Bestseller']
            
            if prediction == 1 or (isinstance(prediction, str) and 'bestseller' in str(prediction).lower()):
                st.balloons()
                st.markdown("### ✅ **This book is predicted to be a BESTSELLER!**")
            else:
                st.markdown("### ❌ **This book is predicted NOT to be a bestseller.**")
            
            # Show probabilities
            if len(probability) == 2:
                st.metric("Bestseller Probability", f"{probability[1]*100:.2f}%")
                st.metric("Not Bestseller Probability", f"{probability[0]*100:.2f}%")
            
        except Exception as e:
            st.error(f"Error making prediction: {e}")
            st.info("The model might expect different features. Check the model structure.")
    
    # Display model info
    with st.expander("Model Information"):
        st.write(f"Model Type: {type(model).__name__}")
        st.write(f"Main Genre Encoder: {type(main_genre_encoder).__name__}")
        st.write(f"Sub Genre Encoder: {type(sub_genre_encoder).__name__}")

if __name__ == "__main__":
    main()
