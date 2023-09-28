import sys
import json
from pathlib import Path
from paddleocr import PaddleOCR


def main(path: str):
  image_dir = Path(path)
  images = image_dir.glob("*.png")
  ocr = PaddleOCR(use_angle_cls=False, lang='en')
  for image in images:
    image_path = str(image)
    results = ocr.ocr(image_path, cls=False)
    boxes = []
    tokens = []
    for result in results[0]:
      bbox, pair = result
      boxes.append(bbox)
      tokens.append(pair[0])
    with open(image_path.replace(".png", ".json"), 'w') as f:
      json.dump({"tokens": tokens, "bboxes": boxes}, f, indent=2)


if __name__ == "__main__":
  path = sys.argv[1]
  main(path)
