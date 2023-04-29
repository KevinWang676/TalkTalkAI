import gradio as gr
import os

stable_diffusion = gr.Blocks.load(name="spaces/runwayml/stable-diffusion-v1-5")

def get_images(prompt):
    gallery_dir = stable_diffusion(prompt, fn_index=2)
    sd_output = [os.path.join(gallery_dir, image) for image in os.listdir(gallery_dir)]
    return sd_output


with gr.Blocks() as demo:
    
    with gr.Tab("AI作画-极速版"):

        gr.Markdown('''# <center>🥳 滔滔AI 🎶</center>
                ### <center>🥰 - 滔滔AI，让有爱的AI滔滔不绝</center>
                ### <center>🦄 - TalkTalkAI, let lovely AI brighten the future</center>
    
        ''')

        with gr.Row():
            inp1 = gr.Textbox(label="请提供关键词(英文)", value="A large cabin on top of a sunny mountain in the style of Dreamworks, artstation", lines=3)
            btn = gr.Button("开始绘制您的专属作品吧")
        with gr.Row():
            out1 = gr.Gallery(
                label="为您绘制的专属作品", show_label=True, elem_id="gallery"
            )
        
        btn.click(get_images, [inp1], [out1])


        gr.HTML('''
        <div class="footer">
                    <p>📧 - 联系我们：talktalkai.kevin@gmail.com
                    </p>
                    
        </div>
        ''') 
        
        gr.HTML('''
        <div class="footer">
                    <p>🖼️💕🎡 - 滔滔AI，为爱滔滔；有意清秋入衡霍，为君无尽写江天
                    </p>
        </div>
        ''')     

    with gr.Tab("发现更多有趣功能"):

        gr.Markdown('''# <center>🥳 滔滔AI 🎶</center>
                ### <center>🥰 - 滔滔AI，让有爱的AI滔滔不绝</center>
                ### <center>🦄 - TalkTalkAI, let lovely AI brighten the future</center>
    
        ''')


        gr.Markdown(
            """ 
            ## 😄 - 更多精彩尽在滔滔AI
            
            ## 🖌️ [Stable Diffusion全家桶](https://kevinwang676-stable-diffusion-for-all.hf.space)：AI画家，为您执笔作画
            ## 🎶 [Sovits](https://kevinwang676-voice-cloning-for-bilibili.hf.space)：AI歌手，为您一展歌喉
            
            ## 🤖 [声音克隆](https://kevinwang676-voice-cloning-demo.hf.space)：AI拟声，为您妙语连珠
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
                    <p>🖼️💕🎡 - 滔滔AI，为爱滔滔；有意清秋入衡霍，为君无尽写江天
                    </p>
                    
        </div>
        ''')     

if __name__ == '__main__':
    demo.queue(concurrency_count=5, max_size=20).launch(debug=True)
