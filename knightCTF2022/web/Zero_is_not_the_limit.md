# Zero is not the limit

## description

50

Flag Format : KCTF{s0m3thing_h3r3}

Note : Burte Force/Fuzzing not required and not allowed. Hint: You have to think out side from '/user/'.

Author: 0xmahi

## writeup

URLにアクセスするとjson形式のデータが表示されました。
`/user1`にアクセスすると`Cannot GET /user1`が表示された。
`/user/1`にアクセスすると`{"name":"Jhon","password":"Jhon123","id":1}`が表示された。タイトルを思い出し、`/user/0`にアクセスすると何も表示されなかった。not the limitだから-1かな？と思い`/user/-1`にアクセスするとフラグが表示された。

```javascript
{
   "user1" : {
      "name" : "Jhon",
      "password" : "Jhon123",
      "id": 1
   },
   
   "user2" : {
      "name" : "Mark",
      "password" : "mark2468@",
      "id": 2
   },
   "user3" : {
      "name" : "Taison",
      "password" : "taisonalu@",
      "id": 3
   },
   "user4" : {
      "name" : "Json",
      "password" : "figmaonalu@",
      "id": 4
   },
   "user5" : {
      "name" : "Altaf",
      "password" : "altaf2489@",
      "id": 5
   }
   
}
```

## FLAG

```txt
KCTF{tHeRe_1s_n0_l1m1t}
```
