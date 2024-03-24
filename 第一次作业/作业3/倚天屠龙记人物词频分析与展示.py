"""
Date: 2024.3.24
Author: 梁玮诚

"""

import jieba
import matplotlib
import matplotlib.pyplot as plt
import os

if os.name == "nt": # Windows系统
    plt.rcParams['font.sans-serif'] = ['FangSong']  # 设置字体
else: # MacOS系统
    plt.rcParams["font.family"] = 'Arial Unicode MS'  
plt.rcParams['axes.unicode_minus'] = False  # 支持负号的正常显示


txt_filename = './data/倚天屠龙记.txt'
result_filename = './output/倚天屠龙记-人物词频.csv'

ignore_list = ['说道','甚么','自己','一个','武功','咱们','教主',
               '心中','一声','只见','少林','弟子','明教','便是',
               '不是','如此','不知','之中','出来','如何','师父',
               '突然','他们','只是','今日','我们','不能','心想',
               '知道','二人','两人','不敢','虽然','众人','这时',
               '可是','姑娘','原来','当下','身子','之下','你们',
               '脸上','倘若','手中','左手']

# 从文件读取文本
txt_file = open(txt_filename, 'r', encoding='ansi')
content = txt_file.read()
txt_file.close()

#添词
jieba.add_word('张教主')
jieba.add_word('杨逍')
jieba.add_word('光明左使')
jieba.add_word('芷若')

# 分词
word_list = jieba.lcut(content)

# 用字典统计每个词的出现次数
word_dict = {}
for w in word_list:
    # 跳过单字
    if len(w) == 1:
        continue
    
    # 跳过不想统计的词
    if w in ignore_list:
        continue
    
    # 对指代同一人物的名词进行合并
    if w == '无忌' or w == '张教主' or w == '教主':
        w = '张无忌'
    elif w == '义父' or w == '金毛狮王':
        w = '谢逊'
    elif w == '太师父':
        w = '张三丰'
    elif w == '韩夫人':
        w = '金花婆婆'
    elif w == '师太':
        w = '灭绝师太'
    elif w == '圆真':
        w = '成昆'
    elif w == '蛛儿' or w == '阿离':
        w = '殷离'
    elif w == '芷若' or w == '周姑娘':
        w = '周芷若'
    elif w == '赵姑娘' or w == '郡主':
        w = '赵敏'
    else:
        pass # pass表示“什么都不做”，常用于为尚未完成的代码占位置
    
    # 已在字典中的词，将出现次数增加1；否则，添加进字典，次数记为1
    if w in word_dict.keys():
        word_dict[w] = word_dict[w] + 1
    else:
        word_dict[w] = 1

# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x:x[1], reverse=True)

total_num = len(items_list)
print('经统计，共有' + str(total_num) + '个不同的词')

# 根据用户需求，打印排名前列的词，同时把统计结果存入文件
num = input('您想查看前多少个人物？（仅保证统计前十个人物）[10]:')
if not num.isdigit() or num == '': # 如果输入的不全是数字，或者直接按了回车
    num = 10  # 默认查看前10名
else:
    num = int(num)  # 如果输入了正常的数字，则按用户需求设置

result_file = open(result_filename, 'w')   # 新建结果文件

result_file.write('人物,出现次数\n')  # 写入标题行

for i in range(num):
    word, cnt = items_list[i]
    message = str(i+1) + '. ' + word + '  ' + str(cnt)
    print(message)
    result_file.write(word + ',' + str(cnt) + '\n')
    
result_file.close()  # 关闭文件

print('已写入文件：' + result_filename)


src_filename = './output/倚天屠龙记-人物词频.csv'

src_file = open(src_filename, 'r', encoding='ansi')
line_list = src_file.readlines()
src_file.close()

word_list = []
cnt_list = []

#print(line_list)
del line_list[0] #删除csv文件中的标题行

for line in line_list:
    line = line.replace('\n', '')
    word_cnt = line.split(',')
    word_list.append(word_cnt[0])
    cnt_list.append(int(word_cnt[1]))

n = num

plt.title('倚天屠龙记人物词频统计') # 图表标题
plt.xlabel('人物') # x轴标签
plt.ylabel('出现次数') # y轴标签
plt.bar(range(n), cnt_list[0:n])
plt.xticks(range(n), word_list[0:n])
plt.yticks(range(0,max(cnt_list)+100,500))
plt.savefig("./output/倚天屠龙记-人物词频.png")
plt.show()