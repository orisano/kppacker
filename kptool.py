#!/usr/bin/env python
import OpenSSL
import six

import argparse
import hashlib
import itertools
import os
import sys
import zipfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(six.u("plugin_dir"))
    parser.add_argument(six.u("-k"), six.u("--key-file"))
    parser.add_argument(six.u("-o"), six.u("--output-dir"), default=six.u("."))
    args = parser.parse_args()

    plugin_dir = os.path.abspath(args.plugin_dir)
    plugin_name = os.path.basename(plugin_dir)

    output_dir = os.path.abspath(args.output_dir)
    zip_path = os.path.join(output_dir, plugin_name + six.u(".zip"))

    if not valid_plugin_dir(plugin_dir):
        sys.exit(1)
        
    if args.key_file:
        key = load_pem(args.key_file)
    else:
        key = gen_pkey()

    plugin_id = archive_plugin(plugin_dir, key, zip_path)

    if args.key_file is None:
        key_file = six.u("{}.{}.pem").format(plugin_name, plugin_id)
        key_path = os.path.join(output_dir, key_file) 
        with open(key_path, "w") as f:
            f.write(dump_pem(key))


def find(path, matchfn):
    # type: (Text, Callable[[Text], bool]) -> Iterator[Text]
    for root, dirs, files in os.walk(path):
        for x in itertools.chain(dirs, files):
            if matchfn(x):
                yield os.path.join(root, x)


def valid_plugin_dir(plugin_dir):
    # type: (Text) -> bool
    if not os.path.exists(plugin_dir):
        six.print_(six.u("Plugin directory {} not found.").format(plugin_dir))
        return False

    manifest_path = os.path.join(plugin_dir, six.u("manifest.json"))
    if not os.path.exists(manifest_path):
        six.print_(six.u("Manifest file {} not found.").format(manifest_path))
        return False

    dotfiles = list(find(plugin_dir, lambda x: x.startswith(six.u("."))))
    if dotfiles:
        six.print_(six.u("PLUGIN_DIR must not contain dot files or directories."))
        for dotfile in dotfiles:
            six.print_(dotfile)
        return False

    pem_files = list(find(plugin_dir, lambda x: x.endswith(six.u(".pem"))))
    if pem_files:
        six.print_(six.u("PLUGIN_DIR must not contain *.pem files."))
        return False

    return True


def archive_dir(fp, directory):
    # type: (IO[bytes], Text) -> IO[bytes]
    base_dir = os.path.abspath(directory)
    assert os.path.isdir(base_dir)

    with zipfile.ZipFile(fp, "w") as zf:
        for root, dirs, files in os.walk(base_dir):
            for x in itertools.chain(dirs, files):
                path = os.path.join(root, x)
                zf.write(path, os.path.relpath(path, base_dir))
    return fp


def archive_plugin(plugin_dir, key, zip_path):
    # type: (Text, OpenSSL.crypto.PKey, Text) -> Text
    contents_zip = archive_dir(six.BytesIO(), plugin_dir).getvalue()
    signature = OpenSSL.crypto.sign(key, contents_zip, b"sha1")
    pubkey = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_ASN1, key)
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr(six.u("contents.zip"), contents_zip)
        zf.writestr(six.u("SIGNATURE"), signature)
        zf.writestr(six.u("PUBKEY"), pubkey)
    return gen_plugin_id(pubkey)


def gen_plugin_id(pubkey):
    # type: (bytes) -> Text
    key_hash = six.u(hashlib.sha256(pubkey).hexdigest()[:32]) # type: Text 
    src = six.u("0123456789abcdef")
    dst = six.u("abcdefghijklmnop")
    return key_hash.translate({ord(s): d for s, d in zip(src, dst)})


def load_pem(key_file):
    # type: (Text) -> OpenSSL.crypto.PKey
    with open(key_file, "r") as f:
        return OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, f.read())


def gen_pkey():
    # type: () -> OpenSSL.crypto.PKey
    pkey = OpenSSL.crypto.PKey()
    pkey.generate_key(OpenSSL.crypto.TYPE_RSA, 1024)
    return pkey


def dump_pem(key):
    # type: (OpenSSL.crypto.PKey) -> bytes
    return OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key)


if __name__ == "__main__":
    main()
