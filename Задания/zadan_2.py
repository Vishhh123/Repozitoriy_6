#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def compare_objects(*args, **kwargs):
    keys = kwargs.get("keys", [])

    result = {}

    for key in keys:
        values = []
        for obj in args:
            value = obj.get(key)
            values.append(value)
        result[key] = values

    return result


if __name__ == "__main__":
    result = compare_objects(
        {"a": 1, "b": 2},
        {"a": 3, "b": 2},
        keys=["a", "b"])
    print(result)





    