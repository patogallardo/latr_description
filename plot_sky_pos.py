import pandas as pd
import numpy as np  # noqa
import matplotlib.pyplot as plt  # noqa

show = False
df = pd.read_csv('field_pos_sky.csv')

plt.scatter(df.TMP_x_deg, df.TMP_y_deg, label='TMA fields')
plt.scatter(df.CD_x_deg, df.CD_y_deg, label='CD fields')

plt.axis('equal')
plt.legend(loc='upper right')

plt.ylim([-4.5, 4.5])

if show:
    plt.show()
else:
    plt.savefig('fields_pos_sky_diagram.pdf')
    plt.close()
