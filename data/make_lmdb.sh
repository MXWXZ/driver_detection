echo "Creating train lmdb..."
convert_imageset --shuffle / train.txt ./train_lmdb
echo "Creating val lmdb..."
convert_imageset --shuffle / val.txt ./val_lmdb
echo "Done."
