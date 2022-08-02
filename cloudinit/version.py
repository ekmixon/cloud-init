# Copyright (C) 2012 Yahoo! Inc.
#
# Author: Joshua Harlow <harlowja@yahoo-inc.com>
#
# This file is part of cloud-init. See LICENSE file for license information.

__VERSION__ = "22.1"
_PACKAGED_VERSION = "@@PACKAGED_VERSION@@"

FEATURES = [
    # supports network config version 1
    "NETWORK_CONFIG_V1",
    # supports network config version 2 (netplan)
    "NETWORK_CONFIG_V2",
]


def version_string():
    """Extract a version string from cloud-init."""
    return __VERSION__ if _PACKAGED_VERSION.startswith("@@") else _PACKAGED_VERSION


# vi: ts=4 expandtab
