# alternative SeleniumURLLOader for heavy javascripts urls page
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.cardekho.com/mahindra/be-6")
doc = loader.load()
prompt = PromptTemplate(
    input_variables=["text"],
    template="Generate a poem of the following text \n {text}"
)

parser = StrOutputParser()

chain = prompt | model | parser

print(len(doc))
print(doc[0].page_content)
print(doc[0].metadata)
