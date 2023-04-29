import gradio as gr
import os

def inference(text,audio):
  os.system('tts --text "'+text+'" --model_name tts_models/multilingual/multi-dataset/your_tts --speaker_wav '+audio+' --language_idx "en"')
  return "tts_output.wav"
  
with gr.Blocks() as demo:
    
    with gr.Tab("声音克隆-极速版"):

        gr.Markdown('''# <center>🥳 滔滔AI 🎶</center>
                ### <center>🥰 - 滔滔AI，让有爱的AI滔滔不绝</center>
                ### <center>🦄 - TalkTalkAI, let lovely AI brighten the future</center>
    
        ''')

        with gr.Row():
            inp1 = gr.Textbox(label="请填写想要进行声音克隆的文本(英文)", placeholder="Hello world", lines=3)
            inp2 = gr.Audio(label="请上传一段您喜欢的语音", type="filepath")
        with gr.Row():
            btn = gr.Button("开始合成您的专属语音吧")
            out1 = gr.Audio(label="为您合成的专属语音", type="filepath")

        btn.click(inference, [inp1, inp2], [out1])


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
            
            ## 🖌️ [Stable Diffusion](https://kevinwang676-stable-diffusion-for-all.hf.space)：AI画家，为您执笔作画
            ## 🎶 [Sovits](https://kevinwang676-voice-cloning-for-bilibili.hf.space)：AI歌手，为您一展歌喉
            
            ## 🤖 [声音克隆-高级版](https://kevinwang676-voice-cloning-demo.hf.space)：AI拟声，为您妙语连珠
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
