# Randomized Encryption and Decryption Script

This Python script allows you to perform randomized encryption and decryption on text messages. The encryption process adds a random offset to the ASCII value of each character, while the decryption process reverses this offset.

## Prerequisites

- Python 3.6 or above should be installed on your system. If Python is not installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)


## How to Run

Follow these steps to run the script using a virtual environment (pipenv):

1. **Clone the Repository:**

```bash
git clone <repository_url>
```

```bash
cd <repository_directory>
```
2. **Navigate to the project directory:**
```shell
cd Encryption-Decryption
```
3. **Create a virtual environment:**

On macOS and Linux:
```shell
python3 -m venv venv
```
On Windows:   
```shell
py -m venv venv
```
5. **Activate the virtual environment:**
On macOS and Linux:
```shell
source venv/bin/activate
```
On Windows:
```shell
venv\Scripts\activate
```
6. **Install the required packages:**
```shell
pip3 install -r requirements.txt
```
This will install all the necessary dependencies for the project in the python environment.

Run the Python script using the following command:

```bash
python3 main.py
```

The script will prompt you to choose between encryption and decryption, specify a seed, and provide the text to be processed.

If you prefer to use a file for input, you can place your text in `input.txt` before running the script.

5. **Viewing the Output:**

The script will display the result on the console. Additionally, the output will be saved to `output.txt`.

## Usage

- When prompted for encryption or decryption, enter `0` for encryption or `1` for decryption.

- The seed you provide will determine the randomness of the encryption. Using the same seed for decryption as used for encryption will yield the original text.

- For text input, simply type or paste your text when prompted. Alternatively, you can provide the input by placing it in the `input.txt` file.

Once you're done, you can exit the venv:

On macOS and Linux:

```shell
deactivate
```

On Windows:
```shell
deactivate.bat
```

You can also delete the files associated with it if you want, but you don't have to.
This action cannot be undone.

On macOS and Linux:

```shell
rm -r venv
```

On Windows:
```shell
rmdir /s /q venv
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to modify the instructions based on your project's specific setup and requirements.