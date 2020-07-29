#!/usr/bin/python

from AnnotatorCore import *


def test_getgenesfromfusion():
    AB_EXAMPLE = ('A', 'B')
    assert getgenesfromfusion('A-B') == AB_EXAMPLE
    assert getgenesfromfusion('A-B ') == AB_EXAMPLE
    assert getgenesfromfusion('a-b') == ('a', 'b')
    assert getgenesfromfusion('A') == ('A', 'A')
    assert getgenesfromfusion('A1-1B') == ('A1', '1B')

    # Test fusion case insensitive
    assert getgenesfromfusion('A-B fusion') == AB_EXAMPLE
    assert getgenesfromfusion('A-B Fusion') == AB_EXAMPLE

    # Test unnecessary characters will be trimmed off after fusion
    assert getgenesfromfusion('A-B fusion archer') == AB_EXAMPLE
    assert getgenesfromfusion('A-B fusion Archer') == AB_EXAMPLE
    assert getgenesfromfusion('A-B fusion -Archer') == AB_EXAMPLE
    assert getgenesfromfusion('A-B fusion -archer') == AB_EXAMPLE
    assert getgenesfromfusion('A-B fusion - archer') == AB_EXAMPLE
    assert getgenesfromfusion('A-B fusion - archer ') == AB_EXAMPLE

    assert getgenesfromfusion('A-B fusion test') == AB_EXAMPLE
    assert getgenesfromfusion('fusion A-B fusion') == AB_EXAMPLE

    # Test intragenic
    assert getgenesfromfusion('MLL2-intragenic') == ('MLL2', 'MLL2')

def ReplaceAll():
    # Test for case insensitivity
    assert ReplaceAll('tyr') == 'Y'
    assert ReplaceAll('tYr') == 'Y'
    assert ReplaceAll('Tyr') == 'Y'
    assert ReplaceAll('tyR') == 'Y'
    assert ReplaceAll('TyR') == 'Y'
    assert ReplaceAll('TYR') == 'Y'
    assert ReplaceAll('tYR') == 'Y'

    # Test ReplaceAll only targets the dict() keys
    assert ReplaceAll('bubblegum juice cup dairy hot pot Tyr melon') == 'bubblegum juice cup dairy hot pot Y melon'
    assert ReplaceAll('Ly Lys Pr Pro Gln Glad Glue Ph PH Phe') == 'Ly K Pr P Q Glad Glue Ph PH F'
    assert ReplaceAll('nOt can fat Tan Rat cat dog man Men FAn rot taR car fAr map TAP Zip poP') == 'nOt can fat Tan Rat cat dog man Men FAn rot taR car fAr map TAP Zip poP'

    # Test ReplaceAll is not affected by numbers
    assert ReplaceAll('Tyr600E Cys56734342342454562456') == 'Y600E C56734342342454562456'
    assert ReplaceAll('60 045 434 345 4 26 567 254 245 34 67567 8 56 8 364 56 6 345 7567 3455 6 8 99 89 7 3') == '60 045 434 345 4 26 567 254 245 34 67567 8 56 8 364 56 6 345 7567 3455 6 8 99 89 7 3'

    # Test ReplaceAll is not affected by empty string and whitespaces
    assert ReplaceAll('') == ''
    assert ReplaceAll(' ') == ' '
    assert ReplaceAll('Tyr Asn As n Ile Il e') == 'Y N As n I Il e'