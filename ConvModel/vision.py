import torch
import torch.nn as nn


class ConvModel(nn.Module):
    def __init__(self):
        super(ConvModel, self).__init__()


        # Needs to take a (batch_size, channels, D, W, H)
        #                 (batch_size, 1, time_len, 50, 50)
        self.encoder = nn.Sequential(
            nn.Conv3d(1, 16, (3, 3, 3), stride=(1, 2, 2), padding=(1, 1, 1)),
            nn.ReLU(),
            nn.Conv3d(16, 64, (3, 3, 3), stride=(1, 3, 3), padding=(0, 1, 1), bias=False),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 128, (1, 3, 3), stride=(1, 3, 3)),
            nn.ReLU()
        )

        self.dense = nn.Sequential(
            nn.Flatten(),
            nn.Linear(1152, 1152),
            nn.Dropout(p=0.5),
            nn.ReLU(),
            nn.Unflatten(dim=1, unflattened_size=(128, 3, 3))
        )

        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(128, 64, 3, stride=3, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 16, 3, stride=3, padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(16, 1, 3, stride=2, padding=1, output_padding=1),
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.dense(x)
        x = self.decoder(x)
        return x