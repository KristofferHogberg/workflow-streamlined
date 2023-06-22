## Workflow Automation with an App Launcher

This is a reference project that demonstrates how to automate your workflows using an app launcher script. By following the steps below, you can customize the script according to your needs and execute it with ease.

### Prerequisites

- Python (ensure it is installed on your system)
- A text editor
- Terminal or command prompt

### Instructions

1. Modify the script `launch_apps.py` to suit your specific requirements.

2. Create a new text document.

3. On the first line of the text document, add the shebang directive:

   ```bash
   #!/usr/bin/env bash
   ```

   This instructs the system to use the Bash shell to execute the script.

4. On the second line, specify the command to run your Python script:

   ```bash
   python <name_of_your_script.py>
   ```

   Replace `<name_of_your_script.py>` with the actual name of your Python script.

5. Save the file with the same location as your Python script, using the `.sh` extension. For example, `my_script.sh`.

6. Open a terminal or command prompt in the same folder where the files are located.

7. Run the following command to make the script executable:

   ```bash
   chmod +x my_script.sh
   ```

8. If double-clicking the `my_script.sh` file opens it in a text editor instead of running the script, follow step 9.

9. Right-click on the `my_script.sh` file and choose "Open With" > "git-bash.exe" (on Windows, the path may be `C:\Program Files\Git\git-bash.exe`).

10. Now you can execute the script by double-clicking the `my_script.sh` file.

Feel free to customize the script and adapt it to your workflow requirements. Enjoy the benefits of workflow automation with this app launcher script!

