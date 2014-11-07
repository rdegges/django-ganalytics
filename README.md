# django-ganalytics

Simple Google Analytics integration for Django.


## Meta

* author: Randall Degges
* email:  r@rdegges.com
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
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', '{{ GANALYTICS_TRACKING_CODE }}', 'auto');
  ga('send', 'pageview');
</script>
```

Easy, right?
