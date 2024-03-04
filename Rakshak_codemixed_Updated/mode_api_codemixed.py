from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route('/')
def start_con():
    return "start"



###============================================================================================================###

import os
import torch
import pandas as pd
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig, PeftModel
from trl import SFTTrainer


import json
from datasets import Dataset

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_NAME = "meta-llama/Llama-2-7b-hf"
access_token = "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" ### huggingface access token

# Fine-tuned model
new_model = "/DATA/priyanshu_2021cs26/armita/codemixed/llama-2-7b-chatbot-2300-codemixed"
#new_model="llama-2-7b-chatbot-5000"

#new_model="/DATA/priyanshu_2021cs26/armita/llama-2-7b-chatbot-5000-5-context"

######################### Model setup ##########################
# def create_model_and_tokenizer():
#     bnb_4bit_compute_dtype = "float16"
#     use_4bit = True
#     compute_dtype = getattr(torch, bnb_4bit_compute_dtype)
#     # Check GPU compatibility with bfloat16
#     if compute_dtype == torch.float16 and use_4bit:
#         major, _ = torch.cuda.get_device_capability()
#         if major >= 8:
#             print("=" * 80)
#             print("Your GPU supports bfloat16: accelerate training with bf16=True")
#             print("=" * 80)

#     bnb_config = BitsAndBytesConfig(
#         load_in_4bit=True,                      # Activate 4-bit precision base model loading
#         bnb_4bit_quant_type="nf4",              # Quantization type (fp4 or nf4)
#         bnb_4bit_compute_dtype=compute_dtype,   # Compute dtype for 4-bit base models
#         bnb_4bit_use_double_quant=False,        # Activate nested quantization for 4-bit base models (double quantization)
#     )

#     model = AutoModelForCausalLM.from_pretrained(
#         MODEL_NAME,
#         quantization_config=bnb_config,
#         trust_remote_code=True,
#         device_map="auto",
#         use_auth_token=access_token,
#     )

#     tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=access_token, trust_remote_code=True)
#     tokenizer.pad_token = tokenizer.eos_token
#     #tokenizer.add_special_tokens(special_tokens_dict)
#     tokenizer.padding_side = "right" # Fix weird overflow issue with fp16 training

#     return model, tokenizer

# model, tokenizer = create_model_and_tokenizer()
# model.config.use_cache = True
# model.config.pretraining_tp = 1
# #print(model.config.quantization_config.to_dict())
# model = PeftModel.from_pretrained(model, new_model)
# pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=100)

# def generate(test_case):
#     result = pipe(f"{test_case}")
#     print(result[0]['generated_text'])
#     print("==============",result[0]['generated_text'].split("[eor]")[0])


@app.route('/gen',methods=['POST'])
def genera():
    print("in")
    # print(model.config.quantization_config.to_dict())
    # x=input()
    # result = pipe(f"{x}")
    # #print(result[0]['generated_text'])
    # #print("==============",result[0]['generated_text'].split("[eor]")[0])
    # return (result[0]['generated_text'].split("[eor]")[0])

        
    # print("in")
    user_text = request.json.get('text')
    # lang=request.get_json()
    # print(lang)
    # d1=lang['tracker']
    # d2=d1['latest_message']
    # d3=d2['text']
    # #lang=request.json.get("text")
    # print("lang--",d3)
    #sprint("text----",lang['text'])
    #text3=lang['text'][0]
    text3=user_text+"[eoc][sor][bot]"
    #text4=text3['latest_message'][0]
    #text5=text4['intent']

    #text1=text4
    print("user_text=====",text3)
    result = pipe(f"{text3}")
    #res=generate(text1)
    #res=generate(text3)
    first_response=(result[0]['generated_text'].split("[eoc][sor][bot]")[1])
    final_response=first_response.split("[eor]")[0]
    
    print("inside"+final_response)
    result1={

        "text": final_response
     }

    return jsonify(result1)


if __name__=="__main__":
    #app.run(debug=True)
    bnb_4bit_compute_dtype = "float16"
    use_4bit = True
    compute_dtype = getattr(torch, bnb_4bit_compute_dtype)
    # Check GPU compatibility with bfloat16
    if compute_dtype == torch.float16 and use_4bit:
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            print("=" * 80)
            print("Your GPU supports bfloat16: accelerate training with bf16=True")
            print("=" * 80)

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,                      # Activate 4-bit precision base model loading
        bnb_4bit_quant_type="nf4",              # Quantization type (fp4 or nf4)
        bnb_4bit_compute_dtype=compute_dtype,   # Compute dtype for 4-bit base models
        bnb_4bit_use_double_quant=False,        # Activate nested quantization for 4-bit base models (double quantization)
    )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config,
        trust_remote_code=True,
        device_map="auto",
        use_auth_token=access_token,
    )

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=access_token, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    #tokenizer.add_special_tokens(special_tokens_dict)
    tokenizer.padding_side = "right" # Fix weird overflow issue with fp16 training

    

#model, tokenizer = create_model_and_tokenizer()
    model.config.use_cache = True
    model.config.pretraining_tp = 1
#print(model.config.quantization_config.to_dict())
    model = PeftModel.from_pretrained(model, new_model)
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200)
    app.run(host='10.12.10.70', port=5020, debug=True)


