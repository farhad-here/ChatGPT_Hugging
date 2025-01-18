import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
st.set_page_config(page_title="🤗💬 HugChat ChatBot Search")
#title
st.header('🤗HugChat ChatBot Search')
#---------------------------------------------------------
#chat 
msgChat=st.chat_input('Your MSG')
email = st.sidebar.text_input('Email:')
password = st.sidebar.text_input('Password:')
# Store LLM generated responses
if msgChat == None:
       st.chat_message("assistant").write("What do you want from me(-_-)?")

else:
       # Log in to huggingface and grant authorization to huggingchat
       if email and password:
              EMAIL = f"{email}"
              PASSWD = f"{password}"
              #log
              sign = Login(EMAIL, PASSWD)
              cookies = sign.login()
              cookie_path_dir = "./cooky/"
              sign.saveCookiesToDir(cookie_path_dir)

              # Create your ChatBot
              bot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
              id = bot.new_conversation()
              bot.change_conversation(id)
              query_result = bot.chat(msgChat, web_search=True)
              st.chat_message("user").write(msgChat)
              st.chat_message("assistant").write(f"{query_result}")
              for source in query_result.web_search_sources:
                     st.chat_message("assistant").write(f"{source.link}")
                     st.chat_message("assistant").write(f"{source.title}")
       