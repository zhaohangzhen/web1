"""

工作室名字：赵航圳
根据地用户：只有几个人知道的秘密基地、分享后所有人可见
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区
现有模块改进灵感：……
原创模块：……
原创模块一句话功能介绍：……
"""
import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('我的首页',['我的兴趣推存','我的图片处理工具','我的智慧词典','我的留言区'])

def music(page):
    with open('轻.mp3','rb') as f:
        mymp3_1 = f.read()
    with open('罗辑 Logic.flac','rb') as f:
        myflac = f.read()
    with open('暮色回响.mp3','rb') as f:
        mymp3_2 = f.read()
    if page == 1:
        st.audio(mymp3_1, format='audio/mp3',start_time=0)
        st.audio(mymp3_2, format='audio/mp3',start_time=0)
    else:
        st.audio(myflac, format='audio/flac',start_time=0)
    
def page1():
    music(1)
    st.write('我有三个，一个个看吧')
    tab1, tab2, tab3 = st.tabs(['第一个推存', '第二个推存', '第三个推存'])
    
    with tab1:
        st.write('第一个，那肯定是编程猫')
        st.image('ClassIn_20240804211659.jpg')
        for i in range(15):
            st.write(' ')
        st.write('中的编程猫社区啦')
        st.image('ClassIn_20240804212132.jpg')
        for i in range(5):
            st.write(' ')
        go = st.selectbox('想玩玩我做的游戏么', ['小黄跑酷', '星际穿越.预告'])
        if go == '小黄跑酷':
            st.link_button('帮我一键三连', 'https://shequ.codemao.cn/work/182548075')
        elif go == '星际穿越.预告':
            st.link_button('帮我一键三连', 'https://shequ.codemao.cn/work/200515939')
            
    with tab2:
        st.write('第二个，我的世界,我第一个接触的游戏就是它，七年了，现在还玩')
        st.image('ClassIn_20240806191150.jpg')
        
    with tab3:
        st.write('第三个，蛋仔派对')
        st.write('EGGY')
        st.image('ClassIn_20240806210229.jpg')
        st.write('至于我怎么入坑的，暂时保密')
    
def page2():
    music(1)
    st.write(':medal:图片处理小程序:medal:')
    uploaded_file=st.file_uploader('上传图片', type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        tab1, tab2, tab3 , tab4 = st.tabs(['原图', '图像变深', '图像变浅', '图像改色'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 1, 2, 2))
        with tab3:
            st.image(img_change(img, 0, 1, 2, 3))
        with tab4:
            tab5, tab6, tab7 , tab8, tab9 = st.tabs(['改色1', '改色2', '改色3', '改色4', '改色5'])
            with tab5:
                st.image(img_change(img, 0, 2, 1, 4))
            with tab6:
                st.image(img_change(img, 1, 0, 2, 4))
            with tab7:
                st.image(img_change(img, 1, 2, 0, 4))
            with tab8:
                st.image(img_change(img, 2, 0, 1, 4))
            with tab9:
                st.image(img_change(img, 2, 1, 0, 4))
    
def page3():
    music(2)
    st.write(':100:智能词典:100:')
    with open('words_space.txt','r',encoding='utf-8') as f:
        word_list=f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i]=word_list[i].split('#')
    word_dict={}
    for i in word_list:
        word_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        time_list = f.read().split('\n')
        for i in range(len(time_list)):
            time_list[i] = time_list[i].split('#')

        time_dict = {}
        for i in time_list:
            time_dict[int(i[0])] = int(i[1])

    word=st.text_input('请输入你想查询的单词：')
    if word in word_dict:
        st.write(word_dict[word])
        n = word_dict[word][0]
        if n in time_dict:
            time_dict[n] += 1
        else:
            time_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in time_dict.items():
                message += str(k)+'#'+str(v)+'\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', time_dict[n])

        if word == 'python':
            st.code('''#恭喜你，触发了彩蛋，这是一行python代码！
                    print("Hello word!")''')
        elif word == 'snow' or word == 'winter' or word == 'cold':
            st.snow()
        elif word == 'balloon' or word == 'birthday':
            st.balloons()
        elif word == 'title':
            st.title('赵航圳')
        elif word == 'success':
            st.success('恭喜你成功了')
        elif word == 'warn':
            st.warning('警告')
        elif word == 'error':
            st.error('报错')
        elif word == 'information':
            st.info('修改后的图片，可以鼠标右键另存为')
        elif word == 'wait':
            with st.spinner('Waiting。。。'):
                time.sleep(3)
            st.success('恭喜你成功了')
    
def page4():
    music(1)
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🃏'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🌔'):
                st.title(i[1] + ':' + i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img,rc,gc,bc, mod):
    width,height=img.size

    if mod == 2:
        img_array=img.load()
        for x in range(width):
            for y in range(height):
                r = (img_array[x,y][rc] + 255 - 50) % 255
                g = (img_array[x,y][gc] + 255 - 50) % 255
                b = (img_array[x,y][bc] + 255 - 50) % 255
                img_array[x,y]=(r,g,b)
        return img
    elif mod == 3:
        img_array=img.load()
        for x in range(width):
            for y in range(height):
                r=(img_array[x,y][rc] + 50) % 255
                g=(img_array[x,y][gc] + 50) % 255
                b=(img_array[x,y][bc] + 50) % 255
                img_array[x,y]=(r,g,b)
        return img
    elif mod == 4:
        img_array=img.load()
        for x in range(width):
            for y in range(height):
                r=img_array[x,y][rc]
                g=img_array[x,y][gc]
                b=img_array[x,y][bc]
                img_array[x,y]=(r,g,b)
        return img
    
if page == '我的兴趣推存':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
#🌟