from argparse import ArgumentParser
from pathlib import Path
import cv2
from paddleocr import PPStructure


def main(img_dir:str, extension:str, out_dir:str):
  if not Path(out_dir).exists():
    Path(out_dir).mkdir()
  
  engine = PPStructure(lang='en')
  engine.layout_predictor = None

  for img_path in Path(img_dir).glob(f"*.{extension}"):
    img = cv2.imread(str(img_path))
    res, _ = engine.table_system(img, return_ocr_result_in_table=True)
    with open(Path(out_dir).joinpath(img_path.name.replace(f".{extension}", ".html")), 'w') as f:
      f.write(res["html"])

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument('--img-dir')
  parser.add_argument('--extension', type=str, default="png")
  parser.add_argument('--out-dir')
  args=parser.parse_args()
  main(args.img_dir, args.extension, args.out_dir)
