import streamlit as st
from model import generate_res


st.set_page_config(
    page_title='Генерация КНИР',
    initial_sidebar_state="expanded",
)
st.title('Генерация для КНИР')


text_ = st.text_area('Введите запрос:', '', height=25, key='text')

button_ = st.button("Сгенерировать:")

if button_:
    container = st.container()
    
    placeholder = container.empty()

    response_ = generate_res(text_)

    placeholder.info(response_)