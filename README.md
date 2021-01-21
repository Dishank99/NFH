# NFH - Namitas's Fitness Hub WebApp
- NFH is the Web Application built, using Python Django with HTML, CSS, JS, for our client Namitas Fitness Hub.
- The WebApp can be used for managing and displaying assets of clients and also the manage Plans, Subscription and Batches for Users.
- A Users can select a particular plan and subscribe to it. Each Plan has a rate and days of validity after which the user will be automatically be unsubscribes from that plan
- All the permissions to manage Plans are been given to Admin.
- An Email Service has been also integrated so that users can be notified time to time regarding plan request approval, payments etc.
- A RazorPay Payment gateway has also been integrated.
- A good UX flow has been taken care of keeping in mind taking care of all the usecases.
- Cron Job Services are used to check the validity for Plan Subcription and Account.
- The static image files are served using Firebase Cloud Storagw which is a CDN in itself.
- Media Images are compressed so that latency is reduced.

## Future Tasks
- To make necessary changes rather enhancements to reduce the latencies as much as possible.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Dishank99/NFH.git
$ cd nfh
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
