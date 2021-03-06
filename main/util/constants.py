from main.util.file_io import with_path

# Spreadsheet Link: https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>
SPREADSHEET_ID = '1Sj8JsgVGipsAsHq5V4AIrLnBf_vzHmUbSWN2WnZAiZI'
BOARD_TAB = 'Scoreboard'
SHOWDOWN_TABS = [
    '08/12/2018 Any%',
    '01/31/2019 Any% (1)',
    '01/31/2019 Any% (2)',
    '02/02/2019 Any%',
    '02/03/2019 Any%',
    '02/05/2019 Any%',
    '02/06/2019 Any%',
    '02/08/2019 Any%',
    '02/09/2019 Any%',
    '02/15/2019 Any%',
    '08/31/2019 Any%',
    '09/04/2019 Any%',
    '09/07/2019 100%-',
    '09/06/2020 Any%',
    '09/09/2020 100%',
    '09/11/2020 Any%',
    '09/11/2020 Invisible Any%',
    '09/18/2020 Any%',
    '09/18/2020 100%',
    '01/01/2022 100%',
    '01/02/2022 Any% (1)',
    '01/02/2022 Any% (2)',
    '01/12/2022 Any%',
    '01/14/2022 Any%',
    '01/19/2022 Any%',
    '01/21/2022 Any% (1)',
    '01/21/2022 Any% (2)',
    '01/24/2022 Any%',
]

MODE = 'Mode'
CHAPTER = 'Chapter'
RESERVED = [MODE, CHAPTER]

DEFAULT_DATE = '01/01/2022'
EMPTY_FIELD = '--'

PREVIOUS_FILE = with_path('previous.csv')
DIFFS_FILE = with_path('changelog.csv')
PROGRESS_FILE = with_path('progress.csv')

CREDENTIALS_FILE = with_path('credentials.json')
PICKLE_FILE = with_path('token.pickle')
