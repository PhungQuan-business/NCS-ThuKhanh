# Step to run the code

## Clone the repository

`git clone https://github.com/PhungQuan-business/NCS-ThuKhanh.git`

## Add the current directory to the environment

- Make sure you are at the parent directory of the project
- If you're using MacOS or Linux

  ```sh
  cd NCS-ThuKhanh
  export PYTHONPATH=$PYTHONPATH:.
  ```

- If you're on a Window

  ```sh
  dir NCS-ThuKhanh
  set PYTHONPATH=%PYTHONPATH%;.
  ```

## Run the code

- **Install necessary packages** \

  ```sh
  pip install -r requirements.txt
  ```

- **Run the code** \
  Provide path to the dataset in file `main.py` and run the following command in the terminal
  ```sh
  python main.py
  ```

new code
based on the result of the previous code, IV values

- IV < 0.1 => remove - this has to do first
- normalized IV values to make sum of it = 1(1/sum(all))

- a function for reverting values(helper)
- a function to normalize all values()
