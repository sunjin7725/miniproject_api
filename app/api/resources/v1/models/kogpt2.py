import torch

from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel
from config import MODEL_DIR

tokenizer = PreTrainedTokenizerFast.from_pretrained(MODEL_DIR + '/kogpt2-base-v2',
                                                    bos_token='</s>', eos_token='</s>', unk_token='<unk>',
                                                    pad_token='<pad>', mask_token='<mask>')
model = GPT2LMHeadModel.from_pretrained(MODEL_DIR + '/kogpt2-base-v2')