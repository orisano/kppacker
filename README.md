# kppacker
kintone plugin packer

## installation
```bash
pip install git+https://github.com/orisano/kppacker
```

## How to Use
```bash
$ kppacker --help
usage: kppacker [-h] [-k KEY_FILE] [-o OUTPUT_DIR] plugin_dir

positional arguments:
  plugin_dir

optional arguments:
  -h, --help            show this help message and exit
  -k KEY_FILE, --key-file KEY_FILE
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR

$ kppacker /path/to/plugin-sdk/examples/vote
$ ls
vote.aiehcaiojjdckhfolkkobjmemiefpkcn.pem  vote.zip

$ mv vote.zip{,.bk}
$ ls
vote.aiehcaiojjdckhfolkkobjmemiefpkcn.pem  vote.zip.bk

$ kppacker -k vote.aiehcaiojjdckhfolkkobjmemiefpkcn.pem /path/to/plugin-sdk/examples/vote
$ ls
vote.aiehcaiojjdckhfolkkobjmemiefpkcn.pem  vote.zip  vote.zip.bk

$ mkdir plugins
$ kppacker -o plugins /path/to/plugin-sdk/examples/vote
$ ls plugins
vote.ahmnkcmjfamplmjlkkkgkbobffjjfnpp.pem  vote.zip

```
