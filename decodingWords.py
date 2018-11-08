import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

tree = ET.parse('words.xml')
root = tree.getroot()

words = pd.DataFrame(columns = ['word','trans','phonetic'])
for item in root:
    df = pd.DataFrame({'word': item[0].text,
                       'trans': item[1].text,
                       'phonetic': item[2].text},
                       index = item)
    print(df)
    words = pd.concat([words, df], ignore_index = True)
    words = words.drop_duplicates()

words.to_excel('words1.xlsx', sheet_name = '1')
