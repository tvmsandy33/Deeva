import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer

model_checkpoint = "distilbert-base-uncased"
model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

def unmask_text(text):
    string = []
    inputs = tokenizer(text, max_length=512, return_tensors="pt", stride=1, truncation=True, return_overflowing_tokens=True, padding='max_length')
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    for input_id, attn_mask in zip(input_ids, attention_mask):
        len_variable = len(input_id[input_id != 0])
        with torch.no_grad():
            outputs = model(input_ids=input_id.unsqueeze(0), attention_mask=attn_mask.unsqueeze(0))
        predictions = outputs[0]
        sorted_preds, sorted_idx = predictions[0].sort(dim=-1, descending=True)
        predicted_index = [sorted_idx[i, 0].item() for i in range(len_variable - 2)]
        predicted_token = [([predicted_index[x]])[0] for x in range(1, len_variable - 2)]
        string.append(tokenizer.decode(predicted_token))

    return ' '.join(string)
