import os 
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader


## streamli app
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

##Get the groq api key and url(YT or website) field to be summarized
with st.sidebar:
    st.title("Settings")
    groq_api_key=st.text_input("Enter Your Groq Api key",type='password',value='')
    temperature=st.slider("Temperature",min_value=0.0,max_value=1.0,value=0.3)
generic_url=st.text_input("Url()",label_visibility="collapsed")
llm=ChatGroq(model='llama-3.3-70b-versatile',groq_api_key=groq_api_key)

#prompt template
prompt_template=""" 
provide the summary of the following content in 300 words.
i want a beautiful presenatation format with amazing way.
content:{text}

"""
prompt=PromptTemplate(input_variables=['text'],template=prompt_template)



if st.button("Summarize the  Content from YT or website"):
    ##validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.warning("please provide the url and Api key")
    elif not validators.url(generic_url):
        st.warning("Please enter valid url(). it can may be a YT video url or website url()")
    else:

        try:
            with st.spinner("waiting...."):
            #loading the website or video data
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,)
                docs=loader.load()

                #chain for summarization
                chain=load_summarize_chain(llm,chain_type='stuff',prompt=prompt)
                output_summary=chain.run(docs)
                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")

                 
                



