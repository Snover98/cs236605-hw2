import torch
import torch.nn as nn
import torch.nn.functional as F

from .blocks import Block, Linear, ReLU, Sigmoid, Dropout, Sequential


class MLP(Block):
    """
    A simple multilayer perceptron model based on our custom Blocks.
    Architecture is (with ReLU activation):

        FC(in, h1) -> ReLU -> FC(h1,h2) -> ReLU -> ... -> FC(hn, num_classes)

    Where FC is a fully-connected layer and h1,...,hn are the hidden layer
    dimensions.
    If dropout is used, a dropout layer is added after every activation
    function.
    """

    def __init__(self, in_features, num_classes, hidden_features=(),
                 activation='relu', dropout=0, **kw):
        super().__init__()
        """
        Create an MLP model Block.
        :param in_features: Number of features of the input of the first layer.
        :param num_classes: Number of features of the output of the last layer.
        :param hidden_features: A sequence of hidden layer dimensions.
        :param activation: Either 'relu' or 'sigmoid', specifying which 
        activation function to use between linear layers.
        :param: Dropout probability. Zero means no dropout.
        """
        blocks = []

        # ====== YOUR CODE: ======
        if activation == 'relu':
            activation_type = ReLU
        elif activation == 'sigmoid':
            activation_type = Sigmoid

        prev_dim = in_features
        for next_dim in list(hidden_features):
            blocks.append(Linear(prev_dim, next_dim))
            blocks.append(activation_type())
            if dropout > 0:
                blocks.append(Dropout(dropout))
            prev_dim = next_dim

        blocks.append(Linear(prev_dim, num_classes))
        # ========================

        self.sequence = Sequential(*blocks)

    def forward(self, x, **kw):
        return self.sequence(x, **kw)

    def backward(self, dout):
        return self.sequence.backward(dout)

    def params(self):
        return self.sequence.params()

    def train(self, training_mode=True):
        self.sequence.train(training_mode)

    def __repr__(self):
        return f'MLP, {self.sequence}'


class ConvClassifier(nn.Module):
    """
    A convolutional classifier model based on PyTorch nn.Modules.

    The architecture is:
    [(Conv -> ReLU)*P -> MaxPool]*(N/P) -> (Linear -> ReLU)*M -> Linear
    """

    def __init__(self, in_size, out_classes, filters, pool_every, hidden_dims):
        """
        :param in_size: Size of input images, e.g. (C,H,W).
        :param out_classes: Number of classes to output in the final layer.
        :param filters: A list of of length N containing the number of
            filters in each conv layer.
        :param pool_every: P, the number of conv layers before each max-pool.
        :param hidden_dims: List of of length M containing hidden dimensions of
            each Linear layer (not including the output layer).
        """
        super().__init__()
        self.in_size = in_size
        self.out_classes = out_classes
        self.filters = filters
        self.pool_every = pool_every
        self.hidden_dims = hidden_dims

        self.feature_extractor = self._make_feature_extractor()
        self.classifier = self._make_classifier()

    def _make_feature_extractor(self):
        in_channels, in_h, in_w, = tuple(self.in_size)

        layers = []
        # TODO: Create the feature extractor part of the model:
        # [(Conv -> ReLU)*P -> MaxPool]*(N/P)
        # Use only dimension-preserving 3x3 convolutions. Apply 2x2 Max
        # Pooling to reduce dimensions.
        # ====== YOUR CODE: ======

        prev_channels = in_channels
        h, w = in_h, in_w
        for idx, num_channels in enumerate(self.filters, 1):
            layers.append(nn.Conv2d(prev_channels, num_channels, 3, padding=1))
            layers.append(nn.ReLU())
            prev_channels = num_channels

            if idx % self.pool_every == 0:
                layers.append(nn.MaxPool2d(2))
                h, w = h // 2, w // 2

        self.features_num = prev_channels * h * w

        # ========================
        seq = nn.Sequential(*layers)
        return seq

    def _make_classifier(self):
        in_channels, in_h, in_w, = tuple(self.in_size)

        layers = []
        # TODO: Create the classifier part of the model:
        # (Linear -> ReLU)*M -> Linear
        # You'll need to calculate the number of features first.
        # The last Linear layer should have an output dimension of out_classes.
        # ====== YOUR CODE: ======
        prev_dim = self.features_num
        for next_dim in list(self.hidden_dims):
            layers.append(nn.Linear(prev_dim, next_dim))
            layers.append(nn.ReLU())
            prev_dim = next_dim

        layers.append(nn.Linear(prev_dim, self.out_classes))
        # ========================
        seq = nn.Sequential(*layers)
        return seq

    def forward(self, x):
        # TODO: Implement the forward pass.
        # Extract features from the input, run the classifier on them and
        # return class scores.
        # ====== YOUR CODE: ======
        features = self.feature_extractor(x)
        out = self.classifier(features.view(features.shape[0], -1))
        # ========================
        return out


class YourCodeNet(ConvClassifier):
    def __init__(self, in_size, out_classes, filters, pool_every, hidden_dims, skip_every=1):
        # super().__init__(in_size, out_classes, filters, pool_every, hidden_dims)

        # TODO: Change whatever you want about the ConvClassifier to try to
        # improve it's results on CIFAR-10.
        # For example, add batchnorm, dropout, skip connections, change conv
        # filter sizes etc.
        # ====== YOUR CODE: ======
        self.skip_every = skip_every
        super().__init__(in_size, out_classes, filters, pool_every, hidden_dims)
        # ========================

    def _make_feature_extractor(self):
        in_channels, in_h, in_w, = tuple(self.in_size)

        layers = []
        # TODO: Create the feature extractor part of the model:
        # [(Conv -> ReLU)*P -> MaxPool]*(N/P)
        # Use only dimension-preserving 3x3 convolutions. Apply 2x2 Max
        # Pooling to reduce dimensions.
        # ====== YOUR CODE: ======

        prev_channels = in_channels
        h, w = in_h, in_w
        for idx, num_channels in enumerate(self.filters, 1):
            layers.append(nn.BatchNorm2d(num_features=prev_channels))

            skip_flag = idx % self.skip_every == 1 or self.skip_every == 1

            conv_type = SkipConv2d if skip_flag else nn.Conv2d

            layers.append(conv_type(prev_channels, num_channels, 3, padding=1))
            layers.append(nn.ReLU())

            if not skip_flag:
                prev_channels = 0
            prev_channels += layers[-2].out_channels

            if idx % self.pool_every == 0:
                layers.append(nn.MaxPool2d(2))
                h, w = h // 2, w // 2

        self.features_num = prev_channels * h * w

        # ========================
        seq = nn.Sequential(*layers)
        return seq

    def _make_classifier(self):
        in_channels, in_h, in_w, = tuple(self.in_size)

        layers = []
        # TODO: Create the classifier part of the model:
        # (Linear -> ReLU)*M -> Linear
        # You'll need to calculate the number of features first.
        # The last Linear layer should have an output dimension of out_classes.
        # ====== YOUR CODE: ======
        prev_dim = self.features_num
        for next_dim in list(self.hidden_dims):
            layers.append(nn.Dropout())
            layers.append(nn.Linear(prev_dim, next_dim))
            layers.append(nn.ReLU())
            prev_dim = next_dim

        layers.append(nn.Dropout())
        layers.append(nn.Linear(prev_dim, self.out_classes))
        # ========================
        seq = nn.Sequential(*layers)
        return seq


class SkipConv2d(nn.Conv2d):
    def forward(self, input):
        out = super(SkipConv2d, self).forward(input)
        return torch.cat((input, out), dim=1)
