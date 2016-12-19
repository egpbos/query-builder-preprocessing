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


Questions:

- instances are regarded children of a node? for example [this snippet](https://github.com/NLeSC-Storyteller/query-builder-preprocessing/blob/d8965af72c0378f771256ac8fb634df1a5048d9a/data/entities.json#L4727-L4741) describes an entity National_Health_Service, with a ``child_count`` of 1, but there is no ``children`` field, while ``instances`` contains one element. 
- Why do both entities and instances-of-entities have a ``type`` field while they are already part of the entity tree?
- Why do instances list their parent? I already know what their parent is, because the data is nested.



