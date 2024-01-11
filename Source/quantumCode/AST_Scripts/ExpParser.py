# Generated from Exp.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

from antlr4 import ParseTreeVisitor, ParseTreeListener

if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,448,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,115,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,132,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,188,
        8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,
        271,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,4,27,326,8,27,11,27,12,27,327,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,4,28,344,8,28,
        11,28,12,28,345,1,28,1,28,1,29,1,29,1,29,1,29,3,29,354,8,29,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,3,37,419,8,37,
        1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,41,1,41,1,41,1,41,5,41,438,8,41,10,41,12,41,441,9,41,1,41,1,41,
        1,41,1,41,1,41,1,41,0,0,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,0,0,443,0,84,1,0,0,0,2,114,1,0,0,0,4,131,1,0,0,
        0,6,133,1,0,0,0,8,187,1,0,0,0,10,189,1,0,0,0,12,193,1,0,0,0,14,200,
        1,0,0,0,16,204,1,0,0,0,18,209,1,0,0,0,20,214,1,0,0,0,22,219,1,0,
        0,0,24,224,1,0,0,0,26,229,1,0,0,0,28,233,1,0,0,0,30,237,1,0,0,0,
        32,241,1,0,0,0,34,246,1,0,0,0,36,251,1,0,0,0,38,270,1,0,0,0,40,272,
        1,0,0,0,42,279,1,0,0,0,44,286,1,0,0,0,46,293,1,0,0,0,48,300,1,0,
        0,0,50,307,1,0,0,0,52,314,1,0,0,0,54,317,1,0,0,0,56,334,1,0,0,0,
        58,353,1,0,0,0,60,355,1,0,0,0,62,363,1,0,0,0,64,371,1,0,0,0,66,378,
        1,0,0,0,68,385,1,0,0,0,70,392,1,0,0,0,72,399,1,0,0,0,74,418,1,0,
        0,0,76,420,1,0,0,0,78,423,1,0,0,0,80,426,1,0,0,0,82,433,1,0,0,0,
        84,85,3,8,4,0,85,86,6,0,-1,0,86,1,1,0,0,0,87,88,3,52,26,0,88,89,
        6,1,-1,0,89,115,1,0,0,0,90,91,3,38,19,0,91,92,6,1,-1,0,92,115,1,
        0,0,0,93,94,3,58,29,0,94,95,6,1,-1,0,95,115,1,0,0,0,96,97,3,40,20,
        0,97,98,6,1,-1,0,98,115,1,0,0,0,99,100,3,42,21,0,100,101,6,1,-1,
        0,101,115,1,0,0,0,102,103,3,44,22,0,103,104,6,1,-1,0,104,115,1,0,
        0,0,105,106,3,46,23,0,106,107,6,1,-1,0,107,115,1,0,0,0,108,109,3,
        48,24,0,109,110,6,1,-1,0,110,115,1,0,0,0,111,112,3,50,25,0,112,113,
        6,1,-1,0,113,115,1,0,0,0,114,87,1,0,0,0,114,90,1,0,0,0,114,93,1,
        0,0,0,114,96,1,0,0,0,114,99,1,0,0,0,114,102,1,0,0,0,114,105,1,0,
        0,0,114,108,1,0,0,0,114,111,1,0,0,0,115,3,1,0,0,0,116,117,3,64,32,
        0,117,118,6,2,-1,0,118,132,1,0,0,0,119,120,3,66,33,0,120,121,6,2,
        -1,0,121,132,1,0,0,0,122,123,3,68,34,0,123,124,6,2,-1,0,124,132,
        1,0,0,0,125,126,3,70,35,0,126,127,6,2,-1,0,127,132,1,0,0,0,128,129,
        3,72,36,0,129,130,6,2,-1,0,130,132,1,0,0,0,131,116,1,0,0,0,131,119,
        1,0,0,0,131,122,1,0,0,0,131,125,1,0,0,0,131,128,1,0,0,0,132,5,1,
        0,0,0,133,134,3,12,6,0,134,135,6,3,-1,0,135,7,1,0,0,0,136,137,3,
        52,26,0,137,138,6,4,-1,0,138,188,1,0,0,0,139,140,3,54,27,0,140,141,
        6,4,-1,0,141,188,1,0,0,0,142,143,3,60,30,0,143,144,6,4,-1,0,144,
        188,1,0,0,0,145,146,3,62,31,0,146,147,6,4,-1,0,147,188,1,0,0,0,148,
        149,3,10,5,0,149,150,6,4,-1,0,150,188,1,0,0,0,151,152,3,14,7,0,152,
        153,6,4,-1,0,153,188,1,0,0,0,154,155,3,16,8,0,155,156,6,4,-1,0,156,
        188,1,0,0,0,157,158,3,18,9,0,158,159,6,4,-1,0,159,188,1,0,0,0,160,
        161,3,20,10,0,161,162,6,4,-1,0,162,188,1,0,0,0,163,164,3,22,11,0,
        164,165,6,4,-1,0,165,188,1,0,0,0,166,167,3,24,12,0,167,168,6,4,-1,
        0,168,188,1,0,0,0,169,170,3,26,13,0,170,171,6,4,-1,0,171,188,1,0,
        0,0,172,173,3,28,14,0,173,174,6,4,-1,0,174,188,1,0,0,0,175,176,3,
        30,15,0,176,177,6,4,-1,0,177,188,1,0,0,0,178,179,3,32,16,0,179,180,
        6,4,-1,0,180,188,1,0,0,0,181,182,3,34,17,0,182,183,6,4,-1,0,183,
        188,1,0,0,0,184,185,3,36,18,0,185,186,6,4,-1,0,186,188,1,0,0,0,187,
        136,1,0,0,0,187,139,1,0,0,0,187,142,1,0,0,0,187,145,1,0,0,0,187,
        148,1,0,0,0,187,151,1,0,0,0,187,154,1,0,0,0,187,157,1,0,0,0,187,
        160,1,0,0,0,187,163,1,0,0,0,187,166,1,0,0,0,187,169,1,0,0,0,187,
        172,1,0,0,0,187,175,1,0,0,0,187,178,1,0,0,0,187,181,1,0,0,0,187,
        184,1,0,0,0,188,9,1,0,0,0,189,190,5,30,0,0,190,191,3,12,6,0,191,
        192,6,5,-1,0,192,11,1,0,0,0,193,194,5,1,0,0,194,195,3,2,1,0,195,
        196,5,2,0,0,196,197,3,2,1,0,197,198,5,3,0,0,198,199,6,6,-1,0,199,
        13,1,0,0,0,200,201,5,31,0,0,201,202,3,12,6,0,202,203,6,7,-1,0,203,
        15,1,0,0,0,204,205,5,32,0,0,205,206,3,12,6,0,206,207,3,8,4,0,207,
        208,6,8,-1,0,208,17,1,0,0,0,209,210,5,33,0,0,210,211,3,2,1,0,211,
        212,3,8,4,0,212,213,6,9,-1,0,213,19,1,0,0,0,214,215,5,34,0,0,215,
        216,3,2,1,0,216,217,3,8,4,0,217,218,6,10,-1,0,218,21,1,0,0,0,219,
        220,5,35,0,0,220,221,3,2,1,0,221,222,3,8,4,0,222,223,6,11,-1,0,223,
        23,1,0,0,0,224,225,5,36,0,0,225,226,3,2,1,0,226,227,3,8,4,0,227,
        228,6,12,-1,0,228,25,1,0,0,0,229,230,5,37,0,0,230,231,3,2,1,0,231,
        232,6,13,-1,0,232,27,1,0,0,0,233,234,5,38,0,0,234,235,3,2,1,0,235,
        236,6,14,-1,0,236,29,1,0,0,0,237,238,5,39,0,0,238,239,3,2,1,0,239,
        240,6,15,-1,0,240,31,1,0,0,0,241,242,5,40,0,0,242,243,3,2,1,0,243,
        244,3,2,1,0,244,245,6,16,-1,0,245,33,1,0,0,0,246,247,5,41,0,0,247,
        248,3,2,1,0,248,249,3,2,1,0,249,250,6,17,-1,0,250,35,1,0,0,0,251,
        252,5,42,0,0,252,253,3,8,4,0,253,254,3,8,4,0,254,255,6,18,-1,0,255,
        37,1,0,0,0,256,257,5,44,0,0,257,271,6,19,-1,0,258,259,5,4,0,0,259,
        260,5,44,0,0,260,271,6,19,-1,0,261,262,5,44,0,0,262,263,5,43,0,0,
        263,264,5,44,0,0,264,271,6,19,-1,0,265,266,5,4,0,0,266,267,5,44,
        0,0,267,268,5,43,0,0,268,269,5,44,0,0,269,271,6,19,-1,0,270,256,
        1,0,0,0,270,258,1,0,0,0,270,261,1,0,0,0,270,265,1,0,0,0,271,39,1,
        0,0,0,272,273,5,1,0,0,273,274,5,5,0,0,274,275,3,8,4,0,275,276,3,
        8,4,0,276,277,5,3,0,0,277,278,6,20,-1,0,278,41,1,0,0,0,279,280,5,
        1,0,0,280,281,5,4,0,0,281,282,3,8,4,0,282,283,3,8,4,0,283,284,5,
        3,0,0,284,285,6,21,-1,0,285,43,1,0,0,0,286,287,5,1,0,0,287,288,5,
        6,0,0,288,289,3,8,4,0,289,290,3,8,4,0,290,291,5,3,0,0,291,292,6,
        22,-1,0,292,45,1,0,0,0,293,294,5,1,0,0,294,295,5,7,0,0,295,296,3,
        8,4,0,296,297,3,8,4,0,297,298,5,3,0,0,298,299,6,23,-1,0,299,47,1,
        0,0,0,300,301,5,1,0,0,301,302,5,8,0,0,302,303,3,8,4,0,303,304,3,
        8,4,0,304,305,5,3,0,0,305,306,6,24,-1,0,306,49,1,0,0,0,307,308,5,
        1,0,0,308,309,5,9,0,0,309,310,3,8,4,0,310,311,3,8,4,0,311,312,5,
        3,0,0,312,313,6,25,-1,0,313,51,1,0,0,0,314,315,5,45,0,0,315,316,
        6,26,-1,0,316,53,1,0,0,0,317,325,5,18,0,0,318,319,5,1,0,0,319,320,
        5,45,0,0,320,321,5,10,0,0,321,322,3,74,37,0,322,323,5,3,0,0,323,
        324,6,27,-1,0,324,326,1,0,0,0,325,318,1,0,0,0,326,327,1,0,0,0,327,
        325,1,0,0,0,327,328,1,0,0,0,328,329,1,0,0,0,329,330,3,8,4,0,330,
        331,5,19,0,0,331,332,3,8,4,0,332,333,6,27,-1,0,333,55,1,0,0,0,334,
        335,5,20,0,0,335,336,3,8,4,0,336,343,5,21,0,0,337,338,5,11,0,0,338,
        339,3,8,4,0,339,340,5,12,0,0,340,341,3,8,4,0,341,342,6,28,-1,0,342,
        344,1,0,0,0,343,337,1,0,0,0,344,345,1,0,0,0,345,343,1,0,0,0,345,
        346,1,0,0,0,346,347,1,0,0,0,347,348,6,28,-1,0,348,57,1,0,0,0,349,
        350,5,28,0,0,350,354,6,29,-1,0,351,352,5,29,0,0,352,354,6,29,-1,
        0,353,349,1,0,0,0,353,351,1,0,0,0,354,59,1,0,0,0,355,356,5,1,0,0,
        356,357,3,8,4,0,357,358,3,8,4,0,358,359,6,30,-1,0,359,360,1,0,0,
        0,360,361,5,3,0,0,361,362,6,30,-1,0,362,61,1,0,0,0,363,364,5,1,0,
        0,364,365,5,22,0,0,365,366,3,4,2,0,366,367,3,8,4,0,367,368,3,8,4,
        0,368,369,5,3,0,0,369,370,6,31,-1,0,370,63,1,0,0,0,371,372,5,1,0,
        0,372,373,5,25,0,0,373,374,3,8,4,0,374,375,3,8,4,0,375,376,5,3,0,
        0,376,377,6,32,-1,0,377,65,1,0,0,0,378,379,5,1,0,0,379,380,5,26,
        0,0,380,381,3,8,4,0,381,382,3,8,4,0,382,383,5,3,0,0,383,384,6,33,
        -1,0,384,67,1,0,0,0,385,386,5,1,0,0,386,387,5,27,0,0,387,388,3,8,
        4,0,388,389,3,8,4,0,389,390,5,3,0,0,390,391,6,34,-1,0,391,69,1,0,
        0,0,392,393,5,1,0,0,393,394,5,13,0,0,394,395,3,8,4,0,395,396,3,8,
        4,0,396,397,5,3,0,0,397,398,6,35,-1,0,398,71,1,0,0,0,399,400,5,1,
        0,0,400,401,5,14,0,0,401,402,3,8,4,0,402,403,3,8,4,0,403,404,5,3,
        0,0,404,405,6,36,-1,0,405,73,1,0,0,0,406,407,3,76,38,0,407,408,6,
        37,-1,0,408,419,1,0,0,0,409,410,3,82,41,0,410,411,6,37,-1,0,411,
        419,1,0,0,0,412,413,3,78,39,0,413,414,6,37,-1,0,414,419,1,0,0,0,
        415,416,3,80,40,0,416,417,6,37,-1,0,417,419,1,0,0,0,418,406,1,0,
        0,0,418,409,1,0,0,0,418,412,1,0,0,0,418,415,1,0,0,0,419,75,1,0,0,
        0,420,421,5,15,0,0,421,422,6,38,-1,0,422,77,1,0,0,0,423,424,5,16,
        0,0,424,425,6,39,-1,0,425,79,1,0,0,0,426,427,5,1,0,0,427,428,3,74,
        37,0,428,429,5,2,0,0,429,430,3,74,37,0,430,431,5,3,0,0,431,432,6,
        40,-1,0,432,81,1,0,0,0,433,439,5,1,0,0,434,435,3,74,37,0,435,436,
        6,41,-1,0,436,438,1,0,0,0,437,434,1,0,0,0,438,441,1,0,0,0,439,437,
        1,0,0,0,439,440,1,0,0,0,440,442,1,0,0,0,441,439,1,0,0,0,442,443,
        5,17,0,0,443,444,3,74,37,0,444,445,5,3,0,0,445,446,6,41,-1,0,446,
        83,1,0,0,0,9,114,131,187,270,327,345,353,418,439
    ]

