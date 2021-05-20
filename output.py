#!/usr/bin/env python 
# -*- coding:utf-8 -*-


from PIL import Image

import json
import os


# 首先要先获取所有的 /test下的图片名 对应的长宽（存成一个字典）
# dict = {'1.jpg': {'height': 123, 'width': 123}}

# 58 0.4675 0.665 0.1575 0.0566667
# 35 0.130625 0.863333 0.25375 0.27
# 70 0.806875 0.603333 0.15125 0.18
# 22 0.349375 0.644167 0.03375 0.0716667
# 242 0.885625 0.546667 0.12625 0.17
# 35 0.314375 0.81 0.53875 0.38
# 242 0.45625 0.5825 0.2025 0.221667

dic = {}

classes = ['lid', 'handle', 'oven', 'door', 'faucet', 'picture', 'stove', 'cabinet', 'bowl', 'sink', 'counter', 'kitchen', 'cabinets', 'wall', 'handles', 'rack', 'shelf', 'towel', 'dish', 'floor', 'tiles', 'cup', 'bottle', 'spoon', 'knob', 'pot', 'doors', 'light', 'ceiling', 'window', 'drawer', 'fruit', 'chairs', 'lights', 'chair', 'table', 'microwave', 'carpet', 'wheel', 'stripes', 'basket', 'bathroom', 'container', 'mirror', 'toilet', 'curtain', 'seat', 'flowers', 'sauce', 'pan', 'flower', 'leaves', 'food', 'computer', 'desk', 'monitor', 'box', 'leg', 'keyboard', 'wires', 'phone', 'frame', 'mug', 'television', 'suitcase', 'tv', 'stand', 'paper', 'remote', 'sign', 'shirt', 'bed', 'blanket', 'room', 'outlet', 'white', 'side', 'plate', 'tire', 'tile', 'ground', 'man', 'lines', 'sky', 'tree', 'roof', 'building', 'helmet', 'pants', 'foot', 'concrete', 'house', 'street', 'hair', 'bike', 'vehicle', 'person', 'motorcycle', 'headlight', 'dog', 'pillows', 'books', 'couch', 'corner', 'sofa', 'speaker', 'legs', 'head', 'paw', 'arm', 'cushion', 'jacket', 'coat', 'ski pole', 'a', 'ski', 'bottom', 'ring', 'letter', 'snow', 'tag', 'writing', 'skis', 'poles', 'sticker', 'pole', 'tray', 'bench', 'book', 'pillow', 'refrigerator', 'cheese', 'bar', 'duck', 'water', 'beak', 'eyes', 'rug', 'plant', 'bag', 'cord', 'cloth', 'line', 'this', 'boat', 'bicycle', 'sand', 'the', 'red', 'black', 'beach', 'rocks', 'rock', 'glasses', 'finger', 'woman', 'shoe', 'top', 'sunglasses', 'belt', 'umbrella', 'dress', 'shoes', 'skirt', 'purse', 'trim', 'tip', 'lady', 'part', 'shadow', 'shade', 'hand', 'knife', 'blinds', 'board', 'edge', 'mountain', 'snowboard', 'stick', 'weeds', 'background', 'hill', 'bear', 'crack', 'hole', 'teddy bear', 'street light', 'truck', 'cloud', 'plants', 'plane', 'air', 'road', 'branches', 'fence', 'distance', 'clouds', 'tail', 'logo', 'dirt', 'buildings', 'tower', 'car', 'wing', 'statue', 'grass', 'path', 'collar', 'body', 'reflection', 'glass', 'clock', 'holder', 'wood', 'back', 'jeans', 'sweater', 'strap', 'buttons', 'signs', 'hood', 'cover', 'pipe', 'windows', 'branch', 'area', 'brick', 'steps', 'numbers', 'post', 'pocket', 'backpack', 'luggage', 'metal', 'bolt', 'cellphone', 'painting', 'eye', 'sock', 'bat', 'object', 'lamp', 'laptop', 'button', 'screen', 'fur', 'jar', 'vase', 'words', 'trash can', 'vegetables', 'bridge', 'candle', 'wire', 'rope', 'cart', 'train car', 'train', 'chain', 'paint', 'guy', 'watch', 'wrist', 'men', 't-shirt', 'boy', 'shorts', 'ear', 'people', 'knee', 'bus', 'blue', 'stripe', 'onion', 'bucket', 'hands', 'curtains', 'cap', 'sidewalk', 'flag', 'pavement', 'license plate', 'ball', 'racket', 'rail', 'stem', 'leaf', 'headlights', 'photo', 'number', 'letters', 'curb', 'cake', 'hat', 'front', 'patch', 'elephant', 'trunk', 'feet', 'cat', 'whiskers', 'face', 'nose', 'windshield', 'wheels', 'banner', 'city', 'neck', 'tie', 'clothes', 'ripples', 'bricks', 'sun', 'skier', 'trees', 'animal', 'surface', 'birds', 'ocean', 'mouth', 'gate', 'bracelet', 'player', 'court', 'spectator', 'tennis racket', 'circle', 'chimney', 'structure', 'shore', 'river', 'stone', 'girl', 'horse', 'sneakers', 'jet', 'runway', 'field', 'airplane', 'skateboard', 'sneaker', 'surfboard', 'controller', 'bird', 'engine', 'cone', 'stairs', 'ramp', 'skateboarder', 'zebra', 'mane', 'hoof', 'poster', 'sleeve', 'bushes', 'kite', 'child', 'park', 'cow', 'cows', 'socks', 'horn', 'name', 'wave', 'waves', 'van', 'tablecloth', 'giraffe', 'design', 'vest', 'lettuce', 'fork', 'napkin', 'meat', 'sandwich', 'bun', 'wine', 'cell phone', 'banana', 'tomato', 'bananas', 'pizza', 'tent', 'walkway', 'word', 'can', 'carrot', 'spots', 'lettering', 'orange', 'slice', 'bread', 'baby', 'suit', 'broccoli', 'kid', 'beard', 'pepper', 'crust', 'label', 'net', 'scarf', 'pen', 'shoulder', 'pattern', 'vegetable', 'column', 'base', 'platform', 'hot dog', 'spot', 'batter', 'glove', 'catcher', 'umpire', 'jersey', 'baseball', 'uniform', 'gloves', 'band', 'camera', 'tennis court', 'boots', 'string', 'railing', 'ears', 'tennis ball', 'log', 'boot', 'track', 'shadows', 'frisbee', 'arms', 'panel', 'graffiti', 'elephants', 'tracks', 'horses', 'cars', 'apple', 'bush', 'pillar', 'mouse', 'goggles', 'key', 'tree trunk', 'doorway', 'star', 'street sign', 'traffic light', 'boats', 'mountains', 'stop sign', 'balcony', 'awning', 'fire hydrant', 'hydrant', 'arrow', 'train tracks', 'surfer', 'giraffes', 'palm tree', 'gravel', 'wetsuit', 'horns', 'zebras', 'sheep', 'necklace', 'tusk', 'square', 'donut']


