import gradio as gr

with gr.Blocks() as demo:
    

    gr.Markdown('''# <center>🌊 滔滔AI 🎶</center>
                ## <center>🌟 - 滔滔AI，为您提供全场景的AI声音服务</center>
                ### <center>🦄 - TalkTalkAI, let lovely AI brighten the future</center>
    ''')
        
    with gr.Tab("🤩 - 重磅首发：最强大的AI歌手界面"):

        gr.Markdown('''
                    ## 🎶 AI歌手：今夜闻君琵琶语，如听仙乐耳暂明 🎸
                    ### 专业版的功能简介：歌声转换 + AI拟声 + 音乐视频一键制作 + 支持动态字幕与音浪特效 🌊
                    ### 合作音乐人(持续更新中)：[一清清清](https://space.bilibili.com/22960772?spm_id_from=333.337.0.0)
                    ## 
                    # 点击这里使用AI歌手：[滔滔AI-音乐](https://kevinwang676-Voice-Cloning-for-Bilibili.hf.space) 🔮
                    ###
                    ### 我们还为您准备了更专业的AI歌手操作界面：[滔滔AI-音乐专业版](https://kevinwang676-test-1.hf.space) （使用[指南](https://www.bilibili.com/video/BV1Zs4y1r7t3/?spm_id_from=333.999.0.0&vd_source=940fe82ece38c8c3078c080ea544aab7)）
                    ### 
                    ### 诚挚邀请所有优秀的音乐人与我们合作(联系方式见网站底部)，我们将竭尽所能的提供AI声音方面的技术支持，并且免费为您制作行业内最高质量的AI歌手！🎙️
                    ### 滔滔AI期待与所有用户和合作伙伴共同谱写AI时代的精彩乐章！💕 欢迎关注我们的B站账号：[滔滔AI-B站](https://space.bilibili.com/501495851?spm_id_from=333.999.0.0)
                    #
        ''')


        gr.HTML('''
        <div class="footer">
                    <p>📧 - 联系我们：talktalkai.kevin@gmail.com
                    </p>
                    
        </div>
        ''') 
        
        gr.HTML('''
        <div class="footer">
                    <p>🌊💕🎶 - 滔滔AI，让有爱的AI滔滔不绝；有意清秋入衡霍，为君无尽写江天
                    </p>
        </div>
        ''')     

    with gr.Tab("🧸 - 发现更多有趣功能"):

        gr.Markdown(
            """ 
            ## 🌊 滔滔AI声音领域的三大板块：1️⃣AI拟声2️⃣AI歌手3️⃣AI变声，为您提供全场景的AI声音服务 🏆
            
            ## 🎙️ [Bark真实拟声](https://kevinwang676-bark-with-voice-cloning.hf.space)：AI拟声，为您妙语连珠（⭐全网首发⭐）
            ## 🎶 [Sovits](https://kevinwang676-voice-cloning-for-bilibili.hf.space)：AI歌手，为您一展歌喉
            
            ## 🤖 [VITS中日英拟声](https://kevinwang676-vits-fast-finetuning-pcr.hf.space)：AI嘴替，为您在线发声
            ## 🌟 [中文声音克隆](https://kevinwang676-personal-tts.hf.space)：AI中文，为您直抒胸臆
            
            ###
            ### 🤗 - 更多精彩，尽在滔滔AI！
            
            #
        """
        )

        gr.HTML('''
        <div class="footer">
                    <p>📧 - 联系我们：talktalkai.kevin@gmail.com
                    </p>
                    
        </div>
        ''')

        gr.HTML('''
        <div class="footer">
                    <p>🌊💕🎶 - 滔滔AI，让有爱的AI滔滔不绝；江水东流急，滔滔无尽声
                    </p>
                    
        </div>
        ''')     


demo.launch(debug=True)
