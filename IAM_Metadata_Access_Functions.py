#!/usr/bin/env python
# coding: utf-8

import xml.etree.ElementTree as ET
import glob

def get_words(path):
    words = []
    names = [f for f in glob.glob(path + "**/*.xml", recursive=True)]
    iterc = 0
    for f in names:
        iterc += 1
        tree = ET.parse(f)
        root = tree.getroot()
        for i in root.iter('word'):
            words.append(i.attrib['text'])
    print(f"{iterc} xml files accessed")
    print(f'{len(words)} words are present')
    return words

def get_lines(path):
    lines = []
    names = [f for f in glob.glob(path + "**/*.xml", recursive=True)]
    iterc = 0
    for f in names:
        iterc += 1
        tree = ET.parse(f)
        root = tree.getroot()
        for i in root.iter('line'):
            lines.append(i.attrib['text'])
    print(f'{iterc} xml files accessed')
    print(f'{len(lines)} lines are present')
    return lines



