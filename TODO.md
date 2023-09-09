# TODO

- Add registration for listener classes (so you do not need to have access to the client object, similar to discord.py's Cogs)

- Implement all models/endpoints
endpoints
- Implement Item- hierarchy and types:

  - Item class inherits from WorldstateObject and MultiQueryModel
  - Put all major infos in the Item class (split them later)

## Version 2.0

- Remove `WorldstateClient.query_list_of(type)` as `WorldstateClient.query(type)` now does the same while keeping the type.
