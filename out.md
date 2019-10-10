# Splunk Documentation

## Machine information

|Machine|Splunk Version|CPU Cores (Physical / Virutal)|Physical Memory Capacity|Operating System|CPU Arch|
|---|---|---|---|---|---|
|sh|enterprise v7.3.1|2 / 2|3.85 GB|Linux 4.9.184-linuxkit|x86_64|


## License information

|License|Quota|
|---|---|
|Splunk Enterprise   Splunk Analytics for Hadoop Download Trial|500.0 MB|
|Splunk Forwarder|1.0 MB|
|Splunk Free|500.0 MB|


## License pool information

|License Pool|Quota|
|---|---|
|auto_generated_pool_download-trial|MAX|
|auto_generated_pool_forwarder|MAX|
|auto_generated_pool_free|MAX|


## Indexes

|Name|Type|App|Current Size|Max Size|Event Count|Earliest Event|Latest Event|Home Path|Cold Path|Frozen Path|Frozen Time Period|
|---|---|---|---|---|---|---|---|---|---|---|---|
|_audit|event|system|1.0 MB|488.28 GB|3604|2019-09-26T13:18:21+0000|2019-09-27T11:51:20+0000|$SPLUNK_DB/audit/db|$SPLUNK_DB/audit/colddb|N/A|6Y|
|_internal|event|system|13.0 MB|488.28 GB|105238|2019-09-26T13:17:53+0000|2019-09-27T11:51:20+0000|$SPLUNK_DB/_internaldb/db|$SPLUNK_DB/_internaldb/colddb|N/A|1M|
|_introspection|event|system|24.0 MB|488.28 GB|16968|2019-09-26T13:18:22+0000|2019-09-27T11:51:18+0000|$SPLUNK_DB/_introspection/db|$SPLUNK_DB/_introspection/colddb|N/A|2W|
|_telemetry|event|system|1.0 MB|488.28 GB|1|2019-09-27T02:10:20+0000|2019-09-27T02:10:20+0000|$SPLUNK_DB/_telemetry/db|$SPLUNK_DB/_telemetry/colddb|N/A|2Y 2D|
|_thefishbucket|event|system|1.0 MB|488.28 GB|0|||$SPLUNK_DB/fishbucket/db|$SPLUNK_DB/fishbucket/colddb|N/A|4W|
|history|event|system|1.0 MB|488.28 GB|0|||$SPLUNK_DB/historydb/db|$SPLUNK_DB/historydb/colddb|N/A|1W|
|main|event|system|1.0 MB|488.28 GB|0|||$SPLUNK_DB/defaultdb/db|$SPLUNK_DB/defaultdb/colddb|N/A|6Y|
|splunklogger|event|system|0 B|488.28 GB|0|||$SPLUNK_DB/splunklogger/db|$SPLUNK_DB/splunklogger/colddb|N/A|6Y|
|summary|event|system|1.0 MB|488.28 GB|0|||$SPLUNK_DB/summarydb/db|$SPLUNK_DB/summarydb/colddb|N/A|6Y|


## Events per index

|server|index|count|
|---|---|---|
|idx|main|16611|
|sh|main|0|


## Apps

