# kptool 
kintone plugin tool 

## Installation
```bash
pip install git+https://github.com/orisano/kptool
```

## How to Use
```bash
$ kptool --help
usage: kptool [-h] [-k KEY_FILE] [-o OUTPUT_DIR] plugin_dir

positional arguments:
  plugin_dir

optional arguments:
  -h, --help            show this help message and exit
  -k KEY_FILE, --key-file KEY_FILE
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR

$ kptool /path/to/plugin-sdk/examples/vote
$ ls
vote.aiehcaiojjdckhfolkkobjmemiefpkcn.pem  vote.zip

$ mv vote.zip{,.bk}
$ ls
vote.aiehcaiojjdckhfolkkobjmemiefpkcn.pem  vote.zip.bk

$ kptool -k vote.aiehcaiojjdckhfolkkobjmemiefpkcn.pem /path/to/plugin-sdk/examples/vote
$ ls
vote.aiehcaiojjdckhfolkkobjmemiefpkcn.pem  vote.zip  vote.zip.bk

$ mkdir plugins
$ kptool -o plugins /path/to/plugin-sdk/examples/vote
$ ls plugins
vote.ahmnkcmjfamplmjlkkkgkbobffjjfnpp.pem  vote.zip

```

## Author
Nao Yonashiro (@orisano)

## License
MIT
