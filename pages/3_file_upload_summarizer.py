import streamlit as st
import pdfplumber
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

def main():
    st.header("Summarize the content of any PDF")
    uploaded_file = st.file_uploader("Choose your .pdf file.", type="pdf")
    if uploaded_file is not None:
        whole_text = extract_data(uploaded_file)
        result = []
        with st.form('summarize_form', clear_on_submit=True):
            openai_api_key = "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"
            submitted = st.form_submit_button('Submit')
            if submitted and openai_api_key.startswith('sk-'):
                with st.spinner('Calculating...'):
                    response = generate_response(whole_text)
                    result.append(response)
                    del openai_api_key
        if len(result):
            st.info(response)

def extract_data(uploaded_pdf):
    with pdfplumber.open(uploaded_pdf) as pdf:
        # printing out the text from pdf
        all_text = ""
        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            print( single_page_text )
            # separate each page's text with newline
            all_text = all_text + '\n' + single_page_text
        return all_text

def generate_response(txt):
    # Instantiate the LLM model
    llm = OpenAI(temperature=0, openai_api_key="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")
    # Split text
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(txt)
    # Create multiple documents
    docs = [Document(page_content=t) for t in texts]
    # Text summarization
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.run(docs)

if __name__ == "__main__":
    main()