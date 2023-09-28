<h1 align="center"> <p>IndoNLP Cendol</p></h1>
<h3 align="center">
    <p>An Indonesian Replicable Instruction-Following Model</p>
</h3>

<p align="center"> <a href="https://haonan-li.github.io/" target="_blank">Haonan Li</a>*, <a href="http://www.fajrikoto.com" target="_blank">Fajri Koto</a>*, <a href="https://twitter.com/WuMinghao_nlp" target="_blank">Minghao Wu</a>, <a href="https://afaji.github.io/" target="_blank">Alham Fikri Aji</a>, <a href="https://people.eng.unimelb.edu.au/tbaldwin/" target="_blank">Timothy Baldwin</a> (*equal contribution) </p>


# DeepSpeed Setup
- Copy the `accelerate_configs/default_config.yaml` into `~/.cache/huggingface/accelerate/default_config.yaml`
- Fix the path for ds_config in the `~/.cache/huggingface/accelerate/default_config.yaml` into `<INDO_T0_HOME>/instruction_tuning/ds_config/ds_config.json`
- Copy the corresponding `ds_config/ds_config_*.json` into the `ds_config/ds_config.json` depending on the model that you run
- Adjust the `--gradient_accumulation` in the `ds_config/ds_config.json`  and the `grad_accum` variable on the training script depending on the model to run

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/DATA_LICENSE)


