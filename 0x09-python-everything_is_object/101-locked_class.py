#!/usr/bin/python3
class LockedClass:
    """Locked class that only lets the user create `attribute 'first_name'"""
    __slots__ = ['first_name']
