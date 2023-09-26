# ocr_table_images
表のpng画像に対するOCR結果をjsonファイルとして書き出します。

### Setup
* install PaddleOCR

### OCRの適用
* `/data/path/tables`以下に表領域を切り出したpngファイルを置き、以下を実行する。
```
python table_ocr.py /data/path
```
* `/data/path/ocr_result`にOCR結果のjsonファイルが出力される。
