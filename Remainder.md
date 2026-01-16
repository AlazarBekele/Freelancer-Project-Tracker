# View Counter Control
## 
### Got Error 
1. "Error | MultipleObjectsReturned On Make publih filter"

```python

    # Handel the Like & View
    post = get_object_or_404 (Make_Publish_Post)
    session_key = f'viewed_post_{post.id}'

    if not request.session.get (session_key):
        post.view += 1
        post.save()
        request.session[session_key] = True
```
#### Why Got This Error
- Didn't Much the Id from Publisher to current request user
#### Solutions
- Remake From New the "Make_Publish_Post" Model to much the ID from orignal
![alt text](<Screenshot 2026-01-16 at 7.24.08 PM.png>)

![alt text](<Screenshot 2026-01-16 at 7.24.22 PM.png>)