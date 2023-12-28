# <center>File to Folder </center>
 [中文文档点我](README_zh_CN.md)

This simple Python script, `file_to_folder.py`, is designed to organize files by moving them into folders based on their names. It can be useful for maintaining a clean and structured file system. The script works for both single files and entire directories.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/file-to-folder-organizer.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd file-to-folder-organizer
   ```

3. **Run the Script:**

   ```bash
   python file_to_folder.py
   ```

   Follow the on-screen instructions to input the file or folder path.

## How it Works

- If the input is a single file, the script extracts the file name (excluding the extension) and checks if it matches the immediate parent folder's name. If not, it creates a new folder with the file name and moves the file into it.

- If the input is a directory, the script recursively goes through all files and subdirectories. For each file, it follows the same logic as for a single file.

## Example

Suppose you have a file named `example.txt` in a folder named `Documents`. Running the script on this file will create a new folder named `example` and move the file into it. The resulting structure will look like this:

```
- Documents
  - example
    - example.txt
```

## Note

- The script does not overwrite existing files. If a folder with the same name already exists, it will append a number to the folder's name to avoid conflicts.

- Be cautious when using this script, especially on important directories, as it involves moving and potentially restructuring files.

Feel free to use, modify, and distribute this script according to your needs. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
```
   