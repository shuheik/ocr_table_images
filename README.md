# ocr_table_images

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

### 表構造認識の適用
* 表領域を切り出した画像を置いたフォルダ(img\_dir)、画像の拡張子(extension)、htmlファイルを出力するフォルダ(out\_dir)を指定し、以下を実行する。
```
python ocr_tsr.py --img-dir img_dir --extension png --out-dir out_dir
```
* out\_dirに表構造認識結果のhtmlファイルが出力される。
