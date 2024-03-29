# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("gapminder.tsv", sep="\t") # 외부 데이터
    return df

def plot_matplotlib():
    st.title("Categorical Bar Plot with Seaborn")
    df = load_data()
    fig, ax = plt.subplots()
    
    # Using Seaborn's barplot function
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("Bar Plot : Year vs. lifeExp")
    
    st.pyplot(fig)

def main():
    st.title("데이터 시각화 : 표 & 그래프")
 
    df = load_data() # 데이터 불러오기
    st.dataframe(df, use_container_width=True)

    #pandas style
    st.title("컬럼별 최대값 표")
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0))

    plot_matplotlib()
    
    
if __name__ == "__main__":
    main()