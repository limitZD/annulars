import pandas as pd
from myspider.db import engine, JobModel
import matplotlib as mpl
import matplotlib.pyplot as plt
from io import BytesIO

def top_city(tablename='job'):
    job_col = JobModel().get_all_column()
    data_frame = pd.read_sql_table(table_name=tablename, con=engine, columns=job_col)
    return data_frame.groupby('city').size().sort_values(ascending=False)

def top_city_plot(format='png'):
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    mpl.rcParams['figure.figsize'] = 10, 5
    c = top_city()
    c.plot(kind='bar')
    plt.xticks(rotation=20)
    #plt.show()
    image = BytesIO()
    plt.savefig(image, format=format)

    return image.getvalue()

