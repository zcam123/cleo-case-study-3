import os
import sys
import argparse

import numpy as np
import matplotlib.pyplot as plt


def plot_lfp(path):
    lfp = np.load(os.path.join(path, 'tklfp.npy'))
    plt.figure()
    plt.plot(lfp)
    plt.title("TKLFP")
    plt.ylabel("μV")
    plt.xlabel("ms")


def plot_input(path):
    npz = np.load(os.path.join(path, 'input.npz'))
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(npz['t_s'], npz['inputs1'])
    ax1.set(title='endogenous input')
    ax2.plot(npz['t_opto_ms'], npz['Irr0_mW_per_mm2'])
    ax2.set(title='optogenetic input')


# def main(args):
#     # TODO(pmin): Implement a neural net here.
#     print(args.model)  # Prints the model type.

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="Train a neural net")

#     parser.add_argument("--model", required=True, help="Model type (resnet or alexnet)")
#     parser.add_argument("--niter", type=int, default=1000, help="Number of iterations")
#     parser.add_argument("--in_dir", required=True, help="Input directory with images")
#     parser.add_argument("--out_dir", required=True, help="Output directory with trained model")

#     args = parser.parse_args()
#     main(args)

if __name__ == '__main__':
    plot_lfp(sys.argv[1])
    plot_input(sys.argv[1])