def getHeightAndWidth():
    for root, dira, files in os.walk('./val/val/'):
        for f in files:
            img = Image.open('./val/val/' + f)
            dic[f] = {'height': img.size[1], 'width': img.size[0]}


def generate():
    new_dic = {}
    object_id = 0
    for imgs in dic:
        pic_name = imgs
        txt_name = './archive/' + pic_name[:-4] + '.txt'
        height = dic[pic_name]['height']
        width = dic[pic_name]['width']
        new_dic[pic_name] = {'height': height, 'width': width, 'depth': 3, 'objects': {}}
        if os.path.exists(txt_name):
            fo = open(txt_name, encoding='utf-8')
            lines = fo.readlines()
            for line in lines:
                set = line[:-1].split(" ")
                class_name = classes[int(set[0])]
                xmin = int((float(set[1]) - float(set[3]) / 2) * width)
                ymin = int((float(set[2]) - float(set[4]) / 2) * height)
                xmax = int((float(set[1]) + float(set[3]) / 2) * width)
                ymax = int((float(set[2]) + float(set[4]) / 2) * height)
                new_dic[pic_name]['objects'][str(object_id)] = {'category': class_name, 'bbox': [xmin, ymin, xmax, ymax]}
                object_id = object_id + 1
    print(new_dic.__len__())
    target = open('./my_val.json', "w", encoding='utf-8')
    json.dump(new_dic, target)


if __name__ == '__main__':
    getHeightAndWidth()
    generate()