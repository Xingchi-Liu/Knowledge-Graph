import re

# 读取文件
text_content_split = []
with open('../复变函数/复变函数论第五版钟玉泉高等教育出版社.txt', 'r', encoding='utf-8') as f:
    text_contents = f.readlines()
    for text_content in text_contents:
        text_content = text_content.strip()  #去除首尾空格
        list = text_content.split(' ')
        listnew = [i for i in list if i != '']
        text_content = ' '.join(listnew)      #去除空格
        text_content = ''.join([i.strip(' ') for i in text_content])   #去除空格
        text_content = text_content.replace('\n', '').replace('\t', '')
        text_content_split_list = re.split(r'。', text_content)
        for i in range(len(text_content_split_list)):
            text_content_split.append(text_content_split_list[i])
        #text_content = text_content.replace('。', '\n')
        #print(text_content_split_list)
#print(text_content_split)

# 将处理后的文本另存为一个新文件
with open('file_处理1.txt', 'w', encoding='utf-8') as f:
    for text_content in text_content_split:
        f.write(text_content + '\n')
#处理1：去除空格及换行，并按照句号分割换行
#处理2：删除新文件中的空行
file1 = open('file_处理1.txt', 'r', encoding='utf-8') # 要去掉空行的文件
file2 = open('file_处理2.txt', 'w', encoding='utf-8') # 生成没有空行的文件
try:
    for line in file1.readlines():
        if line == '\n':
            line = line.strip("\n")
        file2.write(line)
finally:
    file1.close()
    file2.close()


#分节

