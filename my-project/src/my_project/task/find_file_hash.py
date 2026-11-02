import hashlib
from tomllib import load
from os import sep, walk
from typing import Literal

from pydantic import BaseModel

HashAlgo = Literal['md5', 'sha1', 'sha2']

class ConfigModel(BaseModel):
    path: str
    hash: list[HashAlgo]

def get_config():
    with open('configs/config.toml', mode='rb') as data_file:
        toml_node = load(data_file)
        config_model = ConfigModel.model_validate(obj=toml_node)
        return config_model


def main():
    index = dict()
    config = get_config()
    for subdir, _, files in walk(config.path):
        for file in files:
            filepath = subdir + sep + file
            with open(file=filepath, mode = 'rb') as data_file:
                data = data_file.read()
            for algo in config.hash:
                if algo == 'md5':
                    hash_value = hashlib.md5(data).hexdigest()
                    print(hash_value)
                elif algo == 'sha1':
                    hash_value = hashlib.sha1(data).hexdigest()
                    print(hash_value)
                elif algo == 'sha2':
                    hash_value = hashlib.sha256(data).hexdigest()
                    print(hash_value)
                index[hash_value] = filepath


    input_line = ''
    while input_line != 'q':
        input_line = input()
        print(index[input_line])


if __name__ == '__main__':
    main()