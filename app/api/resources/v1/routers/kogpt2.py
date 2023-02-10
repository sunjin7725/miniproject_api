from fastapi import APIRouter

from common.utils import success_response
from api.resources.v1.models.kogpt2 import tokenizer, model
router = APIRouter(
    prefix='/gpt',
    tags=['gpt']
)


@router.post("/")
async def ocr_docs(text: str, max_length: int=128):
    input_tensor = tokenizer.tokenize(text)
    gen_tensor = model.generator(input_tensor,
                                 max_length=max_length,
                                 repetition_penalty=2.0,
                                 pad_token_id=tokenizer.pad_token_id,
                                 eos_token_id=tokenizer.eos_token_id,
                                 bos_token_id=tokenizer.bos_token_id,
                                 use_cache=True)
    return success_response(tokenizer.decode(gen_tensor[0]))

