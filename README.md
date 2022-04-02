# KEDY

- Resources for our WSDM 2022 paper: "[Diversified Query Generation Guided by Knowledge Graph]"
- Paper link: https://dl.acm.org/doi/abs/10.1145/3488560.3498431

## Dependencies

- CUDA > 11
- Prepare requirements: `pip3 install -r requirements.txt`.

## Training KEDY

### 1 Seq2Seq

- `python make_dataset.py -config config/demo/demo-prep.yml`: convert raw corpus to dealable datasets.
- `python preprocess.py -config config/demo/demo-prep.yml`: opennmt style preprocess.

- `python train.py -config config/demo/demo-train.yml`

- `python translate.py -config config/demo/demo-transl.yml -model exp/demo/models/DEMO_step_0.pt`

### 2 Graph

- Use `my_feature_extractor.py` and `ccig.py` to build graph.
- We can do train and inference with `train.py`.
- For evaluation, Use multi-bleu.perl
