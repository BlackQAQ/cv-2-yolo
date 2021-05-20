#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import json

list1 = []

absolute_path="data/custom/images/"

classes = ['lid', 'handle', 'oven', 'door', 'faucet', 'picture', 'stove', 'cabinet', 'bowl', 'sink', 'counter', 'kitchen', 'cabinets', 'wall', 'handles', 'rack', 'shelf', 'towel', 'dish', 'floor', 'tiles', 'cup', 'bottle', 'spoon', 'knob', 'pot', 'doors', 'light', 'ceiling', 'window', 'drawer', 'fruit', 'chairs', 'lights', 'chair', 'table', 'microwave', 'carpet', 'wheel', 'stripes', 'basket', 'bathroom', 'container', 'mirror', 'toilet', 'curtain', 'seat', 'flowers', 'sauce', 'pan', 'flower', 'leaves', 'food', 'computer', 'desk', 'monitor', 'box', 'leg', 'keyboard', 'wires', 'phone', 'frame', 'mug', 'television', 'suitcase', 'tv', 'stand', 'paper', 'remote', 'sign', 'shirt', 'bed', 'blanket', 'room', 'outlet', 'white', 'side', 'plate', 'tire', 'tile', 'ground', 'man', 'lines', 'sky', 'tree', 'roof', 'building', 'helmet', 'pants', 'foot', 'concrete', 'house', 'street', 'hair', 'bike', 'vehicle', 'person', 'motorcycle', 'headlight', 'dog', 'pillows', 'books', 'couch', 'corner', 'sofa', 'speaker', 'legs', 'head', 'paw', 'arm', 'cushion', 'jacket', 'coat', 'ski pole', 'a', 'ski', 'bottom', 'ring', 'letter', 'snow', 'tag', 'writing', 'skis', 'poles', 'sticker', 'pole', 'tray', 'bench', 'book', 'pillow', 'refrigerator', 'cheese', 'bar', 'duck', 'water', 'beak', 'eyes', 'rug', 'plant', 'bag', 'cord', 'cloth', 'line', 'this', 'boat', 'bicycle', 'sand', 'the', 'red', 'black', 'beach', 'rocks', 'rock', 'glasses', 'finger', 'woman', 'shoe', 'top', 'sunglasses', 'belt', 'umbrella', 'dress', 'shoes', 'skirt', 'purse', 'trim', 'tip', 'lady', 'part', 'shadow', 'shade', 'hand', 'knife', 'blinds', 'board', 'edge', 'mountain', 'snowboard', 'stick', 'weeds', 'background', 'hill', 'bear', 'crack', 'hole', 'teddy bear', 'street light', 'truck', 'cloud', 'plants', 'plane', 'air', 'road', 'branches', 'fence', 'distance', 'clouds', 'tail', 'logo', 'dirt', 'buildings', 'tower', 'car', 'wing', 'statue', 'grass', 'path', 'collar', 'body', 'reflection', 'glass', 'clock', 'holder', 'wood', 'back', 'jeans', 'sweater', 'strap', 'buttons', 'signs', 'hood', 'cover', 'pipe', 'windows', 'branch', 'area', 'brick', 'steps', 'numbers', 'post', 'pocket', 'backpack', 'luggage', 'metal', 'bolt', 'cellphone', 'painting', 'eye', 'sock', 'bat', 'object', 'lamp', 'laptop', 'button', 'screen', 'fur', 'jar', 'vase', 'words', 'trash can', 'vegetables', 'bridge', 'candle', 'wire', 'rope', 'cart', 'train car', 'train', 'chain', 'paint', 'guy', 'watch', 'wrist', 'men', 't-shirt', 'boy', 'shorts', 'ear', 'people', 'knee', 'bus', 'blue', 'stripe', 'onion', 'bucket', 'hands', 'curtains', 'cap', 'sidewalk', 'flag', 'pavement', 'license plate', 'ball', 'racket', 'rail', 'stem', 'leaf', 'headlights', 'photo', 'number', 'letters', 'curb', 'cake', 'hat', 'front', 'patch', 'elephant', 'trunk', 'feet', 'cat', 'whiskers', 'face', 'nose', 'windshield', 'wheels', 'banner', 'city', 'neck', 'tie', 'clothes', 'ripples', 'bricks', 'sun', 'skier', 'trees', 'animal', 'surface', 'birds', 'ocean', 'mouth', 'gate', 'bracelet', 'player', 'court', 'spectator', 'tennis racket', 'circle', 'chimney', 'structure', 'shore', 'river', 'stone', 'girl', 'horse', 'sneakers', 'jet', 'runway', 'field', 'airplane', 'skateboard', 'sneaker', 'surfboard', 'controller', 'bird', 'engine', 'cone', 'stairs', 'ramp', 'skateboarder', 'zebra', 'mane', 'hoof', 'poster', 'sleeve', 'bushes', 'kite', 'child', 'park', 'cow', 'cows', 'socks', 'horn', 'name', 'wave', 'waves', 'van', 'tablecloth', 'giraffe', 'design', 'vest', 'lettuce', 'fork', 'napkin', 'meat', 'sandwich', 'bun', 'wine', 'cell phone', 'banana', 'tomato', 'bananas', 'pizza', 'tent', 'walkway', 'word', 'can', 'carrot', 'spots', 'lettering', 'orange', 'slice', 'bread', 'baby', 'suit', 'broccoli', 'kid', 'beard', 'pepper', 'crust', 'label', 'net', 'scarf', 'pen', 'shoulder', 'pattern', 'vegetable', 'column', 'base', 'platform', 'hot dog', 'spot', 'batter', 'glove', 'catcher', 'umpire', 'jersey', 'baseball', 'uniform', 'gloves', 'band', 'camera', 'tennis court', 'boots', 'string', 'railing', 'ears', 'tennis ball', 'log', 'boot', 'track', 'shadows', 'frisbee', 'arms', 'panel', 'graffiti', 'elephants', 'tracks', 'horses', 'cars', 'apple', 'bush', 'pillar', 'mouse', 'goggles', 'key', 'tree trunk', 'doorway', 'star', 'street sign', 'traffic light', 'boats', 'mountains', 'stop sign', 'balcony', 'awning', 'fire hydrant', 'hydrant', 'arrow', 'train tracks', 'surfer', 'giraffes', 'palm tree', 'gravel', 'wetsuit', 'horns', 'zebras', 'sheep', 'necklace', 'tusk', 'square', 'donut']

