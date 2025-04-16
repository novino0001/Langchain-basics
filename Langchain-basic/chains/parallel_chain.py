from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain.schema.runnable import RunnableParallel

load_dotenv()
model1 = ChatOpenAI()
# model2 = ChatAnthropic(model_name = "claude-3-7-sonnet-20250219")
model2 = ChatOpenAI()

prompt1 = PromptTemplate(
    input_variables=["text"],
    template="Generate a short and simple notes from the following {text}"
)

prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Generate short 5 question answer from the following text \n{text}"
)

prompt3 = PromptTemplate(
    input_variables=["notes","quiz"],
    template="Merge the provided notes and quiz in a single document \n notes -> {notes} and quiz -> {quiz}"
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({"notes" : prompt1 | model1 | parser,
                                   "quiz" : prompt2 | model2 | parser})


merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain
 
text = """In June 1975, Prime Minister Indira Gandhi declared a state of emergency in India that lasted until 1977. During this period, known as  many of her political opponents were jailed and opposition groups were banned.[92][93] Modi was appointed general secretary of the Gujarat Lok Sangharsh Samit, an RSS committee coordinating opposition to the Emergency in Gujarat. Shortly afterwards, the RSS was banned.[94] Modi was forced to go underground in Gujarat and frequently travelled in disguise to avoid arrest, once dressing as a monk and once as a Sikh.[95] He became involved in the printing of pamphlets opposing the government, sending them to Delhi and organising demonstrations.[96][97] He was also involved with creating a network of safe houses for individuals who were wanted by the government, and in raising funds for political refugees and activists.[98] During this period, Modi wrote a Gujarati-language book titled Sangharsh Ma Gujarat (In the Struggles of Gujarat), which describes events during the Emergency.[99][100] While in this role, Modi met trade unionist and socialist activist George Fernandes and several other national political figures."""
result = chain.invoke({"text":text})


print(result)

chain.get_graph().print_ascii()

