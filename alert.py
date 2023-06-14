# #declare figure
# fig = go.Figure()

# #Candlestick
# fig.add_trace(go.Candlestick(x=data.index,
#                 open=data['Open'],
#                 high=data['High'],
#                 low=data['Low'],
#                 close=data['Close'], name = 'market data'))

# # Add titles
# fig.update_layout(
#     title='Uber live share price evolution',
#     yaxis_title='Stock Price (USD per Shares)')

# # X-Axes
# fig.update_xaxes(
#     rangeslider_visible=True,
#     rangeselector=dict(
#         buttons=list([
#             dict(count=15, label="15m", step="minute", stepmode="backward"),
#             dict(count=45, label="45m", step="minute", stepmode="backward"),
#             dict(count=1, label="HTD", step="hour", stepmode="todate"),
#             dict(count=3, label="3h", step="hour", stepmode="backward"),
#             dict(step="all")
#         ])
#     )
# )
# import plotly.graph_objs as go

from yfinance import download
from pandas_ta import rsi
data = download(tickers='^NSEI', period='30d', interval='1h')
rsia = rsi(data.Close,14)
print(rsia.tail())