def transform(input_path, prefix):
    with open(input_path, "r", encoding='utf-8') as f:
        pic = json.load(f)

    pictxt = open(prefix + ".txt", "w", encoding='utf-8')

    for i in pic:
        labe = open("./labels/" + prefix + "/" + str(i)[:-4] + ".txt", "w", encoding='utf-8')
        pictxt.write("data/custom/images/" + prefix + "/" + str(i) + "\n")
        width = int(pic[i]['width'])
        height = int(pic[i]['height'])
        for j in pic[i]['objects']:
            catg = pic[i]['objects'][j]['category']
            bbox = pic[i]['objects'][j]['bbox']
            id = 0
            isExist = catg in list1
            if not isExist:
                list1.append(catg)
                id = len(list1) - 1
            else:
                for ind, val in enumerate(list1):
                    if val == catg:
                        id = ind
                        break
            xmin = int(bbox[0])
            ymin = int(bbox[1])
            xmax = int(bbox[2])
            ymax = int(bbox[3])
            labe.write(str(id) + " ")
            labe.write(str(float((xmin + xmax) / (2 * width))) + " ")
            labe.write(str(float((ymin + ymax) / (2 * height))) + " ")
            labe.write(str(float((xmax - xmin) / width)) + " ")
            labe.write(str(float((ymax - ymin) / height)) + "\n")
        labe.close()


def generate_class(filepath, in_list):
    fo = open(filepath, "w", encoding='utf-8')
    for i in in_list:
        fo.write(i)
        fo.write('\n')


if __name__ == '__main__':
    transform("./train/train.json", "train")
    transform("./val/val.json", "val")
    in_list = list1
    generate_class("class.txt", in_list)
    list1.clear()
