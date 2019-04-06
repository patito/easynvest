# Easynvest

Just a simple spider to get data from easynvest.

### License

```
# "THE BARBECUE-WARE LICENSE" (Revision 1):
#
# <benatto@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can make me a brazilian barbecue, including beers
# and caipirinha in return to Paulo Leonardo Benatto.
#
# The quality of the barbecue depends on the amount of beer that has been
# purchased.
```

### Requirements

- scrapy

### Build

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### How to use

```
$ scrapy crawl fixed_income -a email=<EMAIL> -a password=<PASSWORD>
```
 