# 读取文件并存储到列表中
with open('file_处理2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 定义正则表达式
#pattern1 = r'\d{1,2}\.\d{1,2}(?!\.\d)'    #x.x
#pattern1 = r'\d\.\d'
pattern1 = r'(?<!\d)([1-9]|[1-9]\d|100)\.\d(?!\d)'
#pattern1 = r'第(.*?)章.*'

#pattern2 = r'\d{1,2}\.\d{1,2}\.\d{1,2}(?!\.\d)'    #x.x.x
pattern2 = r'(?<!\d)([1-9]|[1-9]\d|100)\.\d{1,2}\.\d{1,2}(?!\.\d)'
#pattern2 = r'第(.*?)条'

pattern = r'[、，。,]'
'''
lists = ['4.1', '4.11.3测试', '5.2.1', '5.1条件', '6.9.3测试']
for e in lists:
    if  re.match(pattern1, e) and re.match(pattern2,e):
        print(e)
'''

# with open file设置成了'a'而不是'w'，写入不覆盖，
# 因为数据中心设计规范有附录，里面有与正文相同的一级二级三级标题，如果重新跑记得要把原来的删除！！！！！
# 一级目录只有一行形如’1 xxx‘,没有增加对一级目录的判断，直接手动找到一级目录的位置并删除

# 遍历列表中的每一行，并将符合条件的行及其后续存储到对应的文件中
i = 0
print(len(lines))
while i < len(lines):
    # 如果当前行符合正则表达式，则将它和后续的行存储到对应的文件中
    if re.match(pattern1, lines[i]):
        #print('第', i, '行符合正则表达式pattern1:', lines[i])
        if re.match(pattern1, lines[i]) and re.match(pattern2, lines[i]):  #这种是形如4.11.3，如果不这么判断，会被匹配到4.1去
            match_level3_2 = re.match(pattern2, lines[i])
            #print('同时匹配pattern1和pattern2，匹配pattern2结果为：', match_level3_2.group())
            if re.search(pattern, lines[i]):
                filename = match_level3_2.group().strip() + '.txt'
                #print('直接用获取到的匹配结果做文件名：', filename)
            else:
                filename = lines[i].replace('\n', '') + '.txt'
                #print('匹配结果可以对应小标题，加入小标题作为文件名', filename)
        if re.match(pattern1, lines[i]) and not re.match(pattern2, lines[i]):
            match_level2 = re.match(pattern1, lines[i])
            #print('该行只能匹配pattern1，匹配结果为：', match_level2.group())
            if re.search(pattern, lines[i]):
                filename = match_level2.group().strip() + '.txt'
                #print('直接用获取到的匹配结果做文件名：', filename)
            else:
                filename = lines[i].replace('\n', '') + '.txt'
                #print('匹配结果可以对应小标题，加入小标题作为文件名', filename)
        if re.match(pattern2, lines[i]) and not re.match(pattern1, lines[i]):
            match_level3_1 = re.match(pattern1, lines[i])
            #print('该行只能匹配pattern2，匹配结果为：', match_level3_1.group())
            if re.search(pattern, lines[i]):
                filename = match_level3_1.group().strip() + '.txt'
                #rint('直接用获取到的匹配结果做文件名：', filename)
            else:
                filename = lines[i].replace('\n', '') + '.txt'
                #print('匹配结果可以对应小标题，加入小标题作为文件名', filename)
        #filename = match_level2.group().strip() + '.txt'

        with open(filename, 'a', encoding='utf-8') as f:
            f.write(lines[i])
            #print('打开filename文件，写入行line',i)
            i += 1
            #print('i+1,处理下一行', i)
            while i < len(lines):
                if re.match(pattern2, lines[i]):
                    #print('该行与pattern2匹配，break跳出while循环，回到第62行，重新开始和pattern1匹配')
                    break
                if re.match(pattern1, lines[i]):
                    #print('该行与pattern1匹配')
                    match_level2_2 = re.match(pattern1, lines[i])
                    #print('匹配结果为：', match_level2_2)
                    if match_level2_2 != match_level2:
                        #print('该行匹配出的pattern1与最开始的pattern1不一致，不属同一小节，break跳出循环，回到62行，重新开始与pattern1匹配')
                        break
                    if match_level2_2 == match_level2:
                        f.write(lines[i])
                        i += 1
                        #print(i)
                    break
                #print('既不与pattern1匹配也不与pattern2匹配，判定为该小节的正文，写入filename：', lines[i])
                f.write(lines[i])
                i += 1
                #print('i+1，处理下一行', i)
    else:
        i += 1
        #print(i)


'''
j=0
written_lines = set()
while j < len(lines):
    # 如果当前行符合正则表达式，则将它和后续的行存储到对应的文件中
    if re.match(pattern2, lines[j]):
        print(lines[j])
        match_level3 = re.match(pattern2, lines[j])
        print(match_level3.group())

        pattern = r'[、，。,]'
        if re.search(pattern, lines[j]):
            filename = match_level3.group().strip() + '.txt'
            print('直接用匹配到的正则表达式作为文件名：', filename)
        else:
            filename = lines[j].replace('\n', '') + '.txt'
            print('小节具有小标题，用正则表达式+小标题作为文件名：', filename)

        with open(filename, 'a', encoding='utf-8') as f:
            if lines[j] not in written_lines:
                f.write(lines[j])
                written_lines.add(lines[j])
                j += 1
                print(j)
            while j < len(lines):
                if re.match(pattern1, lines[j]):   #匹配到x.x则打断循环
                    break
                if re.match(pattern2, lines[j]):  #匹配到x.x.x
                    match_level3_2 = re.match(pattern2, lines[j])  #匹配到和已匹配到不同的x.x.x 也跳出循环
                    if match_level3_2 != match_level3:
                        break
                    else:
                        if lines[j] not in written_lines:
                            f.write(lines[j])
                            written_lines.add(lines[j])
                            print(lines[j])
                            j += 1
                            print(j)
                else:
                    print(lines[j])
                    f.write(lines[j])
                    j += 1
                    print(j)

    else:
        j += 1
        print(j)
'''


'''
pattern1 = r'\d{1,2}\.\d{1,2}(?!\.)'    #x.x
#pattern1 = r'第(.*?)章.*'
pattern2 = r'\d{1,2}\.\d{1,2}\.\d{1,2}(?!\.)'    #x.x.x
#pattern2 = r'第(.*?)节.*'
i = 0
while i < len(lines):
    # 如果当前行符合正则表达式，则将它和后续的行存储到对应的文件中
    if re.match(pattern1, lines[i]):
        match_level2 = re.match(pattern1, lines[i])
        filename = match_level2.group().strip() + '.txt'
        #filename = lines[i].replace('\n', '') + '.txt'
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(lines[i])
            i += 1
            while i < len(lines):
                if re.match(pattern2, lines[i]):
                    break
                if re.match(pattern1, lines[i]):
                    match_level2_2 = re.match(pattern1, lines[i])
                    if match_level2_2 != match_level2:
                        break
                    break
                f.write(lines[i])
                i += 1
    else:
        i += 1
'''
