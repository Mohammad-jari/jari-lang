# JariLang Documentation

Welcome to **JariLang**, a simple, fun, and powerful custom programming language! This documentation will guide you through the basics of JariLang, its syntax, and how to use the interpreter.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
  - [For Windows Users](#for-windows-users)
  - [For macOS and Linux Users](#for-macos-and-linux-users)
  - [Adding to PATH (Optional)](#adding-to-path-optional)
- [Syntax Overview](#syntax-overview)
  - [Variables](#variables)
  - [Printing Output](#printing-output)
  - [Conditionals](#conditionals)
  - [Loops](#loops)
  - [Functions](#functions)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
JariLang is a lightweight, custom programming language designed for simplicity and readability. It features a clean syntax inspired by natural language, making it easy for beginners to learn and use. Whether you're writing simple scripts or exploring programming concepts, JariLang is here to make coding fun and accessible.

---

## Installation

### For Windows Users
#### Download the Installer:
- Go to the **Releases** page.
- Download the latest **JariInstaller.exe** for Windows.

#### Run the Installer:
- Double-click the downloaded `JariInstaller.exe`.
- Follow the installation wizard to install JariLang.

#### Run the Interpreter:
Open **Command Prompt** or **PowerShell** and run:
```bash
jari example.jari
```

---

### For macOS and Linux Users
#### Download the Executable:
- Go to the **Actions** page.
- Select the latest successful workflow run.
- Download the artifact for your operating system (**macOS** or **Linux**).

#### Make the Executable:
Extract the downloaded artifact and make the file executable:
```bash
chmod +x jari
```

#### Run the Interpreter:
Run the interpreter directly:
```bash
./jari example.jari
```

---

### Adding to PATH (Optional)
If the interpreter is not working directly, you may need to add its directory to your system's PATH environment variable.

#### For Windows:
1. Open the **Start** menu and search for *Environment Variables*.
2. Click **Edit the system environment variables**.
3. In the **System Properties** window, click **Environment Variables**.
4. Under **System variables**, find the `Path` variable and click **Edit**.
5. Click **New** and add the full path to the directory containing `jari_interpreter.exe` (e.g., `C:\Program Files\JariInterpreter`).
6. Click **OK** to save the changes.

#### For macOS/Linux:
1. Open a **terminal**.
2. Add the following line to your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`):
```bash
export PATH=$PATH:/path/to/jari
```
3. Reload the shell configuration:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

---

## Syntax Overview

### Variables
Variables in JariLang are dynamically typed and declared using the `:` operator.
```jari
x : 10
name : "JariLang"
is_fun : true
```

---

### Printing Output
Use the `boliye` command to print output.
```jari
boliye "Hello, World!"
boliye "The value of x is:" x
```

---

### Conditionals
JariLang supports `agar` (if) and `nito` (else) for conditional logic.
```jari
agar x > 10 :
    boliye "x is greater than 10"
nito :
    boliye "x is 10 or less"
end
```

---

### Loops
Use `dohraye jbtk` to create loops.
```jari
counter : 0
dohraye jbtk counter < 5 :
{
    boliye "Counter is:" counter
    counter : counter + 1
}
```

---

### Functions
Functions are defined using the `:` operator and can accept parameters.
```jari
add(a, b) : {
    result : a + b
    boliye "The sum is:" result
}

add(5, 10)  # Output: The sum is: 15
```

---

## Examples

### Example 1: Hello World
```jari
boliye "Hello, World!"
```

### Example 2: Simple Calculator
```jari
calculate(a, b) : {
    sum : a + b
    product : a * b
    boliye "Sum:" sum
    boliye "Product:" product
}

x : 10
y : 5
calculate(x, y)
```

### Example 3: Loop and Condition
```jari
counter : 0
dohraye jbtk counter < 5 :
{
    agar counter % 2 == 0 :
        boliye counter "is even"
    nito :
        boliye counter "is odd"
    counter : counter + 1
}
```

---

## Contributing
We welcome contributions to JariLang! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated. Here’s how you can contribute:

### Fork the Repository:
- Click the **Fork** button on the GitHub repository page.

### Create a Branch:
Create a new branch for your feature or bug fix:
```bash
git checkout -b feature-name
```

### Make Changes:
Make your changes and commit them:
```bash
git commit -m "Add feature-name"
```

### Submit a Pull Request:
Push your changes to your forked repository and submit a **pull request**.

---

## License
JariLang is released under the **MIT License**. See the `LICENSE` file for more details.

---

## Let’s Build Something Amazing Together!
JariLang is more than just a programming language—it’s a community. Join us in making programming accessible, fun, and powerful for everyone.

