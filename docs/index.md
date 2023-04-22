# Documentation

# Command generation
### Endpoint: /api/plsmc/command
### Expects: 
```json
{
    "prompt": "summon a cow"
}
```
### Response: 
```json
{
    "command": "/summon cow"
}
```

# Datapack generation
### Endpoint: /api/plsmc/datapack
### Expects: 
```json
{
    "prompt": "lightning snowballs"
}
```
### Response: 
```
A zip file containing the datapack
```

# Chat Moderation
### Endpoint: /api/plsmc/moderation
### Expects: 
```json
{
    "message": "I want to kill them."
}
```
### [Response](https://platform.openai.com/docs/api-reference/moderations): 
```json
{
    "categories": {
        "hate": false,
        "hate/threatening": true,
        "self-harm": false,
        "sexual": false,
        "sexual/minors": false,
        "violence": true,
        "violence/graphic": false
    },
    "category_scores": {
        "hate": 0.22714105248451233,
        "hate/threatening": 0.4132447838783264,
        "self-harm": 0.005232391878962517,
        "sexual": 0.01407341007143259,
        "sexual/minors": 0.0038522258400917053,
        "violence": 0.9223177433013916,
        "violence/graphic": 0.036865197122097015
    },
    "flagged": true
}
```

# Chat Translation
### Endpoint: /api/plsmc/translation
### Expects: 
```json
{
    "message": "How are you?",
    "to": "French",
    "from": "English"
}
```
### Response: 
```json
{
    "translation": "Comment allez-vous?"
}
```

