import os
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

def parse_log(log_file, batch_size=1):
    os.system('%s/parse_log.sh %s' % (os.path.dirname(os.path.realpath(__file__)),log_file))
    train_loss = np.genfromtxt('train_loss.csv', delimiter=',')
    test_iter = np.genfromtxt('test_iter.csv', delimiter=',')
    test_loss = np.genfromtxt('test_loss.csv', delimiter=',')
    test_acc = np.genfromtxt('test_acc.csv', delimiter=',')
    return train_loss[:,0]*batch_size,train_loss[:,1],test_iter*batch_size,test_loss,test_acc

def parse_log_google(log_file, batch_size=1):
    os.system('%s/parse_log_google.sh %s' % (os.path.dirname(os.path.realpath(__file__)),log_file))
    train_loss = np.genfromtxt('train_loss.csv', delimiter=',')
    test_iter = np.genfromtxt('test_iter.csv', delimiter=',')
    test_loss1 = np.genfromtxt('test_loss1.csv', delimiter=',')
    test_loss2 = np.genfromtxt('test_loss2.csv', delimiter=',')
    test_loss3 = np.genfromtxt('test_loss3.csv', delimiter=',')
    test_loss = test_loss1
    if test_loss2.size > 0:
        test_loss += test_loss2
    if test_loss3.size > 0:
        test_loss += test_loss3
    test_acc = np.genfromtxt('test_acc.csv', delimiter=',')
    return train_loss[:,0]*batch_size,train_loss[:,1],test_iter*batch_size,test_loss,test_acc

def create_subplots(c = None, figsize = None):
    if c is None:
        c = cycler('linestyle', ['-', '--', ':', '-.']) * cycler('color', ['r', 'g', 'b', 'y'])
    f,axis_loss = plt.subplots()
    if figsize:
        f.set_figwidth(figsize[0])
        f.set_figheight(figsize[1])
    axis_acc = axis_loss.twinx()
    axis_loss.set_prop_cycle(c)
    axis_acc._get_lines.prop_cycler = axis_loss._get_lines.prop_cycler
    return axis_loss, axis_acc

def plot_log(log_file, axis_loss, axis_acc, batch_size=1, loss_legend="", accuracy_legend="", set_label=True, show_train_loss=True, show_test_loss=True, show_test_acc=True):
    train_img_num, train_loss, test_img_num, test_loss, test_acc = parse_log(log_file, batch_size)
    if not accuracy_legend:
        accuracy_legend = loss_legend
    if show_train_loss:
        axis_loss.plot(train_img_num,train_loss,label='train ' + loss_legend + ' loss')
        axis_loss.legend(loc=2)
    if show_test_loss:
        axis_loss.plot(test_img_num,test_loss,label='val ' + loss_legend + ' loss')
        axis_loss.legend(loc=2)
    if show_test_acc:
        axis_acc.plot(test_img_num,test_acc,label='val ' + accuracy_legend + ' accuracy')
        axis_acc.legend(loc=5)
    if set_label:
        axis_loss.set_xlabel('number of images')
        axis_loss.set_ylabel('loss')
        axis_acc.set_ylabel('val accuracy')

def plot_log_google(log_file, axis_loss, axis_acc, batch_size=1, loss_legend="", accuracy_legend="", set_label=True, show_train_loss=True, show_test_loss=True, show_test_acc=True):
    train_img_num, train_loss, test_img_num, test_loss, test_acc = parse_log_google(log_file, batch_size)
    if not accuracy_legend:
        accuracy_legend = loss_legend
    if show_train_loss:
        axis_loss.plot(train_img_num,train_loss,label='train ' + loss_legend + ' loss')
        axis_loss.legend(loc=2)
    if show_test_loss:
        axis_loss.plot(test_img_num,test_loss,label='val ' + loss_legend + ' loss')
        axis_loss.legend(loc=2)
    if show_test_acc:
        axis_acc.plot(test_img_num,test_acc,label='val ' + accuracy_legend + ' accuracy')
        axis_acc.legend(loc=5)
    if set_label:
        axis_loss.set_xlabel('number of images')
        axis_loss.set_ylabel('loss')
        axis_acc.set_ylabel('val accuracy')