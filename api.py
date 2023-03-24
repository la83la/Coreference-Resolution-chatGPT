from dotenv import load_dotenv
import os
import requests
import time

# config
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
N = os.getenv('N')
if N is not None:
    N = int(N)

# preprocess
with open('input.txt', 'r', encoding="utf-8") as f:
    text_file = f.read()
text_file = text_file.split('\n')
output = []

# main program
for line in text_file: 

    if N is not None:
        if len(line) > N:
            continue
    start_time = time.time()
    messages = [
        # teach chatgpt the right answer
        {"role": "system", "content": "請你辨識輸入的句子中的名詞及代名詞，並將代名詞轉換為對應的名詞後，輸出新的句子。"},
        {"role": "user", "content": "小明買了一碗飯，他接著又買了一碗湯。"},
        {"role": "assistant", "content": "小明買了一碗飯，小明接著又買了一碗湯。"},
        {"role": "user", "content": "今天媽媽煮了咖啡，她煮的咖啡是最好喝的！"},
        {"role": "assistant", "content": "今天媽媽煮了咖啡，媽媽煮的咖啡是最好喝的！"},
        {"role": "user", "content": "小美覺得今天天氣真好，猜猜她今天要去哪裡玩？"},
        {"role": "assistant", "content": "小美覺得今天天氣真好，猜猜小美今天要去哪裡玩？"},
        {"role": "user", "content": line}
    ]

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        },
        json = {
            'model': 'gpt-3.5-turbo', 
            'messages' : messages
        })

    #使用json解析
    json = response.json()
    try:         
        output.append(json['choices'][0]['message']['content'])
        print('Line completed. Time spent: {:.2f} s'.format(time.time() - start_time))
    except Exception as e:
        print(f'Failed with {e.__class__}, response: {json}')
        break
         

with open('output.txt', 'w', encoding='utf-8') as f:
    for line in output:
	    f.write(line + "\n")