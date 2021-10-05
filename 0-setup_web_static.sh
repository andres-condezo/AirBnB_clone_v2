#!/usr/bin/env bash
# This script sets up a web server for deployment
apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data
chgrp -R ubuntu /data

cat > /etc/nginx/sites-available/default << EOF
# Default server configuration
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	add_header X-Served-By \$hostname;

	root /var/www/html;
	index index.html index.htm;
 
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location =/redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /404.html;
}
EOF

service nginx restart