|App|Name|Author|Version|Build|State|
|---|---|---|---|---|---|
|Log Event Alert Action|alert_logevent|Splunk|7.3.1|N/A|Enabled|
|Webhook Alert Action|alert_webhook|Splunk|7.3.1|N/A|Enabled|
|Apps Browser|appsbrowser|Splunk|7.3.1|N/A|Enabled|
|baseline_sh|baseline_sh|N/A|N/A|N/A|Enabled|
|Getting started|gettingstarted|Splunk|1.0|N/A|Disabled|
|introspection_generator_addon|introspection_generator_addon|Splunk|7.3.1|N/A|Enabled|
|Home|launcher|N/A|N/A|N/A|Enabled|
|learned|learned|N/A|N/A|N/A|Enabled|
|legacy|legacy|N/A|N/A|N/A|Disabled|
|modin|modin|N/A|N/A|N/A|Enabled|
|rblcheck|rblcheck|N/A|N/A|N/A|Enabled|
|sample data|sample_app|N/A|N/A|N/A|Disabled|
|Search & Reporting|search|Splunk|7.3.1|N/A|Enabled|
|Splunk Archiver App|splunk_archiver|Splunk Inc|1.0|N/A|Enabled|
|Splunk Enterprise On Docker|splunk_enterprise_on_docker|Splunk|1.0.0|N/A|Enabled|
|Splunk Get Data In|splunk_gdi|Splunk|1.0.2|2|Enabled|
|splunk_httpinput|splunk_httpinput|N/A|N/A|N/A|Enabled|
|Instrumentation|splunk_instrumentation|Splunk|4.2.2|N/A|Enabled|
|Splunk Metrics Workspace|splunk_metrics_workspace|Splunk|1.1.6|207238437|Enabled|
|Monitoring Console|splunk_monitoring_console|Splunk|7.3.1|N/A|Enabled|
|SplunkForwarder|SplunkForwarder|N/A|N/A|N/A|Disabled|
|SplunkLightForwarder|SplunkLightForwarder|N/A|N/A|N/A|Disabled|
|ssl_config|ssl_config|N/A|N/A|N/A|Enabled|


## Roles

|Role|Imported Roles|Allowed Indexes|Default Indexes|Max Search Jobs|Max RT Search Jobs|
|---|---|---|---|---|---|
|admin|power, user|*, _*|os, main|50|100|
|can_delete||||3|6|
|power|user|*|main|10|20|
|splunk-system-role|admin|*, _*|os, main|3|6|
|user||*|main|3|6|


## Users

|Name|Full Name|Email address|Authentication System|Lang|Time Zone|Default App|Roles|Status|
|---|---|---|---|---|---|---|---|---|
|admin|Administrator|changeme@example.com|Splunk|||launcher|admin|Active|


## Forwarders

|ForwarderType|ConnectionType|Version|SourceHost|SourceIP|Indexer|DestPort|
|---|---|---|---|---|---|---|
|Heavy Forwarder|cookedSSL|7.3.1|ds|172.27.0.4|idx|9997|
|Heavy Forwarder|cookedSSL|7.3.1|hf|172.27.0.6|idx|9997|
|Heavy Forwarder|cookedSSL|7.3.1|sh|172.27.0.3|idx|9997|
|Universal Forwarder|cookedSSL|7.3.1|uf|172.27.0.2|idx|9997|
|Universal Forwarder|cookedSSL|7.3.1|uf|172.27.0.9|idx|9997|


## Deployment Clients



## Active Saved Searches

|Name|App|State|Scheduled|Schedule|Next Run|
|---|---|---|---|---|---|
|Bucket Copy Trigger|splunk_archiver|Enabled|True|17 * * * *|2019-10-10 13:17:00 UTC|
|DMC Forwarder - Build Asset Table|splunk_monitoring_console|Enabled|True|3,18,33,48 * * * *|2019-10-10 13:03:00 UTC|
|instrumentation.usage.authMethod.config|splunk_instrumentation|Enabled|True|0 3 * * 1|2019-10-14 03:00:00 UTC|
|instrumentation.usage.healthMonitor.report|splunk_instrumentation|Enabled|True|0 3 * * 1|2019-10-14 03:00:00 UTC|
|instrumentation.usage.passwordPolicy.config|splunk_instrumentation|Enabled|True|0 3 * * 1|2019-10-14 03:00:00 UTC|
|instrumentation.usage.smartStore.config|splunk_instrumentation|Enabled|True|0 3 * * 1|2019-10-14 03:00:00 UTC|
|instrumentation.usage.workloadManagement.report|splunk_instrumentation|Enabled|True|0 3 * * 1|2019-10-14 03:00:00 UTC|
