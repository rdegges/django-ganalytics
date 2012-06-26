# django-ganalytics

Simple Google Analytics integration for Django.


## Meta

* author: Randall Degges
* email:  rdegges@gmail.com
* status: maintained, in development

[![Build Status](https://secure.travis-ci.org/rdegges/django-ganalytics.png?branch=master)](http://travis-ci.org/rdegges/django-ganalytics)


## Purpose

Honestly, all the other Google Analytics Django apps suck. All I want to do is
put my Google Analytics code in my ``settings.py`` file, and use a simple
template tag to render the Google Analytics asynchronous javascript code,
damnet!

Unfortunately, all the existing solutions don't do this, and that pisses me
off!

![squint](https://github.com/rdegges/django-ganalytics/raw/master/assets/squint.png)


## Installation and Usage

Anyway, let's install this bitch! The first thing you'll want to do is run:

``` bash
$ pip install django-ganalytics
```

Next, modify your ``settings.py`` file, and add your Google Analytics code
(usually something like ``UA-XXXXXXXX-XX``), as well as put
``ganalytics`` in your ``INSTALLED_APPS``:

``` python
# settings.py

INSTALLED_APPS = (
    # ...
    'ganalytics',
)

GANALYTICS_TRACKING_CODE = 'UA-XXXXXXXX-XX'
```

Now, to actually render your Google Analytics asynchronous javascript code,
edit your desired Django template (I like to do this in my ``base.html``
template), and add the following:

``` html
{% load ganalytics %}
<!--- ... -->

<head>
  {% ganalytics %}
</head>

<!--- ... -->
```

When Django processes your template, it'll replace ``{% ganalytics %}``
with:

``` html
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', '{{ GANALYTICS_TRACKING_CODE }}']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
```

Easy, right?
