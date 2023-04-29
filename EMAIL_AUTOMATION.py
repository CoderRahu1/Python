# THIS CODE ENABLES YOU TO AUTOMATE EMAIL OPENING EVERYDAY AT SPECIFIED TIME USING TASK SCHEDULER.


# Modules which need to be imported

import webbrowser

# Site which you want to Open in your
# Browser
url = "mail.google.com"

# Below code is used to specify
# location of webbrowser which you
# want to use.
edge_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# Below code will open your URL
webbrowser.register(
'firefox', None, webbrowser.BackgroundBrowser(edge_path))

webbrowser.get('firefox').open_new_tab(url)
