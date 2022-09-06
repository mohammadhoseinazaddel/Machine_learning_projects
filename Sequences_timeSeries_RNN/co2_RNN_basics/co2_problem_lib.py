from matplotlib import pylab as plt
import matplotlib.dates as mdates
from sklearn.metrics import mean_squared_error
from co2_data import co2_by_month, co2_dates, NUMBER_FORECAST_STEPS, co2_by_month_test_data

co2_loc = mdates.YearLocator(3)
co2_fmt = mdates.DateFormatter('%Y')


def calculate_rmse(y_pred):
    assert y_pred.shape == (120,)
    return mean_squared_error(y_true=co2_by_month_test_data, y_pred=y_pred, squared=False)


def plot_forecast(forecast=None, return_plot=False):
    """Plot a forecast against the 'true' time series."""

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(co2_dates[:-NUMBER_FORECAST_STEPS], co2_by_month[:-NUMBER_FORECAST_STEPS], lw=2,
            label="training data")
    ax.plot(co2_dates[-NUMBER_FORECAST_STEPS:], co2_by_month[-NUMBER_FORECAST_STEPS:], ls='--',
            c='b', lw=2, label="validation data")
    if forecast is not None:
        assert len(forecast) == NUMBER_FORECAST_STEPS
        ax.plot(co2_dates[-NUMBER_FORECAST_STEPS:], forecast, c='g', lw=2, label="forecasted data")
        err = calculate_rmse(forecast)
        print(f'Root Mean Squared Error: {err:0.3f}')
    ax.xaxis.set_major_locator(co2_loc)
    ax.xaxis.set_major_formatter(co2_fmt)
    ax.set_ylabel("Atmospheric CO2 concentration (ppm)")
    ax.set_xlabel("Year")
    fig.suptitle("Monthly average CO2 concentration, Mauna Loa, Hawaii", fontsize=15)
    fig.autofmt_xdate()
    ax.axvline(co2_dates[-NUMBER_FORECAST_STEPS], linestyle="--")
    ax.legend(loc="upper left")
    ax.set_ylabel("Atmospheric CO2 concentration (ppm)")
    ax.set_xlabel("Year")
    fig.autofmt_xdate()
    if return_plot:
        return fig, ax
