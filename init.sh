sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart

sudo gunicorn -c /home/box/etc/gunicorn-django.conf ask.wsgi:application
