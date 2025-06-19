from dotenv import load_dotenv

load_dotenv()


import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Streamlitページ設定
st.set_page_config(page_title="専門家に質問しよう", layout="centered")

# UI：タイトルと説明
st.title("専門家に質問しよう")
st.markdown("""
このアプリでは、選択した専門家（歴史 or 健康）に質問することで、LLMから回答を得られます。
下のフォームに質問を入力し、専門家を選んでください。
""")

# 入力フォーム
user_input = st.text_input("質問を入力してください：")

# ラジオボタンで専門家選択
expert_type = st.radio(
    "質問先の専門家を選んでください：",
    ("歴史の専門家", "健康の専門家")
)

# LLM（GPT-4 or GPT-3.5）設定
llm = ChatOpenAI(temperature=0.7, model="gpt-4")

# 専門家ごとのシステムプロンプト
def get_system_prompt(expert):
    if expert == "歴史の専門家":
        return "あなたは博識な歴史の専門家です。質問に対して正確で分かりやすく答えてください。"
    elif expert == "健康の専門家":
        return "あなたは信頼できる健康アドバイザーです。質問者に親身になって健康面のアドバイスをしてください。"
    else:
        return "あなたはあらゆる分野に精通したアシスタントです。"

# プロンプト生成と回答関数
def get_llm_response(user_text, expert):
    messages = [
        SystemMessage(content=get_system_prompt(expert)),
        HumanMessage(content=user_text)
    ]
    return llm(messages).content

# 実行ボタンと出力
if st.button("質問する") and user_input:
    with st.spinner("専門家が考え中です..."):
        answer = get_llm_response(user_input, expert_type)
        st.success("回答:")
        st.write(answer)

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
