import torch
import torch.nn as nn
from monai.networks.blocks import UnetOutBlock


class EnsembleModel(nn.Module):
    def __init__(self, modelA, modelB):
        super().__init__()
        self.modelA = modelA
        self.modelB = modelB
        self.conv0 = nn.Conv3d(96, 3, kernel_size=(1, 1, 1), stride=(1, 1, 1), padding=0)

    def forward(self, x):
        x1 = self.modelA(torch.clone(x))
        x2 = self.modelB(x)
        list = []
        for i in range(6):
            x = torch.cat((x1[i], x2[i]), dim=1)
            x = self.conv0(x)
            list.append(x)
        return list