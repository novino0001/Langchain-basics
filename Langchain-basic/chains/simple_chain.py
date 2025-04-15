from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    input_variables=["question"],
    template="What about of {question}?"
)
model = ChatOpenAI(temperature=0.7)
parser = StrOutputParser()

chain = prompt | model | parser 

result = chain.invoke({"question": "France"})
print(result)
chain.get_graph().print_ascii()  