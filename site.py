# Other required imports
...
from .cache import cache

bp = Blueprint('site', __name__)

# other views and functions
...

@bp.route('/book', methods=('GET', 'POST'))
def book():
    # Connect to calendar or fail gracefully
    service = cache.get("service") # now the cache is available within a view
    if service is None: # service hasn't been added to cache or is expired
        try: # rebuild the service to connect to calendar
            service = connectToCalendar() # uses google.oauth2 and googleapiclient.discovery
            cache.set("service", service) # store service in cache
            g.error = False
        except Exception as e:
            flash(e)
            g.error = True
            return render_template('site/book.html') # jinja2 template that checks for g.error

    # remaining logic for the 'book' view
    ...

    # Cache results of queries
    if cache.get("week_{}".format(offset)) is None:
        # get new results
        week = getWeek(service)
        cache.set("week_{}".format(offset), week)
    else:
        week = cache.get("week_{}".format(offset))

    return render_template('site/book.html', <...arguments...>)