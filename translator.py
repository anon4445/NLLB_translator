import ctranslate2
import transformers 
def translate(text,tgt_lang): 
    translator = ctranslate2.Translator("nllb-200-distilled-600M")
    tokenizer = transformers.AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
    source = tokenizer.convert_ids_to_tokens(tokenizer.encode(text))
    target_prefix = [tgt_lang]
    results = translator.translate_batch([source], target_prefix=[target_prefix])
    target = results[0].hypotheses[0][1:]
    final_result = tokenizer.decode(tokenizer.convert_tokens_to_ids(target))
    return final_result

#tgt_lang = "eng_Latn"
#translated_text = translate("জাপান একটি সুন্দর দেশ। আমি জাপান যেতে আগ্রহী।", tgt_lang)
#print(translated_text)