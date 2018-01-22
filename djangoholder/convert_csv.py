
import os, sys
import pandas as pd

import pytz
from datetime import datetime

dfx = pd.read_excel(open('CourseFactorTable.xlsx','rb'), sheet_name='Sheet1')
g_tz_pst = pytz.timezone('America/Los_Angeles')

def compact_datetime_String():
    return datetime.now(g_tz_pst).strftime("%Y%m%d-%H%M-%Z")

def fix_csv(filename):
    classdata = pd.read_csv(filename)
    '''
    del classdata['textBox35']
    del classdata['textBox5']
    del classdata['textBox37']
    del classdata['textBox38']
    '''
    cols = [0, 1, -3, -2]
    classdata.drop(classdata.columns[cols], axis=1, inplace=True)
    cols = classdata.columns.tolist()
    cols = cols[-3:-2] + cols[:-3] + cols[-2:]
    cols = cols[0:7] + cols[-2:-1] + cols[7:-2] + cols[-1:]
    classdataFixed = classdata[cols]
    classdataFixed.columns = ['Class Code',
                              'Room',
                              'Min',
                              'Max',
                              'Enrolled',
                              'Pending',
                              'Waitlisted',
                              'Open',
                              'Start Date',
                              'End Date',
                              'Start Time',
                              'End Time',
                              'Days',
                              'Adjudicator',
                              'Status']
    classdataFixed.is_copy = False
    classdataFixed['Factor'] = 0
    classdataFixed['Time'] = 0
    for i, row in classdataFixed.iterrows():
        r = dfx[(dfx['CourseCode'] == row['Class Code']) |
                (dfx['CourseCode'] == row['Class Code'][:-2])]
        if len(r.index) == 1:
            factor = r.iloc[0]['ScheduleFactor']
            classdataFixed.set_value(i, 'Factor', factor)
            classdataFixed.set_value(i, 'Time', factor * (row['Enrolled'] + row['Pending']))
    cols = classdataFixed.columns.tolist()
    cols = cols[:2] + cols[-2:] + cols[2:-2]
    classdataFixed = classdataFixed[cols]
    filenamefixed = 'CourseSummary-{}.csv'.format(compact_datetime_String())
    classdataFixed.to_csv(filenamefixed, index = False)
    return filenamefixed

if __name__ == "__main__":
    fix_csv(sys.argv[1])
