#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions and classes related with namespaces
"""


def get_namespace(name):
    """
    Returns the namespace of the given name
    :param name: str, name to get namespace from
    :return: str
    """

    namespace = name.rpartition(':')[0]

    return namespace


def remove_namespace_from_string(name):
    """
    Removes the namespace from the given string
    :param name: str, string we want to remove namespace from
    :return: str
    """

    sub_name = name.split(':')
    new_name = ''
    if sub_name:
        new_name = sub_name[-1]

    return new_name
