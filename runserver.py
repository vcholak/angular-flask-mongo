__author__ = 'vcholak'

from products import app

# Use this to use the Flask's internal debugger
# In this mode auto-reloading is enabled but breakpoints are disabled
app.run(debug=True)

# Use this to run in production environment
# Also use it to debug under PyCharm's debugger
# In this debug mode auto-reloading is disabled but breakpoints are enabled
#app.run()