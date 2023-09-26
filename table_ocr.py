import os
import sys
import json
from paddleocr import PaddleOCR

def main(path:str): 
  image_dir = os.path.join(path, "tables")
  images = os.listdir(image_dir)
  
  out_dir = os.path.join(path, "ocr_result")
  if not os.path.exists(out_dir):
    os.mkdir(out_dir)
  
  ocr = PaddleOCR(use_angle_cls=False, lang='en')

  for image_file in images:
    image_path = os.path.join(image_dir, image_file)
    results = ocr.ocr(image_path, cls=False)
    
    boxes = []
    tokens = []
    
    for result in results:
      bbox, pair = result
      boxes.append(bbox)
      tokens.append(pair[0])
    
    with open(os.path.join(out_dir, image_file.replace(".png", ".json")), 'w') as f:
      json.dump({"tokens": tokens, "bboxes": boxes}, f, indent=2)


if __name__ == "__main__":
  path = sys.argv[1]
  main(path)
