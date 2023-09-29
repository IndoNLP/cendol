<h1 align="center"> <p>IndoNLP Cendol</p></h1>
<h3 align="center">
    <p>An Indonesian Replicable Instruction-Following Model</p>
</h3>

# DeepSpeed Setup
- Copy the `accelerate_configs/default_config.yaml` into `~/.cache/huggingface/accelerate/default_config.yaml`
- Fix the path for ds_config in the `~/.cache/huggingface/accelerate/default_config.yaml` into `<INDO_T0_HOME>/instruction_tuning/ds_config/ds_config_*.json` (see `ds_config/ds_config_*.json`)
- Adjust the `--gradient_accumulation` in the `ds_config/ds_config_*.json`  and the `grad_accum` variable on the training script depending on the model to run

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/DATA_LICENSE)


