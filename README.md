# ocr_table_images
表のpng画像に対するOCR結果をjsonファイルとして書き出します。

### Setup
* Python 3.7+
* install PaddlePaddle
  * GPUの有無やCUDAのバージョンによって変更が必要になるので https://www.paddlepaddle.org.cn/en を参照してください。
```
python -m pip install paddlepaddle-gpu -i https://pypi.tuna.tsinghua.edu.cn/simple
```
* install PaddleOCR
```
pip install paddleocr
```

### OCRの適用
* `/data/path/tables`以下に表領域を切り出したpngファイルを置き、以下を実行する。
```
python table_ocr.py /data/path
```
* `/data/path/tables`以下にOCR結果のjsonファイルが出力される。
