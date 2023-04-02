import torch
from torch.utils.data import DataLoader, random_split
from torchvision.transforms import ToTensor
from data import CrimeDataset
from vision import ConvModel
import numpy as np
import torch.nn as nn
import matplotlib.pyplot as plt

images = torch.tensor(np.load('./all_data.npy'))

print("Number of data examples: ", len(images))

model = ConvModel()
loss_func = nn.MSELoss(reduction='sum')
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)

batches = torch.empty((35, 1, 3, 50, 50))
targets = torch.empty((35, 1, 50, 50))

for idx in range(35):
    if idx + 4 > 34:
        continue
    batches[idx] = images[idx:idx+3]
    targets[idx] = images[idx+3]

epochs = 500
show_val = True
plot_loss = True

train_batches = batches[:25]
val_batches = batches[25:30]

train_targets = targets[:25]
val_targets = targets[25:30]


train_loss_hist = []
val_loss_hist = []

for e in range(epochs):
    optimizer.zero_grad()

    out = model(train_batches)
    loss = loss_func(out, train_targets)
    
    loss.backward()
    optimizer.step()

    train_loss_hist.append(loss.item() / train_batches.shape[0])

    with torch.no_grad():
        model.eval()
        out = model(val_batches)
        val_loss = loss_func(out, val_targets)
        model.train()
    val_loss_hist.append(val_loss.item() / val_batches.shape[0])
    print(f"Epoch: {e:3},   Train loss: {loss.item() / len(train_batches):.5f},   Val loss: {val_loss.item() / len(val_batches):.5f}")



torch.save(model.state_dict(), './model.pt')

if plot_loss:
    plt.plot(train_loss_hist)
    plt.plot(val_loss_hist)
    plt.show()

if show_val:
    with torch.no_grad():
        for i in range(5):
            plt.subplot(5, 2, 1+(2*i))
            plt.imshow(np.squeeze(model(np.reshape(val_batches[i], (1, 1, 3, 50, 50)))))


            plt.subplot(5, 2,(2*i)+2)
            plt.imshow(np.squeeze(val_targets[i]))
        plt.show()