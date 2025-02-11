# Step-by-Step Instructions

Setup instructions for uploading data to S3 with and without using environment variables.

The simplest way would be using `upload_to_s3.py` without environment variables. The file must not be pushed or shared with others due too the sensitive information it contains.

`upload_to_s3.py` and `upload_to_s3_env.py` are Python scripts that demonstrate how to upload data to an S3 bucket using the boto3 library. The main difference between the two scripts is the way they handle environment variables.

## 1. Set Environment Variables:

In your operating system, set the following environment variables:

`AWS_ACCESS_KEY_ID`

`AWS_SECRET_ACCESS_KEY`

`AWS_REGION`

### Linux or macOS
For example, on a Unix-based system (Linux or macOS), you can add the following lines to your `~/.bashrc`, `~/.bash_profile`, or `~/.zshrc` file:

```sh
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_REGION=your_aws_region
```

### Windows

Simplest way on Windows, you can set environment variables through the System Properties:

 > Open the Start Search, type in "env", and select "Edit the system environment variables".
 In the System Properties window, click on the "Environment Variables" button.
 Add the environment variables under "User variables" or "System variables".

Alternatively, you can set environment variables globally or project-specific.

#### Using .bashrc or .bash_profile for Global Settings

1. **Find/Create `.bashrc` or `.bash_profile`**:
   - Open Git Bash or your WSL terminal.
   - Navigate to your home directory:
     ```sh
     cd ~
     ```
   - Check if `.bashrc` or `.bash_profile` exists:
     ```sh
     ls -a
     ```
   - If not, create one:
     ```sh
     touch ~/.bashrc
     ```

2. **Edit `.bashrc` or `.bash_profile`**:
   - Open the file with a text editor:
     ```sh
     nano ~/.bashrc
     ```
   - Add your export commands at the bottom:
     ```sh
     export VAR_NAME="value"
     ```
   - Save and exit the editor (`Ctrl + X` in `nano`, then `Y` to confirm, then `Enter`).

3. **Apply the changes**:
   - To apply the changes immediately without restarting the terminal, source the file:
     ```sh
     source ~/.bashrc
     ```

#### Project-Specific Environment Variables

1a. **Environment Files (`.env`)**:
   - **Create a `.env` file** in each project directory:
     ```sh
     cd /path/to/your/project
     nano .env
     ```
   - **Add your environment variables**:
     ```sh
     VAR_NAME=value
     ```
   - Save and exit the editor.

1b. **Using `dotenv` (or similar tools)**:
   - Use a tool like `dotenv` in your project to load these variables when you start your project. This depends on the language or framework you are using (e.g., `require('dotenv').config();` in Node.js).

2a. **Shell Scripts**:
   - **Create a shell script** in your project directory:
     ```sh
     cd /path/to/your/project
     nano set_env.sh
     ```
   - **Add your export commands**:
     ```sh
     export VAR_NAME="value"
     ```
   - Save and exit the editor.

2b. **Source the script**:
   - To apply the environment variables from the script:
     ```sh
     source ./set_env.sh
     ```

In summary:
- **Global Variables:** Use `.bashrc` or `.bash_profile` for variables you need across all sessions and projects.
- **Project-Specific Variables:** Use `.env` files or shell scripts for variables that are specific to a project.


## 2. The Python Scripts:

- Without Environment Variables: `upload_to_s3.py`
- With Environment Variables: `upload_to_s3_env.py`

Both scripts use the boto3 library's default credential chain, which automatically picks up credentials from environment variables.

In this case, we use set the environment variables using shell scripts method:

### Step-by-Step Guide

1. **Create the Shell Script**:
   - Open a terminal and navigate to your project directory:
     ```bash
     cd /path/to/your/project
     ```
   - Create a new shell script file named `set_env.sh` using a text editor like `nano`:
     ```bash
     nano set_env.sh
     ```

2. **Add Export Commands**:
   - In the `set_env.sh` file, add the following lines with your actual AWS credentials and region:
     ```bash
     export AWS_ACCESS_KEY_ID="your_access_key_id"
     export AWS_SECRET_ACCESS_KEY="your_secret_access_key"
     export AWS_REGION="your_aws_region"
     ```
   - Save the file and exit the editor (in `nano`, you can do this by pressing `CTRL + X`, then `Y`, and `Enter`).

3. **Make the Script Executable**:
   - Ensure the script has execute permissions:
     ```bash
     chmod +x set_env.sh
     ```

4. **Source the Script**:
   - Before running your Python script, source the `set_env.sh` script to apply the environment variables:
     ```bash
     source ./set_env.sh
     ```

5. **Run Your Python Script**:
   - After sourcing the environment variables, run your Python script:
     ```bash
     python your_script.py
     ```

### Important Notes

- **Security**: Be cautious about storing your AWS credentials in plain text. Ensure that the `set_env.sh` file is not exposed or shared publicly. Consider using more secure methods like AWS IAM roles or environment-specific secret management tools for production environments.

- **Scope**: The environment variables set by the `source ./set_env.sh` command will only be available in the current terminal session. If you open a new terminal, you will need to source the script again.

- **Verification**: You can verify that the environment variables are set correctly by running:
  ```bash
  echo $AWS_ACCESS_KEY_ID
  echo $AWS_SECRET_ACCESS_KEY
  echo $AWS_REGION
  ```

By following these steps, your Python script should be able to use the AWS credentials and region specified in the `set_env.sh` script to interact with AWS services.

