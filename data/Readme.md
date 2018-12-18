# Training data
## Download
data: https://www.kaggle.com/c/state-farm-distracted-driver-detection/data
pretrained caffemodel: 
- http://dl.caffe.berkeleyvision.org/bvlc_alexnet.caffemodel
- http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel
- https://onedrive.live.com/?authkey=%21AAFW2-FVoxeVRck&id=4006CBB8476FF777%2117887&cid=4006CBB8476FF777

## usage
1. extract `imgs` folder here.
2. make sure `imgs` folder is in this path and you can see `test` and `train` folder in it.
3. run `make_val.sh` to make val data (20%).
4. run `make_txt.sh` to make txt path file
5. run `make_lmdb.sh` to make lmdb file
6. run `make_mean.sh` to make meanfile
