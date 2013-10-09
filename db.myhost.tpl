;
; BIND data file for my dyndns.
;
$TTL    60
@       IN      SOA     myhost.com. root.myhost.com. (
                        {{ serial }}    ; Serial
                             60         ; Refresh
                             60         ; Retry
                             60         ; Expire
                             60 )       ; Negative Cache TTL
;
@       IN      A       12.34.56.78
@       IN      NS      ns
ns      IN      A       12.34.56.78
{% for name,ip in items %}{{ name }}	IN	A	{{ ip }}
{% endfor %}
