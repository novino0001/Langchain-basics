from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()
model = ChatOpenAI()
pdf_filename = "ICPC Graph Optimization Challenge, Powered by Huawei, Conditions of Participation.docx.pdf"
# This gets the project root (one level up from Document-Loaders)
project_root = os.path.dirname(os.path.dirname(__file__))
pdf_path = os.path.join(project_root, pdf_filename)

loader = PyPDFLoader(pdf_path)
doc = loader.load()

 
print(len(doc))
print(doc[0].page_content)
print(doc[0].metadata)