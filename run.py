from maia2 import model, dataset, inference
maia2_model = model.from_pretrained(type="rapid", device="gpu")
from maia2 import train, utils
cfg = utils.parse_args(cfg_file_path="./maia2_models/config.yaml")
train.run(cfg)