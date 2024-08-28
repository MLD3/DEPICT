import os
import random
import numpy as np
import pandas as pd
import torch
import sys
from matplotlib import pyplot as plt
from PIL import Image
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms as trn
from torchvision.datasets.folder import default_loader
import csv
np.random.seed(88)
torch.manual_seed(88)
random.seed(88)


def get_loader(batch_size,split="all"):
    all = Source(split)
    
    loader = DataLoader(all, batch_size=batch_size, shuffle=False, num_workers=40)
    return loader

class Source(Dataset):
    def __init__(self, split,loader=default_loader):
        self.loader = default_loader
        self.split = split

        # NOTE: these were the transformations they used in their code 
        trans = [trn.Resize((256,256)),
                 trn.CenterCrop(224),
                 trn.ToTensor(),
                 trn.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]
            
        self.trans = trn.Compose(trans)
        
        self._load_metadata()

    def _load_metadata(self):
        self.data = pd.read_csv('DEPICT_coco_concepts.csv')
        if self.split == "all":
            return
        elif self.split == "val":
            self.data = self.data[self.data['split'] == 'val']
        elif self.split == "train":
            self.data = self.data[self.data['split'] == 'train']
        elif self.split == "test":
            self.data = self.data[self.data['split'] == 'test']
                
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        id = row.image_id
        img_path = row.file_name
        img = self.loader(img_path)
        img = self.trans(img)
        return id, img