'''
Created on May 6, 2011

@author: ppa
'''
import traceback

class Errors(object):
    """ class hosts error code constants """
    # general errors
    UNKNOWN_ERROR = 1
    FILE_NOT_EXIST = 2
    FILE_EXIST = 3
    UNDEFINED_METHOD = 4

    NETWORK_ERROR = 100
    NETWORK_400_ERROR = 101

    INDEX_RANGE_ERROR = 200
    INVALID_DAM_NAME = 201

    STOCK_SYMBOL_ERROR = 300
    STOCK_PARSING_ERROR = 301

    HBASE_CREATE_ERROR=401
    HBASE_UPDATE_ERROR=402

    #type eroor
    SIDE_TYPE_ERROR=500
    ORDER_TYPE_ERROR=501
    TRANSITION_TYPE_ERROR=502

    #tickFeeder
    FEEDER_INVALID_ERROR = 600
    SYMBOL_EXIST = 601
    INVALID_TYPE = 602
    SYMBOL_NOT_IN_SOURCE = 604

    #account error
    ORDER_INVALID_ERROR = 700

    #excelLib error
    SHEET_NAME_EXIST = 800
    SHEET_NAME_INVALID = 801
    INVALID_EXCEL_MODE = 802

    #trading error
    INVALID_ACCOUNT = 901

    #metric
    INVALID_METRIC_NAME = 1001

    #strategy
    INVALID_STRATEGY_NAME = 1200
    NONE_ACCOUNT_ID = 1201

class UfException(Exception):
    """ Ultra-Finance exception """
    def __init__(self, error, errorMsg):
        """ constructor  """
        Exception.__init__(self)
        self.__error = error
        self.__errorMsg = errorMsg

    def __str__(self):
        """ string """
        return repr(self.__errorMsg)

    def getCode(self):
        """ accessor """
        return self.__error

    def getMsg(self):
        """ accessor """
        return "%s: %s" % (self.__errorMsg, traceback.format_exc(5))