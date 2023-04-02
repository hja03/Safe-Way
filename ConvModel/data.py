from torch.utils.data import Dataset
import pandas as pd
import numpy as np

class CrimeDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
        self.images = np.load('./all_data.npy')
        self.month_year = np.load('./month_year.npy')

    def __len__(self):
        return len(self.month_year)
    
    def __getitem__(self, index):
        return self.images[index], self.month_year[index]
    