# favicon-generator 🚀

favicon-generator is a Python tool that creates multi-resolution favicons from a single image input. It leverages [imgrszr](https://github.com/kevinveenbirkenbach/image-resizer-cli) for resizing and [ImageMagick](https://imagemagick.org/) to combine the images into one multi-resolution `.ico` file.

## Features ✨

- Generate favicons in multiple resolutions (default: 15, 32, 48, 64, 180)
- Combines resized images into one `.ico` file using ImageMagick
- Easy installation with Kevin's Package Manager

## Installation 📦

Install favicon-generator using Kevin's Package Manager:

```bash
pkgmgr install favgen
```

When installed via the package manager, you can simply run the tool with:

```bash
favgen
```

instead of running `python main.py`.

## Usage 🎯

After installation, run the following command to generate your favicon from a full-size image:

```bash
favgen /path/to/your/fullsize-image.png
```

You can also specify custom sizes by using the `--sizes` option:

```bash
favgen /path/to/your/fullsize-image.png --sizes 16 32 48 64 180
```

Get help on usage:

```bash
favgen --help
```

## Author 👤

Kevin Veen-Birkenbach  
Website: [veen.world](https://www.veen.world)

## License 📜

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Reference 💬

This README and tool documentation was inspired by a conversation on [ChatGPT](https://chatgpt.com/share/67db624c-2348-800f-92eb-e5f8bdc7a112).

---
Happy favicon generating! 😄
