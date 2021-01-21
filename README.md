# NFH - Namitas's Fitness Hub WebApp
- NFH is the Web Application built, using Python Django with HTML, CSS, JS, for our client Namitas Fitness Hub.
- The WebApp can be used for managing and displaying assets of clients and also the manage Plans, Subscription and Batches for Users.
- An User Subscription Model is developed to manage the user subscription.
- A Users can select a particular plan and subscribe to it. Each Plan has a rate and days of validity after which the user will be automatically be unsubscribes from that plan
- A user can select a particular batch to which a link to a video lecture is associated.
- All the necessary permissions to manage Plans, Batches and Subscriptions are been given to Admin.
- For the required default plans A Request Model has been developed so that authorized users only can subscribe.
- In order to attend a session, a user has to fulfill necesaary requirements. If not done then, he or she womt be able to attend.
- An Email Service has been also integrated so that users can be notified time to time regarding plan request approval, payments etc.
- A RazorPay Payment gateway has also been integrated.
- A good UX flow has been taken care of keeping in mind taking care of all the usecases.
- Cron Job Services are used to check the validity for Plan Subcription and Account.
- A user's account will be closed if he/she is inactive(does not have any active plans) for 365 days.
- The static image files are served using Firebase Cloud Storage which is a CDN in itself.
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
