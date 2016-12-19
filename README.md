# query-builder-preprocessing
Collects data preprocessing scripts for query-builder-server


# Piek's new data model

|   | Type | Phrase  | Instance  |
|---|---|---|---|
| entity | [entityType](#entitytype) | [entityPhrase](#entityphrase) | [entityInstance](#entityinstance) |
| event | [eventType](#eventtype) | [eventPhrase](#eventphrase) | [eventInstance](#eventinstance) |
| source | [sourceType](#sourcetype) | [sourcePhrase](#sourcephrase) | [sourceInstance](#sourceinstance) |
| topic | [topicType](#topictype) | [topicPhrase](#topicphrase) | [topicInstance](#topicInstance) |



## entityType

## entityPhrase

## entityInstance

## eventType

## eventPhrase

## eventInstance

## sourceType

## sourcePhrase

## sourceInstance

## topicType

## topicPhrase

## topicInstance


Maybe a more succinct description is:

- nodes can be of 1 of 4 types:
    1. entity
    1. event
    1. source
    1. topic
- nodes can have children and instances.
- a node's children and instances must be of the same type as the parent. The resulting data structure can thus be a nested one.
- a node's children are sorted by decreasing ``mention_count``.



