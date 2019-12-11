### Back Tests with Zipline in Ipython Environment

```
pip install virtualenv
```
install virtual environment and then you build python version 3.5 in your python

```
conda create -n quant python=3.5
```

```
# C:/User/XXX/Anaconda3/envs/quant/Scripts
source activate quant
```

```
conda install -c Quantopian zipline

pip install jupyter
```
Default jupyter notebook using bash enviroment , if you forget install jupyter ... 

Because zipline default benchmark Api not found , so must be change code 

in benchmark.py you must change like that
```
import numpy as np
import pandas as pd
import pandas_datareader.data as pd_reader

def get_benchmark_returns(symbol, first_date, last_date):
    """
    Get a Series of benchmark returns from Yahoo associated with `symbol`.
    Default is `SPY`.

    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.

    The data is provided by Yahoo Finance
    """
    data = pd_reader.DataReader(
        symbol,
        'yahoo',
        first_date,
        last_date
    )

    data = data['Close']

    data[pd.Timestamp('2008-12-15')] = np.nan
    data[pd.Timestamp('2009-08-11')] = np.nan
    data[pd.Timestamp('2012-02-02')] = np.nan

    data = data.fillna(method='ffill')

    return data.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
```

Then in loaders.py, replacedata = get_benchmark_returns(symbol) withdata = get_benchmark_returns(symbol, first_date, last_date)

In this example NYSE is used, but it also works when I use AlwaysOpenCalendar in my backtest, so I did not try to change it to some other calendar.

This is only a hack. In the long run I would suggest to change the benchmark downloading method to request other API in case you would like to use benchmarks in the future.
