def translator(transcribed_text:str , language_convertable:str)->str:
    TRANSLATOR_PROMPT = f""" 
React Yourself as a translater . A sentence will be provided in English. The Input Given will be a streaming Input reduce the inputs by reducing the repeated words and provide only the content .
you must provide text in the language that have suggested as following . Here the suggested language is to be strictly followed.
when you got to know about the language you should be well versed at the language and also save the grammer of the language for future references. Now you must convert the sentence bellow to the required language suggested
The grammer of the language and meaningfulness of the sentence shouldn't get changed . 
Note : 
1) The raw data you achieve to convert is a live streaming data so please consider yourself as the speaker and present in the same way as the speaker does. 
2) Always check for the meaningfulness of the sentence and the grammer of the language to be used . 
3) Always look for the cripsy terms in that converting language . Act  good as much as a translator . 
4) EXTERMELY IMP: Here Only the output of the converted  sentence should be shown in the json format as following the fields langname,content.
5) Please verify the output that you have generated once and also check the structure that have been provided is supercorrect .
Check the grammer twice before writing -
The Above Notes are to be strictly followed if not if any inconvivnence happened you will be rated low.

The sentence to get converted is -  {transcribed_text}
The language to be converted is - {language_convertable}
"""
    return TRANSLATOR_PROMPT

def generate_ppt(context:str,categories:str,suggestions:str)->str:
    try:
     json_data = """
   {
     "title": "Presentation Title",  
     "slides": [
        {
            "title": "Slide Title 1", 
            "content": [
                {
                    "text": "Content text here"  
                }
            ]
        },
        {
            "title": "Slide with Table",  
            "table_data": {
                "headers": ["Column 1", "Column 2", "Column 3"],  
                "rows": [
                    ["Row 1, Col 1", "Row 1, Col 2", "Row 1, Col 3"],  
                    ["Row 2, Col 1", "Row 2, Col 2", "Row 2, Col 3"]
                ]
            }
        },
        {
            "title": "Slide with Bar Chart",  
            "chart_type": "bar", 
            "data": {
                "Category 1": 0, 
                "Category 2": 0,
                "Category 3": 0
            }
        },
        {
            "title": "Slide with Pie Chart",  
            "chart_type": "pie", 
            "data": {
                "Category A": 0,  
                "Category B": 0,
                "Category C": 0
            }
        }
      ]
      }
     """
     PPT_GENERATE_INFO = f"""
     {json_data}
     Generate the Output in this standard json format.
       Your a Professionalistic Designer where you can design and formulate various raw data into powerpoint.Here I will provide Three categories of 
      input data  namely Content, Categories and Sugeestions.One is the Content which can make the body content and Other one is the Categories that are to be defined for making the PPT as a Suggestion and the Other are the Informations 
     as Additional valuable inputs. All these inputs are provided in a form of list. so, process the list and provide the content for the ppt generation strictly as json object format mentioned above.
     content - {context}
     categories - {categories}
     suggestions - {suggestions}
     Note: Provide Only the Json Very Imp Don't Provide any other answers or other suggestions to it.
     """
     print(PPT_GENERATE_INFO)
     return PPT_GENERATE_INFO
    except Exception as e:
     print(e)
