import talib
import numpy as np
import pandas as pd
from finlab_crypto.strategy import Strategy

@Strategy(timeperiod=14)
def rsi_strategy(ohlcv, combination=False):
  if combination:
    pass

    windows = sorted(list(set(list(rsi_strategy.timeperiod))))
    rsis = {}
    for t in rsi_strategy.timeperiod:
      rsi = talib.RSI(ohlcv.close, timeperiod=t)
      rsis[t] = (rsi)
    rsi = pd.concat(rsis, axis=1)
  else:
    rsi = talib.RSI(ohlcv.close, timeperiod=rsi_strategy.timeperiod)

  entries = rsi > 52
  exits = (rsi < 50)

  figure = {
    'figures': {
        str(rsi_strategy.timeperiod) + '_rsi': rsi
    }
  }

  return entries, exits, figure