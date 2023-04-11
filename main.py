import os
import wget

import streamlit as st

# Page Config
# Setting Page Layout to wide streamlit
st.set_page_config(layout='wide')

# sidebar
st.sidebar.title('Navigation')

# Navigational Pages
pages = [
    'Home', 'Data Pre-Processing', 'Data Profiling', 'Classifier',
    'Neural Nets'
]
# Dropdown in sidebar
page = st.sidebar.selectbox('', pages)

# streamlit session variables
if 'file' not in st.session_state:
    st.session_state.file = f''

if 'cwd' not in st.session_state:
    st.session_state.cwd = os.getcwd()

if 'file_ch' not in st.session_state:
    st.session_state.file_ch = ''

# HomePage
if page == 'Home':
    st.title('Welcome to the world of Data Science')
    st.image(f"{st.session_state.cwd}/Images/home.png")
    st.write()
    st.subheader("You can find all the learning materials here:")
    st.write('Data Science Community: https://www.kaggle.com/')
    st.write('Famous Datasets: https://www.kaggle.com/datasets')
    st.write(f'Developer: \n Pratik Mishra')

# Data Pre Processing
elif page == 'Data Pre-Processing':
    st.header('Data Pre Processing')
    st.image("./Images/data.jpg")
    st.write()
    file_dir = f"{st.session_state.cwd}/Files/"
    file_choice = ['web', 'upload from local']
    st.session_state.file_ch = st.selectbox(
        "Please select your choice to upload file:", file_choice)
    if st.session_state.file_ch == 'web':
        url = st.text_input('Please enter the url to download the dataset:')
        file_name = st.text_input(
            "Please enter the file name along with extension e.g: file.csv")
        d = st.button('Download')
        if d:
            if url == '':
                st.error('Url cannot be empty !!')
            elif ('.' or 'https' or 'http') not in url:
                st.error('Please enter a valid url !!')
            elif file_name == '':
                st.error('File name cannot be empty !!')
            else:
                # downloading file
                wget.download(url, f'{st.session_state.cwd}/Files/{file_name}')
                st.session_state.file = f"{st.session_state.cwd}/Files/{file_name}"
    elif st.session_state.file_ch == 'upload from local':
        uploaded_file = st.file_uploader('Please select file to upload:',
                                         type=['csv', 'xlsx'])
        if uploaded_file is not None:
            st.write(uploaded_file)

# Data Profiling
elif page == 'Data Profiling':
    pass

# Classification
elif page == 'Classifier':
    pass

# Neural Network - Deep Learning
elif page == 'Neural Nets':
    pass
