import torch
from torch.utils.data import DataLoader, random_split
from torchvision.transforms import ToTensor
from data import CrimeDataset
from vision import ConvModel
import numpy as np
import torch.nn as nn
import matplotlib.pyplot as plt

images = torch.tensor(np.load('./all_data.npy'), dtype=torch.float64)

model = ConvModel().double()

checkpoint = torch.load('./model.pt')
model.load_state_dict(checkpoint)
model.eval()

latest = []
latest.append(torch.reshape(images[-3], (1, 1, 50, 50)).double())
latest.append(torch.reshape(images[-2], (1, 1, 50, 50)).double())
latest.append(torch.reshape(images[-1], (1, 1, 50, 50)).double())

predicts = []
for i in range(10):
    with torch.no_grad():
        batch = torch.concat((latest[-1], latest[-2], latest[-3]), dim=1)
        batch = torch.reshape(batch, (1,1,3,50,50))
        predict = model(batch)
        
        latest.append(predict)
        predicts.append(predict)

forecast = torch.squeeze(torch.concat(predicts, dim=0))




to_save = torch.cat([images, forecast], dim=0).numpy()




my = np.load('./month_year.npy')

add = np.array([[3, 2032],
[4, 2032],
[5, 2032],
[6, 2032],
[7, 2032],
[8, 2032],
[9, 2032],
[10, 2032],
[11, 2032],
[12, 2032]], dtype=np.int64)

my = np.concatenate((my, add))

print(my.shape)
print(to_save.shape)

np.save('./all_data.npy', to_save)
np.save('./month_year.npy', my)