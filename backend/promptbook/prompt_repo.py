def translator(transcribed_text:str , language_convertable:str)->str:
    TRANSLATOR_PROMPT = f""" 
React Yourself as a translater . A sentence will be provided in English .The Input Given will be a streaming Input reduce the inputs by reducing the repeated words and provide only the content .
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