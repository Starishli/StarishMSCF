import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from source import DATA_DIR


vix_data = pd.read_csv(os.path.join(DATA_DIR, "vixcurrent.csv"), index_col="Date", parse_dates=["Date"])
print(vix_data.loc["2004-01-07", "VIX Low"])

# t_rate_data = pd.read_csv(os.path.join(DATA_DIR, "DGS1.csv"), index_col="DATE", parse_dates=["DATE"])
#
# to_plot_data = pd.concat([vix_data["VIX Close"], t_rate_data["DGS1"]], axis=1)
#
# to_plot_data["VIX Close"].plot()
# to_plot_data["DGS1"] = to_plot_data["DGS1"].replace(".", np.nan)
# to_plot_data["DGS1"] = to_plot_data["DGS1"].fillna(method="ffill")
#
# to_plot_data["DGS1"].plot()
# plt.show()
