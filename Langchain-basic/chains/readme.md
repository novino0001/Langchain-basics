******************************chains in Langchain-******************************
simple chaining--------------

What about France?
France is a country located in Western Europe known for its rich history, culture, and cuisine. It is famous for landmarks such as the Eiffel Tower, the Louvre Museum, and the Palace of Versailles. 
France is also known for its wine regions, fashion industry, and art scene. The country has a diverse landscape that includes mountains, beaches, and picturesque countryside. France is a popular tourist destination and a leading global power in terms of economics, politics, and culture.
                                                                        +-------------+       
                                                                        | PromptInput |
                                                                        +-------------+
                                                                                *
                                                                                *
                                                                                *
                                                                        +----------------+
                                                                        | PromptTemplate |
                                                                        +----------------+
                                                                                *
                                                                                *
                                                                                *
                                                                        +------------+
                                                                        | ChatOpenAI |
                                                                        +------------+
                                                                                *
                                                                                *
                                                                                *
                                                                    +-----------------+
                                                                    | StrOutputParser |
                                                                    +-----------------+
                                                                                *
                                                                                *
                                                                                *
                                                                    +-----------------------+
                                                                    | StrOutputParserOutput |
                                                                    +-----------------------+


