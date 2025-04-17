from langchain_community.document_loaders import DirectoryLoader ,PyPDFLoader

loader  = DirectoryLoader("policies", glob="*.pdf", loader_cls=PyPDFLoader)
doc = loader.load()

# print(len(doc))
print(doc[4].page_content)
# print(doc[0].metadata)