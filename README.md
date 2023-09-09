# ElecPy

ElecPy is a Python project created by Parshwanath V Jain (PVJ) on September 8, 2023. It aims to combine the fields of electronics and computer science on a surface level, making it easier to perform basic electronic calculations and experiments. The project provides a command-line interface for various electronic calculations and simulations.

#### Video Demo:  https://youtu.be/heNWHnkTJ-I

## Features

ElecPy offers the following features:

1. **Ohm's Law Calculator**: Calculate voltage, current, or resistance using Ohm's Law.
2. **Drain Current Calculator**: Compute drain current in a MOSFET based on input parameters.
3. **Common Source (CS) Amplifier Gain Calculator**: Calculate midband gain for a CS amplifier.
4. **CS Amplifier Frequency Response Plotter**: Generate frequency response plots for a CS amplifier.
5. **Common Emitter (CE) Amplifier Gain Calculator**: Calculate midband gain for a CE amplifier.
6. **CE Amplifier Frequency Response Plotter**: Generate frequency response plots for a CE amplifier.
7. **Signal Sampling**: Plot the sampled version of various signals.
8. **Fast Fourier Transform (FFT) Calculator**: Calculate and visualize the FFT of a given sequence.

## Getting Started

To use ElecPy, follow these steps:

### Prerequisites

- Python 3.x installed on your system.
- Required Python packages installed. You can install them using `pip install -r requirements.txt`.

### Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.

## Usage

You can use ElecPy by running it from the command line with various arguments. Here are some examples:

### Ohm's Law Calculator

```bash
python elecpy.py --ohm "10_V" "5_A"
```

### Drain Current Calculator

```bash
python elecpy.py --dracurr 3.5 2.0
```

### CS Amplifier Gain Calculator

```bash
python elecpy.py --csamp 10.0 20.0 0.01 50.0 100.0 1.0
```

### CS Amplifier Frequency Response Plotter

```bash
python elecpy.py --csamp_g 1.0 20.0 1000.0
```

### CE Amplifier Gain Calculator

```bash
python elecpy.py --ceamp 5.0 50.0 100.0 200.0 0.02 2.0 3.0 1000.0
```

### CE Amplifier Frequency Response Plotter

```bash
python elecpy.py --ceamp_g 1.0 30.0 2000.0
```

### Signal Sampling

```bash
python elecpy.py --sample 0
```
**Always zero for execution you can choose different signals in the second menu.**
You can input the name of signal **as mentioned** in the menu for the type of signal and then you can enter specifications for each signal.

### Fast Fourier Transform (FFT) Calculator

```bash
python elecpy.py --fft 1000.0 50.0
```

Choose the desired operation by passing the appropriate command-line arguments.

## Contributing

ElecPy is open-source, and contributions from the community are welcome. If you have suggestions, bug reports, or want to contribute new features, please feel free to fork the repository and create a pull request.

## License

This project is licensed under the MIT License. You can find the full license details in the [LICENSE.md](LICENSE.md) file.

Thank you for using ElecPy! I hope it helps you with your electronic calculations and experiments.