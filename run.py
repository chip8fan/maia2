from maia2 import train, utils
cfg = utils.parse_args(cfg_file_path="/kaggle/working/maia2/maia2_models/config.yaml")
train.run(cfg)