from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route('/')
def start_con():
    return "start"



###============================================================================================================###

import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
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

#from sklearn.model_selection import train_test_split
import json
from datasets import Dataset


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


@app.route('/gen',methods=['POST'])
def genera():
    print("in")
   
    # print("in")
    user_text = request.json.get('text')
   
    text3=user_text+"[eoc][sor][bot]"
    
    print("user_text=====",text3)
    result = pipe(f"{text3}")
    
    first_response=(result[0]['generated_text'].split("[eoc][sor][bot]")[1])
    final_response=first_response.split("[eor]")[0]
    
    print("inside"+final_response)
    result1={

        "text": final_response
     }

    return jsonify(result1)


if __name__=="__main__":
    
    new_model = "/DATA/priyanshu_2021cs26/armita/bloomz/OPENHATHI/OpenHathi-7B-Hi-v0.1-Base-Finetune-5000"
    tokenizer = LlamaTokenizer.from_pretrained('sarvamai/OpenHathi-7B-Hi-v0.1-Base')
    model = LlamaForCausalLM.from_pretrained('sarvamai/OpenHathi-7B-Hi-v0.1-Base', torch_dtype=torch.bfloat16)


    model.config.use_cache = True
    model.config.pretraining_tp = 1

    model = PeftModel.from_pretrained(model, new_model)
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=150)
    app.run(host='10.12.10.70', port=5013, debug=True)


