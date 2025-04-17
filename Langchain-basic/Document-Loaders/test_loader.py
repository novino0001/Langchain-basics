import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    input_variables=["text"],
    template="Generate a poem of the following text \n {text}"
)

parser = StrOutputParser()

txt_filename = "text_loader.txt"
script_dir = os.path.dirname(__file__)
project_root = os.path.dirname(script_dir)

# Try script directory first, then project root
txt_paths = [
    os.path.join(script_dir, txt_filename),
    os.path.join(project_root, txt_filename)
]

txt_path = None
for path in txt_paths:
    if os.path.isfile(path):
        txt_path = path
        break

if not txt_path:
    print("Error: File not found in either location:")
    for path in txt_paths:
        print(f"  - {path}")
else:
    loader = TextLoader(txt_path, encoding="utf-8")
    doc = loader.load()
    chain = prompt | model | parser
    result = chain.invoke({"text": doc[0].page_content})
    print(result)