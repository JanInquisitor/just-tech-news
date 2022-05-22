from .home import bp as home
from .dashboard import bp as dashboard
from .api import bp as api

# Personal note create namespaces for modules and files and all that, at least get into the habit when it becomes
# useful

# Let's review what's happening here. First, the .home syntax directs the program to find the module named home in the current directory.
# Next, we want to import the bp object, but we rename it home as part of the import process, for practicality's sake.

# Note that you can import home directly from the routes package, because its __init__.py file imported (and renamed) the blueprint.
# Otherwise, you'd have to add from app.routes.home import bp as home and then repeat that line for any new modules that you added to routes.
# You could simplify this further by adding .routes instead of app.routes (which merely indicates that routes belongs to the parent app package).
