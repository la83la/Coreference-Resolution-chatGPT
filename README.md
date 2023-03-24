# Coreference-Resolution: a solution

### User manual

1. 在 root directory 中新增`.env `檔案，並新增變數 `OPENAI_API_KEY`，值為自己的金鑰。

2. 將要輸入的句子放入 `input.txt`，並注意每個句子以`\n`分隔，以及每個句子需有完整標點符號。

3. 執行`api.py`，輸出的檔案為`output.txt`。

### 參數 N

- 在`.env`中新增名稱為`N`的變數。

- 若輸入的句子字數大於參數 N，則該行自動跳過。

### ChatGPT API 收費方式

- 當前提供的 model gpt-3.5-turbo 收費為 0.002 美元 / 1K tokens [[1](https://openai.com/pricing)]

- 中文字經測約會產生比字元數多一倍的 token，可參考 [[2](https://platform.openai.com/tokenizer)]，目前 prompt 中所使用的 token 數為 323。