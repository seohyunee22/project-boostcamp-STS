import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_folder.predict import load_model, get_prediction

def main():
    st.title('문맥적 유사도 측정하기')
    st.header(': Semantic Text Similarity(STS)')

    st.image(Image.open('1.png'))
    st.image(Image.open('2.png'))


    model = load_model()
    model.eval()

    # 측정 결과들 모아두는 df
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame({
            'sentence 1': [],
            'sentence 2' : [],
            'similarity' : []
        })

    with st.form(key='문장입력 form'):
        sentence1 = st.text_input("Enter Sentence 1:")
        sentence2 = st.text_input("Enter Sentence 2:")
        form_submitted = st.form_submit_button('유사도 측정')

    if form_submitted:
        if sentence1 and sentence2:
            similarity_score = get_prediction(model, sentence1, sentence2)

            if not ((st.session_state.df['sentence 1'] == sentence1) & (st.session_state.df['sentence 2'] == sentence2)).any():    # 이미 있을 경우 추가 제외
                new_data = pd.DataFrame({
                    'sentence 1': [sentence1],
                    'sentence 2': [sentence2],
                    'similarity': [similarity_score]
                })
                st.session_state.df = pd.concat([st.session_state.df, new_data])
                
                # similarity 기준으로 순위 매기기
                st.session_state.df = st.session_state.df.sort_values(by='similarity', ascending=False).reset_index(drop=True)
                
                # rank 컬럼 추가
                st.session_state.df['rank'] = st.session_state.df.index + 1

            st.write(f"두 문장의 유사도 : {similarity_score}")
            st.success('성공!')
        else:
            st.error('error!')

    st.divider()
    col1, col2, col3 = st.columns(3)
    
    # df 크기 조절
    col1.checkbox("창 크기조절", value=True, key="use_container_width")

    # df 리셋
    if col2.button("데이터 리셋"):
        st.session_state.df = pd.DataFrame({
            'sentence 1': [],
            'sentence 2' : [],
            'similarity' : []
        })

    # df csv로 다운로드
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False, header=True).encode('cp949')
    csv = convert_df(st.session_state.df)
    col3.download_button(
        label="CSV로 다운받기",
        data=csv,
        file_name='outputs.csv',
        mime='text/csv',
    )

    st.dataframe(st.session_state.df, use_container_width=st.session_state.use_container_width)

main()
