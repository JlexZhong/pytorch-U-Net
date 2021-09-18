import os

root
log_dir = "./logs"
loss_dir_list = []

loss_list = []
val_loss_list = []

for loss_dir in os.listdir(log_dir):
    if os.path.isdir(loss_dir):
        for loss_file in os.listdir(loss_dir):
            if "epoch_loss" in os.path.split(loss_file)[1]: #检验文件名里是否包含某字符串
                loss_list.append(open(loss_file,'r').read().splitlines())
            if "epoch_val_loss" in os.path.split(loss_file)[1]:
                loss_list.append(open(loss_file,'r').read().splitlines())
                
print(loss_list)
print(val_loss_list)