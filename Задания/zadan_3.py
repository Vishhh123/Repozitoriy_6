#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def build_tree(pairs, root):
    tree = {}

    for parent, child in pairs:
        if parent == root:
            tree[child] = build_tree(pairs, child)

    return tree


pairs = [("root", "A"), ("root", "B"), ("A", "C"), ("B", "D"), ("D", "E")]
result = {"root": build_tree(pairs, "root")}
print(result)



