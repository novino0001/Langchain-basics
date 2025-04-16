from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain.schema.runnable import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal


load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal["positive" , "negative"] = Field(description="Sentiment of the feedback")
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    input_variables=["feedback"],
    template="Classify the sentiment of the following feedback text into positive or negative\n {feedback} \n {format_instructions}",
    partial_variables={"format_instructions" : parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({"feedback" : "I love this product but you should not buy it because currently this product have many issues"})
# print(result)
# print(result.sentiment)
prompt2 = PromptTemplate(
    input_variables=["feedback"],
    template="Write a appropriate response for the positive feedback \n {feedback}", 
)

prompt3 = PromptTemplate(
    input_variables=["feedback"],
    template="Write a appropriate response for the negative feedback \n {feedback}",
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "could not classify the sentiment"),
)


chain = classifier_chain | branch_chain

result = chain.invoke({"feedback" : "I loved this product but you should not buy it because currently this product have many issues"})
print(result)

chain.get_graph().print_ascii()
