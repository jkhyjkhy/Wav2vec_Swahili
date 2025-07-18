# LR_ASR
##### Contributors: 
@jkhyjkhy  
@annettehjc  
@chyulle  
@Khattab273  


---
library_name: transformers
license: apache-2.0
base_model: facebook/wav2vec2-large-xlsr-53
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-large-xlsr-sw-ASR
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-sw-ASR

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the Swahili dataset from common voice.
It achieves the following results on the evaluation set:
- Loss: 0.1446
- Wer: 0.2453

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|
| No log        | 0.0740 | 1000  | 0.8588          | 0.7661 |
| No log        | 0.1480 | 2000  | 0.3139          | 0.4159 |
| 1.9537        | 0.2220 | 3000  | 0.2514          | 0.3524 |
| 1.9537        | 0.2960 | 4000  | 0.2217          | 0.3292 |
| 1.9537        | 0.3700 | 5000  | 0.1986          | 0.3029 |
| 0.3639        | 0.4440 | 6000  | 0.1847          | 0.2903 |
| 0.3639        | 0.5181 | 7000  | 0.1754          | 0.2747 |
| 0.3639        | 0.5921 | 8000  | 0.1657          | 0.2689 |
| 0.3039        | 0.6661 | 9000  | 0.1587          | 0.2598 |
| 0.3039        | 0.7401 | 10000 | 0.1565          | 0.2560 |
| 0.3039        | 0.8141 | 11000 | 0.1529          | 0.2518 |
| 0.2688        | 0.8881 | 12000 | 0.1478          | 0.2476 |
| 0.2688        | 0.9621 | 13000 | 0.1446          | 0.2453 |


### Framework versions

- Transformers 4.53.0
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.2
