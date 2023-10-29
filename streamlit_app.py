import streamlit
import pandas
streamlit.title("YashOne Food App")
streamlit.header("Get your food at your Door step...")
streamlit.text("what food We Serves :")
food = pandas.read_csv(uni-lab-files.s3.us-west-2-amazonaws.com/dabw/fruit_macros.txt)
streamlit.dataframe(food)
