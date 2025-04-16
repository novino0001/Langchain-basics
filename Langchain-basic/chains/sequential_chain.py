from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Generate a detailed report on {topic}"
)

prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Generate a 5 pointer summary from the following text \n {text}"
)

model = ChatOpenAI()
parser = StrOutputParser()

chain = prompt1 | model | prompt2 | model | parser

result = chain.invoke({"topic": "Is AI Reduce the job in corporate"})

print(result)

chain.get_graph().print_ascii() 