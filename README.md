# 🚀 PlanEx - Planet Express, Inc.

Our mission is to deliver OpenStreetMap packages to dangerous and lethal places where no one is brave and stupid enough to go through.


## 📦 Usage

Create a self-contained environment and enter it

    make
    make run

Create a package from an internal base map or for testing e.g. from [Geofabrik](http://download.geofabrik.de/europe.html)

    ./bin/planex map.osm.pbf map.pkg --version 20190503 --layers layers.toml

With psql create tables, bulk import, and index table against a Postgres database

    postgres=# \include /data/sql/initdb.sql
    postgres=# \copy segments from /data/map.pkg csv
    postgres=# \include /data/sql/indexdb.sql


## 🚧 Development

Use a small base map for development e.g. Monaco

    wget http://download.geofabrik.de/europe/monaco-latest.osm.pbf
    ./bin/planex monaco-latest.osm.pbf map.pkg --version 20191106 --layers layers.toml

To develop against a local Postgres 12 database

    docker run -it --rm --network=host -e POSTGRES_PASSWORD="$(uuidgen -r)" postgres:12

Then use psql from the Postgres 12 client tools

    docker run -it --rm --network=host -v $PWD:/data postgres:12 psql -h localhost -U postgres

    \include /data/sql/initdb.sql
    \copy segments from /data/map.pkg csv
    \include /data/sql/indexdb.sql


## 📖 Example Queries

Query for all roundabout segments

```sql
postgres=# SELECT osm_segment_from AS from, osm_segment_to AS to FROM segments WHERE osm_tag_key='junction' AND osm_tag_val='roundabout' LIMIT 10;
    from    |     to
------------+------------
   25177422 |   25238111
   25238111 | 4939779390
 4939779390 | 4939779389
 4939779389 |   25204713
   25204713 | 4939779388
 4939779388 |   25204264
  257076297 | 1780610235
 1780610235 |  257076299
  257076299 |  257076301
  257076301 | 1780610236
(10 rows)
```


## ⛔ Differentiation

What this project is and is not about
- 💙 We primary want a segment mapping `(from, to)` node ids to `(key, val)` tags
- 💙 We extract these mappings from all segments in all ways without restrictions
- ❤️ We do not handle relations triplets `(from, via, to)`
- ❤️ We do not store location information with the mappings


## 🐙 FAQ

Why not Zoidberg?


## License

Copyright © 2019 MoabitCoin

Distributed under the MIT License (MIT).
