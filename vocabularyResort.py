# For markdown vocabulary resort
'''
目前实现了读取vocabulary.md
接下来需要按以下算法实现自动排序功能：
0. 建一个列表数据结构，列表中每项包含单词和单元（包含单词和音标、解释等）两项。
1. 将文件中所有单元split成个体，并放入上述列表每项的第2个位置。
2. 列表每项中，提取单元中的“单词”，并放入第1个位置。
3. 列表根据每项第一个位置的单词重新排序。
4. 按照定制格式输出到vocabulary.md文件。
'''

import os
os.chdir("C:\mcode\mDoc")

print("CurrentDIR：", os.getcwd())
print("FilesList:", os.listdir())

file = open("vocabulary.md", encoding='utf-8', errors='ignore')
data = file.read()
print(data)
file.close()