class ExpParser ( Parser ):

    grammarFileName = "Exp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'-'", "'+'", "'*'", 
                     "'/'", "'%'", "'^'", "':'", "'|'", "'=>'", "'&&'", 
                     "'||'", "'bool'", "'num'", "'->'", "'let'", "'in'", 
                     "'match'", "'with'", "'if'", "'car'", "'cdr'", "'<'", 
                     "'='", "'>'", "'#t'", "'#f'", "'SKIP'", "'X'", "'CU'", 
                     "'RZ'", "'RRZ'", "'SR'", "'SRR'", "'Lshift'", "'Rshift'", 
                     "'Rev'", "'QFT'", "'RQFT'", "';'", "'.'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Let", "IN", "Match", "With", 
                      "If", "Car", "Cdr", "Less", "Equal", "Greater", "TrueLiteral", 
                      "FalseLiteral", "SKIPEXP", "Xgate", "CU", "RZ", "RRZ", 
                      "SR", "SRR", "Lshift", "Rshift", "Rev", "QFT", "RQFT", 
                      "Seq", "Dot", "Number", "Identifier", "Letter", "LetterOrDigit", 
                      "StrLiteral", "AT", "ELLIPSIS", "WS", "Comment", "Line_Comment" ]

    RULE_program = 0
    RULE_vexp = 1
    RULE_bexp = 2
    RULE_posi = 3
    RULE_exp = 4
    RULE_skipexp = 5
    RULE_posiexp = 6
    RULE_xgexp = 7
    RULE_cuexp = 8
    RULE_rzexp = 9
    RULE_rrzexp = 10
    RULE_srexp = 11
    RULE_srrexp = 12
    RULE_lshiftexp = 13
    RULE_rshiftexp = 14
    RULE_revexp = 15
    RULE_qftexp = 16
    RULE_rqftexp = 17
    RULE_seqexp = 18
    RULE_numexp = 19
    RULE_addexp = 20
    RULE_subexp = 21
    RULE_multexp = 22
    RULE_divexp = 23
    RULE_modexp = 24
    RULE_expexp = 25
    RULE_varexp = 26
    RULE_letexp = 27
    RULE_matchexp = 28
    RULE_boolexp = 29
    RULE_callexp = 30
    RULE_ifexp = 31
    RULE_lessexp = 32
    RULE_equalexp = 33
    RULE_greaterexp = 34
    RULE_andexp = 35
    RULE_orexp = 36
    RULE_typea = 37
    RULE_booleantype = 38
    RULE_numtype = 39
    RULE_pairtype = 40
    RULE_funct = 41

    ruleNames =  [ "program", "vexp", "bexp", "posi", "exp", "skipexp", 
                   "posiexp", "xgexp", "cuexp", "rzexp", "rrzexp", "srexp", 
                   "srrexp", "lshiftexp", "rshiftexp", "revexp", "qftexp", 
                   "rqftexp", "seqexp", "numexp", "addexp", "subexp", "multexp", 
                   "divexp", "modexp", "expexp", "varexp", "letexp", "matchexp", 
                   "boolexp", "callexp", "ifexp", "lessexp", "equalexp", 
                   "greaterexp", "andexp", "orexp", "typea", "booleantype", 
                   "numtype", "pairtype", "funct" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    Let=18
    IN=19
    Match=20
    With=21
    If=22
    Car=23
    Cdr=24
    Less=25
    Equal=26
    Greater=27
    TrueLiteral=28
    FalseLiteral=29
    SKIPEXP=30
    Xgate=31
    CU=32
    RZ=33
    RRZ=34
    SR=35
    SRR=36
    Lshift=37
    Rshift=38
    Rev=39
    QFT=40
    RQFT=41
    Seq=42
    Dot=43
    Number=44
    Identifier=45
    Letter=46
    LetterOrDigit=47
    StrLiteral=48
    AT=49
    ELLIPSIS=50
    WS=51
    Comment=52
    Line_Comment=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e = None # ExpContext

        def exp(self):
            return self.getTypedRuleContext(ExpParser.ExpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExpParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            localctx.e = self.exp()
            localctx.ast =  localctx.e.ast
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.va = None # VarexpContext
            self.num = None # NumexpContext
            self.bl = None # BoolexpContext
            self.add = None # AddexpContext
            self.sub = None # SubexpContext
            self.mul = None # MultexpContext
            self.div = None # DivexpContext
            self.mod = None # ModexpContext
            self.expa = None # ExpexpContext

        def varexp(self):
            return self.getTypedRuleContext(ExpParser.VarexpContext,0)


        def numexp(self):
            return self.getTypedRuleContext(ExpParser.NumexpContext,0)


        def boolexp(self):
            return self.getTypedRuleContext(ExpParser.BoolexpContext,0)


        def addexp(self):
            return self.getTypedRuleContext(ExpParser.AddexpContext,0)


        def subexp(self):
            return self.getTypedRuleContext(ExpParser.SubexpContext,0)


        def multexp(self):
            return self.getTypedRuleContext(ExpParser.MultexpContext,0)


        def divexp(self):
            return self.getTypedRuleContext(ExpParser.DivexpContext,0)


        def modexp(self):
            return self.getTypedRuleContext(ExpParser.ModexpContext,0)


        def expexp(self):
            return self.getTypedRuleContext(ExpParser.ExpexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_vexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVexp" ):
                listener.enterVexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVexp" ):
                listener.exitVexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVexp" ):
                return visitor.visitVexp(self)
            else:
                return visitor.visitChildren(self)




    def vexp(self):

        localctx = ExpParser.VexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vexp)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                localctx.va = self.varexp()
                localctx.ast =  localctx.va.ast
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                localctx.num = self.numexp()
                localctx.ast =  localctx.num.ast
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                localctx.bl = self.boolexp()
                localctx.ast =  localctx.bl.ast
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                localctx.add = self.addexp()
                localctx.ast =  localctx.add.ast
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                localctx.sub = self.subexp()
                localctx.ast =  localctx.sub.ast
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 102
                localctx.mul = self.multexp()
                localctx.ast =  localctx.mul.ast
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 105
                localctx.div = self.divexp()
                localctx.ast =  localctx.div.ast
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 108
                localctx.mod = self.modexp()
                localctx.ast =  localctx.mod.ast
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 111
                localctx.expa = self.expexp()
                localctx.ast =  localctx.expa.ast
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.less = None # LessexpContext
            self.eq = None # EqualexpContext
            self.gt = None # GreaterexpContext
            self.anda = None # AndexpContext
            self.ora = None # OrexpContext

        def lessexp(self):
            return self.getTypedRuleContext(ExpParser.LessexpContext,0)


        def equalexp(self):
            return self.getTypedRuleContext(ExpParser.EqualexpContext,0)


        def greaterexp(self):
            return self.getTypedRuleContext(ExpParser.GreaterexpContext,0)


        def andexp(self):
            return self.getTypedRuleContext(ExpParser.AndexpContext,0)


        def orexp(self):
            return self.getTypedRuleContext(ExpParser.OrexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_bexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBexp" ):
                listener.enterBexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBexp" ):
                listener.exitBexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBexp" ):
                return visitor.visitBexp(self)
            else:
                return visitor.visitChildren(self)




    def bexp(self):

        localctx = ExpParser.BexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bexp)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                localctx.less = self.lessexp()
                localctx.ast =  localctx.less.ast
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                localctx.eq = self.equalexp()
                localctx.ast =  localctx.eq.ast
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                localctx.gt = self.greaterexp()
                localctx.ast =  localctx.gt.ast
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                localctx.anda = self.andexp()
                localctx.ast =  localctx.anda.ast
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                localctx.ora = self.orexp()
                localctx.ast =  localctx.ora.ast
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PosiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.posii = None # PosiexpContext

        def posiexp(self):
            return self.getTypedRuleContext(ExpParser.PosiexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_posi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosi" ):
                listener.enterPosi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosi" ):
                listener.exitPosi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPosi" ):
                return visitor.visitPosi(self)
            else:
                return visitor.visitChildren(self)




    def posi(self):

        localctx = ExpParser.PosiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_posi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            localctx.posii = self.posiexp()
            localctx.ast =  localctx.posii.ast
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.vb = None # VarexpContext
            self.let = None # LetexpContext
            self.call = None # CallexpContext
            self.i = None # IfexpContext
            self.skipa = None # SkipexpContext
            self.xgate = None # XgexpContext
            self.cu = None # CuexpContext
            self.rz = None # RzexpContext
            self.rrz = None # RrzexpContext
            self.sr = None # SrexpContext
            self.srr = None # SrrexpContext
            self.lshift = None # LshiftexpContext
            self.rshift = None # RshiftexpContext
            self.rev = None # RevexpContext
            self.qft = None # QftexpContext
            self.rqft = None # RqftexpContext
            self.seq = None # SeqexpContext

        def varexp(self):
            return self.getTypedRuleContext(ExpParser.VarexpContext,0)


        def letexp(self):
            return self.getTypedRuleContext(ExpParser.LetexpContext,0)


        def callexp(self):
            return self.getTypedRuleContext(ExpParser.CallexpContext,0)


        def ifexp(self):
            return self.getTypedRuleContext(ExpParser.IfexpContext,0)


        def skipexp(self):
            return self.getTypedRuleContext(ExpParser.SkipexpContext,0)


        def xgexp(self):
            return self.getTypedRuleContext(ExpParser.XgexpContext,0)


        def cuexp(self):
            return self.getTypedRuleContext(ExpParser.CuexpContext,0)


        def rzexp(self):
            return self.getTypedRuleContext(ExpParser.RzexpContext,0)


        def rrzexp(self):
            return self.getTypedRuleContext(ExpParser.RrzexpContext,0)


        def srexp(self):
            return self.getTypedRuleContext(ExpParser.SrexpContext,0)


        def srrexp(self):
            return self.getTypedRuleContext(ExpParser.SrrexpContext,0)


        def lshiftexp(self):
            return self.getTypedRuleContext(ExpParser.LshiftexpContext,0)


        def rshiftexp(self):
            return self.getTypedRuleContext(ExpParser.RshiftexpContext,0)


        def revexp(self):
            return self.getTypedRuleContext(ExpParser.RevexpContext,0)


        def qftexp(self):
            return self.getTypedRuleContext(ExpParser.QftexpContext,0)


        def rqftexp(self):
            return self.getTypedRuleContext(ExpParser.RqftexpContext,0)


        def seqexp(self):
            return self.getTypedRuleContext(ExpParser.SeqexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ExpParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                localctx.vb = self.varexp()
                $ ast = localctx.vb.ast;
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                localctx.let = self.letexp()
                localctx.ast =  localctx.let.ast
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                localctx.call = self.callexp()
                localctx.ast =  localctx.call.ast
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 145
                localctx.i = self.ifexp()
                localctx.ast =  localctx.i.ast
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                localctx.skipa = self.skipexp()
                localctx.ast =  localctx.skipa.ast
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
                localctx.xgate = self.xgexp()
                localctx.ast =  localctx.xgate.ast
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 154
                localctx.cu = self.cuexp()
                localctx.ast =  cu.ast
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 157
                localctx.rz = self.rzexp()
                localctx.ast =  rz.ast
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 160
                localctx.rrz = self.rrzexp()
                localctx.ast =  rrz.ast
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 163
                localctx.sr = self.srexp()
                localctx.ast =  sr.ast
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 166
                localctx.srr = self.srrexp()
                localctx.ast =  srr.ast
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 169
                localctx.lshift = self.lshiftexp()
                localctx.ast =  lshift.ast
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 172
                localctx.rshift = self.rshiftexp()
                localctx.ast =  rshift.ast
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 175
                localctx.rev = self.revexp()
                localctx.ast =  rev.ast
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 178
                localctx.qft = self.qftexp()
                localctx.ast =  qft.ast
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 181
                localctx.rqft = self.rqftexp()
                localctx.ast =  rqft.ast
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 184
                localctx.seq = self.seqexp()
                localctx.ast =  seq.ast
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkipexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # PosiexpContext

        def SKIPEXP(self):
            return self.getToken(ExpParser.SKIPEXP, 0)

        def posiexp(self):
            return self.getTypedRuleContext(ExpParser.PosiexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_skipexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSkipexp" ):
                listener.enterSkipexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSkipexp" ):
                listener.exitSkipexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkipexp" ):
                return visitor.visitSkipexp(self)
            else:
                return visitor.visitChildren(self)




    def skipexp(self):

        localctx = ExpParser.SkipexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_skipexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(ExpParser.SKIPEXP)
            self.state = 190
            localctx.e1 = self.posiexp()
            localctx.ast =  new SkipExp(e1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PosiexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext
            self.e2 = None # VexpContext

        def vexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.VexpContext)
            else:
                return self.getTypedRuleContext(ExpParser.VexpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_posiexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosiexp" ):
                listener.enterPosiexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosiexp" ):
                listener.exitPosiexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPosiexp" ):
                return visitor.visitPosiexp(self)
            else:
                return visitor.visitChildren(self)




    def posiexp(self):

        localctx = ExpParser.PosiexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_posiexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(ExpParser.T__0)
            self.state = 194
            localctx.e1 = self.vexp()
            self.state = 195
            self.match(ExpParser.T__1)
            self.state = 196
            localctx.e2 = self.vexp()
            self.state = 197
            self.match(ExpParser.T__2)
            localctx.ast =  new PosiExp(localctx.e1.ast,localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class XgexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e = None # PosiexpContext

        def Xgate(self):
            return self.getToken(ExpParser.Xgate, 0)

        def posiexp(self):
            return self.getTypedRuleContext(ExpParser.PosiexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_xgexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXgexp" ):
                listener.enterXgexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXgexp" ):
                listener.exitXgexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXgexp" ):
                return visitor.visitXgexp(self)
            else:
                return visitor.visitChildren(self)




    def xgexp(self):

        localctx = ExpParser.XgexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_xgexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ExpParser.Xgate)
            self.state = 201
            localctx.e = self.posiexp()
            localctx.ast = new XExp(localctx.e.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # PosiexpContext
            self.e2 = None # ExpContext

        def CU(self):
            return self.getToken(ExpParser.CU, 0)

        def posiexp(self):
            return self.getTypedRuleContext(ExpParser.PosiexpContext,0)


        def exp(self):
            return self.getTypedRuleContext(ExpParser.ExpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_cuexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuexp" ):
                listener.enterCuexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuexp" ):
                listener.exitCuexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCuexp" ):
                return visitor.visitCuexp(self)
            else:
                return visitor.visitChildren(self)




    def cuexp(self):

        localctx = ExpParser.CuexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cuexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ExpParser.CU)
            self.state = 205
            localctx.e1 = self.posiexp()
            self.state = 206
            localctx.e2 = self.exp()
            localctx.ast = new CUExp(localctx.e1.ast, localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RzexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext
            self.e2 = None # ExpContext

        def RZ(self):
            return self.getToken(ExpParser.RZ, 0)

        def vexp(self):
            return self.getTypedRuleContext(ExpParser.VexpContext,0)


        def exp(self):
            return self.getTypedRuleContext(ExpParser.ExpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_rzexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRzexp" ):
                listener.enterRzexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRzexp" ):
                listener.exitRzexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRzexp" ):
                return visitor.visitRzexp(self)
            else:
                return visitor.visitChildren(self)




    def rzexp(self):

        localctx = ExpParser.RzexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_rzexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(ExpParser.RZ)
            self.state = 210
            localctx.e1 = self.vexp()
            self.state = 211
            localctx.e2 = self.exp()
            localctx.ast = new RZExp(localctx.e1.ast, localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RrzexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext
            self.e2 = None # ExpContext

        def RRZ(self):
            return self.getToken(ExpParser.RRZ, 0)

        def vexp(self):
            return self.getTypedRuleContext(ExpParser.VexpContext,0)


        def exp(self):
            return self.getTypedRuleContext(ExpParser.ExpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_rrzexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRrzexp" ):
                listener.enterRrzexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRrzexp" ):
                listener.exitRrzexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRrzexp" ):
                return visitor.visitRrzexp(self)
            else:
                return visitor.visitChildren(self)




    def rrzexp(self):

        localctx = ExpParser.RrzexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_rrzexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ExpParser.RRZ)
            self.state = 215
            localctx.e1 = self.vexp()
            self.state = 216
            localctx.e2 = self.exp()
            localctx.ast = new RRZExp(localctx.e1.ast, localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SrexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext
            self.e2 = None # ExpContext

        def SR(self):
            return self.getToken(ExpParser.SR, 0)

        def vexp(self):
            return self.getTypedRuleContext(ExpParser.VexpContext,0)


        def exp(self):
            return self.getTypedRuleContext(ExpParser.ExpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_srexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSrexp" ):
                listener.enterSrexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSrexp" ):
                listener.exitSrexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSrexp" ):
                return visitor.visitSrexp(self)
            else:
                return visitor.visitChildren(self)

    def srexp(self):

        localctx = ExpParser.SrexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_srexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(ExpParser.SR)
            self.state = 220
            localctx.e1 = self.vexp()
            self.state = 221
            localctx.e2 = self.exp()
            localctx.ast = new SRExp(localctx.e1.ast, localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SrrexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext
            self.e2 = None # ExpContext

        def SRR(self):
            return self.getToken(ExpParser.SRR, 0)

        def vexp(self):
            return self.getTypedRuleContext(ExpParser.VexpContext,0)


        def exp(self):
            return self.getTypedRuleContext(ExpParser.ExpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_srrexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSrrexp" ):
                listener.enterSrrexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSrrexp" ):
                listener.exitSrrexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSrrexp" ):
                return visitor.visitSrrexp(self)
            else:
                return visitor.visitChildren(self)




    def srrexp(self):

        localctx = ExpParser.SrrexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_srrexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ExpParser.SRR)
            self.state = 225
            localctx.e1 = self.vexp()
            self.state = 226
            localctx.e2 = self.exp()
            localctx.ast = new SRRExp(localctx.e1.ast, localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LshiftexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext

        def Lshift(self):
            return self.getToken(ExpParser.Lshift, 0)

        def vexp(self):
            return self.getTypedRuleContext(ExpParser.VexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_lshiftexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLshiftexp" ):
                listener.enterLshiftexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLshiftexp" ):
                listener.exitLshiftexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLshiftexp" ):
                return visitor.visitLshiftexp(self)
            else:
                return visitor.visitChildren(self)




    def lshiftexp(self):

        localctx = ExpParser.LshiftexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lshiftexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ExpParser.Lshift)
            self.state = 230
            localctx.e1 = self.vexp()
            localctx.ast = new LshExp(localctx.e1.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RshiftexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext

        def Rshift(self):
            return self.getToken(ExpParser.Rshift, 0)

        def vexp(self):
            return self.getTypedRuleContext(ExpParser.VexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_rshiftexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRshiftexp" ):
                listener.enterRshiftexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRshiftexp" ):
                listener.exitRshiftexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRshiftexp" ):
                return visitor.visitRshiftexp(self)
            else:
                return visitor.visitChildren(self)




    def rshiftexp(self):

        localctx = ExpParser.RshiftexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_rshiftexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ExpParser.Rshift)
            self.state = 234
            localctx.e1 = self.vexp()
            localctx.ast = new RshExp(localctx.e1.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RevexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext

        def Rev(self):
            return self.getToken(ExpParser.Rev, 0)

        def vexp(self):
            return self.getTypedRuleContext(ExpParser.VexpContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_revexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRevexp" ):
                listener.enterRevexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRevexp" ):
                listener.exitRevexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRevexp" ):
                return visitor.visitRevexp(self)
            else:
                return visitor.visitChildren(self)




    def revexp(self):

        localctx = ExpParser.RevexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_revexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(ExpParser.Rev)
            self.state = 238
            localctx.e1 = self.vexp()
            localctx.ast = new RevExp(localctx.e1.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QftexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext
            self.e2 = None # VexpContext

        def QFT(self):
            return self.getToken(ExpParser.QFT, 0)

        def vexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.VexpContext)
            else:
                return self.getTypedRuleContext(ExpParser.VexpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_qftexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQftexp" ):
                listener.enterQftexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQftexp" ):
                listener.exitQftexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQftexp" ):
                return visitor.visitQftexp(self)
            else:
                return visitor.visitChildren(self)




    def qftexp(self):

        localctx = ExpParser.QftexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_qftexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ExpParser.QFT)
            self.state = 242
            localctx.e1 = self.vexp()
            self.state = 243
            localctx.e2 = self.vexp()
            localctx.ast = new QFTExp(localctx.e1.ast, localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RqftexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # VexpContext
            self.e2 = None # VexpContext

        def RQFT(self):
            return self.getToken(ExpParser.RQFT, 0)

        def vexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.VexpContext)
            else:
                return self.getTypedRuleContext(ExpParser.VexpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_rqftexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRqftexp" ):
                listener.enterRqftexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRqftexp" ):
                listener.exitRqftexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRqftexp" ):
                return visitor.visitRqftexp(self)
            else:
                return visitor.visitChildren(self)




    def rqftexp(self):

        localctx = ExpParser.RqftexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_rqftexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ExpParser.RQFT)
            self.state = 247
            localctx.e1 = self.vexp()
            self.state = 248
            localctx.e2 = self.vexp()
            localctx.ast = new RQFTExp(localctx.e1.ast, localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeqexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def Seq(self):
            return self.getToken(ExpParser.Seq, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_seqexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeqexp" ):
                listener.enterSeqexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeqexp" ):
                listener.exitSeqexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeqexp" ):
                return visitor.visitSeqexp(self)
            else:
                return visitor.visitChildren(self)




    def seqexp(self):

        localctx = ExpParser.SeqexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_seqexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(ExpParser.Seq)
            self.state = 252
            localctx.e1 = self.exp()
            self.state = 253
            localctx.e2 = self.exp()
            localctx.ast = new SeqExp(localctx.e1.ast, localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.n0 = None # Token
            self.n1 = None # Token

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.Number)
            else:
                return self.getToken(ExpParser.Number, i)

        def Dot(self):
            return self.getToken(ExpParser.Dot, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_numexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumexp" ):
                listener.enterNumexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumexp" ):
                listener.exitNumexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumexp" ):
                return visitor.visitNumexp(self)
            else:
                return visitor.visitChildren(self)




    def numexp(self):

        localctx = ExpParser.NumexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_numexp)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                localctx.n0 = self.match(ExpParser.Number)
                localctx.ast =  new NumExp(Integer.parseInt((None if localctx.n0 is None else localctx.n0.text)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.match(ExpParser.T__3)
                self.state = 259
                localctx.n0 = self.match(ExpParser.Number)
                localctx.ast =  new NumExp(-Integer.parseInt((None if localctx.n0 is None else localctx.n0.text)))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                localctx.n0 = self.match(ExpParser.Number)
                self.state = 262
                self.match(ExpParser.Dot)
                self.state = 263
                localctx.n1 = self.match(ExpParser.Number)
                localctx.ast =  new NumExp(Double.parseDouble((None if localctx.n0 is None else localctx.n0.text)+"."+(None if localctx.n1 is None else localctx.n1.text)))
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.match(ExpParser.T__3)
                self.state = 266
                localctx.n0 = self.match(ExpParser.Number)
                self.state = 267
                self.match(ExpParser.Dot)
                self.state = 268
                localctx.n1 = self.match(ExpParser.Number)
                localctx.ast =  new NumExp(Double.parseDouble("-" + (None if localctx.n0 is None else localctx.n0.text)+"."+(None if localctx.n1 is None else localctx.n1.text)))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_addexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddexp" ):
                listener.enterAddexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddexp" ):
                listener.exitAddexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddexp" ):
                return visitor.visitAddexp(self)
            else:
                return visitor.visitChildren(self)




    def addexp(self):

        localctx = ExpParser.AddexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_addexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ExpParser.T__0)
            self.state = 273
            self.match(ExpParser.T__4)
            self.state = 274
            localctx.e1 = self.exp()
            self.state = 275
            localctx.e2 = self.exp()
            self.state = 276
            self.match(ExpParser.T__2)
            localctx.ast =  new AddExp(localctx.e1.ast,localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_subexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubexp" ):
                listener.enterSubexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubexp" ):
                listener.exitSubexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexp" ):
                return visitor.visitSubexp(self)
            else:
                return visitor.visitChildren(self)




    def subexp(self):

        localctx = ExpParser.SubexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(ExpParser.T__0)
            self.state = 280
            self.match(ExpParser.T__3)
            self.state = 281
            localctx.e1 = self.exp()
            self.state = 282
            localctx.e2 = self.exp()
            self.state = 283
            self.match(ExpParser.T__2)
            localctx.ast =  new SubExp(localctx.e1.ast,localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_multexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultexp" ):
                listener.enterMultexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultexp" ):
                listener.exitMultexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultexp" ):
                return visitor.visitMultexp(self)
            else:
                return visitor.visitChildren(self)




    def multexp(self):

        localctx = ExpParser.MultexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ExpParser.T__0)
            self.state = 287
            self.match(ExpParser.T__5)
            self.state = 288
            localctx.e1 = self.exp()
            self.state = 289
            localctx.e2 = self.exp()
            self.state = 290
            self.match(ExpParser.T__2)
            localctx.ast =  new MultExp(localctx.e1.ast,localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DivexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_divexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivexp" ):
                listener.enterDivexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivexp" ):
                listener.exitDivexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivexp" ):
                return visitor.visitDivexp(self)
            else:
                return visitor.visitChildren(self)




    def divexp(self):

        localctx = ExpParser.DivexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_divexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ExpParser.T__0)
            self.state = 294
            self.match(ExpParser.T__6)
            self.state = 295
            localctx.e1 = self.exp()
            self.state = 296
            localctx.e2 = self.exp()
            self.state = 297
            self.match(ExpParser.T__2)
            localctx.ast =  new DivExp(localctx.e1.ast,localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_modexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModexp" ):
                listener.enterModexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModexp" ):
                listener.exitModexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModexp" ):
                return visitor.visitModexp(self)
            else:
                return visitor.visitChildren(self)




    def modexp(self):

        localctx = ExpParser.ModexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_modexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ExpParser.T__0)
            self.state = 301
            self.match(ExpParser.T__7)
            self.state = 302
            localctx.e1 = self.exp()
            self.state = 303
            localctx.e2 = self.exp()
            self.state = 304
            self.match(ExpParser.T__2)
            localctx.ast =  new ModExp(localctx.e1.ast,localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_expexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpexp" ):
                listener.enterExpexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpexp" ):
                listener.exitExpexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpexp" ):
                return visitor.visitExpexp(self)
            else:
                return visitor.visitChildren(self)




    def expexp(self):

        localctx = ExpParser.ExpexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(ExpParser.T__0)
            self.state = 308
            self.match(ExpParser.T__8)
            self.state = 309
            localctx.e1 = self.exp()
            self.state = 310
            localctx.e2 = self.exp()
            self.state = 311
            self.match(ExpParser.T__2)
            localctx.ast =  new ExpExp(localctx.e1.ast,localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.ida = None # Token

        def Identifier(self):
            return self.getToken(ExpParser.Identifier, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_varexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarexp" ):
                listener.enterVarexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarexp" ):
                listener.exitVarexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarexp" ):
                return visitor.visitVarexp(self)
            else:
                return visitor.visitChildren(self)




    def varexp(self):

        localctx = ExpParser.VarexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_varexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            localctx.ida = self.match(ExpParser.Identifier)
            localctx.ast =  new VarExp((None if localctx.ida is None else localctx.ida.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.names = None
            self.types = None
            self.ida = None # Token
            self.t = None # TypeaContext
            self.e = None # ExpContext
            self.body = None # ExpContext

        def Let(self):
            return self.getToken(ExpParser.Let, 0)

        def IN(self):
            return self.getToken(ExpParser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.Identifier)
            else:
                return self.getToken(ExpParser.Identifier, i)

        def typea(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.TypeaContext)
            else:
                return self.getTypedRuleContext(ExpParser.TypeaContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_letexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetexp" ):
                listener.enterLetexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetexp" ):
                listener.exitLetexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetexp" ):
                return visitor.visitLetexp(self)
            else:
                return visitor.visitChildren(self)




    def letexp(self):

        localctx = ExpParser.LetexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_letexp)
        localctx.names =  new ArrayList<String>() localctx.types = new ArrayList<Type>()
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(ExpParser.Let)
            self.state = 325 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 318
                    self.match(ExpParser.T__0)
                    self.state = 319
                    localctx.ida = self.match(ExpParser.Identifier)
                    self.state = 320
                    self.match(ExpParser.T__9)
                    self.state = 321
                    localctx.t = self.typea()
                    self.state = 322
                    self.match(ExpParser.T__2)
                    localctx.names.add((None if localctx.ida is None else localctx.ida.text));localctx.types.add(localctx.t.ast);

                else:
                    raise NoViableAltException(self)
                self.state = 327 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 329
            localctx.e = self.exp()
            self.state = 330
            self.match(ExpParser.IN)
            self.state = 331
            localctx.body = self.exp()
            localctx.ast =  new LetExp(localctx.names, localctx.types, localctx.e.ast, localctx.body.ast)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.value_exps = None
            self.e = None # ExpContext
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def Match(self):
            return self.getToken(ExpParser.Match, 0)

        def With(self):
            return self.getToken(ExpParser.With, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_matchexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchexp" ):
                listener.enterMatchexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchexp" ):
                listener.exitMatchexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchexp" ):
                return visitor.visitMatchexp(self)
            else:
                return visitor.visitChildren(self)




    def matchexp(self):

        localctx = ExpParser.MatchexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_matchexp)
        localctx.value_exps =  new ArrayList<Pair<Exp,Exp>>()
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(ExpParser.Match)
            self.state = 335
            localctx.e = self.exp()
            self.state = 336
            self.match(ExpParser.With)
            self.state = 343 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 337
                self.match(ExpParser.T__10)
                self.state = 338
                localctx.e1 = self.exp()
                self.state = 339
                self.match(ExpParser.T__11)
                self.state = 340
                localctx.e2 = self.exp()
                Pair<Exp,Exp> tmp = new Pair<Exp,Exp>(localctx.e1.ast,localctx.e2.ast); localctx.value_exps.add(tmp);
                self.state = 345 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11):
                    break

             localctx.ast =  new MatchExp(localctx.e.ast, localctx.value_exps) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None

        def TrueLiteral(self):
            return self.getToken(ExpParser.TrueLiteral, 0)

        def FalseLiteral(self):
            return self.getToken(ExpParser.FalseLiteral, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_boolexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolexp" ):
                listener.enterBoolexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolexp" ):
                listener.exitBoolexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolexp" ):
                return visitor.visitBoolexp(self)
            else:
                return visitor.visitChildren(self)




    def boolexp(self):

        localctx = ExpParser.BoolexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_boolexp)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(ExpParser.TrueLiteral)
                localctx.ast =  new BoolExp(true)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(ExpParser.FalseLiteral)
                localctx.ast =  new BoolExp(false)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.arguments = new ArrayList<Exp>();
            self.f = None # ExpContext
            self.e = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_callexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallexp" ):
                listener.enterCallexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallexp" ):
                listener.exitCallexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallexp" ):
                return visitor.visitCallexp(self)
            else:
                return visitor.visitChildren(self)




    def callexp(self):

        localctx = ExpParser.CallexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_callexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(ExpParser.T__0)
            self.state = 356
            localctx.f = self.exp()

            self.state = 357
            localctx.e = self.exp()
            localctx.arguments.add(localctx.e.ast);
            self.state = 360
            self.match(ExpParser.T__2)
            localctx.ast =  new CallExp(localctx.f.ast,localctx.arguments)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # BexpContext
            self.e2 = None # ExpContext
            self.e3 = None # ExpContext

        def If(self):
            return self.getToken(ExpParser.If, 0)

        def bexp(self):
            return self.getTypedRuleContext(ExpParser.BexpContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_ifexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfexp" ):
                listener.enterIfexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfexp" ):
                listener.exitIfexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfexp" ):
                return visitor.visitIfexp(self)
            else:
                return visitor.visitChildren(self)




    def ifexp(self):

        localctx = ExpParser.IfexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ifexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(ExpParser.T__0)
            self.state = 364
            self.match(ExpParser.If)
            self.state = 365
            localctx.e1 = self.bexp()
            self.state = 366
            localctx.e2 = self.exp()
            self.state = 367
            localctx.e3 = self.exp()
            self.state = 368
            self.match(ExpParser.T__2)
            localctx.ast =  new IfExp(localctx.e1.ast,localctx.e2.ast,localctx.e3.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LessexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def Less(self):
            return self.getToken(ExpParser.Less, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_lessexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessexp" ):
                listener.enterLessexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessexp" ):
                listener.exitLessexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessexp" ):
                return visitor.visitLessexp(self)
            else:
                return visitor.visitChildren(self)




    def lessexp(self):

        localctx = ExpParser.LessexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_lessexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(ExpParser.T__0)
            self.state = 372
            self.match(ExpParser.Less)
            self.state = 373
            localctx.e1 = self.exp()
            self.state = 374
            localctx.e2 = self.exp()
            self.state = 375
            self.match(ExpParser.T__2)
            localctx.ast =  new LessExp(localctx.e1.ast,localctx.e2.ast)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def Equal(self):
            return self.getToken(ExpParser.Equal, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_equalexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualexp" ):
                listener.enterEqualexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualexp" ):
                listener.exitEqualexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualexp" ):
                return visitor.visitEqualexp(self)
            else:
                return visitor.visitChildren(self)




    def equalexp(self):

        localctx = ExpParser.EqualexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_equalexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(ExpParser.T__0)
            self.state = 379
            self.match(ExpParser.Equal)
            self.state = 380
            localctx.e1 = self.exp()
            self.state = 381
            localctx.e2 = self.exp()
            self.state = 382
            self.match(ExpParser.T__2)
             localctx.ast =  new EqualExp(localctx.e1.ast,localctx.e2.ast) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GreaterexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def Greater(self):
            return self.getToken(ExpParser.Greater, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_greaterexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterexp" ):
                listener.enterGreaterexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterexp" ):
                listener.exitGreaterexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterexp" ):
                return visitor.visitGreaterexp(self)
            else:
                return visitor.visitChildren(self)




    def greaterexp(self):

        localctx = ExpParser.GreaterexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_greaterexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(ExpParser.T__0)
            self.state = 386
            self.match(ExpParser.Greater)
            self.state = 387
            localctx.e1 = self.exp()
            self.state = 388
            localctx.e2 = self.exp()
            self.state = 389
            self.match(ExpParser.T__2)
             localctx.ast =  new GreaterExp(localctx.e1.ast,localctx.e2.ast) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_andexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndexp" ):
                listener.enterAndexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndexp" ):
                listener.exitAndexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndexp" ):
                return visitor.visitAndexp(self)
            else:
                return visitor.visitChildren(self)




    def andexp(self):

        localctx = ExpParser.AndexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_andexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(ExpParser.T__0)
            self.state = 393
            self.match(ExpParser.T__12)
            self.state = 394
            localctx.e1 = self.exp()
            self.state = 395
            localctx.e2 = self.exp()
            self.state = 396
            self.match(ExpParser.T__2)
             localctx.ast =  new LessExp(localctx.e1.ast,localctx.e2.ast) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e1 = None # ExpContext
            self.e2 = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_orexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrexp" ):
                listener.enterOrexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrexp" ):
                listener.exitOrexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrexp" ):
                return visitor.visitOrexp(self)
            else:
                return visitor.visitChildren(self)




    def orexp(self):

        localctx = ExpParser.OrexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_orexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(ExpParser.T__0)
            self.state = 400
            self.match(ExpParser.T__13)
            self.state = 401
            localctx.e1 = self.exp()
            self.state = 402
            localctx.e2 = self.exp()
            self.state = 403
            self.match(ExpParser.T__2)
             localctx.ast =  new EqualExp(localctx.e1.ast,localctx.e2.ast) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.b = None # BooleantypeContext
            self.f = None # FunctContext
            self.n = None # NumtypeContext
            self.p = None # PairtypeContext

        def booleantype(self):
            return self.getTypedRuleContext(ExpParser.BooleantypeContext,0)


        def funct(self):
            return self.getTypedRuleContext(ExpParser.FunctContext,0)


        def numtype(self):
            return self.getTypedRuleContext(ExpParser.NumtypeContext,0)


        def pairtype(self):
            return self.getTypedRuleContext(ExpParser.PairtypeContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_typea

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypea" ):
                listener.enterTypea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypea" ):
                listener.exitTypea(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypea" ):
                return visitor.visitTypea(self)
            else:
                return visitor.visitChildren(self)




    def typea(self):

        localctx = ExpParser.TypeaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_typea)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                localctx.b = self.booleantype()
                 localctx.ast =  localctx.b.ast 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                localctx.f = self.funct()
                 localctx.ast =  localctx.f.ast 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 412
                localctx.n = self.numtype()
                 localctx.ast =  localctx.n.ast 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                localctx.p = self.pairtype()
                 localctx.ast =  localctx.p.ast 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleantypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None


        def getRuleIndex(self):
            return ExpParser.RULE_booleantype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleantype" ):
                listener.enterBooleantype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleantype" ):
                listener.exitBooleantype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleantype" ):
                return visitor.visitBooleantype(self)
            else:
                return visitor.visitChildren(self)




    def booleantype(self):

        localctx = ExpParser.BooleantypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_booleantype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(ExpParser.T__14)
             localctx.ast =  new BoolT() 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None


        def getRuleIndex(self):
            return ExpParser.RULE_numtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumtype" ):
                listener.enterNumtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumtype" ):
                listener.exitNumtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumtype" ):
                return visitor.visitNumtype(self)
            else:
                return visitor.visitChildren(self)




    def numtype(self):

        localctx = ExpParser.NumtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_numtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(ExpParser.T__15)
             localctx.ast =  new NumT() 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.fst = None # TypeaContext
            self.snd = None # TypeaContext

        def typea(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.TypeaContext)
            else:
                return self.getTypedRuleContext(ExpParser.TypeaContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_pairtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPairtype" ):
                listener.enterPairtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPairtype" ):
                listener.exitPairtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPairtype" ):
                return visitor.visitPairtype(self)
            else:
                return visitor.visitChildren(self)




    def pairtype(self):

        localctx = ExpParser.PairtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_pairtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(ExpParser.T__0)
            self.state = 427
            localctx.fst = self.typea()
            self.state = 428
            self.match(ExpParser.T__1)
            self.state = 429
            localctx.snd = self.typea()
            self.state = 430
            self.match(ExpParser.T__2)
             localctx.ast =  new PairT(localctx.fst.ast, localctx.snd.ast) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.formals = None
            self.e = None # TypeaContext
            self.ret = None # TypeaContext

        def typea(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.TypeaContext)
            else:
                return self.getTypedRuleContext(ExpParser.TypeaContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_funct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct" ):
                listener.enterFunct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct" ):
                listener.exitFunct(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunct" ):
                return visitor.visitFunct(self)
            else:
                return visitor.visitChildren(self)




    def funct(self):

        localctx = ExpParser.FunctContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_funct)
         localctx.formals =  new ArrayList<Type>() 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(ExpParser.T__0)
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 98306) != 0):
                self.state = 434
                localctx.e = self.typea()
                 localctx.formals.add(localctx.e.ast);
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 442
            self.match(ExpParser.T__16)
            self.state = 443
            localctx.ret = self.typea()
            self.state = 444
            self.match(ExpParser.T__2)
             localctx.ast =  new FuncT(localctx.formals, localctx.ret.ast) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





