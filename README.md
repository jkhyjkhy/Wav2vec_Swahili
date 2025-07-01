# LR_ASR
##### Contributors: 
@jkhyjkhy  
@annettehjc  
@chyulle  
@Khattab273  
@Sanwantori-bai
##### Transcription Function(Added on 12.06.2025)

Here, We provide a simple `transcribe()` helper that takes a path to a WAV file, runs it through our Wav2Vec2 ASR pipeline, and returns a decoded string.

```python
def transcribe(path):                                      
    speech, _ = librosa.load(path, sr=16000)                # <---------- Resampling waveforms to 16 kHz for the model
    inputs = processor(                                     
        speech,
        return_tensors="pt",                                # <---------- Returns PyTorch tensors
        padding=True                                        # <---------- Pads to uniform sequence length
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}   # <---------- Moves all tensors to the model’s device
    with torch.no_grad():                                   # <---------- Disables gradient tracking for inference
        logits = model(**inputs).logits                     # <---------- Runs the model to get raw scores (logits)
    pred_ids = torch.argmax(logits, dim=-1)                 # <---------- Chooses highest-score token(greedy decoding) ID at each time step
    return processor.batch_decode(pred_ids)[0]              # <---------- Converts token IDs into the final text string
