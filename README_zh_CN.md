# 文件到文件夹整理器
 [English](README.md)

这个简单的Python脚本，`file_to_folder.py`，旨在通过将文件移动到以其名称命名的文件夹中来整理文件。它对于保持干净和结构化的文件系统非常有用。该脚本既适用于单个文件，也适用于整个目录。

## 用法

1. **克隆仓库:**

   ```bash
   git clone https://github.com/your-username/file-to-folder-organizer.git
   ```

2. **进入项目目录:**

   ```bash
   cd file-to-folder-organizer
   ```

3. **运行脚本:**

   ```bash
   python file_to_folder.py
   ```

   按照屏幕上的提示输入文件或文件夹路径。

## 工作原理

- 如果输入是单个文件，脚本提取文件名（不包括扩展名）并检查它是否与直接父文件夹的名称匹配。如果不匹配，它将创建一个新文件夹，以文件名命名，并将文件移动到其中。

- 如果输入是一个目录，脚本将递归遍历所有文件和子目录。对于每个文件，它遵循与单个文件相同的逻辑。

## 示例

假设您有一个名为`example.txt`的文件在一个名为`Documents`的文件夹中。在此文件上运行脚本将创建一个名为`example`的新文件夹，并将文件移动到其中。结果的结构将如下所示：

```
- Documents
  - example
    - example.txt
```

## 注意

- 该脚本不会覆盖现有文件。如果同名文件夹已经存在，它将在文件夹的名称后附加一个数字以避免冲突。

- 在使用此脚本时要谨慎，特别是在重要目录上，因为它涉及移动和潜在的文件重组。

请随意根据您的需求使用、修改和分发此脚本。如果遇到任何问题或有改进建议，请提出问题或提交拉取请求。

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
```