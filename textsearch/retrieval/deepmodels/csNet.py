'''LeNet in PyTorch.'''
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

import pdb

class csNet(nn.Module):
    def __init__(self, numClasses=10000, embedSize=2048):
        super(csNet,self).__init__()

        self.fc1 = nn.Linear(2048, embedSize)
        self.bn1 = nn.BatchNorm1d(embedSize)

        self.fc2 = nn.Linear(embedSize, embedSize)
        self.bn2 = nn.BatchNorm1d(embedSize)

        self.fc3 = nn.Linear(embedSize,numClasses)

        # #Weight Initialization
        # for m in self.modules():
        #     if isinstance(m, nn.BatchNorm1d):
        #         m.weight.data.fill_(1)
        #         m.bias.data.zero_()
        #     elif isinstance(m, nn.Linear):
        #         n = m.in_features * m.out_features
        #         m.weight.data.normal_(0, math.sqrt(2. / n))

    # def resetLastLayer(self, num_classes):
    #     self.fc3 = nn.Linear(2048,num_classes)
    #     n = self.fc3.in_features * self.fc3.out_features
    #     self.fc3.weight.data.normal_(0, math.sqrt(2. / n))

    def forward(self, x):

        out = F.relu(self.bn1(self.fc1(x)))
        outFeat = self.bn2(self.fc2(out))

        out = self.fc3(F.relu(outFeat))

        return out, outFeat
