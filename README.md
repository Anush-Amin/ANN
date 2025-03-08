# Using GitHub Copilot in VS Code

To use GitHub Copilot in VS Code, follow these steps:

1. **Install GitHub Copilot Extension**: 
    - Open VS Code.
    - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
    - Search for "GitHub Copilot" and click `Install`.

2. **Sign In to GitHub**:
    - After installing the extension, you will be prompted to sign in to GitHub.
    - Follow the on-screen instructions to complete the sign-in process.

3. **Start Using GitHub Copilot**:
    - Open a new or existing file in VS Code.
    - Start typing your code, and GitHub Copilot will provide suggestions.
    - Use `Tab` to accept a suggestion or `Esc` to dismiss it.

## Shortcuts
- **Trigger Suggestions**: `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (macOS)
- **Next Suggestion**: `Alt+]` (Windows/Linux) or `Option+]` (macOS)
- **Previous Suggestion**: `Alt+[` (Windows/Linux) or `Option+[` (macOS)
- **Accept Suggestion**: `Tab`
- **Dismiss Suggestion**: `Esc`

## Copilot Edits
GitHub Copilot can also provide inline suggestions and edits as you type. These suggestions appear in real-time and can be accepted or dismissed using the shortcuts mentioned above.

## Copilot Chat
GitHub Copilot Chat allows you to interact with Copilot in a conversational manner. You can ask questions, get explanations, and receive code suggestions in a chat interface.

### Difference Between Copilot Edits and Copilot Chat
- **Copilot Edits**: Provides inline code suggestions and completions as you type. It is designed to assist with writing code quickly and efficiently.
- **Copilot Chat**: Offers a conversational interface where you can ask questions, get explanations, and receive code suggestions. It is useful for understanding code, debugging, and getting more detailed assistance.

By following these steps, you can start using GitHub Copilot to assist you with coding in VS Code.

# Setting Up Python Environment in VS Code

To create a Python environment in VS Code using the terminal, follow these steps:

1. **Open VS Code**: Launch Visual Studio Code.

2. **Open Terminal**: Open the integrated terminal in VS Code by selecting `View` > `Terminal` from the top menu or by pressing `` Ctrl+` ``.

3. **Navigate to Your Project Directory**: Use the `cd` command to navigate to your project directory. For example:
    ```sh
    cd /c:/Anush/Anush_Documents/Machine_learning/Deep_Learning/ANN/Classification
    ```

4. **Create a Virtual Environment**: For a Python deep learning project, it is recommended to use `conda` to create a virtual environment as it provides better package management and dependency handling. Run the following command to create a virtual environment using `conda`. Replace `env` with your preferred environment name.
    ```sh
    conda create --name env python=3.11 -y
    ```
    The --name flag creates the environment in Conda's default directory for environments, typically under anaconda3/envs/ or miniconda3/envs/.
    You provide a name (env), and Conda handles the location automatically
    ```sh
    conda create -p ./env python=3.11 -y
    ```
    The -p flag allows you to specify a custom path (in this case, venv) where the environment will be created.

Alternatively, you can use `venv` to create a virtual environment. Run the following command:
    ```sh
    python -m venv env
    ```

5. **Activate the Virtual Environment**:
    - On Windows:
        ```sh
        conda activate env/
        ```
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```

6. **Install Required Packages**: Once the virtual environment is activated, you can install the necessary packages using `pip` and a `requirements.txt` file. For example:
    ```sh
    pip install -r requirements.txt
    ```

7. **Deactivate the Virtual Environment**: When you are done working, you can deactivate the virtual environment by running:
    ```sh
    deactivate
    ```

By following these steps, you can set up a Python environment in VS Code using the terminal.

# Working with Git

To work with Git in your project, follow these steps:

1. **Create a `.gitignore` File**: Create a `.gitignore` file in the root of your project directory if it doesn't already exist. You can do this using VS Code:
    - Open VS Code.
    - In the Explorer sidebar, right-click on the root folder of your project.
    - Select `New File`.
    - Name the file `.gitignore`.

2. **Add `venv` to `.gitignore`**: Add the `venv` directory to the `.gitignore` file to ensure it is not tracked by Git.
    ```plaintext
    venv/
    ```

3. **Initialize a Git Repository**: If your project is not already a Git repository, initialize it by running:
    ```sh
    git init
    ```

4. **Clone a Repository**: To clone an existing repository, use the `git clone` command followed by the repository URL. For example:
    ```sh
    git clone https://github.com/username/repository.git
    ```

5. **Check the Current Branch**: To check the current branch you are on, use:
    ```sh
    git branch
    ```
    If the command does not provide any output, it means there are no branches created yet, and you are on the default branch (usually `main` or `master`).

6. **Create a New Branch**: To create a new branch, use:
    ```sh
    git checkout -b new-branch-name
    ```

7. **Add Changes**: To add changes to the staging area, use:
    ```sh
    git add .
    ```

8. **Commit Changes**: To commit the changes with a message, use:
    ```sh
    git commit -m "Your commit message"
    ```

9. **Push Changes**: To push the changes to the remote repository, use:
    ```sh
    git push origin branch-name
    ```

10. **Pull Changes**: To pull the latest changes from the remote repository, use:
    ```sh
    git pull origin branch-name
    ```

11. **Work on Development Branch and Merge to Main Branch**:

    1. **Create and Switch to the Development Branch**:
        - If the development branch does not exist, create it and switch to it:
            ```sh
            git checkout -b development
            ```
        - If the development branch already exists, switch to it:
            ```sh
            git checkout development
            ```

    2. **Make Your Changes**:
        - Work on your project and make the necessary changes.

    3. **Add and Commit Your Changes**:
        - Add your changes to the staging area:
            ```sh
            git add .
            ```
        - Commit your changes with a meaningful message:
            ```sh
            git commit -m "Your commit message"
            ```

    4. **Push Changes to the Remote Development Branch**:
        - Push your changes to the remote development branch:
            ```sh
            git push origin development
            ```

    5. **Merge Development Branch into Main Branch**:
        - Switch to the main branch:
            ```sh
            git checkout main
            ```
        - Merge the development branch into the main branch:
            ```sh
            git merge development
            ```

    6. **Push Changes to the Remote Main Branch**:
        - Push the merged changes to the remote main branch:
            ```sh
            git push origin main
            ```

By following these steps, you can work on the development branch and then merge your changes into the main branch.

By following these steps, you can effectively manage your project using Git.