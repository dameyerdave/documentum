# Splunk Documentation
## Machine information
{"localsplunk": { "content": "serverinfo" }}

## License information
{"localsplunk": { "content": "licenseinfo" }}

## License pool information
{"localsplunk": { "content": "licensepoolinfo" }}

## Indexes
{"localsplunk": { "content": "indexes" }}

## Indexes
{"localsplunk": { "search": "| eventcount summarize=f | table index, count" }}

## Apps
{"localsplunk": { "content": "apps" }}

## Roles
{"localsplunk": { "content": "roles" }}

## Users
{"localsplunk": { "content": "users" }}

## Forwarders
{"localsplunk": { "search": "search index=_internal source=*metrics.log group=tcpin_connections | eval sourceHost=if(isnull(hostname), sourceHost, hostname) | rename connectionType as connectType | eval connectType=case(fwdType==\"uf\",\"Universal Forwarder\", fwdType==\"lwf\", \"Lightweight Forwarder\",fwdType==\"full\", \"Heavy Forwarder\", connectType==\"cooked\" or connectType==\"cookedSSL\",\"Splunk Forwarder\", connectType==\"raw\" or connectType==\"rawSSL\",\"Legacy Forwarder\") | eval version=if(isnull(version),\"pre 4.2\",version) | rename version as Ver | fields connectType sourceIp sourceHost destPort kb tcp_eps tcp_Kprocessed tcp_KBps splunk_server Ver | eval Indexer= splunk_server | stats count by connectType sourceIp sourceHost destPort Indexer Ver | fields - count" }}
