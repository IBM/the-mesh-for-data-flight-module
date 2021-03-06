#
# Copyright 2020 IBM Corp.
# SPDX-License-Identifier: Apache-2.0
#
import yaml


class Config:
    def __init__(self, config_path):
        # TODO: change to schemed yaml using schemed-yaml-config
        with open(config_path, 'r') as stream:
            self.values = yaml.safe_load(stream)

    def for_asset(self, asset_name: str) -> dict:
        for asset_info in self.values.get('data', []):
            if asset_info['name'] == asset_name:
                return asset_info
        raise ValueError(
            "Requested config for undefined asset: {}".format(asset_name))

    @property
    def workers(self) -> list:
        return self.values.get('workers', [])

    @property
    def auth(self) -> dict:
        return self.values.get('auth', {})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def connection_type(self, asset_name: str) -> str:
       asset_info = self.for_asset(asset_name)
       if 'connection' in asset_info:
           return asset_info['connection'].get('type')
       return None
