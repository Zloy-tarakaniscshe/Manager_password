# Manager_password (TestTask)
![Static Badge](https://img.shields.io/badge/3.11-blue?label=Python)
![Static Badge](https://img.shields.io/badge/Django-blue)
![Static Badge](https://img.shields.io/badge/Django_Rest_Framework-green)

_____________________________________________________
![logo](https://media.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkh7rm3q2amm9arskcjtm.png)

### How to start a project:
* Download the project from the repository
### Install utils for Ubuntu:
```
sudo apt install docker-compose
```

#### Run the project build command:
```
command: cd ./Manager_password
command: docker-compose up --build
```
____________________________________________
### Example Manager_password:

```
GET /password/?service_name=l
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 19,
        "service_name": "lol",
        "encrypted_password": "b'gAAAAABnARD5tvWGQ1TCfdxRGGbOxOIcjNk8d85ILjms5gNSNM38wkw_tUrhUZl2T3vbsrgk0EjQxxBt59NMnQTJswlVOPBGBCF_fo4UmO6TqUEF9ds5stU='"
    },
    {
        "id": 23,
        "service_name": "lll",
        "encrypted_password": "b'gAAAAABnARchXwd3wGCrEb2hWK8KKZ04s5yiUE3CTDOc-dHwLB20x1EKo_exW0g8QZjwB0hCYCpiHOaAK_2UWPnYR21LxNZ8xgKwJLYLXyUtpuEaWYGG94I='"
    },
    {
        "id": 24,
        "service_name": "ll",
        "encrypted_password": "b'gAAAAABnARfaz34HkDAPTF4aNMyMScnzff0zjuFROAsvG_aQhfNJTDBPz182FIF6SjKykx1nJleab5bcUumJszGpdOSSfCN03MrEBYEtM4D24koTlb5PzV0='"
    }
]
```
```
GET /password/yandex/
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "service_name": "yandex",
    "password": "b'gAAAAABnAStEjkXDgLA_lQ78cRVHeNJPMrOp0AfTAmW128Hs9MlTuHLbG9nCOBUWxOY2qKbuHsEwL0Tt7G6zBVkFlLAN5qJTd_cs07ytgsSk3doVDoE_of0='"
}
```
```
POST /password/yandex/
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "password": "gAAAAABnAWW4C_GspyAkU4tXDdiYj6EdDnYf2YogyomFAnqshm9PKe2Cn9pyvsh5tarE6o9Hk0xzLF95rE6Lna96a3KGXQxNUfg3Unh7hfDe10p3t2NTLEI="
}
```
