# query-builder-preprocessing
Collects data preprocessing scripts for query-builder-server


# Data structure

- nodes can be of 1 of 4 types:
    1. entity
    1. event
    1. source
    1. topic
- nodes can have children and instances.
- a node's children and instances must be of the same type as the parent. The resulting data structure can thus be a nested one.
- a node's children are sorted by decreasing ``mention_count``.

Examples:

```
entities/
└── entity0
    ├── entity1
    ├── entity2
    └── instance0
```

```
events
└── event0
```

```
sources/
└── source0
    ├── instance0
    ├── instance1
    └── instance2
```

```
topics/
└── topic0
    ├── instance0
    ├── instance1
    ├── instance2
    ├── topic1
    ├── topic2
    ├── topic3
    └── topic4
```


Questions:

- instances are regarded children of a node? for example [this snippet](https://github.com/NLeSC-Storyteller/query-builder-preprocessing/blob/d8965af72c0378f771256ac8fb634df1a5048d9a/data/entities.json#L4727-L4741) describes an entity National_Health_Service, with a ``child_count`` of 1, but there is no ``children`` field, while ``instances`` contains one element. 
- Why do both entities and instances-of-entities have a ``type`` field while they are already part of the entity tree?
- Why do instances list their parent? I already know what their parent is, because the data is nested.
- How would phrases fit into the succint data model?
- There aren't any instances of anything (for example, a ``grep`` on ``"event`` returns 1032 occurrences in events.json, of which there are 977 ``eventPhrase``s and 55 ``eventType``s, but no ``eventInstance``s.) Also the ``eventPhrase`` part of an array called ``instances``.


# How to parse the JSONs into an sqlite3 database

```bash
cd src
python3 create_sqlite.py --input ../data/entities.json --name ../data/storyteller.db --tablename entities
python3 create_sqlite.py --input ../data/events.json --name ../data/storyteller.db --tablename events
python3 create_sqlite.py --input ../data/sources.json --name ../data/storyteller.db --tablename sources
python3 create_sqlite.py --input ../data/topics.json --name ../data/storyteller.db --tablename topics

# afterwards, the snippet below should return some records
sqlite3 ../data/storyteller.db
sqlite> SELECT * FROM entities;
sqlite> SELECT * FROM events;
sqlite> SELECT * FROM sources;
sqlite> SELECT * FROM topics;
```

