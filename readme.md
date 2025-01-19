# Social links
Host all your socials in one place.
![](./gitassets/image.png)





## The data
Create a file called `links.json`. The content should look like this.
```json
{
    "links": [
        {
            "title": "Bluesky",
            "url": "https://bsky.app/profile/*******"
        },
        {
            "title": "Github",
            "url": "https://github.com/*******"
        },
        {
            "title": "Facebook",
            "url": "https://facebook.com/*******"
        },
        {
            "title": "Instagram",
            "url": "https://instagram.com/*******"
        }
    ]
}
```

## Running
When you have created the link file you need to build the docker image.
```
docker build . -t social_links
```

To run the image use 
```
docker run -p 8080:80 --rm social_links
```