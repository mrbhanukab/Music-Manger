# Music Manager

This script helps organize your music collection by renaming and moving MP3 files into artist and album folders.

## Requirements

To use this script, you need to have Python 3.x and the following packages installed:

- mutagen

You can install the required packages by running the following command:

```
python3 -m pip install mutagen
```

## Usage

1. Put all your MP3 files in a folder.
2. Open the terminal or command prompt and navigate to the folder where the `rename_files.py` script is located.
3. Run the following command:

```
python music.py
```

## Example

Suppose you have the following folder structure:
Music <br>
├── song1.mp3<br>
├── song2.mp3<br>
├── song3.mp3<br>
└── song4.mp3

You can organize your music by running the following command:

```
python music.py
```

After running the script, your folder structure will look like this:

Music <br>
├── Artist1 <br>
│ └── Album1 <br>
│ ├── Song1.mp3 <br>
│ └── Song2.mp3 <br>
└── Artist2 <br>
└── Album2 <br>
├── Song3.mp3 <br>
└── Song4.mp3 <br>

## Credits

This script was created by [MrBhanuka](https://github.com/mrbhanukab).

[![website](https://img.shields.io/badge/Github%20Page-mrbhanukab.github.io-lightgrey?style=for-the-badge&logo=GitHubr&logoColor=white)](https://mrbhanukab.github.io/) <br>
[![github](https://img.shields.io/badge/Github-mrbhanukab-%23333?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/mrbhanukab) <br>
[![twitter](https://img.shields.io/badge/Twitter-mrbhanuka-%2300acee?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/mrbhanuka)

**Note: Please make sure to replace folder_path in the README.md file with the actual path to your music folder.**
