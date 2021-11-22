# Suggesty Backend Application
Suggesty Backend Application developed with Django Framework.

Packages used in this project are listed in requirements.txt file with their versions.

Instructions of how to run the application are given in main ReadMe.md file in root directory of repository.

This application ready-to-use with Docker.


## API Usage

#### Get Playlist

```http
  GET /api/v1/tracks/${genre}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `genre`      | `string` | **Gerekli**. Genre of desired type of artist/band |


#### Response Codes
| Code | Description                       |
| :-------- | :-------------------------------- |
| `200`   | Success. Request fullfiled |
| `404`   | Not Found. Requested resource not found.  |
| `400`   | Bad syntax. This endpoint doesn't accept requests in given syntax and format.  |
| `500`   | Server-side application error.  |

#### Returns on Success
````json
{
  "RESULT":string
  "MESSAGE":string
  "data":
  {
    artist:string
    track:string
    album_image_url:string
    preview_url:string|null
  }
} 
````

#### Returns on Error
````json
{
  "RESULT":string
  "MESSAGE":string
} 
````