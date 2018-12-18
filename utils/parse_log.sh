#!/bin/bash


$( dirname "$0" )/dump_train_loss.sh $1 > train_loss.csv
$( dirname "$0" )/dump_test_iter.sh $1 > test_iter.csv
$( dirname "$0" )/dump_test_loss.sh $1 loss > test_loss.csv
$( dirname "$0" )/dump_test_acc.sh $1 > test_acc.csv
