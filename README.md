# BIP39 test tool
Tool for testing BIP39 wallet keywords

## Basic solution (implemented)

This tool tests if a given set ot words represent a BIP39 compatible wallet - the words are chekced vs. the english.txt list and transformed in order to calculate if the wallet checksum is OK. Further the order of the words can be altered to detect if the words were moved in any way.
