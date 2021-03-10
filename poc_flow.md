# POC flow example

Two persons editing the title of the same US cyclically, while N other people keep re-loading the kanban, which contains 
more than 1000 user stories.

```
Pruebas:
	- Editar dos personas a la vez una US
	- 1000 US y ver el list de FastApi cómo lo resuelve (simultaneando la anterior edición de USs)
```

## Involved requests

### Listing the Kanban

`Projects folder`
~~api/v1/projects?member=5&order_by=user_order&slight=true~~

`Project's settings`
~~api/v1/projects/by_slug?slug=taiga-sp003~~

`Project's tag colors`
api/v1/projects/15/tags_colors 

`Project's USs`
**api/v1/userstories?project=15&status__is_archived=false**

`Project swimlanes`
api/v1/swimlanes?project=15

`Project's filters`
api/v1/userstories/filters_data?project=15

`User's Notifications`
~~api/v1/web-notifications?only_unread=true&page=1~~

### Editing the User Story

`User story's title update`
api/v1/userstories/118 (PATCH)

```json
// From 'US001' to 'US002'
{
  // The new value
  subject: "US002",
  // Consequent updates increase this number by 1
  version: 2
}
```

`User story's activity` api/v1/history/userstory/118?page=1&type=activity (GET)


## POC Options

1. Using a simplified front-end 
   
* Against both taiga-back (Django) and the POC (FastAPI), to compare timings and behaviours
* Just against the FastAPi POC

2. Same current front-end, served by taiga-front into two different urls:
    * one resolving against the previous Django (as it is now)
    * the other one resolving against the new api POC's urls


* More reliable POC
* Real conclusions about being integrated with taiga-front, working with two api instances 
* Not all the requests have to be migrated


3. Two scripts that launches programmatically the same sequence of cURL requests.

* The quickest option
* More control about the requests and response times
* The less conclusive POC



