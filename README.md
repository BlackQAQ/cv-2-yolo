## 使用方法

1、将数据集放在data文件夹中，路径为：

训练集: data/images/train

验证集: data/images/val

测试集: data/images/test

标注路径为:

训练集: data/labels/train

验证集: data/labels/val

测试集: data/labels/test



2、Train

```
python train.py --img img_size(default: 640) --batch batch_size --epochs epoch_num --data dataset.yaml --weights pretrained_weights
```



3、Inference

```
python detect.py --source data/images/test --weights trained_weights --conf confidence [--save-txt](save *.txt results)
```

