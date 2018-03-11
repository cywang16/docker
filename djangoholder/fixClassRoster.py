
import os, sys
import pandas as pd

import pytz
from datetime import datetime

g_tz_pst = pytz.timezone('America/Los_Angeles')

def compact_datetime_String():
    return datetime.now(g_tz_pst).strftime("%Y%m%d-%H%M-%Z")

def fixProgramValue(rawValue):
    lines = rawValue.split('<br>')
    outlines = []
    for line in lines:
        outline = line.strip().replace('Q: Ensemble Size A:', ' - ')
        outline = outline.replace('Q: Instrument/Voice A:', '</li><li>Instrument/Voice:', 1)
        outline = outline.replace('Q: Instrument/Voice A:', '<ul><li>Instrument/Voice:', 1)
        outline = outline.replace('Q: Piece 1a Title and Opus, etc. A:', '</li><li>')
        outline = outline.replace('Q: Piece 1b Composer Full Name A:', ' by ')
        outline = outline.replace('Q: Piece 2a Title and Opus, etc. A:', '</li><li>')
        outline = outline.replace('Q: Piece 2b Composer Full Name A:', ' by ')
        # outline = outline.replace('Q: Teacher Full Name A:', '</li></ul>')
        if 'Q: Teacher Full Name A:' in outline:
            teacher = outline.replace('Q: Teacher Full Name A:', '').strip()
            outline = '</li></ul>'
        outline = outline.replace('Q: Ensemble Name A:', '<ul><li>Ensemble:')
        outline = outline.replace('Q: Performer Names-Instruments (Separated by commas) A:', '</li><li>Performers:')
        outline = outline.replace('Q: Performer Names (Separated by commas) A:', '</li><li>Performers:')
        outline = outline.replace('Q: Piece 1a Full Title and Opera A:', '</li><li>')
        outline = outline.replace('Q: Piece 2a Full Title and Opera A:', '</li><li>')
        outline = outline.replace('Q: Piece 3a Full Title and Opera A:', '</li><li>')
        outline = outline.replace('Q: Piece 3b Composer Full Name A:', ' by ')
        outlines.append(outline)
    result = {'outlines': ''.join(outlines), 'teacher': teacher}
    return result

def fix_csv(filename):
    classdata = pd.read_csv(filename)

    for i, row in classdata.iterrows():
        startDate = row['Start Date'].strip()
        startTime = row['Start Time'].strip()
        endDate = row['Enddate'].strip()
        endTime = row['End Time'].strip()
        classdata.set_value(i, 'Start Date', '{} {}'.format(startDate, startTime))
        classdata.set_value(i, 'Enddate', '{} {}'.format(endDate, endTime))
    del classdata['Name']
    del classdata['Group Name']
    del classdata['Department']
    del classdata['Site Name']
    del classdata['Days']
    del classdata['Minimum Enrollment']
    del classdata['Capacity']
    del classdata['Enrolled']
    del classdata['Pending']
    del classdata['Waitlist']
    del classdata['Primary Phone']
    del classdata['Gender']
    del classdata['Class Fee']
    del classdata['Customerid']
    del classdata['Account ID']
    del classdata['DCol1']
    del classdata['Invoice Total']
    del classdata['Invoice Status CD']
    del classdata['Discount Amt']
    del classdata['Pmt Applied']
    del classdata['Amt Due']
    del classdata['Invoice Id']
    del classdata['Discount Flag']
    del classdata['Enrollment Status CD']
    del classdata['Males']
    del classdata['Females']
    del classdata['Collumn1']
    del classdata['Collumn2']
    del classdata['Collumn3']
    del classdata['Collumn4']
    del classdata['Event ID']
    del classdata['Courseid']
    del classdata['Custom Fields']
    del classdata['Start Time']
    del classdata['End Time']
    classdata.columns = ['ClassCode',
                         'CourseName',
                         'StartDate',
                         'EndDate',
                         'FestivalName',
                         'AdjudicatorLName',
                         'AdjudicatorFName',
                         'Room',
                         'StudentLName',
                         'StudentFName',
                         'Age',
                         'Program']
    classdata['TeacherName'] = ''
    classdata['RawProgram'] = classdata['Program']

    for i, row in classdata.iterrows():
        oneCourse = row['CourseName'].strip()
        classdata.set_value(i, 'CourseName', oneCourse)

    for i, row in classdata.iterrows():
        fixedProgram = fixProgramValue(row['Program'])
        classdata.set_value(i, 'Program', fixedProgram['outlines'])
        classdata.set_value(i, 'TeacherName', fixedProgram['teacher'])

    classdata.to_csv('ClassRoster-{}.csv'.format(compact_datetime_String()), index = False)

if __name__ == "__main__":
    fix_csv(sys.argv[1])
