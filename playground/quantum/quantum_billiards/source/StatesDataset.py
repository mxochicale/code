from typing import Optional, Callable
import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset


class StatesDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, states_pkl: str,
                 is_test: bool = False,
                 min_state: int = 50,
                 transform: Optional[Callable] = None):
        """
        Args:
            states_pkl (string): File path to the pickled csv containing the state array
            the state classes, and the train/test indicator variable
            is_test: whether or not to use only test samples
            min_state: the lowest state number used for modeling (0 corresponds to ground state)
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.states_pkl = states_pkl
        self.is_test = is_test
        self.min_state = min_state
        self.transform = transform

        # load and filter the states based on inputs
        self.states = self._prep_data()

    def _prep_data(self):
        # load the states
        states = pd.read_pickle(self.states_pkl)

        # filter
        states = states[states.is_test == self.is_test]
        states = states[states.state_number >= self.min_state]

        return states

    def __len__(self):
        return self.states.shape[0]

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        row = self.states.iloc[idx]
        sample = {'wave_function': row['image'][None]**2,
                  'is_integrable': row['is_integrable'],
                  'mass_ratio': row['mass_ratio'],
                  'state_number': row['state_number']}

        if self.transform:
            sample = self.transform(sample)

        return sample
