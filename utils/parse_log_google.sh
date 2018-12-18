#!/bin/bash


$( dirname "$0" )/dump_train_loss.sh $1 > train_loss.csv
$( dirname "$0" )/dump_test_iter.sh $1 > test_iter.csv
$( dirname "$0" )/dump_test_loss.sh $1 loss1 > test_loss1.csv
$( dirname "$0" )/dump_test_loss.sh $1 loss2 > test_loss2.csv
$( dirname "$0" )/dump_test_loss.sh $1 loss3 > test_loss3.csv
$( dirname "$0" )/dump_test_acc.sh $1 > test_acc.csv
