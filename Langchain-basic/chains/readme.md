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


****************************************sequential chaining****************************************
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


*************************************parallel chaining*********************************************                                                                       
Notes and Quiz

- In June 1975, Prime Minister Indira Gandhi declared a state of emergency in India that lasted until 1977. This period was marked by the suspension of civil liberties and the suppression of political opposition.
- During the emergency, many political opponents of Gandhi were jailed and opposition groups were banned. It was a challenging time for those who spoke out against the government.
- Narendra Modi, currently the Prime Minister of India, was appointed general secretary of the Gujarat Lok Sangharsh Samiti, an RSS committee opposing the Emergency in Gujarat. He played a significant role in coordinating opposition activities.
- The RSS, a right-wing organization to which Modi belonged, was banned during the emergency. This forced Modi to go underground and travel in disguise to avoid arrest.
- Despite the risks, Modi was actively involved in printing pamphlets, organizing demonstrations, creating safe houses, and raising funds for political refugees and activists fighting against the emergency rule.
- Modi's efforts during the emergency brought him into contact with prominent national political figures, including trade unionist George Fernandes. These connections would later prove beneficial in his political career.
- Modi even wrote a book titled "Sangharsh Ma Gujarat" describing the events and his experiences during the Emergency, shedding light on the struggles faced by the opposition.

Quiz:
1. When did Indira Gandhi declare a state of emergency in India?
2. What did Modi do during the state of emergency?
3. How did Modi avoid arrest during the emergency?
4. What was Modi's role in coordinating opposition to the government?
5. Who did Modi meet during his involvement in political activism during the emergency?
                                                        +---------------------------+
                                                        | Parallel<notes,quiz>Input |
                                                        +---------------------------+
                                                            **               **
                                                        ***                   ***
                                                        **                         **
                                            +----------------+                +----------------+
                                            | PromptTemplate |                | PromptTemplate |
                                            +----------------+                +----------------+
                                                    *                               *
                                                    *                               *
                                                    *                               *
                                            +------------+                    +------------+
                                            | ChatOpenAI |                    | ChatOpenAI |
                                            +------------+                    +------------+
                                                    *                               *
                                                    *                               *
                                                    *                               *
                                            +-----------------+              +-----------------+
                                            | StrOutputParser |              | StrOutputParser |
                                            +-----------------+              +-----------------+
                                                            **               **
                                                            ***         ***
                                                                **     **
                                                    +----------------------------+
                                                    | Parallel<notes,quiz>Output |
                                                    +----------------------------+
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

***************************conditional chaining**************************

I am sorry to hear about your experience. We are constantly striving to improve and your feedback is valuable to us. Please let us know how we can make things right and ensure a better experience in the future. Thank you for bringing this to our attention.
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
                                                        +----------------------+
                                                        | PydanticOutputParser |
                                                        +----------------------+
                                                                    *
                                                                    *
                                                                    *
                                                            +--------+
                                                            | Branch |
                                                            +--------+
                                                                    *
                                                                    *
                                                                    *
                                                            +--------------+
                                                            | BranchOutput |
                                                            +--------------+